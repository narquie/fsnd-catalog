# README
## Overview
This code is used to create a board game website on the virtual machine that runs this code. 
Users can log in through third party authentication, add and edit the site, and view the results in real time.
## What the code does
The code implements Flask and SQLAlchemy to create the website and mantain the database, respectively. 
Everything is set up so that the machine can interpret the HTTP at a high level and return TCP commands on a low level. 
These inherent commands can be quite tricky so the key to debugging is watching the HTTP calls and finding all of the 400 errors.
## Setup
Initial downloads setup you need to finish:

[Python3 Installation](https://realpython.com/installing-python/): used to run the source code.
[VirtualBox Installation](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) is the software that actually runs the VM. Please install the platform package for your operating system.
[FSND-Catalog](https://github.com/narquie/fsnd-catalog): fork the repository on github and clone it with ```git clone http://github.com/<username>/fsnd-catalog``` with your own username. Starting up vagrant (the virtual machine) will initialize it with the correct software.
[Vagrant](https://www.vagrantup.com/downloads.html) is the virtual machine itself. At this step you can cd to the vagrant folder within FSND ```cd /vagrant``` and use the shell command ```vagrant up``` and ```vagrant ssh```.

The webserver has all of its files and code in the ```catalog``` folder, so cd'ing into it with ```cd /catalog``` will grant you access.
Please make sure that you have all the dependencies required. This can be initialized without any further work on your part by entering ```sudo pip install -r requirements.txt``` into your terminal.
To initialize the database, you need to run ```python database_setup.py```. After it has resolved (you should see no errors) you can run ```python lotsofboardgames.py```. This will fill up the database with actual records of board games!

Use ```python project.py``` to run the code itself.

Now, head to a web browser (Edge, Firefox, Chrome...) and type in ```http://localhost:5000```. It should send you to the home page of the project. Feel free to login (top right corner), look through categories of games, and (if you're logged in) you can create your own categories with whatever games you feel.

## How to interpret the code and results
The code communicates with the user by setting up pages in HTML / CSS (which make the site easier to handle), runs on SQL to bring the relevant data to the users that are displayed in the web pages. 
The python code is capable of managing the issues and requests from Facebook and Google as well as the users itself, and is the core power of the web server. 
