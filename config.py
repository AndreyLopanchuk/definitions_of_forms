from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class MongoDBSettings(BaseSettings):
    uri: str = "mongodb://mongo:27017"
    db_name: str = "templates"
    collection: str = "forms"
    templates_path: Optional[str] = "templates/templates.json"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=False)
    mongodb: MongoDBSettings = MongoDBSettings()


settings = Settings()
