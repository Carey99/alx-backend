import express from 'express';
import { createClient } from 'redis';
import Kue from 'kue';
import { reserveSeat, getCurrentAvailableSeats } from './redisClient.js';

const app = express();
const port = 1245;
const queue = Kue.createQueue();

let reservationEnabled = true;

// Set initial available seats
reserveSeat(50);

app.get('/available_seats', async (req, res) => {
  const availableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: availableSeats.toString() });
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservations are blocked' });
  }
  
  const job = queue.create('reserve_seat').save((err) => {
    if (err) {
      return res.json({ status: 'Reservation failed' });
    }
    res.json({ status: 'Reservation in process' });
  });

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on('failed', (err) => {
    console.log(`Seat reservation job ${job.id} failed: ${err.message}`);
  });
});

app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (job, done) => {
    try {
      let availableSeats = await getCurrentAvailableSeats();
      if (availableSeats <= 0) {
        return done(new Error('Not enough seats available'));
      }

      availableSeats -= 1;
      await reserveSeat(availableSeats);

      if (availableSeats === 0) {
        reservationEnabled = false;
      }

      done();
    } catch (err) {
      done(err);
    }
  });
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
