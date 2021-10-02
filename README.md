# Djanger

<p float="left">

<img src="Images/python.png" alt="Pyhton" width="100"/>

<img src="Images/django.png" alt="Django" width="195"/>

</p>

Python & Django application that communicates with the `Twitter API`

## Installation

1 - Clone the project to the desired location:

``git clone https://github.com/frederikblais/Djanger.git``

2 - Create a virtual environment to install required packages:

`` python3 -m venv <name of environment> ``

3 - Activate the created environment:

`` source <name of environment>/bin/activate ``

## Programs

Access the web page:

`` python manage.py runserver ``

Like tweets with the Database keywords

`` python manage.py like_tweet ``

Retweet with the Database keywords

`` python manage.py retweet_tweet ``

Dm the latest followers with the Database message

`` python manage.py dm_new_follower ``

Save all inbound dms to the Database

`` python manage.py save_inbound_dm ``
