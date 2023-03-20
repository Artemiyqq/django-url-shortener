# URL Shortener

My project is a URL shortener, which is a web application that allows users to enter long URLs and convert them into short, easy-to-remember URLs.

## Built With

* Python
* Django
* HTML/CSS
* JS
* PostgreSQL 14

## Deployment

This project has been prepared for deployment on the Railway. For other deployment services, you will need to modify the project yourself.

### Railway
1. Create new project on Railway.
2. Add an app from this repo with a Django template to the created project.
3. Create an empty Postgres db in the created project.
4. Set up domain of django_url_shortener app. Set your own domain in the settings, or let Railway generate it for you automatically.
5. Create `SITE_DOMAIN` variable for django_url_shortener with the domain value you got in the step four.
6. Create `SITE_URL` variable for django_url_shortener with the domain value you got in the step four and the protocol prefix in front of it (https://).
7. Get the secret key for your app from [https://djecrety.ir/](https://djecrety.ir/) or from somewhere else.
8. Add the secret key from the previous step as `SECRET_KEY` variable to this app.

* Now everything should work as it should.

## License
This project is licensed under the MIT Licence—see the LICENSE.md file for details.