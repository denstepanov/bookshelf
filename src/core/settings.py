from pydantic import BaseSettings

# Для парсинга настроек требуется пакет python-dotenv
class Settings(BaseSettings):
    db_host: str
    db_port: int
    db_name: str
    db_user: str
    db_user_password: str

settings = Settings(_env_file="src/core/dev.env", _env_file_encoding="utf-8")