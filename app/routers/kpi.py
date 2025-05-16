from fastapi import APIRouter

router = APIRouter(prefix="/kpi", tags=["KPIs"])


@router.get("/")
async def kpi_generales():
    # Valores tontos de ejemplo
    return {"facturas_pendientes": 4, "sincronizaciones_activas": 2}
