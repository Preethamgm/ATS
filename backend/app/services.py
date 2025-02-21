from sqlalchemy.orm import Session
from fastapi import HTTPException
from .models import Job, Applicant, Application
from .schemas import JobCreate, ApplicantCreate, ApplicationCreate
from datetime import datetime

# ------------------- Job Services -------------------

def create_job(db: Session, job_data: JobCreate):
    db_job = Job(**job_data.dict())
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

def get_jobs(db: Session):
    return db.query(Job).all()

def get_job_by_id(db: Session, job_id: int):
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job

# ------------------- Applicant Services -------------------

def create_applicant(db: Session, applicant_data: ApplicantCreate):
    db_applicant = Applicant(**applicant_data.dict())
    db.add(db_applicant)
    db.commit()
    db.refresh(db_applicant)
    return db_applicant

def get_applicants(db: Session):
    return db.query(Applicant).all()

def get_applicant_by_id(db: Session, applicant_id: int):
    applicant = db.query(Applicant).filter(Applicant.id == applicant_id).first()
    if not applicant:
        raise HTTPException(status_code=404, detail="Applicant not found")
    return applicant

# ------------------- Application Services -------------------

def apply_for_job(db: Session, application_data: ApplicationCreate):
    job = db.query(Job).filter(Job.id == application_data.job_id).first()
    applicant = db.query(Applicant).filter(Applicant.id == application_data.applicant_id).first()

    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    if not applicant:
        raise HTTPException(status_code=404, detail="Applicant not found")

    db_application = Application(
        job_id=application_data.job_id,
        applicant_id=application_data.applicant_id,
        status="Pending",
        applied_at=datetime.utcnow()
    )
    db.add(db_application)
    db.commit()
    db.refresh(db_application)
    return db_application

def get_applications(db: Session):
    return db.query(Application).all()

def get_application_by_id(db: Session, application_id: int):
    application = db.query(Application).filter(Application.id == application_id).first()
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    return application
