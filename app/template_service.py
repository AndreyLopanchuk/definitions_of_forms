from config import settings


class TemplateService:
    """Сервис для работы с шаблонами в базе данных."""
    def __init__(self, db_client):
        self.db_client = db_client

    async def get_templates(self, data_types):
        """
        Получает шаблоны из базы данных по указанным типам данных.

        Args:
            data_types: Словарь с условиями поиска шаблонов в базе данных.

        Returns:
            dict: Шаблон, соответствующий условиям поиска, или None, если шаблон не найден.
        """
        db = await self.db_client.get_db()
        collection = db[settings.mongodb.collection]
        return await collection.find_one(data_types, projection={"name": 1, "_id": 0})
