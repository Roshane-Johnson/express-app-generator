module.exports = {
	content: ['./views/**/*.ejs'],
	theme: {
		extend: {},
	},
	plugins: [require('@tailwindcss/forms'), require('@tailwindcss/typography')],
}
