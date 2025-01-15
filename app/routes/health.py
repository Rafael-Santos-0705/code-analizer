from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health():
    """
    Retorna o status do agente.
    """
    return {"status": "ok"}
