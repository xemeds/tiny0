from flask import render_template, redirect, request, flash, url_for
from tiny0 import app
#from tiny0.forms import URLForm
#from tiny0.models import URLs
#from token import gen_valid_token

@app.route("/")
def index():
	return "Hello, world!"
