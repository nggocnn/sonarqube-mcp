from typing import Annotated, Optional, Dict, Any
from pydantic import Field
from sonarqube_mcp.server import mcp, sonar_client


@mcp.tool(
    description="""
Assign a permission to a group for a specific project or globally.
"""
)
async def add_group_permission(
    group_name: Annotated[
        str, Field(description="Name of the group to receive the permission.")
    ],
    permission: Annotated[
        str,
        Field(
            description="Permission to grant (global: admin, gateadmin, etc.; project: admin, codeviewer, etc.)."
        ),
    ],
    project_key: Annotated[
        Optional[str],
        Field(description="Project key for project-level permission; None for global."),
    ] = None,
):
    """Grants a permission to a group for a specific project or globally.

    Args:
        group_name (str): The name of the group to receive the permission.
        permission (str): The permission to grant (e.g., 'admin', 'scan').
            - Possible values for global permissions: admin, gateadmin, profileadmin, provisioning, scan, applicationcreator, portfoliocreator
            - Possible values for project permissions admin, codeviewer, issueadmin, securityhotspotadmin, scan, user
        project_key (str, optional): The key of the project for the permission. If None, the permission is global. Defaults to None.
    """
    response = await sonar_client.add_group_permission(
        group_name=group_name,
        permission=permission,
        project_key=project_key,
    )
    return response


@mcp.tool(
    description="""
Remove a permission from a group for a specific project or globally.
"""
)
async def remove_group_permission(
    group_name: Annotated[
        str, Field(description="Name of the group to remove the permission from.")
    ],
    permission: Annotated[
        str,
        Field(
            description="Permission to remove (global: admin, gateadmin, etc.; project: admin, codeviewer, etc.)."
        ),
    ],
    project_key: Annotated[
        Optional[str],
        Field(description="Project key for project-level permission; None for global."),
    ] = None,
):
    """Revokes a permission from a group for a specific project or globally.

    Args:
        group_name (str): The name of the group to remove the permission from.
        permission (str): The permission to grant (e.g., 'admin', 'scan').
            - Possible values for global permissions: admin, gateadmin, profileadmin, provisioning, scan, applicationcreator, portfoliocreator
            - Possible values for project permissions admin, codeviewer, issueadmin, securityhotspotadmin, scan, user
        project_key (str, optional): The key of the project for the permission. If None, the permission is global. Defaults to None.
    """
    response = await sonar_client.remove_group_permission(
        group_name=group_name,
        permission=permission,
        project_key=project_key,
    )
    return response


@mcp.tool(
    description="""
List group permissions for a specific project or globally.
"""
)
async def get_group_permission(
    project_key: Annotated[
        Optional[str],
        Field(
            description="Project key to fetch permissions for; None for global permissions."
        ),
    ] = None,
    page: Annotated[int, Field(description="Page number for pagination.", ge=1)] = 1,
    page_size: Annotated[
        int, Field(description="Number of results per page (max 20).", ge=1, le=20)
    ] = 20,
) -> Dict[str, Any]:
    """Fetches a list of group permissions for a specific project or globally.

    Args:
        project_key (str, optional): The key of the project to fetch permissions for. If None, global permissions are returned. Defaults to None.
        page (int, optional): Page number for pagination (positive integer). Defaults to 1.
        page_size (int, optional): Number of results per page (positive integer, max 20). Defaults to 20.

    Returns:
        Dict[str, Any]: A dictionary with group permission details.
    """

    response = await sonar_client.get_group_permission(
        project_key=project_key, page=page, page_size=page_size
    )
    return response


@mcp.tool(
    description="""
Assign a permission to a user for a specific project or globally.
"""
)
async def add_user_permission(
    username: Annotated[
        str, Field(description="Name of the user to receive the permission.")
    ],
    permission: Annotated[
        str,
        Field(
            description="Permission to grant (global: admin, gateadmin, etc.; project: admin, codeviewer, etc.)."
        ),
    ],
    project_key: Annotated[
        Optional[str],
        Field(description="Project key for project-level permission; None for global."),
    ] = None,
):
    """Grants a permission to a user for a specific project or globally.

    Args:
        username (str): The name of the user to receive the permission.
        permission (str): The permission to grant (e.g., 'admin', 'scan').
            - Possible values for global permissions: admin, gateadmin, profileadmin, provisioning, scan, applicationcreator, portfoliocreator
            - Possible values for project permissions admin, codeviewer, issueadmin, securityhotspotadmin, scan, user
        project_key (str, optional): The key of the project for the permission. If None, the permission is global. Defaults to None.
    """
    response = await sonar_client.add_user_permission(
        username=username,
        permission=permission,
        project_key=project_key,
    )
    return response


@mcp.tool(
    description="""
Remove a permission from a user for a specific project or globally.
"""
)
async def remove_user_permission(
    username: Annotated[
        str, Field(description="Name of the user to remove the permission from.")
    ],
    permission: Annotated[
        str,
        Field(
            description="Permission to remove (global: admin, gateadmin, etc.; project: admin, codeviewer, etc.)."
        ),
    ],
    project_key: Annotated[
        Optional[str],
        Field(description="Project key for project-level permission; None for global."),
    ] = None,
):
    """Revokes a permission from a user for a specific project or globally.

    Args:
        username (str): The name of the user to remove the permission from.
        permission (str): The permission to grant (e.g., 'admin', 'scan').
            - Possible values for global permissions: admin, gateadmin, profileadmin, provisioning, scan, applicationcreator, portfoliocreator
            - Possible values for project permissions admin, codeviewer, issueadmin, securityhotspotadmin, scan, user
        project_key (str, optional): The key of the project for the permission. If None, the permission is global. Defaults to None.
    """
    response = await sonar_client.remove_user_permission(
        username=username,
        permission=permission,
        project_key=project_key,
    )
    return response


@mcp.tool(
    description="""
List user permissions for a specific project or globally.
"""
)
async def get_user_permission(
    project_key: Annotated[
        Optional[str],
        Field(
            description="Project key to fetch permissions for; None for global permissions."
        ),
    ] = None,
    page: Annotated[int, Field(description="Page number for pagination.", ge=1)] = 1,
    page_size: Annotated[
        int, Field(description="Number of results per page (max 20).", ge=1, le=20)
    ] = 20,
) -> Dict[str, Any]:
    """Fetches a list of users permissions for a specific project or globally.

    Args:
        project_key (str, optional): The key of the project to fetch permissions for. If None, global permissions are returned. Defaults to None.
        page (int, optional): Page number for pagination (positive integer). Defaults to 1.
        page_size (int, optional): Number of results per page (positive integer, max 20). Defaults to 20.

    Returns:
        Dict[str, Any]: A dictionary with users permission details.
    """
    response = await sonar_client.get_user_permission(
        project_key=project_key, page=page, page_size=page_size
    )
    return response
