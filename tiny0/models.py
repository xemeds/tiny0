from tiny0 import db

class URL(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	token = db.Column(db.String(8), index=True, unique=True, nullable=False)
	url = db.Column(db.String(2000), nullable=False)

	def __repr__(self):
		return f"'{self.id}' '{self.token}' '{self.url}'"
