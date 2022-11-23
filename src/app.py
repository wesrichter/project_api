from models import create_app, db
from models.project import Project
from models.file import File
from flask import request

app = create_app('DevelopmentConfig')
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/project', methods=['GET'])
def get_projects():
    result = db.paginate(db.select(Project).order_by(Project.start_date))
    return [r.serialize for r in result]

@app.route('/project/<int:id>', methods=['GET'])
def get_project(id):
    result = db.session.query(Project).where(Project.id == id).first()
    return result.serialize

@app.route('/project', methods=['POST'])
def create_projects():
    projects = []
    for project in request.get_json():
        new_project = Project.create(project)
        db.session.add(new_project)
        db.session.commit()
        db.session.flush()
        db.session.refresh(new_project)

        if('files' in project.keys()):
            files = [File.create(file, new_project.id) for file in project['files']]
            db.session.add_all(files)
            db.session.commit()

        projects.append(new_project.serialize)
    return projects
