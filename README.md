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
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.
