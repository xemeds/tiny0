from flask import render_template, redirect, request, url_for
from tiny0 import app
from tiny0.forms import URLForm
#from tiny0.models import URLs
#from token import gen_valid_token

# Index Page
@app.route("/", methods=['GET', 'POST'])
def index():
	# Create a instance of the form
	form = URLForm()

	# If the form was valid
	if form.validate_on_submit():
		return render_template("url.html", url=form.url.data)

	# If the form was invalid or not submitted
	else:
		# Return the index page with the form
		return render_template("index.html", form=form)
