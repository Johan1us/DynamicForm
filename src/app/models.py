from pydantic import BaseModel


class ProblemDescription(BaseModel):
    description: str


class ProblemDescriptionResponse(BaseModel):
    description: str
    location: str
    specific_location: str
    category: str
    part: str
