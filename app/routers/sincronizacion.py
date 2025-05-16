from fastapi import APIRouter, status
from pydantic import BaseModel
from datetime import datetime

router = APIRouter(prefix="/sync", tags=["Sincronización"])


class SyncRequest(BaseModel):
    origen: str  # "SINTAD", "MANTRA", "SISPAC"
    destino: str
    tipo_dato: str  # p. ej. "facturas", "kpis"


@router.post("/", status_code=status.HTTP_202_ACCEPTED)
async def iniciar_sincronizacion(req: SyncRequest):
    # ✨ Aquí iría la llamada real a tu servicio de integración.
    # Por ahora respondemos algo simulado:
    tarea_id = f"TASK-{int(datetime.utcnow().timestamp())}"
    return {
        "tarea_id": tarea_id,
        "msg": f"Sincronización {req.tipo_dato} {req.origen}->{req.destino} aceptada"
    }


@router.get("/{tarea_id}")
async def estado_sincronizacion(tarea_id: str):
    # Simulación: siempre “en progreso”
    return {"tarea_id": tarea_id, "estado": "en progreso"}
