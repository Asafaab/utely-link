from fastapi import APIRouter

router = APIRouter(prefix="/datos", tags=["Datos"])


@router.get("/ping")
async def ping():
    return {"status": "ok"}
