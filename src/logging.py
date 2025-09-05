import structlog
import logfire
from dotenv import load_dotenv

load_dotenv()

logfire.configure()

structlog.configure(
    processors=[
        structlog.contextvars.merge_contextvars,
        structlog.processors.add_log_level,
        structlog.processors.StackInfoRenderer(),
        structlog.dev.set_exc_info,
        structlog.processors.TimeStamper(fmt='%Y-%m-%d %H:%M:%S', utc=False),
        logfire.StructlogProcessor(),
        structlog.dev.ConsoleRenderer(),
    ],
)
logger = structlog.get_logger()
