import fastapi
import uvicorn
from core.config import settings
from fastapi.middleware.cors import CORSMiddleware
from crud_users.routes import router as users
from crud_records.routes import router as records
from auth.routes import router as auth
from database.services import create_database

def start_application():
    
    app = fastapi.FastAPI(
        title=settings.PROJECT_TITLE,
        description=settings.DESCRIPTION,
        version=settings.PROJECT_VERSION,
        openapi_tags=settings.TAGS,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True,
    )

    return app

try:
    create_database()
except Exception as ex:
    print(ex)

app = start_application()
app.include_router(auth)
app.include_router(users)
app.include_router(records)


if __name__ == "__main__":
    uvicorn.run(app, port=8005)