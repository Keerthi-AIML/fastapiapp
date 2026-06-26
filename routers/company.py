from fastapi import APIRouter

router=APIRouter(prefix="/company",tags=["company"])

@router.get("/")
def read_comapany():
    return {"company":"company root"}