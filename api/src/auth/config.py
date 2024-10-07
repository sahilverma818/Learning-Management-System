import configparser
from pydantic_settings import BaseSettings

config = configparser.ConfigParser()
config.read('config.ini')
class Settings(BaseSettings):
    SECRET_KEY: str = config['settings']['SECRET_KEY']
    ALGORITHM: str = config['settings']['ALGORITHMS']
    ACCESS_TOKENS_EXPIRY_MINUTES: int = config['settings']['ACCESS_TOKENS_EXPIRY_MINUTES']
    REFRESH_TOKENS_EXPIRY_MINUTES: int = config['settings']['REFRESH_TOKENS_EXPIRY_MINUTES']

settings = Settings()