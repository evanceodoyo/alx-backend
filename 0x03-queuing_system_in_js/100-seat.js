import { createClient } from 'redis';
import { createQueue } from 'kue';
import express from 'express';
import { promisify } from 'util';

const client = createClient();
const app = express();
const queue = createQueue();
let reservationEnabled = true;

async function reserveSeat (number) {
  return promisify(client.set).bind(client)('available_seats', number);
}

async function getCurrentAvailableSeats () {
  return promisify(client.get).bind(client)('available_seats');
}

async function resetAvailableSeats () {
  return promisify(client.set).bind(client)('available_seats', 50);
}

app.get('/available_seats', (_req, res) => {
  getCurrentAvailableSeats()
    .then((numberOfAvailableSeats) => {
      res.json({ numberOfAvailableSeats });
    });
});

app.get('/reserve_seat', (_req, res) => {
  if (!reservationEnabled) {
    res.json({ status: 'Reservation are blocked' });
    return;
  }

  const job = queue.create('reserve_seat');

  job.on('complete', (_result) => {
    console.log(`Seat reservation job ${job.id} completed`);
  }).on('failed', (err) => {
    console.log(`Seat reservation job ${job.id} failed: ${err}`);
  });
  job.save((err) => {
    if (err) {
      res.json({ status: 'Reservation failed' });
    } else {
      res.json({ status: 'Reservation in process' });
    }
  });
});

app.get('/process', (_req, res) => {
  res.json({ status: 'Queue processing' });
  queue.process('reserve_seat', (_job, done) => {
    getCurrentAvailableSeats()
      .then((availableSeats) => {
        if (availableSeats <= 0) {
          reservationEnabled = false;
        }
        if (availableSeats >= 1) {
          reserveSeat(availableSeats - 1)
            .then(() => done());
        } else {
          done(new Error('Not enough seats available'));
        }
      });
  });
});

app.listen(1245, () => {
  resetAvailableSeats()
    .then(() => {
      console.log('Server listening on port 1245');
    });
});
