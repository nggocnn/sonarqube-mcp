from typing import Annotated, Dict, Any
from pydantic import Field
from sonarqube_mcp.server import mcp, sonar_client


@mcp.tool(
    description="""
Retrieve all available metric types in SonarQube.
"""
)
async def get_metrics_type() -> Dict[str, Any]:
    """Retrieve all available metric types in SonarQube.

    Lists the types of metrics (e.g., 'INT', 'FLOAT') supported by SonarQube.
    Returns:
        Dict[str, Any]: A dictionary with a list of metric type names.
    """
    response = await sonar_client.get_metrics_type()
    return response


@mcp.tool(
    description="""
Retrieve all available metrics in SonarQube with pagination.
"""
)
async def get_metrics(
    page: Annotated[
        int, Field(description="Page number for pagination (positive integer).", ge=1)
    ] = 1,
    page_size: Annotated[
        int,
        Field(
            description="Number of metrics per page (positive integer, max 20).",
            ge=1,
            le=20,
        ),
    ] = 20,
) -> Dict[str, Any]:
    """Retrieve all available metrics in SonarQube with pagination.

    Lists metrics (e.g., 'complexity') with details like name, type, and domain.

    Args:
        page (int, optional): Page number for pagination (positive integer). Defaults to 1.
        page_size (int, optional): Number of metrics per page (positive integer, max 20). Defaults to 20.

    Returns:
        Dict[str, Any]: A dictionary with metric details and pagination info.
    """
    response = await sonar_client.get_metrics(page=page, page_size=page_size)
    return response
