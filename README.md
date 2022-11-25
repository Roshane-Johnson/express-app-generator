# Express App Generator (EXAG) - Roshane-Johnson

This express app generator has a few starter features that are custom for my current needs which includes:

- [x] TailwindCSS
- - TailwindCSS Forms
- - TailwindCSS Typography
- [x] MySQL Setup
- [x] ExpressJS Response Helper Functions
- [x] ExpressJS Layouts, Partials, Flash and Session

If you'd like to contribute to this project, simply create a fork and make a pull request following this projects pull request format.

## Pre-requsites

- Python `3.9.x` or later
- Windows Operating System

## Usage

- Double click `expressgen.bat` to get started
- (Recommended) Change variables in `.env` to match your database and application.
- (Optional) Change the navbar located in `/views/partials/navbar.ejs`

## NPM Commands

- Development command `npm run watch`
- Build command `npm run build`
- Deploy command `npm run start` or `npm start`

## Where Stuff Goes

- Write frontend JavaScript in `/public/assets/js/main.js`
- Write CSS in `/public/assets/css/_style.css` (TailwindCSS will compile it to `style.css`. This is the reason why `style.css` is linked in the HTML)
- Add images in `/public/assets/images`
- Add JavaScript and CSS import in `/views/partials/imports.ejs`
