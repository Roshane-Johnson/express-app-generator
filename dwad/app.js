require('dotenv').config()
const express = require('express')
const session = require('express-session')
const expressLayouts = require('express-ejs-layouts')
const cors = require('cors')
const path = require('path')
const flash = require('express-flash')
const app = express()

const PORT = process.env.PORT || 8080
const APP_NAME = process.env.NAME || 'Express App'

// Express configs
app.set('view engine', 'ejs')
app.set('layout', 'layouts/layout')

// Middlewares
app.use(expressLayouts)
app.use(express.json())
app.use(express.urlencoded({ extended: true }))
app.use(express.static(path.join(__dirname, 'public')))
app.use(cors(['*']))
app.use(flash())
app.use(
	session({
		secret: process.env.SESSION_SECRET || 'secret8080',
		resave: false,
		saveUninitialized: false,
		cookie: {
			maxAge: 1000 * 60 * 60 * 24, // day in milliseconds
		},
	})
)

// View Routes
app.use('/', require('./routes/index'))

// Start express app
const _app = app.listen(PORT, require('os').hostname(), () => {
	console.log(`\n\t${APP_NAME} listening on http://${_app.address().address}:${_app.address().port}\n`)
})
