import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
  let queue;

  beforeAll(() => {
    queue = kue.createQueue();
    queue.testMode.enter();
  });

  afterAll(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  test('should throw an error if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('not an array', queue))
      .toThrow('Jobs is not an array');
  });

  test('should create jobs in the queue for valid inputs', () => {
    const jobs = [
      { phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account' },
      { phoneNumber: '4153518781', message: 'This is the code 4562 to verify your account' },
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).toBe(2);
    expect(queue.testMode.jobs[0].type).toBe('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).toEqual(jobs[0]);
    expect(queue.testMode.jobs[1].type).toBe('push_notification_code_3');
    expect(queue.testMode.jobs[1].data).toEqual(jobs[1]);
  });
});
