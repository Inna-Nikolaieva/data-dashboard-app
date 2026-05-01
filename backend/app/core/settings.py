from pathlib import Path, PosixPath

from dotenv import load_dotenv
from pydantic import model_validator
from pydantic_settings import BaseSettings

load_dotenv()


class DbSettings(BaseSettings):
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_NAME: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    class Config:
        env_file = ".env"
        extra = "allow"


class Settings(BaseSettings):
    HOST: str
    PORT: int
    RELOAD: bool

    DEBUG: bool

    BASE_DIR: PosixPath
    ROOT_DIR: PosixPath

    DB: DbSettings = DbSettings()

    DUMMYJSON_BASE_API_URL: str

    class Config:
        env_file = ".env"
        extra = "allow"

    @model_validator(mode="before")
    def _dynamic_settings(cls, values):
        values["BASE_DIR"] = Path(__file__).resolve().parent.parent
        values["ROOT_DIR"] = Path(__file__).resolve().parent.parent.parent

        return values


settings = Settings()
