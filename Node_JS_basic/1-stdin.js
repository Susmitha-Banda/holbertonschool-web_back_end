// Import the 'readline' module
const readline = require('readline');

// Create an interface to read from stdin and write to stdout
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Display the initial message
console.log('Welcome to Holberton School, what is your name?');

// Read the user input
rl.question('', (name) => {
  // Display the user's name with a carriage return
  console.log(`Your name is: ${name}\r\n`);
  
  // Close the interface and display the closing message
  rl.close();
  console.log('This important software is now closing');
});
