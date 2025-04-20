import os
import logging
from dotenv import load_dotenv
from contextlib import asynccontextmanager
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')  # example: username
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')  # example: password
DATABASE_ADDRESS = os.getenv('DATABASE_ADDRESS')    # example: 127.0.0.1
DATABASE_PORT = os.getenv('DATABASE_PORT')          # example: 5432
DATABASE_NAME = os.getenv('DATABASE_NAME')          # example: dbname

if not all([DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_ADDRESS, DATABASE_PORT, DATABASE_NAME]):
    raise ValueError("Missing required environment variables.")
    
DATABASE_URL = f"postgresql+asyncpg://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_ADDRESS}:{DATABASE_PORT}/{DATABASE_NAME}"

engine = create_async_engine(DATABASE_URL, echo=False)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

Base = declarative_base()

async def init_db():
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        logger.info("Database initialized successfully.")
    except Exception as e:
        logger.error(f"Error initializing database: {e}")
        raise

@asynccontextmanager
async def get_session():
    async with AsyncSessionLocal() as session:
        yield session