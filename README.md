# How it works

Each URL that is submitted goes through a simple check for validity and/or added http:// before it to redirect successful.
After that, a base 64 string is generated and added to a SQLite database with the corresponding URL that was submitted.
The user is then given a short URL that is formatted as: WEBSITE_DOMAIN/token, the token being the base 64 string.
Whenever this URL is visited the user will get redirected to the tokens corresponding URL in the database.

# Run locally

**Highly encouraged to create a python environment first.**

Clone the repository:

	$ git clone https://github.com/xemeds/tiny0.git

Move into the cloned folder and install the required libraries:

	$ cd tiny0
	$ pip install -r requirements.txt

After that run with:

	$ python run.py

Visit the below URL to view the flask app:

	127.0.0.1:5000

**NOTE:** When running locally all redirects will also be local.

# Deploying

If you do not have a dedicated server, I highly recommend using [Linode](https://www.linode.com/), [Heroku](https://www.heroku.com/) or [PythonAnywhere](https://www.pythonanywhere.com/) to host your application.

Before deploying, make sure to set the following environment variables:

	$ export WEBSITE_DOMAIN=
	$ export SECRET_KEY=
	$ export DEBUG=
	$ export SQLALCHEMY_DATABASE_URI=

If not they will default to the following values:

	WEBSITE_DOMAIN=127.0.0.1:5000
	SECRET_KEY=SECRET_KEY
	DEBUG=true
	SQLALCHEMY_DATABASE_URI=sqlite:///database.db

# License

This project is under the [MIT](https://github.com/xemeds/tiny0/blob/master/LICENSE) license.
