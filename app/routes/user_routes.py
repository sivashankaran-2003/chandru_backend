from fastapi import APIRouter
from app.schemas.user_schema import UserCreate, UserOut
from app.models.user_model import user_collection
from app.auth_utils import get_password_hash

router = APIRouter()

@router.post("/", response_model=UserOut)
def create_user(user: UserCreate):
    user_dict = user.dict()
    user_dict["password"] = get_password_hash(user.password)
    user_collection.insert_one(user_dict)
    return user_dict

@router.get("/")
def get_users():
    users = list(user_collection.find({}, {"_id": 0}))
    return users
