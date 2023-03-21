# URL Shortener

My project is a URL shortener, which is a web application that allows users to enter long URLs and convert them into short, easy-to-remember URLs.

## Built With

* Python
* Django
* HTML/CSS
* JS
* PostgreSQL 14

## Getting Started

### Dependencies

* Python
* Pip
* PostgreSQL 14

### Installing
1. Create an empty Postgre's db for this project (Optionally, you can create a separate user in db for this project).

2. Clone the repo.
```
git clone https://github.com/Artemiyqq/django-url-shortener
```

3. Create a virtual environment for this project with the help of any package or with python's built-in module venv. Below you can see how to do this with venv.
```
python -m venv <the_path_to_the_place_where_you_want_to_create>\<the_name_of_folder_for_venv>
```

4. Activate your virtual environment. If you did it using the built-in module as I showed above, follow this link to see a table of how to do it [https://docs.python.org/3/library/venv.html#how-venvs-work](https://docs.python.org/3/library/venv.html#how-venvs-work)

5. Install the necessary packages (check if you have accurately activated the virtual environment).
```
pip install -r requirements.txt
```

6. Create a file named '.env' in 'url_shortener' folder (...\django_url_shortener\url_shortener\.env).

7. Fill in this file as follows (you can get Django secret password from the following link [https://djecrety.ir/](https://djecrety.ir/)):
```
SECRET_KEY=<your_django's_secret_key>
DATABASE_NAME=<name_of_db_that_you_created_earlier>
DATABASE_USER=<the_name_of_an_existing user_of_your_db >
DATABASE_PASS=<password_of_that_user>

```

### Executing program

1. Activate the virtual environment you created earlier for this project.

2. Start the server
```
python manage.py runserver
```
* Now, you can follow [the link](http://127.0.0.1:8000/) and start using the project the way you want.

## Deployment
If you are interested in deploying this project, there is a separate git branch with files prepared for deployment to Railway and modified README.md for this purpose.

## License
This project is licensed under the MIT Licence — see the LICENSE.md file for details.

## Authors
Only [me](https://github.com/Artemiyqq)
