from models import db


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(128))

    @property
    def serialize(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }

    @classmethod
    def create(cls, values: dict):
        return cls(name=values['name'], email=values['email'])

    def __repr__(self):
        return f'<User id={id} name={self.name} email={self.email}>'
