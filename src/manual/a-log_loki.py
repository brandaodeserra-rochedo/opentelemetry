import logging

from opentelemetry._logs import set_logger_provider
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from opentelemetry.exporter.otlp.proto.grpc._log_exporter import (
    OTLPLogExporter
)
from opentelemetry.sdk.resources import SERVICE_NAME, Resource

resource = Resource({SERVICE_NAME: 'app-send-log'})
provider = LoggerProvider(resource=resource)

# Exporter via OTLP
processor = BatchLogRecordProcessor(
    OTLPLogExporter(endpoint='http://localhost:4317', insecure=True)
)

provider.add_log_record_processor(processor)

set_logger_provider(provider)

handler = LoggingHandler(level=logging.INFO, logger_provider=provider)

logger = logging.getLogger(__name__)

# OTel Handler
logger.addHandler(handler)
logger.addHandler(logging.StreamHandler())

logger.setLevel(logging.WARNING)

logger.critical('Send error for Opentelemetry')
