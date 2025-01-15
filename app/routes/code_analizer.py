from fastapi import APIRouter, Depends, HTTPException
from services import CodeAnalyzerService
from adapters.dtos import CodeDTO, ResponseDTO

router = APIRouter(
    prefix="/analyze-code",
    tags=["CodeAnalysis"],
)

@router.post("/", response_model=ResponseDTO)
def ctrl_analyze_code(
    data: CodeDTO,
    service: CodeAnalyzerService = Depends()
):
    try:
        result = service.code_analizer(data.code)
        return ResponseDTO(message="Análise concluída com sucesso.", data=result)
    except Exception as e:
        return ResponseDTO( message=str(e))
