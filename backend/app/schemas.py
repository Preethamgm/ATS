from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# ------------------- Job Schemas -------------------

class JobBase(BaseModel):
    title: str
    description: str
    company: str
    location: Optional[str] = None

class JobCreate(JobBase):
    pass  # Used for creating a job (inherits fields from JobBase)

class JobResponse(JobBase):
    id: int
    posted_at: datetime

    class Config:
        from_attributes = True

# ------------------- Applicant Schemas -------------------

class ApplicantBase(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None
    resume: Optional[str] = None  # Path to uploaded resume

class ApplicantCreate(ApplicantBase):
    pass  # Used for creating an applicant

class ApplicantResponse(ApplicantBase):
    id: int

    class Config:
        from_attributes = True

# ------------------- Application Schemas -------------------

class ApplicationBase(BaseModel):
    job_id: int
    applicant_id: int
    status: Optional[str] = "Pending"  # Default status is "Pending"

class ApplicationCreate(ApplicationBase):
    pass  # Used for submitting a job application

class ApplicationResponse(ApplicationBase):
    id: int
    applied_at: datetime

    class Config:
        from_attributes = True
