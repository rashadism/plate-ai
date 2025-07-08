from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import UUID
from datetime import datetime

class MealComponentBase(BaseModel):
    name: str
    calories: float
    fat_g: float
    protein_g: float
    carbs_g: float

class MealComponentCreate(MealComponentBase):
    pass

class MealComponentRead(MealComponentBase):
    component_id: UUID

class MealBase(BaseModel):
    meal_date: datetime
    description: Optional[str] = None

class MealCreate(MealBase):
    components: List[MealComponentCreate]

class MealRead(MealBase):
    mealId: UUID = Field(..., alias="meal_id")
    components: List[MealComponentRead]
    created_at: datetime
    updated_at: datetime

class MealSummary(BaseModel):
    mealId: UUID = Field(..., alias="meal_id")
    meal_date: datetime
    description: Optional[str]
    total_calories: float 