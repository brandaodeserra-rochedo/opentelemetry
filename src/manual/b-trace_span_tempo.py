from logging import INFO, Filter
from loguru import logger

from opentelemetry._logs import set_logger_provider
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.exporter.otlp.proto.grpc._log_exporter import OTLPLogExporter  # noqa

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter  # noqa
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.trace import get_tracer


resource = Resource(attributes={SERVICE_NAME: 'ops-application'})
provider = LoggerProvider(resource=resource)
processor = BatchLogRecordProcessor(OTLPLogExporter(endpoint='http://localhost:4317', insecure=True)) # noqa
provider.add_log_record_processor(processor)
set_logger_provider(provider)

trace_provider = TracerProvider(resource=resource)
trace.set_tracer_provider(trace_provider)
span_processor = BatchSpanProcessor(OTLPSpanExporter(endpoint='http://localhost:4317', insecure=True)) # noqa
trace_provider.add_span_processor(span_processor)


class RemoveExtra(Filter):
    def filter(self, record):
        if 'extra' in record.__dict__:
            del record.__dict__['extra']
        return True


handler = LoggingHandler(level=INFO, logger_provider=provider)
handler.addFilter(RemoveExtra())

logger.add(handler, level='DEBUG', serialize=True)

tracer = get_tracer(__name__)


@logger.catch
def run_operations():
    with tracer.start_as_current_span("integration-operation"):
        sum()
        multiply()
        substract()
        divide()


def sum():
    with tracer.start_as_current_span("calc-tarifacao"):
        logger.info("Iniciando a operação de tarifação Subscription")
        result_sum = 1 + 1
        logger.info(f"Sum ok with result = {result_sum}")


def multiply():
    with tracer.start_as_current_span("star-camc-integration"):
        logger.info("Iniciando a operação de integração com CAMC")
        result_multiply = 2 * 2
        logger.info(f"ok with result = {result_multiply}")


def substract():
    with tracer.start_as_current_span("publish-mom-bcc"):
        logger.info("Iniciando publicação no RabbitMQ BCC")
        result_substract = 10-5
        logger.info(f"ok with result = {result_substract}")


def divide():
    with tracer.start_as_current_span("taxes-integration"):
        logger.info("Error calc taxes Subscription")
        print(1 / 0)


run_operations()
