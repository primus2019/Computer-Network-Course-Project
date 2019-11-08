# Document for OneBox

- [Design and development][#design and development]
- [Application structure][#application structure]
- [Requirements and examples][#requirements and examples]

---

## Design and development

The mailbox is designed and developed as the Computer Network course project. I made it solely as I enjoyed the process of pushing every features to what I want it to be. It's really achieving.

As can be seen in README.md, I design the features initially on Python GUI package Tkinter and relative web packages. To my surprise, Tkinter should not support normal utf-8 charset as it said to have done. So, I abandoned the components and start from zero in web Browser/Server structure. It's really hard at first time, but I made it through to apply the powerful Vue.js framework along with Flask server to build the application.

The B/S structure has a frontend(client) and backend(server). The frontend is build with Vue.js, the backend is powered by Flask, and with the support of AJAX I can send datagram from client to server. I build utils package to apply complex content manipulations for backend server. The frontend implements the Bootstrap Vue components which prettifies the whole appearance.

## Application structure

For server: 

# server

- \_\_pycache\_\_, .vscode: launch jsonified configurations
- env: virtualization for server environment
- attachments: folder for attached files in mails
- log: folder for server running logs
- mails: folder for all mails(desensitized with hex-uuid naming)
- utils:
  - Login: support for login
  - Mails: manipulations for mail contents
  - Sender: support for sending sessions
  - Transfer: powerful charset and encoding detection and transfer
- app.py: main application for server
- requirements.txt: running dependencies for virtualization
- test.py: for test

For client: 

# client

- src
  - assets: static client resources
  - components: components and webpage templates for Vue application
- router: transfer station between components and main App
- views: original settings
- App.vue: main client application
- main.js: main client application support
- router.js: main client application support

## Requirements and examples

Requirements: 

1. Python >3.7
2. Node.js package manager(NPM)

Install required dependencies by locating at server folder and typing: 

```
pip install -r requirements.txt
```

and wait for finishing.

Locating at client folder and typing: 

```
npm build
```

and wait for finishing.

---

1. Launch the application by locating at server folder and type: 

```
python app.py

C:\Primus\Codes\Python\CN\Computer-Network-Course-Project\server/app.py       
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 913-937-337
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

when the cmd shows that the server is working properly, launch another window and locate at client folder: 

```
npm run serve

C:\Primus\Codes\Python\CN\Computer-Network-Course-Project\client>npm run serve

> client@0.1.0 serve C:\Primus\Codes\Python\CN\Computer-Network-Course-Project\client
> vue-cli-service serve

 INFO  Starting development server...
98% after emitting CopyPlugin

 DONE  Compiled successfully in 5949ms                                                             1:58:55 PM

  App running at:
  - Local:   http://localhost:8080/
  - Network: unavailable

  Note that the development build is not optimized.
  To create a production build, run npm run build.
```

when the cmd shows that the client is working properly, open your Chrome browser and visit localhost:8080

the application looks like this: 

# demo

and click login: 

# login

enter the information, confirm and wait for reply(the server is working hard to process your mails!)

when the mails are ok and sent to client, it looks like this:

# mails

click one mail, we get: 

# checkmail

the Date, From, To details are presented on the header.

Click Reply, we get: 

# reply

click Browse in attachment column, we get: 

# attach

(the attachment can currently be obtained only from 'server/attachment' folder, as the application is not authorized to browse system files at other positions)

and for mails that contains attachment(s):

# getattach

press ctrl+C to shut the client and server(alternative sequence is ok)

That's all for the OneBox!

