from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str = "sfhsdjfdjfsjdfkdsnfsndfsdnflsdsldkfsd"
    ALGORITHM: str = "HS256"
    ACCESS_TOKENS_EXPIRY_MINUTES: int = 30
    REFRESH_TOKENS_EXPIRY_MINUTES: int = 45

    class Config:
        env_file = ".env"

settings = Settings()