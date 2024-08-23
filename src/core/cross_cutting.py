import logging
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from opentelemetry import trace
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.jaeger.thrift import JaegerExporter

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set up tracing
trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)

# Set up Jaeger exporter
jaeger_exporter = JaegerExporter(
    agent_host_name="localhost",
    agent_port=6831,
)
span_processor = BatchSpanProcessor(jaeger_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        logger.info(f"Incoming request: {request.method} {request.url}")
        response = await call_next(request)
        logger.info(f"Outgoing response: {response.status_code}")
        return response

def setup_instrumentation(app):
    FastAPIInstrumentor.instrument_app(app)

def log_error(error: Exception):
    logger.error(f"An error occurred: {str(error)}", exc_info=True)

@tracer.start_as_current_span("process_request")
async def process_request(request_data):
    # This is a placeholder for request processing logic
    # You would typically call your LLM service here
    pass