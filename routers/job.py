from fastapi import APIRouter,Depends
from schemas.job import JobCreate,JobUpdate,JobResponse
from ..database import get_db,SessionLocal
from sqlalchemy.orm import session

router =APIRouter(prefix="/job",tags=["job"])
jobs=[]

@router.post("/",,status_code=status.HTTP_201_CREATED,response_model=JobResponse)
def create_job(job,JobCreate,db:session=Depends(get_db)):
    db_job=job(**job.dict())
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

@router.get("/")
def get_all_job():
    return jobs

@router.get("/{job_id}")
def get_company(job_id:int):
    return jobs[job_id]



@router.put("/{job_id}")
def update_job(job_id:int,job:JobUpdate):
    jobs[job_id]=job
    return jobs


@router.delete("/{job_id}")
def delete_job(job_id:int):
    jobs.pop(job_id)
    return jobs



@router.get("/")
def read_job():
    return {"job":"Job root"}

@router.get("/(job_id)")
def read_job(job_id:int):
    return{"job_id":job_id}