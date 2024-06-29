export default function createPushNotificationsJobs (jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  jobs.forEach((jobObj) => {
    const job = queue.create('push_notification_code_3', jobObj).save((err) => {
      if (!err) { console.log(`Notification job created: ${job.id}`); }
    });

    job.on('progress', (progress, _data) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    }).on('complete', (_result) => {
      console.log(`Notification job ${job.id} completed`);
    }).on('failed', (err) => {
      console.log(`Notification job ${job.id} failed: ${err}`);
    });
  });
}
