const express = require('express');
const indexRouter = require('./routes/index');

const app = express();
const PORT = 1245;

// Use the indexRouter for the base path and students path
app.use('/', indexRouter);
app.use('/students', indexRouter);

// Correct route for students with a major parameter
app.use('/students/:major', indexRouter);

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

module.exports = app;
