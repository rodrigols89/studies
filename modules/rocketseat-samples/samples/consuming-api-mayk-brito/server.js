const cors = require('cors');
const express = require('express');
const axios = require('axios');

const app = express();
app.use(cors());

app.get('/', async (req, res) => {

  try {
    // "response" é a resposta do axios, MAS eu tiro o "data" de "response".
    const { data } = await axios.get('https://jsonplaceholder.typicode.com/users');
    return res.json(data);
  } catch (error) {
    console.log(error);
  }
});

app.listen('4567');
