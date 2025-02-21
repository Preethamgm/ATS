from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Job, Applicant, Application
from .schemas import JobCreate, JobResponse, ApplicantCreate, ApplicantResponse, ApplicationCreate, ApplicationResponse

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ------------------- Job Endpoints -------------------

@router.post("/jobs/", response_model=JobResponse)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    db_job = Job(**job.dict())
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

@router.get("/jobs/", response_model=list[JobResponse])
def get_jobs(db: Session = Depends(get_db)):
    return db.query(Job).all()

@router.get("/jobs/{job_id}", response_model=JobResponse)
def get_job(job_id: int, db: Session = Depends(get_db)):
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job

# ------------------- Applicant Endpoints -------------------

@router.post("/applicants/", response_model=ApplicantResponse)
def create_applicant(applicant: ApplicantCreate, db: Session = Depends(get_db)):
    db_applicant = Applicant(**applicant.dict())
    db.add(db_applicant)
    db.commit()
    db.refresh(db_applicant)
    return db_applicant

@router.get("/applicants/", response_model=list[ApplicantResponse])
def get_applicants(db: Session = Depends(get_db)):
    return db.query(Applicant).all()

@router.get("/applicants/{applicant_id}", response_model=ApplicantResponse)
def get_applicant(applicant_id: int, db: Session = Depends(get_db)):
    applicant = db.query(Applicant).filter(Applicant.id == applicant_id).first()
    if not applicant:
        raise HTTPException(status_code=404, detail="Applicant not found")
    return applicant

# ------------------- Application Endpoints -------------------

@router.post("/applications/", response_model=ApplicationResponse)
def apply_for_job(application: ApplicationCreate, db: Session = Depends(get_db)):
    job = db.query(Job).filter(Job.id == application.job_id).first()
    applicant = db.query(Applicant).filter(Applicant.id == application.applicant_id).first()

    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    if not applicant:
        raise HTTPException(status_code=404, detail="Applicant not found")

    db_application = Application(**application.dict())
    db.add(db_application)
    db.commit()
    db.refresh(db_application)
    return db_application

@router.get("/applications/", response_model=list[ApplicationResponse])
def get_applications(db: Session = Depends(get_db)):
    return db.query(Application).all()

@router.get("/applications/{application_id}", response_model=ApplicationResponse)
def get_application(application_id: int, db: Session = Depends(get_db)):
    application = db.query(Application).filter(Application.id == application_id).first()
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    return application
