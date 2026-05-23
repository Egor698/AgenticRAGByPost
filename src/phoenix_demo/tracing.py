from phoenix.otel import register
from openinference.instrumentation.langchain import LangChainInstrumentor


def trace():
    trace_provider = register(
        endpoint='http://localhost:6006/v1/traces',
        project_name='Agentic RAG'
    )

    LangChainInstrumentor().instrument(trace_provide=trace_provider)