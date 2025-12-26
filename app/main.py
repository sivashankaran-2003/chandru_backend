from fastapi import FastAPI
from app.routes.user_routes import router as user_router
from app.routes.auth_routes import router as auth_router
from app.routes.tournament_routes import router as tournament_router
from app.routes.fixtures_routes import router as fixtures_router
from app.routes.gallery_routes import router as gallery_router

app = FastAPI(title="Chandru Backend")

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(tournament_router, prefix="/tournaments", tags=["Tournaments"])
app.include_router(fixtures_router, prefix="/fixtures", tags=["Fixtures"])
app.include_router(gallery_router, prefix="/gallery", tags=["Gallery"])

@app.get("/")
def root():
    return {"message": "Backend running 🚀"}
