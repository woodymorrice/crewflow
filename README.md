# Crewflow

Crewflow is a fully featured employee management system that facilitates management of employee information, scheduling, and company communication.

## Requirements

Python 3.11 or higher - https://www.python.org.
Git 2.39 or higher - https://git-scm.com/downloads.
A server or a webhost that supports Python Django. A cloud web service is
highly recommended. A list of compatible webhosts can be found at
https://djangofriendly.com.

## Installation

Installation by terminal/command line:

Clone the project repository to your chosen folder:
```
git clone https://git.cs.usask.ca/wam553/project370.git ./chosenfolder
```

Enter the folder:
```
cd chosenfolder
```

Create a new python virtual environment named "env":
```
python3 -m venv env
```

Activate the virtual environment:
```
source env/bin/activate
```

Install the project requirements:
```
pip install -r requirements.txt
```

Create the database:
```
python manage.py migrate
```

Create the superuser(administrator):
```
python manage.py createsuperuser
```

Choose a username, enter an email, and choose a password.

Run the server:
```
python manage.py runserver
```

## Usage
Crewflow can be used by management to distribute schedules, manage time off requests, employee information, expense reports and other company finances, and broadcast company-wide announcements.
Employees can submit availability, time-off requests and expense reports, view schedules and company communications.

## Support
Support concerns may be directed to woody.morrice@usask.ca.

## Roadmap
Future plans include automated schedule generation and direct messaging, among other more minor improvements, however, this project is not currently in development any longer.

## Contributing
Any contributions or changes to the product may be made with permission. Contact woody.morrice@usask.ca with any inquiries.

## Authors and acknowledgment
Many appreciative gestures (such as thumbs up and back pats) go out to everyone involved in bringing this project to life, including:
Matthew Sielski
Bojan Bunarov
Lucas Hilderman
Hongshen Wang
Austin Long
Jeffrey Xia
Woody Morrice

## License
Python software and documentation are licensed under the PSF License Agreement.
https://docs.python.org/3/license.html
Django is distributed under the 3-clause BSD license. This is an open source license granting broad permissions to modify and redistribute Django.
https://docs.djangoproject.com/en/4.2/faq/general/#how-is-django-licensed


## Project status
This project is no longer in development.
