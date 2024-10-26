import configparser
from pydantic_settings import BaseSettings

config = configparser.ConfigParser()
config.read('config.ini')
class Settings(BaseSettings):
    SECRET_KEY: str = config['settings']['SECRET_KEY']
    ALGORITHM: str = config['settings']['ALGORITHMS']
    ACCESS_TOKENS_EXPIRY_MINUTES: int = config['settings']['ACCESS_TOKENS_EXPIRY_MINUTES']
    REFRESH_TOKENS_EXPIRY_MINUTES: int = config['settings']['REFRESH_TOKENS_EXPIRY_MINUTES']
    FORGET_PASSWORD_EXPIRY_MINUTES: int = config['settings']['FORGET_PASSWORD_EXPIRY_MINUTES']
    EMAIL_ADDRESS: str = config['gmail']['EMAIL_ADDRESS']
    EMAIL_PASSWORD: str = config['gmail']['EMAIL_PASSWORD']
    SMTP_SERVER: str = config['gmail']['SMTP_SERVER']
    SMTP_PORT: int = config['gmail']['SMTP_PORT']

settings = Settings()