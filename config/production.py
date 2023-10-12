from .settings import Settings

class ProductionSettings(Settings):
    database_url: str = ""
    enviroment: str = "development"

    class Config:
        env_file = ".env"

production_settings = ProductionSettings()