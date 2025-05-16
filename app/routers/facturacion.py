from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/facturas", tags=["Facturación"])


class Factura(BaseModel):
    cliente_id: int
    monto: float


# base de datos simulada en memoria
_FAKE_DB: dict[int, Factura] = {}


@router.post("/")
async def crear_factura(factura: Factura):
    _FAKE_DB[len(_FAKE_DB) + 1] = factura
    return {"msg": "Factura registrada", "total": len(_FAKE_DB)}


@router.get("/{cliente_id}")
async def obtener_factura(cliente_id: int):
    return _FAKE_DB.get(cliente_id, {"error": "No existe"})
