import os
import tkinter
from tkinter import filedialog


# Main function
def main():
    input_dir = input("What's the name of your project? ")
    input("Where should this project be stored? [Hit enter to select location]")
    tkinter.Tk().withdraw()
    gen_directory = filedialog.askdirectory()
    project_dir: str = os.path.join(gen_directory, input_dir)
    folders: list[str] = ["views", 'views/layouts', "views/partials", "public", "public/assets", "public/assets/images",
                          "public/assets/js", "public/assets/css", "routes", "lib"]
    files: list[str] = ["app.js", ".env", ".gitignore", "tailwind.config.js", "package.json", "views/index.ejs",
                        "views/layouts/layout.ejs", "views/partials/imports.ejs", "views/partials/navbar.ejs", "public/assets/css/_style.css",
                        "routes/index.js", "lib/db.js", "lib/helpers.js"]
    os.mkdir(project_dir)

    # Create folders
    for folder in folders:
        depth_1_folder: str = os.path.join(project_dir, folder)
        os.mkdir(depth_1_folder)

    # Create files
    for file in files:
        if file == ".env":
            f = open(os.path.join(project_dir, file), "x")
            f.write('APP_NAME=ExpressApp\n'
                    'APP_PORT=8080\n'
                    'APP_SESSION_SECRET=expressapp2022\n'
                    '\n'
                    'DB_HOST=\n'
                    'DB_USER=\n'
                    'DB_PASS=\n'
                    'DB_NAME=')
            f.close()
            continue
        if file == ".gitignore":
            f = open(os.path.join(project_dir, file), "x")
            f.write('# Logs\n'
                    'logs\n'
                    '*.log\n'
                    'npm-debug.log*\n'
                    'yarn-debug.log*\n'
                    'yarn-error.log*\n'
                    'lerna-debug.log*\n'
                    '\n'
                    '# Diagnostic reports (https://nodejs.org/api/report.html)\n'
                    'report.[0-9]*.[0-9]*.[0-9]*.[0-9]*.json\n'
                    '\n'
                    '# Runtime data\n'
                    'pids\n'
                    '*.pid\n'
                    '*.seed\n'
                    '*.pid.lock\n'
                    '\n'
                    '# Directory for instrumented libs generated by jscoverage/JSCover\n'
                    'lib-cov\n'
                    '\n'
                    '# Coverage directory used by tools like istanbul\n'
                    'coverage\n'
                    '*.lcov\n'
                    '\n'
                    '# nyc test coverage\n'
                    '.nyc_output\n'
                    '\n'
                    '# Grunt intermediate storage (https://gruntjs.com/creating-plugins#storing-task-files)\n'
                    '.grunt\n'
                    '\n'
                    '# Bower dependency directory (https://bower.io/)\n'
                    'bower_components\n'
                    '\n'
                    '# node-waf configuration\n'
                    '.lock-wscript\n'
                    '\n'
                    '# Compiled binary addons (https://nodejs.org/api/addons.html)\n'
                    'build/Release\n'
                    '\n'
                    '# Dependency directories\n'
                    'node_modules/\n'
                    'jspm_packages/\n'
                    '\n'
                    '# TypeScript v1 declaration files\n'
                    'typings/\n'
                    '\n'
                    '# TypeScript cache\n'
                    '*.tsbuildinfo\n'
                    '\n'
                    '# Optional npm cache directory\n'
                    '.npm\n'
                    '\n'
                    '# Optional eslint cache\n'
                    '.eslintcache\n'
                    '\n'
                    '# Microbundle cache\n'
                    '.rpt2_cache/\n'
                    '.rts2_cache_cjs/\n'
                    '.rts2_cache_es/\n'
                    '.rts2_cache_umd/\n'
                    '\n'
                    '# Optional REPL history\n'
                    '.node_repl_history\n'
                    '\n'
                    '# Output of \'npm pack\'\n'
                    '*.tgz\n'
                    '\n'
                    '# Yarn Integrity file\n'
                    '.yarn-integrity\n'
                    '\n'
                    '# dotenv environment variables file\n'
                    '.env\n'
                    '.env.test\n'
                    '\n'
                    '# parcel-bundler cache (https://parceljs.org/)\n'
                    '.cache\n'
                    '\n'
                    '# Next.js build output\n'
                    '.next\n'
                    '\n'
                    '# Nuxt.js build / generate output\n'
                    '.nuxt\n'
                    'dist\n'
                    '\n'
                    '# Gatsby files\n'
                    '.cache/\n'
                    '# Comment in the public line in if your project uses Gatsby and *not* Next.js\n'
                    '# https://nextjs.org/blog/next-9-1#public-directory-support\n'
                    '# public\n'
                    '\n'
                    '# vuepress build output\n'
                    '.vuepress/dist\n'
                    '\n'
                    '# Serverless directories\n'
                    '.serverless/\n'
                    '\n'
                    '# FuseBox cache\n'
                    '.fusebox/\n'
                    '\n'
                    '# DynamoDB Local files\n'
                    '.dynamodb/\n'
                    '\n'
                    '# TernJS port file\n'
                    '.tern-port\n')
            f.close()
            continue
        if file == "package.json":
            f = open(os.path.join(project_dir, file), "x")
            f.write('{\n'
                    '	"name": "express-app",\n'
                    '	"version": "1.0.0",\n'
                    '	"description": "Just another express application.",\n'
                    '	"main": "app.js",\n'
                    '	"scripts": {\n'
                    '		"start": "concurrently \\"nodemon app.js\\" \\"npx tailwindcss -i ./public/assets/css/_style.css -o ./public/assets/css/style.css --watch\\""\n'
                    '	},\n'
                    '	"keywords": [],\n'
                    '	"author": "Roshane-Johnson",\n'
                    '	"license": "ISC",\n'
                    '	"type": "commonjs",\n'
                    '	"dependencies": {\n'
                    '		"bcrypt": "^5.0.1",\n'
                    '		"cors": "^2.8.5",\n'
                    '		"dotenv": "^16.0.0",\n'
                    '		"ejs": "^3.1.7",\n'
                    '		"express": "^4.18.1",\n'
                    '		"express-ejs-layouts": "^2.5.1",\n'
                    '		"express-flash": "^0.0.2",\n'
                    '		"express-session": "^1.17.3",\n'
                    '		"mysql": "^2.18.1"\n'
                    '	},\n'
                    '	"devDependencies": {\n'
                    '		"concurrently": "^7.2.1",\n'
                    '		"nodemon": "^2.0.16",\n'
                    '		"tailwindcss": "^3.0.24"\n'
                    '	}\n'
                    '}\n')
            f.close()
            continue
        if file == "app.js":
            f = open(os.path.join(project_dir, file), "x")
            f.write('require(\'dotenv\').config()\n'
                    'const express = require(\'express\')\n'
                    'const session = require(\'express-session\')\n'
                    'const expressLayouts = require(\'express-ejs-layouts\')\n'
                    'const cors = require(\'cors\')\n'
                    'const path = require(\'path\')\n'
                    'const flash = require(\'express-flash\')\n'
                    'const app = express()\n'
                    '\n'
                    'const PORT = process.env.APP_PORT || 8080\n'
                    'const APP_NAME = process.env.APP_NAME || \'Express App\'\n'
                    '\n'
                    '// Express configs\n'
                    'app.set(\'view engine\', \'ejs\')\n'
                    'app.set(\'layout\', \'layouts/layout\')\n'
                    '\n'
                    '// Middlewares\n'
                    'app.use(expressLayouts)\n'
                    'app.use(express.json())\n'
                    'app.use(express.urlencoded({ extended: true }))\n'
                    'app.use(express.static(path.join(__dirname, \'public\')))\n'
                    'app.use(cors([\'*\']))\n'
                    'app.use(flash())\n'
                    'app.use(\n'
                    '	session({\n'
                    '		secret: process.env.APP_SESSION_SECRET || \'secret8080\',\n'
                    '		resave: false,\n'
                    '		saveUninitialized: false,\n'
                    '		cookie: {\n'
                    '			maxAge: 1000 * 60 * 60 * 24, // day in milliseconds\n'
                    '		},\n'
                    '	})\n'
                    ')\n'
                    '\n'
                    '// View Routes\n'
                    'app.use(\'/\', require(\'./routes/index\'))\n'
                    '\n'
                    '// Start express app\n'
                    'app.listen(PORT, () => {\n'
                    '	console.log(`${APP_NAME} listening on http://localhost:${PORT}`)\n'
                    '})\n')
            f.close()
            continue
        if file == "routes/index.js":
            f = open(os.path.join(project_dir, file), "x")
            f.write('const express = require(\'express\')\n'
                    'const router = express.Router()\n'
                    '\n'
                    'router.get(\'/\', (req, res) => {\n'
                    '	res.render(\'index\', { page_title: \'Home\' })\n'
                    '})\n'
                    '\n'
                    'module.exports = router\n')
            f.close()
            continue
        if file == "views/index.ejs":
            f = open(os.path.join(project_dir, file), "x")
            f.write('<div class="h-screen grid place-items-center">\n'
                    '	<h1 class="">Express App Works</h1>\n'
                    '</div>\n')
            f.close()
            continue
        if file == "views/layouts/layout.ejs":
            f = open(os.path.join(project_dir, file), "x")
            f.write('<!DOCTYPE html>\n'
                    '<html lang="en">\n'
                    '	<head>\n'
                    '		<meta charset="UTF-8" />\n'
                    '		<meta http-equiv="X-UA-Compatible" content="IE=edge" />\n'
                    '		<meta name="viewport" content="width=device-width, initial-scale=1.0" />\n'
                    '		<%- include("../partials/imports.ejs") %>\n'
                    '		<title>Express App - <%= page_title %></title>\n'
                    '	</head>\n'
                    '	<body>\n'
                    '		<%- include("../partials/navbar.ejs") %>\n'
                    '		<%- body %>\n'
                    '	</body>\n'
                    '</html>\n')
            f.close()
            continue
        if file == "views/partials/imports.ejs":
            f = open(os.path.join(project_dir, file), "x")
            f.write('<script defer src="/assets/js/main.js"></script>\n'
                    '<link rel="stylesheet" href="/assets/css/style.css" />\n')
            f.close()
            continue
        if file == "views/partials/navbar.ejs":
            f = open(os.path.join(project_dir, file), 'x')
            f.write('<nav class="fixed top-0 w-full">\n'
                    '	<div class="w-10/12 mx-auto py-5 grid grid-cols-2">\n'
                    '		<a href="/">Express Application</a>\n'
                    '		<ul class="flex justify-end">\n'
                    '			<li><a href="/">Home</a></li>\n'
                    '			<li><a href="/test1">Test 1</a></li>\n'
                    '			<li><a href="/test2">Test 2</a></li>\n'
                    '		</ul>\n'
                    '	</div>\n'
                    '</nav>\n')
            f.close()
            continue
        if file == "lib/db.js":
            f = open(os.path.join(project_dir, file), "x")
            f.write('const mysql = require(\'mysql\')\n'
                    'require(\'dotenv\').config()\n'
                    '\n'
                    'const DB = mysql.createConnection({\n'
                    '	host: process.env.DB_HOST || \'localhost\',\n'
                    '	user: process.env.DB_USER || \'root\',\n'
                    '	password: process.env.DB_PASS || \'\',\n'
                    '	database: process.env.DB_NAME || process.env.APP_NAME.toLowerCase() || \'\',\n'
                    '	dateStrings: true,\n'
                    '})\n'
                    '\n'
                    'DB.connect((err) => {\n'
                    '	if (err) throw err\n'
                    '\n'
                    '	console.log(\'Database Connected\')\n'
                    '})\n'
                    '\n'
                    'module.exports = DB\n')
            f.close()
            continue
        if file == "lib/helpers.js":
            f = open(os.path.join(project_dir, file), "x")
            f.write('function SuccessResponse(res, data, message = \'success\', status = 200) {\n'
                    '	return res.json({ message: message, status: status, data: data })\n'
                    '}\n'
                    '\n'
                    'function ErrorResponse(res, data = [], message = \'error\', status = 500) {\n'
                    '	return res.json({ message: message, status: status, data: data })\n'
                    '}\n'
                    '\n'
                    'module.exports = { SuccessResponse, ErrorResponse }\n')
            f.close()
            continue
        if file == "tailwind.config.js":
            f = open(os.path.join(project_dir, file), "x")
            f.write('module.exports = {\n'
                    '	content: [\'./views/**/*.ejs\'],\n'
                    '	theme: {\n'
                    '		extend: {},\n'
                    '	},\n'
                    '	plugins: [],\n'
                    '}\n')
            f.close()
            continue
        if file == "public/assets/css/_style.css":
            f = open(os.path.join(project_dir, file), "x")
            f.write('@tailwind base;\n'
                    '@tailwind components;\n'
                    '@tailwind utilities;\n'
                    '\n'
                    'nav ul li {\n'
                    '	--nav-padding: 10px;\n'
                    '	display: flex;\n'
                    '	padding-left: var(--nav-padding);\n'
                    '	padding-right: var(--nav-padding);\n'
                    '}\n')
            f.close()
            continue
        if file == "public/assets/js/main.js":
            f = open(os.path.join(project_dir, file), "x")
            f.close()
            continue


def banner():
    print('\n'
          '███████ ██   ██ ██████  ██████  ███████ ███████ ███████      ██████  ███████ ███    ██ \n'
          '██       ██ ██  ██   ██ ██   ██ ██      ██      ██          ██       ██      ████   ██ \n'
          '█████     ███   ██████  ██████  █████   ███████ ███████     ██   ███ █████   ██ ██  ██ \n'
          '██       ██ ██  ██      ██   ██ ██           ██      ██     ██    ██ ██      ██  ██ ██ \n'
          '███████ ██   ██ ██      ██   ██ ███████ ███████ ███████      ██████  ███████ ██   ████ \n'
          '\n')


# Script entry point
if __name__ == "__main__":
    try:
        banner()
        main()
    except KeyboardInterrupt:
        print("\033[93m\n\nUnexpected Exit\n\033[0m")
        exit(0)
