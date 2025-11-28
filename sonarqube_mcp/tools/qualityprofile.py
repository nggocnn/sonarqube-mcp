from typing import Annotated, Optional, Dict, Any
from pydantic import Field
from sonarqube_mcp.server import mcp, sonar_client


@mcp.tool(
    description="""
Associate a quality profile with a project in SonarQube.
"""
)
async def add_quality_profile_project(
    language: Annotated[
        str,
        Field(description="Programming language of the profile (e.g., 'java', 'py')."),
    ],
    project_key: Annotated[
        str, Field(description="Key of the project (e.g., 'my_project').")
    ],
    quality_profile: Annotated[
        str, Field(description="Name of the quality profile (e.g., 'Sonar way').")
    ],
):
    """Associates a quality profile with a project in SonarQube.

    Args:
        language (str): The programming language of the quality profile (e.g., 'java', 'py').
        project_key (str): The key of the project to associate with the quality profile (e.g., 'my_project').
        quality_profile (str): The name of the quality profile to apply (e.g., 'Sonar way').
    """

    response = await sonar_client.add_quality_profile_project(
        language=language,
        project_key=project_key,
        quality_profile=quality_profile,
    )

    return response


@mcp.tool(
    description="""
Remove a quality profile association from a project in SonarQube.
"""
)
async def remove_quality_profile_project(
    language: Annotated[
        str,
        Field(description="Programming language of the profile (e.g., 'java', 'py')."),
    ],
    project_key: Annotated[
        str, Field(description="Key of the project (e.g., 'my_project').")
    ],
    quality_profile: Annotated[
        str, Field(description="Name of the quality profile (e.g., 'Sonar way').")
    ],
):
    """Removes a quality profile association from a project in SonarQube.

    Args:
        language (str): The programming language of the quality profile (e.g., 'java', 'py').
        project_key (str): The key of the project to remove the quality profile from (e.g., 'my_project').
        quality_profile (str): The name of the quality profile to remove (e.g., 'Sonar way').
    """

    response = await sonar_client.remove_quality_profile_project(
        language=language,
        project_key=project_key,
        quality_profile=quality_profile,
    )

    return response


@mcp.tool(
    description="""
Retrieve SonarQube quality profiles.
"""
)
async def get_quality_profiles(
    defaults: Annotated[
        bool, Field(description="If true, return default profiles only.")
    ] = False,
    language: Annotated[
        Optional[str],
        Field(description="Filter by programming language (e.g., 'java', 'py')."),
    ] = None,
    project_key: Annotated[
        Optional[str], Field(description="Filter by project key.")
    ] = None,
) -> Dict[str, Any]:
    """Search for quality profiles in SonarQube.

    Retrieves quality profiles, optionally filtered by default profiles, language, or associated project.

    Args:
        defaults (bool, optional): If True, return only default profiles. Defaults to False.
        language (str, optional): Filter by programming language (e.g., 'java', 'py'). Defaults to None.
        project_key (str, optional): Filter by project key (e.g., 'my_project'). Defaults to None.

    Returns:
        Dict[str, Any]: A dictionary with quality profile details.
    """
    response = await sonar_client.get_quality_profiles(
        defaults=defaults,
        language=language,
        project_key=project_key,
    )

    return response
