import { createClient } from 'redis';

const client =  createClient();

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

const setNewSchool = async (schoolName, value) => {
  try {
    await client.set(schoolName, value, redis.print);
  } catch (err) {
    console.log(`${err.message}`);
  }
};

const displaySchoolValue = async (schoolName) => {
  try {
    const value_display = await client.get(schoolName);
    console.log(value_display);
  } catch (err) {
    console.log(`Error fetching value: ${err.message}`);
  };
  
};

const run = async() => {
  await client.connect();
  await displaySchoolValue('Holberton');
  await setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
};

run();
