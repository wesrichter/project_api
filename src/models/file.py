from models import db


class File(db.Model):
    __tablename__ = "file"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128))
    file_type = db.Column(db.String(16))
    
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))

    @property
    def serialize(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'file_type': self.file_type,
        }

    @classmethod
    def create(cls, values: dict, project_id: int):
        return cls(name=values['name'], file_type=values['file_type'], project_id=project_id)

    def __repr__(self):
        return f'<File id={self.id} name={self.name} file_type={self.file_type}'