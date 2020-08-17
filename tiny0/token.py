from tiny0 import db
from tiny0.models import URL
from secrets import choice

# The characters used to generate the token
token_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz_-"

def gen_valid_token():
	while True:
		# Generate a token
		token = "".join(choice(token_characters) for i in range(6))

		# If the token does not exists in the database
		if not db.session.query(db.session.query(URL).filter_by(token=token).exists()).scalar():
			# Break the loop
			break

	# Return the token
	return token

