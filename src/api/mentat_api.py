from fastapi import FastAPI, Depends, HTTPException
from sql.sql import get_db_session
from models import Application, ProjectCreate, get_application_schema, get_project_create_schema
from sqlalchemy.orm import Session

app = FastAPI()

# get application schema
@app.get("/schema/application")
async def get_application_schema():
    schema = get_application_schema()
    print(schema)
    return {f"{schema}"}


# get project create schema
@app.get("/schema/project_create")
async def get_project_schema():
    schema = get_project_create_schema()
    print(schema)
    return {f"{schema}"}


# create a new project
@app.post("/project/create")
async def create_project(project: ProjectCreate, db: Session = Depends(get_db_session)):

    # check if project already exists
    existing_project = db.query(Project).filter(Project.project_name == project.project_name).first()
    if existing_project:
        raise HTTPException(status_code=400, detail="Project already exists")

    # create the project
    new_project = Project(project_name=project.project_name)

    # add and commit project to db
    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    return {"message": "Project created", "Project ID": new_project.id}


# add an application to a project
@app.post("/project/{project_id}/add_application")
async def add_application(project_id: int, application: Application):
    return {"project_id": project_id, "application": application}

