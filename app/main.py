from fastapi import FastAPI

from app.routers.sincronizacion import router as sync_router
from app.routers.facturacion    import router as factura_router
from app.routers.kpi            import router as kpi_router
from app.models.datos           import router as datos_router

app = FastAPI(
    title="UTELY Link",
    description="API de integración Elyon – SINTAD, MANTRA y SISPAC",
    version="1.0.0",
)

# Saludo
@app.get("/")
async def root():
    return {"message": "UTELY Link corriendo correctamente 🚀"}

# Rutas de negocio
app.include_router(sync_router)
app.include_router(factura_router)
app.include_router(kpi_router)
app.include_router(datos_router)
