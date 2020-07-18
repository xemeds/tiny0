from flask import render_template, redirect, request, flash, url_for
from tiny0 import app
from tiny0.forms import URLForm
#from tiny0.models import URLs
#from token import gen_valid_token

# Index Page
@app.route("/", methods=['GET', 'POST'])
def index():
	# Get request
	if request.method == "GET":
		# Create a instance of the form
		form = URLForm()

		# Return the index page with the form
		return render_template("index.html", form=form)

	# Post request
	else:
		# Create a instance of the form
		form = URLForm()

		# If the form was valid
		if form.validate_on_submit():
			return "Valid URL: " + form.url.data

		return render_template("index.html", form=form)
