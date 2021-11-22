# Requirements
Before you clone the project make sure you have the following requirements installed.
<h2> Python </h2>
Install Python 3.7 or higher, you can use the command

`!pip install Python`

<h2> Django </h2>
Install Django, you can use the command

`!pip install django` 

Alternatively if you want to make a virtual environment along with it you can use

`!pipenv install django`

# Starting the server
After installing the requirements you can run the application on your server by using 

`!python manage.py runserver`

in the directory of the manage.py file.

# Table of Contents

- [Home](#Home)
- [Manager App](#Manager)
  - [Home](#MHome)
  - [Missions](#MMissions)
  - [Mission Profile](#MMissionProfile)
  - [Officers](#MOfficers)
  - [Officer Profile](#MOfficerProfile)
  - [Sign Out](#MSignout)
- [Officer App](#Officer)
  - [Home](#OHome)
  - [Mission](#OMission)
  - [Notifications](#ONotifications)
  - [Sign Out](#OSignout)


# MyPolice

MyPolice is an application to monitor police's activities.


<a name='Home'></a>
 <h1> Home Page </h1>
 In the home page, there are links to go to the manager and police specific apps! If the manager isn't logged in they are redirected to a login page.

<a name='Manager'></a>
 <h1> Manager App </h1>

The manager has many seperate sections

<a name='MHome'></a>
<h2> Home </h2>

 
 The home page where a welcome message is displayed.
<a name='MMissions'></a>
<h2> Missions </h2>

In this page you can see a list of all the available missions, and there is also the **Add Mission** button to create new missions.

There is also a button for each mission to view its profile with the mission id on it.
<a name='MMissionProfile'></a>
<h2> Mission Profile </h2>

In this page you can see the details of the mission such as id, start time, status, description and assign police officers to the mission.
There's also a button to end in-progress missions.
A mission that is in progress displays the list of the currently assigned officers if there are any, or a list of available officers along with an assign button otherwise.
<a name='MOfficers'></a>
<h2> Officers </h2>
 On this page the manager can view all the officers with their details and buttons to their profile pages.

 There's also a button to create new accounts for officers.
<a name='MOfficerProfile'></a>
 <h2> Officer Profile </h2>
 On this page you can view all the details about the officer and also send them a notification.
<a name='MSignout'></a>
 <h2> Sign Out </h2>
 This signs the manager out.
<a name='Officer'></a>
 <h1> Officer App </h1>
 Upon entering the officer app, the officer is presented with a login page and they must login.
<a name='OHome'></a>
 <h2> Home </h2>
 Upon logging in, the officer is redirected to the home page where a welcome page is displayed.
<a name='OMission'></a>
 <h2> Mission </h2>
 This page shows the mission that the officer is currently assigned to.
<a name='ONotifications'></a>
 <h2> Notifications </h2>
 This page shows the notification sent by the manager.
<a name='OSignout'></a>
 <h2> Sign Out </h2>
 This signs the officer out.

