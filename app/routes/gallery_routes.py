from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_gallery():
    # Placeholder for gallery list
    return [
        {"id": 1, "url": "https://example.com/img1.jpg", "caption": "Action Shot 1"},
        {"id": 2, "url": "https://example.com/img2.jpg", "caption": "Action Shot 2"}
    ]
