from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_tournaments():
    # Placeholder for tournament list
    return [
        {"id": 1, "name": "Summer Championship", "status": "Open"},
        {"id": 2, "name": "Winter League", "status": "Closed"}
    ]

@router.post("/create")
def create_tournament_trigger():
    # Hit create button no payload required just hit create
    return {"message": "Tournament creation triggered successfully"}
