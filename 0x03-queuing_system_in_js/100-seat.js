import { createClient } from 'redis';
import { createQueue } from 'kue';
import { express } from 'express';
import { promisify } from 'util';

const client = createClient();
const app = express();

async function reserveSeat (number) {
  return promisify(client.set).bind(client)('available_seats', number);
}

async function getCurrentAvailableSeats () {
  return promisify(client.get).bind(client)('available_seats');
}

async function resetAvailableSeats () {
  return Promise((resolve, reject) => {
    resolve(promisify(client.set).bind(client)('available_seats', 50))
  });
}

const reservationEnabled = true;

const queue = createQueue();


app.listen(1245, () => {
  resetAvailableSeats()
    .then(() => {
      console.log('Server listening on port 1245');
    });
}

);
