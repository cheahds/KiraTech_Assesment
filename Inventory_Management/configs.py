from pydantic_settings import SettingsConfigDict, BaseSettings


class Configs(BaseSettings):
    DJANGO_KEY: str
    API_HOSTNAME: str
    API_PORT: int

    model_config = SettingsConfigDict(env_file="../.env")


CONFIGS = Configs()
