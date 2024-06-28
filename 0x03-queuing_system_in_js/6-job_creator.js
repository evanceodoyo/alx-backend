import { createQueue } from 'kue';

const queue = createQueue();

const job = queue.create('push_notification_code', {
  phoneNumber: '254712345678',
  message: 'This is a notification message'
}).save((err) => {
  if (!err) { console.log(`Notification job created: ${job.id}`); }
});

job.on('complete', (_result) => {
  console.log('Notification job completed');
}).on('failed', (_err) => {
  console.log('Notification job failed');
});
