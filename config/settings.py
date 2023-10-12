from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "BanpayTechnicalTest"
    database_url: str = ""
    enviroment: str = "development"

    class Config:
        env_file = ".env"

settings = Settings()