from typing import Optional, List
from pydantic import BaseModel, EmailStr, validator



class CreatePurchaseModel(BaseModel):
    price: float
    currency: str
    tags: List[str]