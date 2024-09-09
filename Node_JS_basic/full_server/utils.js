const fs = require('node:fs/promises');

async function readDatabase(filePath) {
  try {
    const data = await fs.readFile(filePath, 'utf8');
    const rows = data.split('\n').slice(1);

    const studentsCS = [];
    const studentsSWE = [];

    for (const row of rows) {
      const columns = row.split(',');

      if (columns[3] === 'CS') {
        studentsCS.push(columns[0]);
      }

      if (columns[3] === 'SWE') {
        studentsSWE.push(columns[0]);
      }
    }
    return {
      CS: studentsCS,
      SWE: studentsSWE
    };
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = readDatabase;
