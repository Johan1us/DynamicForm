from fastapi import APIRouter, status

from typing import Dict
from app.models import ProblemDescription, ProblemDescriptionResponse

router = APIRouter()


async def call_ai_service(description: str) -> Dict:
    # Create a fake response for now
    response = {
        "location": "Unknown",
        "specific_location": "Unknown",
        "category": "Unknown",
        "part": "Unknown"
    }

    return response


@router.post("/", response_model=ProblemDescriptionResponse, status_code=status.HTTP_201_CREATED)
async def receive_problem_description(description: ProblemDescription):
    # Call AI/LLM API for automatic field filling
    fields = await call_ai_service(description.description)

    # Construct response data
    response_data = {
        "description": description.description,
        "location": fields.get("location", "Unknown"),
        "specific_location": fields.get("specific_location", "Unknown"),
        "category": fields.get("category", "Unknown"),
        "part": fields.get("part", "Unknown")
    }

    return response_data
