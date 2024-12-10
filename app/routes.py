from typing import Dict

from fastapi import APIRouter, Request

from app.data_type_detector import get_data_type
from app.database import db_client
from app.schemas import FormData
from app.template_service import TemplateService

router = APIRouter()


@router.post("/get_form", response_model=Dict[str, str], status_code=200)
async def get_form(request: Request):
    """
    Обрабатывает POST-запрос для получения формы на основе входящих данных.

    Args:
        request (Request): Объект запроса FastAPI, содержащий данные формы.

    Returns:
        Dict[str, str]: Словарь с именем формы, если она найдена, или словарь с типами входящих данных.
    """
    data = await request.form()
    data_dict = FormData(**data).model_dump()
    data_types = get_data_type(data_dict)
    template_repository = TemplateService(db_client)
    form_name = await template_repository.get_templates(data_types)
    if form_name:
        return form_name
    return data_types
