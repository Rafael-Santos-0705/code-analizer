import uvicorn
import logging
from dotenv import load_dotenv
from alembic.config import Config
from alembic import command
from utils import Environment, ApplicationLogger
from app import create_app

def run_migrations():
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")

if __name__ == "__main__":
    load_dotenv()

    # Configure logger
    logger = logging.getLogger("application.engine")
    handle = ApplicationLogger.configure([
        "application.engine",
        "application.service",
        "uvicorn",
        "uvicorn.access",
        "sqlalchemy",
        "sqlalchemy.engine",
        "sqlalchemy.engine.Engine",
    ])

    handle.setLevel(getattr(
        logging,
        str(Environment.get("LOGGING_LEVEL", default="INFO")).upper(),
        logging.INFO
    ))


    if Environment.get("RUN_MAIN") == "true":
        if Environment.get("APPLICATION_MIGRATE") == "true":
            logger.warning("Starting the execution of migrations.")
            try:
                run_migrations()
            except Exception as e:
                logger.error(f"Error occurred while executing migrations: {str(e)}")

    # Start the server
    uvicorn.run(
        "main:create_app",
        host="0.0.0.0",
        port=int(Environment.get("APPLICATION_PORT", default=5000)),
        reload=True
    )
