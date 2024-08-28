import kue from 'kue';

/**
 * Creates push notification jobs in the specified queue.
 * 
 * @param {Array} jobs - Array of job objects, each containing `phoneNumber` and `message`.
 * @param {Object} queue - Kue queue instance.
 * 
 * @throws {Error} If `jobs` is not an array.
 */
const createPushNotificationsJobs = (jobs, queue) => {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  jobs.forEach((jobData) => {
    const job = queue.create('push_notification_code_3', jobData);

    job
      .on('enqueue', () => {
        console.log(`Notification job created: ${job.id}`);
      })
      .on('complete', () => {
        console.log(`Notification job ${job.id} completed`);
      })
      .on('failed', (errorMessage) => {
        console.log(`Notification job ${job.id} failed: ${errorMessage}`);
      })
      .on('progress', (progress) => {
        console.log(`Notification job ${job.id} ${progress}% complete`);
      });

    job.save();
  });
};

export default createPushNotificationsJobs;
