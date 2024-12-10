import json

from motor.motor_asyncio import AsyncIOMotorClient

from config import settings


class DatabaseClient:
    """Класс для работы с базой данных MongoDB."""
    def __init__(self, database_uri, db_name, collection, templates_path=None):
        """
        Инициализирует экземпляр DatabaseClient.

        Args:
            database_uri (str): URI для подключения к базе данных.
            db_name (str): Имя базы данных.
            collection (str): Имя коллекции в базе данных.
            templates_path (str, optional): Путь к файлу с шаблонами. По умолчанию None.
        """
        self.templates_path = templates_path
        self.database_url = database_uri
        self.collection = collection
        self.db_name = db_name
        self.client = None

    async def connect(self):
        """
        Устанавливает соединение с базой данных.

        Если указан путь к шаблонам, загружает их в коллекцию.
        """
        try:
            self.client = AsyncIOMotorClient(self.database_url)
            if self.templates_path:
                await self.set_templates()
        except Exception as e:
            print(f"Ошибка подключения к базе данных: {e}")

    async def close(self):
        """Закрывает соединение с базой данных."""
        if self.client is None:
            return
        try:
            self.client.close()
        except Exception as e:
            print(f"Ошибка закрытия соединения с базой данных: {e}")
        finally:
            self.client = None

    async def get_db(self):
        """
        Получает доступ к базе данных.

        Если соединение еще не установлено, вызывает метод connect.

        Returns:
            Database: Объект базы данных.
        """
        if self.client is None:
            await self.connect()
        return self.client[self.db_name]

    async def set_templates(self):
        """
        Загружает шаблоны из файла в коллекцию базы данных.

        Очищает коллекцию перед загрузкой новых шаблонов.
        """
        db = await self.get_db()
        templates_collection = db[self.collection]
        await templates_collection.drop()
        templates_collection = db[self.collection]
        with open(self.templates_path, "r") as f:
            templates = json.load(f)
        await templates_collection.insert_many(templates)


db_client = DatabaseClient(
    database_uri=settings.mongodb.uri,
    db_name=settings.mongodb.db_name,
    templates_path=settings.mongodb.templates_path,
    collection=settings.mongodb.collection,
)
