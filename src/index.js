const express = require('express');
const session = require('express-session');
require('dotenv').config();
require('./strategies/discord');

// Routes
const authRoute = require('./routes/auth');

require('./database');

const app = express();
const PORT = process.env.PORT || 3001;

app.use(express.json());
app.use(express.urlencoded());

app.use(
    session({
    secret: process.env.COOKIE_SECRET,
    resave: 'false',
    saveUninitialized: 'false',
}))

app.use('/api/v1/auth', authRoute)

app.listen(PORT, () => console.log(`Running Express Server on Port ${PORT}!`));