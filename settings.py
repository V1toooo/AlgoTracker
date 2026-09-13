from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_host: str
    postgres_port: int

    @property
    def sqlalchemy_url(self) -> str:
        """
        Build synchronous PostgreSQL URL for Alembic migrations.

        :return: SQLAlchemy connection string using psycopg2 driver.
        """
        return (
            f"postgresql+psycopg2://{self.postgres_user}:"
            f"{self.postgres_password}@{self.postgres_host}:"
            f"{self.postgres_port}/{self.postgres_db}"
        )

    @property
    def database_url(self) -> str:
        """
        Build asynchronous PostgreSQL URL for the FastAPI application.

        :return: SQLAlchemy connection string using asyncpg driver.
        """
        return (
            f"postgresql+asyncpg://{self.postgres_user}:"
            f"{self.postgres_password}@{self.postgres_host}:"
            f"{self.postgres_port}/{self.postgres_db}"
        )

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()