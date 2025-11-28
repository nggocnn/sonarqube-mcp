import os
import asyncio
import logging
from mcp.server.fastmcp import FastMCP
from sonarqube_mcp.sonarqube import SonarQubeClient

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Reduce httpx logging verbosity
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("httpcore").setLevel(logging.WARNING)

mcp = FastMCP(name="SonarQube MCP Server", host="0.0.0.0")

SONARQUBE_URL = os.environ.get("SONARQUBE_URL", "http://localhost:9000")
SONARQUBE_TOKEN = os.environ.get("SONARQUBE_TOKEN", "")
SONARQUBE_USERNAME = os.environ.get("SONARQUBE_USERNAME", "")
SONARQUBE_PASSWORD = os.environ.get("SONARQUBE_PASSWORD", "")
SONARQUBE_ORGANIZATION = os.environ.get("SONARQUBE_ORGANIZATION", None)


async def init_sonar_client() -> SonarQubeClient:
    """Initialize the SonarQube client asynchronously."""
    try:
        client = await SonarQubeClient.create(
            base_url=SONARQUBE_URL,
            token=SONARQUBE_TOKEN,
            username=SONARQUBE_USERNAME,
            password=SONARQUBE_PASSWORD,
            organization=SONARQUBE_ORGANIZATION,
        )
        return client
    except Exception as e:
        raise ConnectionError(f"Failed to initialize SonarQube client: {str(e)}")


loop = asyncio.get_event_loop()
sonar_client = loop.run_until_complete(init_sonar_client())
