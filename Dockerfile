
FROM python:3.11-slim
WORKDIR /app

# Create a non-root user
RUN adduser --disabled-password --gecos "" myuser

# Switch to the non-root user
USER myuser

# Set up environment variables
ENV PATH="/home/myuser/.local/bin:$PATH"

ENV GOOGLE_GENAI_USE_VERTEXAI=1
ENV GOOGLE_CLOUD_PROJECT=harmony-city-zoo
ENV GOOGLE_CLOUD_LOCATION=us-central1

# Set environment variables for Poetry
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

# Install Poetry
RUN pip install poetry

# Copy pyproject.toml and poetry.lock to leverage Docker's build cache
COPY pyproject.toml poetry.lock ./

# Install project dependencies
# Use --no-dev for production builds to exclude development dependencies
RUN poetry install --no-dev --no-root && rm -rf $POETRY_CACHE_DIR

# Install ADK 
RUN pip install google-adk==1.13.0

# Copy agent
# Set permission
COPY --chown=myuser:myuser "agents/zoo_concierge/" "/app/agents/zoo_concierge/"

EXPOSE 8000

CMD adk web --port=8000 --host=0.0.0.0       "/app/agents"
