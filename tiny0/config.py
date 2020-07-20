import json

with open("tiny0/config.json", "r") as config_file:

	config_data = json.load(config_file)

	WEBSITE_DOMAIN = config_data.get("WEBSITE_DOMAIN")
	SECRET_KEY = config_data.get("SECRET_KEY")
	SQLALCHEMY_DATABASE_URI = config_data.get("SQLALCHEMY_DATABASE_URI")
