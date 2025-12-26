from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_fixtures():
    # Placeholder for fixtures list
    return [
        {"id": 101, "team_a": "Strikers", "team_b": "Warriors", "time": "2025-01-10T15:00:00"},
        {"id": 102, "team_a": "Eagles", "team_b": "Hawks", "time": "2025-01-11T16:00:00"}
    ]
