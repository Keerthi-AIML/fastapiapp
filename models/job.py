from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)

    company_id = Column(Integer, ForeignKey("companies.id"))

    # IMPORTANT: THIS FIXES YOUR ERROR
    company = relationship("Company", back_populates="jobs")