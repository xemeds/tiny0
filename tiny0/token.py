from tiny0.models import URL
from secrets import choice

# The characters used to generate the token
token_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz_-"

def gen_valid_token():
	while True:
		# Generate a token
		token = "".join(choice(token_characters) for i in range(8))

		# If the token does not exists in the database
		if not URL.query.filter_by(token=token).first():
			# Break the loop
			break

	# Return the token
	return token

