from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    """
    Application configuration class.

    This class uses Pydantic's BaseSettings to manage configuration variables,
    allowing for easy loading from environment variables and .env files.

    Attributes:
        APP_NAME (str): The name of the application.
        DEBUG (bool): Debug mode flag.
        OPENAI_API_KEY (str): API key for OpenAI services.
        ANTHROPIC_API_KEY (str): API key for Anthropic services.
        REDIS_HOST (str): Hostname for the Redis server.
        REDIS_PORT (int): Port number for the Redis server.
        REDIS_DB (int): Redis database number to use.
        DEFAULT_MODEL (str): Default LLM model to use.
        MAX_TOKENS (int): Maximum number of tokens for LLM responses.
        LOG_LEVEL (str): Logging level for the application.
        JAEGER_HOST (str): Hostname for the Jaeger tracing server.
        JAEGER_PORT (int): Port number for the Jaeger tracing server.
    """

    APP_NAME: str = "LLM-Powered Microservice"
    DEBUG: bool = Field(False, env="DEBUG")
    
    # API Keys
    OPENAI_API_KEY: str = Field(..., env="OPENAI_API_KEY")
    ANTHROPIC_API_KEY: str = Field(..., env="ANTHROPIC_API_KEY")
    
    # Redis Configuration
    REDIS_HOST: str = Field("localhost", env="REDIS_HOST")
    REDIS_PORT: int = Field(6379, env="REDIS_PORT")
    REDIS_DB: int = Field(0, env="REDIS_DB")
    
    # LLM Configuration
    DEFAULT_MODEL: str = Field("gpt-3.5-turbo", env="DEFAULT_MODEL")
    MAX_TOKENS: int = Field(100, env="MAX_TOKENS")

    # Logging and Tracing
    LOG_LEVEL: str = Field("INFO", env="LOG_LEVEL")
    JAEGER_HOST: str = Field("localhost", env="JAEGER_HOST")
    JAEGER_PORT: int = Field(6831, env="JAEGER_PORT")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True

# Create a global instance of the settings
settings = Settings()