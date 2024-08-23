from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="llm-powered-microservice",
    version="0.1.0",
    author="Dominic Thompson",
    author_email="codewiththompson@gmail.com",
    description="A FastAPI-based microservice for interacting with Large Language Models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/llm-powered-microservice",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.8",
    install_requires=[
        "fastapi>=0.68.0,<0.69.0",
        "uvicorn>=0.15.0,<0.16.0",
        "pydantic>=1.8.2,<2.0.0",
        "python-dotenv>=0.19.0,<0.20.0",
        "aioredis>=2.0.0,<3.0.0",
        "openai>=0.27.0,<0.28.0",
        "anthropic>=0.2.6,<0.3.0",
        "opentelemetry-api>=1.11.1,<2.0.0",
        "opentelemetry-sdk>=1.11.1,<2.0.0",
        "opentelemetry-exporter-jaeger>=1.11.1,<2.0.0",
        "opentelemetry-instrumentation-fastapi>=0.30b1,<0.31.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.2.5,<7.0.0",
            "pytest-asyncio>=0.15.1,<0.16.0",
            "httpx>=0.18.2,<0.19.0",
        ],
    },
)