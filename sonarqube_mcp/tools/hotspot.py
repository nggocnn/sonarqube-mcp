from typing import Annotated, Optional, Dict, Any
from pydantic import Field
from sonarqube_mcp.server import mcp, sonar_client


@mcp.tool(
    description="""
Retrieve security hotspots in a SonarQube project.
"""
)
async def get_project_hotspots(
    project_key: Annotated[
        str, Field(description="Key of the project (e.g., 'my_project').")
    ],
    file_paths: Annotated[
        Optional[str],
        Field(description="Comma-separated file paths to filter hotspots."),
    ] = None,
    only_mine: Annotated[
        Optional[bool],
        Field(description="If true, return only user's assigned hotspots."),
    ] = None,
    page: Annotated[int, Field(description="Page number for pagination.", ge=1)] = 1,
    page_size: Annotated[
        int, Field(description="Number of hotspots per page (max 20).", ge=1, le=20)
    ] = 20,
    resolution: Annotated[
        Optional[str],
        Field(description="Filter by resolution: FIXED, SAFE, ACKNOWLEDGED."),
    ] = None,
    status: Annotated[
        Optional[str], Field(description="Filter by status: TO_REVIEW, REVIEWED.")
    ] = None,
) -> Dict[str, Any]:
    """Retrieve security hotspots in a SonarQube project.

    Retrieves a paginated list of security hotspots, filtered by project, file paths, ownership, resolution, or status.

    Args:
        project_key (str): The key of the project (e.g., 'my_project'). Must be non-empty.
        file_paths (str, optional): Comma-separated list of file paths to filter hotspots (e.g., 'src/main.java,src/utils.js'). Defaults to None.
        only_mine (bool, optional): If True, return only hotspots assigned to the authenticated user. Defaults to None.
        page (int, optional): Page number for pagination (positive integer, default 1).
        page_size (int, optional): Number of hotspots per page (positive integer, max 20, default 20).
        resolution (str, optional): Filter by resolution (e.g., 'FIXED', 'SAFE'). Possible values: FIXED, SAFE, ACKNOWLEDGED.
        status (str, optional): Filter by status (e.g., 'TO_REVIEW', 'REVIEWED'). Possible values: TO_REVIEW, REVIEWED.

    Returns:
        Dict[str, Any]: A dictionary with hotspot details and pagination info.
    """
    response = await sonar_client.get_project_hotspots(
        project_key=project_key,
        file_paths=file_paths,
        only_mine=only_mine,
        page=page,
        page_size=page_size,
        resolution=resolution,
        status=status,
    )

    return response


@mcp.tool(
    description="""
Retrieve details of a specific SonarQube security hotspot.
"""
)
async def get_hotspot_detail(
    hotspot_key: Annotated[str, Field(description="Key of the hotspot.")],
):
    """Retrieve detailed information about a specific security hotspot.

    Provides details such as the hotspot's location, rule, and status.

    Args:
        hotspot_key (str): The key of the hotspot. Must be non-empty.

    Returns:
        Dict[str, Any]: A dictionary with hotspot details.
    """
    response = await sonar_client.get_hotspot_detail(hotspot_key=hotspot_key)

    return response
