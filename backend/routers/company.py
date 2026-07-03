from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from backend.utils.oauth2 import get_current_user, role_required
from backend.schemas.company import CompanyCreate, CompanyUpdate, CompanyResponse
from backend.models.company import Company
from backend.database import get_db

router = APIRouter(
    prefix="/company",
    tags=["company"]
)

@router.post("/", response_model=CompanyResponse, status_code=status.HTTP_201_CREATED)
def create_company(company: CompanyCreate, db: Session = Depends(get_db), current_user=Depends(role_required(["admin"]))):
    db_company = Company(**company.model_dump())
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company


@router.get("/", response_model=list[CompanyResponse],status_code=status.HTTP_200_OK)
def get_all_company(db: Session = Depends(get_db),current_user=Depends(get_current_user)):
    companies=db.query(Company).all()
    return companies


@router.get("/{company_id}", response_model=CompanyResponse)
def get_company(company_id: int, db: Session = Depends(get_db),current_user=Depends(get_current_user)):
    company = db.query(Company).filter(Company.id == company_id).first()

    if not company:
        raise HTTPException(status_code=404, detail="Company not found")

    return company


@router.put("/{company_id}", response_model=CompanyResponse, status_code=status.HTTP_200_OK)
def update_company(company_id: int, company: CompanyUpdate, db: Session = Depends(get_db), current_user=Depends(role_required(["admin"]))):
    db_company = db.query(Company).filter(Company.id == company_id).first()
    if not db_company:
        raise HTTPException(status_code=404, detail="Company not found")
    update_data = company.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_company, key, value)
    db.commit()
    db.refresh(db_company)
    return db_company


@router.delete("/{company_id}")
def delete_company(company_id: int, db: Session = Depends(get_db)):
    db_company = db.query(Company).filter(Company.id == company_id).first()

    if not db_company :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Company not found")
    db.delete(db_company)
    db.commit()
    return {"message": "Company deleted successfully"}