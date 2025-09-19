import time
import random
from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader

# Configura o exportador OTLP (envia para o OTel Collector)
otlp_exporter = OTLPMetricExporter(endpoint="http://localhost:4317",insecure=True)

# Configura o Provider de métricas
reader = PeriodicExportingMetricReader(otlp_exporter)
provider = MeterProvider(metric_readers=[reader])
metrics.set_meter_provider(provider)

# Cria o meter
meter = metrics.get_meter("python-app")

# Cria um contador simples
request_counter = meter.create_counter(
    name="python_app_requests",
    description="Total de requisições",
    unit="1",
)

print(f"Métrica Iniciada: {request_counter.name}")
while True:
    value = random.randint(1, 5)  # valor aleatório entre 1 e 5
    request_counter.add(value)
    print(f"Métrica enviada: {value}")
    time.sleep(2)
