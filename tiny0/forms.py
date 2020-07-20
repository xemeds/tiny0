from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length
from tiny0.config import WEBSITE_DOMAIN

# Validates a URL
def validate_URL(form, field):
	# Make sure the url is not too short or long
	if len(field.data) < 4 or len(field.data) > 2000:
		return

	# If the url contains spaces or does not have any dots
	if field.data.count(" ") > 0 or field.data.count(".") == 0:
		# Raise a ValidationError
		raise ValidationError("Invalid URL")

	# If the url starts with a dot after http:// or after https:// or just starts with a dot
	if field.data.startswith("http://.") or field.data.startswith("https://.") or field.data.startswith("."):
		# Raise a ValidationError
		raise ValidationError("Invalid URL")

	# If the url ends with a dot and it is the only dot
	if field.data.endswith(".") and field.data.count(".") == 1:
		# Raise a ValidationError
		raise ValidationError("Invalid URL")

	# If the url contains the websites domain
	if WEBSITE_DOMAIN in field.data:
	# Raise a ValidationError
		raise ValidationError("Invalid URL")

	# If the URL does not start with http:// and https://
	if not(field.data.startswith("http://")) and not(field.data.startswith("https://")):
		# Add https:// to the beginning of the URL
		field.data = "https://" + field.data


class URLForm(FlaskForm):
	url = StringField(validators=[DataRequired(), 
		Length(min=4, max=2000, message="Invalid URL Length"), 
		validate_URL])

	submit = SubmitField("Shorten")
