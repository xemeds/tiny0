from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, ValidationError
from wtforms.validators import DataRequired, Length, Optional
from tiny0.config import WEBSITE_DOMAIN
from tiny0 import db
from tiny0.models import URL

# Validates a url
def validate_URL(form, field):
	# Make sure the url is not too short or long
	if len(field.data) < 4 or len(field.data) > 2000:
		return

	# If the url contains spaces or does not have any dots
	if (" " in field.data) or not("." in field.data):
		# Raise a ValidationError
		raise ValidationError("Invalid URL")

	# If the url starts with a dot after http:// or after https:// or just starts with a dot
	if field.data.lower().startswith("http://.") or field.data.lower().startswith("https://.") or field.data.startswith("."):
		# Raise a ValidationError
		raise ValidationError("Invalid URL")

	# If the url starts with a slash after http:// or after https:// or just starts with a slash
	if field.data.lower().startswith("http:///") or field.data.lower().startswith("https:///") or field.data.startswith("/"):
		# Raise a ValidationError
		raise ValidationError("Invalid URL")

	# If the url ends with a dot and it is the only dot
	if field.data.endswith(".") and field.data.count(".") == 1:
		# Raise a ValidationError
		raise ValidationError("Invalid URL")

	# If the url contains the websites domain
	if WEBSITE_DOMAIN in field.data.lower():
		# Raise a ValidationError
		raise ValidationError("Invalid URL")

	# If the URL does not start with http:// and https://
	if not(field.data.lower().startswith("http://")) and not(field.data.lower().startswith("https://")):
		# Add http:// to the beginning of the URL
		field.data = "http://" + field.data

# Validates a token
def validate_token(form, field):
	# Make sure the token is not too short or long
	if len(field.data) < 6 or len(field.data) > 16:
		return

	# If the token is the same as a pages route
	if field.data == "tracker" or field.data == "lookup" or field.data == "report" or field.data == "donate" or field.data == "removed":
		# Raise a ValidationError
		raise ValidationError("Token already exists")

	# For each character in the token
	for char in field.data:
		# If it is not a valid character
		if not(char.isalpha()) and not(char.isdigit()) and not(char == "_") and not(char == '-'):
			# Raise a ValidationError
			raise ValidationError("Token contains invalid characters")

	# If the token exists in the database
	if db.session.query(db.session.query(URL).filter_by(token=field.data).exists()).scalar():
		# Raise a ValidationError
		raise ValidationError("Token already exists")

# Validates a short url
def validate_short_URL(form, field):
	# Make sure the short url is not too short or long
	if len(field.data) < (len(WEBSITE_DOMAIN) + 7) or len(field.data) > (len(WEBSITE_DOMAIN) + 25):
		return

	# If the start of the short url is not valid
	if (not(field.data.lower().startswith(WEBSITE_DOMAIN + "/"))
		and not(field.data.lower().startswith("http://" + WEBSITE_DOMAIN + "/"))
		and not(field.data.lower().startswith("https://" + WEBSITE_DOMAIN + "/"))):
		# Raise a ValidationError
		raise ValidationError("Invalid short URL")

	# Get the token of the short url
	if field.data.lower().startswith(WEBSITE_DOMAIN + "/"):
		token = field.data[len(WEBSITE_DOMAIN) + 1:]

	elif field.data.lower().startswith("http://" + WEBSITE_DOMAIN + "/"):
		token = field.data[len(WEBSITE_DOMAIN) + 8:]

	elif field.data.lower().startswith("https://" + WEBSITE_DOMAIN + "/"):
		token = field.data[len(WEBSITE_DOMAIN) + 9:]

	# If the token of the short url does not exist in the database
	if not db.session.query(db.session.query(URL).filter_by(token=token).exists()).scalar():
		# Raise a ValidationError
		raise ValidationError("That short URL does not exists")

	# After all the validation is done set the forms url value as the token
	field.data = token

class URLForm(FlaskForm):
	url = StringField(validators=[DataRequired(), Length(min=4, max=2000, message="Invalid URL length"), validate_URL])

	token = StringField(validators=[Optional(), Length(min=6, max=16, message="Invalid token length"), validate_token])

	submit = SubmitField("Shorten")

class ShortURLForm(FlaskForm):
	url = StringField(validators=[DataRequired(), Length(min=len(WEBSITE_DOMAIN) + 7, max=len(WEBSITE_DOMAIN) + 25, message="Invalid short URL"), validate_short_URL])

	submit = SubmitField("Submit")

class ReportForm(FlaskForm):
	url = StringField(validators=[DataRequired(), Length(min=len(WEBSITE_DOMAIN) + 7, max=len(WEBSITE_DOMAIN) + 25, message="Invalid short URL"), validate_short_URL])

	message = TextAreaField(validators=[DataRequired(), Length(1, 200, message="Message too short or too long")])

	submit = SubmitField("Submit")
