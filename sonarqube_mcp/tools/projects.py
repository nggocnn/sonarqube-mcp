from typing import Annotated, Optional, Dict, Any
from pydantic import Field
from sonarqube_mcp.server import mcp, sonar_client


@mcp.tool(
    description="""
Create a new SonarQube project.
"""
)
async def create_project(
    project_name: Annotated[
        str, Field(description="Name of the project (max 500 characters).")
    ],
    project_key: Annotated[
        str,
        Field(
            description="Unique key identifier for the project (max 400 characters)."
        ),
    ],
    main_branch: Annotated[str, Field(description="Name of the main branch.")] = "main",
    new_code_definition_type: Annotated[
        Optional[str],
        Field(
            description="Type of new code definition: 'PREVIOUS_VERSION', 'NUMBER_OF_DAYS', 'REFERENCE_BRANCH'."
        ),
    ] = None,
    new_code_definition_value: Annotated[
        Optional[str],
        Field(
            description="Value for new code definition (number 1-90 for NUMBER_OF_DAYS)."
        ),
    ] = None,
) -> Dict[str, Any]:
    """Creates a new project in SonarQube.

    Args:
        project_name (str): The name of the project (max length: 500 characters, abbreviated if longer).
        project_key (str): A unique key identifier for the project (max length: 400 characters).
        main_branch (str, optional): The name of the main branch (default: "main"). Available since version 9.8.
        new_code_definition_type (str, optionale of new code definition. Allowed values: "PREVIOUS_VERSION", "NUMBER_OF_DAYS", "REFERENCE_BRANCH" (defaults to main branch). Available since version 10.1.
        new_code_definition_value (str, optional): The value for the new code definition. Expected values:
            - None for "PREVIOUS_VERSION" or "REFERENCE_BRANCH".
            - A number between 1 and 90 for "NUMBER_OF_DAYS".

    Returns:
        Dict[str, Any]: A dictionary with details of the created project. If the request fails, it may include an 'error' key.
    """
    response = await sonar_client.create_project(
        project_name=project_name,
        project_key=project_key,
        main_branch=main_branch,
        new_code_definition_type=new_code_definition_type,
        new_code_definition_value=new_code_definition_value,
    )
    return response


@mcp.tool(
    description="""
Search for SonarQube projects with optional name or key filtering.
"""
)
async def get_projects(
    projects: Annotated[
        Optional[str],
        Field(
            description="Comma-separated list of project keys (e.g., 'proj1,proj2')."
        ),
    ] = None,
    search: Annotated[
        Optional[str],
        Field(description="Partial project name or key to filter results."),
    ] = None,
    analyzed_before: Annotated[
        Optional[str],
        Field(
            description="Filter projects with last analysis before this date (YYYY-MM-DD or YYYY-MM-DDThh:mm:ssZ)."
        ),
    ] = None,
    page: Annotated[int, Field(description="Page number for pagination.", ge=1)] = 1,
    page_size: Annotated[
        int, Field(description="Number of projects per page (max 20).", ge=1, le=20)
    ] = 20,
) -> Dict[str, Any]:
    """Search for projects in SonarQube, with optional filtering by name.

    Retrieves a paginated list of projects the authenticated user can access.

    Args:
    projects (str, optional): Comma-separated list of project keys to filter results (e.g., 'my_project,other_project'). Defaults to None.
    search (str, optional): Partial project name or key to filter results (e.g., 'my_proj'). Defaults to None.
    analyzed_before (str, optional): Filter projects where the last analysis of all branches is older than this date (exclusive, server timezone). Accepts date ('YYYY-MM-DD') or datetime ('YYYY-MM-DDThh:mm:ssZ'). Example: '2017-10-19' or '2017-10-19T13:00:00+0200'. Defaults to None.
    page (int, optional): Page number for pagination (positive integer). Defaults to 1.
    page_size (int, optional): Number of projects per page (positive integer, max 20). Defaults to 20.

    Returns:
    Dict[str, Any]: A dictionary with project details and pagination info.
    """
    response = await sonar_client.get_projects(
        analyzed_before=analyzed_before,
        page=page,
        page_size=page_size,
        search=search,
        projects=projects,
    )
    return response


@mcp.tool(
    description="""
List projects accessible to the authenticated user
"""
)
async def get_user_projects(
    page: Annotated[int, Field(description="Page number for pagination.", ge=1)] = 1,
    page_size: Annotated[
        int, Field(description="Number of projects per page (max 20).", ge=1, le=20)
    ] = 20,
) -> Dict[str, Any]:
    """Lists projects accessible to the authenticated user.

    Retrieves a paginated list of projects the user can administer.

    Args:
        page (int, optional): Page number for pagination (positive integer). Defaults to 1.
        page_size (int, optional): Number of projects per page (positive integer, max 20). Defaults to 20.

    Returns:
        Dict[str, Any]: A dictionary with project details and pagination info.
    """
    response = await sonar_client.get_user_projects(page=page, page_size=page_size)
    return response


@mcp.tool(
    description="""
List projects the authenticated user can scan.
"""
)
async def get_user_scannable_projects(
    search: Annotated[
        Optional[str],
        Field(description="Partial project name or key to filter results."),
    ] = None,
) -> Dict[str, Any]:
    """List projects the authenticated user has permission to scan.

    Retrieves a list of projects where the user can perform analysis (scanning).

    Args:
        search (str, optional): Partial project name or key to filter results. Defaults to None.

    Returns:
        Dict[str, Any]: A dictionary with project keys.
    """
    response = await sonar_client.get_user_scannable_projects(search=search)
    return response


@mcp.tool(
    description="""
List analyses for a SonarQube project with optional filters.
"""
)
async def get_project_analyses(
    project_key: Annotated[
        str, Field(description="Key of the project (e.g., 'my_project').")
    ],
    category: Annotated[
        Optional[str],
        Field(
            description="Event category filter: VERSION, OTHER, QUALITY_PROFILE, QUALITY_GATE, etc."
        ),
    ] = None,
    page: Annotated[int, Field(description="Page number for pagination.", ge=1)] = 1,
    page_size: Annotated[
        int, Field(description="Number of analyses per page (max 20).", ge=1, le=20)
    ] = 20,
):
    """List analyses for a specified SonarQube project, with optional filters.

    Retrieves a paginated list of analyses for a project, optionally filtered by event category or branch.

    Args:
        project_key (str): The key of the project (e.g., 'my_project').
        category (str, optional): Event category to filter analyses (e.g., 'VERSION', 'QUALITY_GATE'). Possible values: VERSION, OTHER, QUALITY_PROFILE, QUALITY_GATE, DEFINITION_CHANGE, ISSUE_DETECTION, SQ_UPGRADE. Defaults to None.
        page (int, optional): Page number for pagination (positive integer). Defaults to 1.
        page_size (int, optional): Number of analyses per page (positive integer, max 20). Defaults to 20.

    Returns:
        Dict[str, Any]: A dictionary with analysis details and pagination info.
    """
    response = await sonar_client.get_project_analyses(
        project_key=project_key,
        category=category,
        page=page,
        page_size=page_size,
    )

    return response
