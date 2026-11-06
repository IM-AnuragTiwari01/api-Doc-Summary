from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra = "ignore")
    OPENAI_API_KEY: str
    OPENAI_MODEL: str
    DB_CONNECTION: str
    
settings = Settings()