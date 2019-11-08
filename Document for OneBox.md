# Document for OneBox

- [Design and development][#design and development]
- [Application structure][#application structure]
- [Application usage examples][#application usage examples]

---

## Design and development

The mailbox is designed and developed as the Computer Network course project. I made it solely as I enjoyed the process of pushing every features to what I want it to be. It's really achieving.

As can be seen in README.md, I design the features initially on Python GUI package Tkinter and relative web packages. To my surprise, Tkinter should not support normal utf-8 charset as it said to have done. So, I abandoned the components and start from zero in web Browser/Server structure. It's really hard at first time, but I made it through to apply the powerful Vue.js framework along with Flask server to build the application.

The B/S structure has a frontend(client) and backend(server). The frontend is build with Vue.js, the backend is powered by Flask, and with the support of AJAX I can send datagram from client to server. I build utils package to apply complex content manipulations for backend server. 