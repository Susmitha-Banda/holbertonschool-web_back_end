import { uploadPhoto, createUser } from './utils.js';

// Function to handle profile signup
export default function handleProfileSignup() {
  // Use Promise.all to handle multiple promises
  return Promise.all([uploadPhoto(), createUser()])
    .then((results) => {
      // Destructure the results array
      const [photo, user] = results;
      // Log the desired values to the console
      console.log(`${photo.body} ${user.firstName} ${user.lastName}`);
    })
    .catch(() => { console.log('Signup system offline'); });
}
