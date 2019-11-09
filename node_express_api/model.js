const sqlite3 = require('sqlite3').verbose()

let db = new sqlite3.Database('./db/chinook.db', sqlite3.OPEN_READWRITE, (err) => {
  if (err) {
    console.error(err.message);
  }
  console.log('Connected to the chinook database.');
});


const books = [
  {
    id: 1,
    title: 'Don Quijote de la Mancha',
    author: 'Miguel de Cervantes'
  },
  {
    id: 2,
    title: 'Cien años de soledad',
    author: 'Gabriel García Márquez' 
  }
]

module.exports = { books }