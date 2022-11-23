from sqlalchemy.orm import relationship
from models import db
from models.file import File
from models.user import User

project_user = db.Table('project_user', 
    db.Column('id', db.Integer, primary_key=True, autoincrement=True),
    db.Column('project_id', db.ForeignKey('project.id')),
    db.Column('user_id', db.ForeignKey('user.id')))

class Project(db.Model):
    __tablename__ = "project"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    start_date = db.Column(db.DateTime)
    files = relationship(File, uselist=True)
    users = relationship(User, secondary=project_user, backref='users')

    @property
    def serialize(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'start_date': self.start_date,
            'files': [file.serialize for file in self.files],
            'users': [user.serialize for user in self.users]
        }

    @classmethod
    def create(cls, values: dict):
        project = cls(name=values['name'], start_date=values['start_date'])
        if('users' in values.keys()):
            users = [User.create(user) for user in values['users']]
            project.users = users
        return project

    def __repr__(self):
        return f'<Project id={self.id} name={self.name} start_date={self.start_date}>'