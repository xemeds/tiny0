from flask import render_template, redirect, url_for
from tiny0 import app, db
from tiny0.forms import URLForm, ShortURLForm, ReportForm
from tiny0.models import URL, Reports
from tiny0.token import gen_valid_token
from tiny0.config import WEBSITE_DOMAIN

# Index route
@app.route("/", methods=['GET', 'POST'])
def index():
	# Create a instance of the form
	form = URLForm()

	# If the form was valid
	if form.validate_on_submit():

		# If a token was given
		if form.token.data:
			# Add the token and the given url to the database
			db.session.add(URL(token=form.token.data, url=form.url.data))
			db.session.commit()

			# Return the url page with the shortened url
			return render_template("url.html", url=WEBSITE_DOMAIN + "/" + form.token.data)

		# Else if a token was not given
		else:
			# Generate a valid token
			token = gen_valid_token()

			# Add the token and the given url to the database
			db.session.add(URL(token=token, url=form.url.data))
			db.session.commit()

			# Return the url page with the shortened url
			return render_template("url.html", url=WEBSITE_DOMAIN + "/" + token)

	# Else if the form was invalid or not submitted
	else:
		# Return the index page with the form
		return render_template("index.html", form=form)

# Shortened url route
@app.route("/<token>")
def short_url(token):
	# Query the token in the database
	query = URL.query.filter_by(token=token).first()

	# If the query response was empty
	if not query:
		# Return the error page with a 404 not found error
		return render_template("error.html", error_code=404, error_message="Not Found"), 404

	# Else if the query response contained data 
	else:
		# Addd one to the clicks of the shortened url
		query.clicks += 1
		db.session.commit()

		# Redirect to the url of the token
		return redirect(query.url)

# Click tracker route
@app.route("/tracker", methods=['GET', 'POST'])
def tracker():
	# Create a instance of the form
	form = ShortURLForm()

	# If the form was valid
	if form.validate_on_submit():
		# Get the clicks of the given token
		clicks = URL.query.filter_by(token=form.url.data).first().clicks

		# Return the clicks page with the clicks of that token
		return render_template("clicks.html", clicks=clicks)

	# Else if the form was invalid or not submitted
	else:
		# Return the tracker page with the form
		return render_template("tracker.html", form=form)

# url lookup route
@app.route("/lookup", methods=['GET', 'POST'])
def lookup():
	# Create a instance of the form
	form = ShortURLForm()

	# If the form was valid
	if form.validate_on_submit():
		# Get the original url of the given token
		url = URL.query.filter_by(token=form.url.data).first().url

		# Return the original url page with the url
		return render_template("original-url.html", url=url)

	# Else if the form was invalid or not submitted
	else:
		# Return the lookup page with the form
		return render_template("lookup.html", form=form)

# url report route
@app.route("/report", methods=['GET', 'POST'])
def report():
	# Create a instance of the form
	form = ReportForm()

	# If the form was valid
	if form.validate_on_submit():
		# Add the report to the database
		db.session.add(Reports(token=form.url.data, message=form.message.data))
		db.session.commit()

		# Return the thanks page
		return render_template("thanks.html")

	# Else if the form was invalid or not submitted
	else:
		# Return the report page with the form
		return render_template("report.html", form=form)

# Donate route
@app.route("/donate")
def donate():
	return render_template("donate.html")

# Removed url route
@app.route("/removed")
def removed():
	return render_template("removed.html")

# Error handling routes
@app.errorhandler(404)
def error_404(error):
	return render_template("error.html", error_code=404, error_message="Not Found"), 404

@app.errorhandler(500)
def error_500(error):
	return render_template("error.html", error_code=500, error_message="Internal Server Error"), 500
