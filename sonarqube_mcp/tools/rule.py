from typing import Annotated, Optional, Dict, Any
from pydantic import Field
from sonarqube_mcp.server import mcp, sonar_client


@mcp.tool(
    description="""
Retrieve SonarQube rules with optional filters.
"""
)
async def get_rules(
    page: Annotated[int, Field(description="Page number for pagination.", ge=1)] = 1,
    page_size: Annotated[
        int, Field(description="Number of rules per page (max 20).", ge=1, le=20)
    ] = 20,
    severities: Annotated[
        Optional[str],
        Field(
            description="Comma-separated severities: INFO, MINOR, MAJOR, CRITICAL, BLOCKER."
        ),
    ] = None,
    statuses: Annotated[
        Optional[str],
        Field(
            description="Comma-separated statuses: BETA, DEPRECATED, READY, REMOVED."
        ),
    ] = None,
    languages: Annotated[
        Optional[str], Field(description="Comma-separated languages (e.g., 'java,js').")
    ] = None,
    types: Annotated[
        Optional[str],
        Field(
            description="Comma-separated types: CODE_SMELL, BUG, VULNERABILITY, SECURITY_HOTSPOT."
        ),
    ] = None,
) -> Dict[str, Any]:
    """Retrieve for rules in SonarQube.

    Retrieves a paginated list of rules, optionally filtered by severity, status, or type.

    Args:
        page (int, optional): Page number for pagination (positive integer, default 1).
        page_size (int, optional): Number of rules per page (positive integer, max 20, default 20).
        severities (str, optional): Comma-separated list of severities (e.g., 'BLOCKER,CRITICAL'). Defaults to None. Possible values: INFO, MINOR, MAJOR, CRITICAL, BLOCKER.
        statuses (str, optional): Comma-separated list of statuses (e.g., 'BETA,READY'). Defaults to None. Possible values: BETA, DEPRECATED, READY, REMOVED.
        languages (str, optional): Comma-separated list of languages (e.g. 'java,js'). Defaults to None
        types (str, optional): Comma-separated list of rule types (e.g., 'BUG,CODE_SMELL'). Defaults to None. Possible values: CODE_SMELL, BUG, VULNERABILITY, SECURITY_HOTSPOT.

    Returns:
        Dict[str, Any]: A dictionary with rule details and pagination info.
    """
    response = await sonar_client.get_rules(
        page=page,
        page_size=page_size,
        severities=severities,
        statuses=statuses,
        languages=languages,
        types=types,
    )

    return response


@mcp.tool(
    description="""
Retrieve details of a specific SonarQube rule.
"""
)
async def get_rule_details(
    rule_key: Annotated[str, Field(description="Key of the rule.")],
    actives: Annotated[
        bool, Field(description="If true, include active quality profiles.")
    ] = False,
) -> Dict[str, Any]:
    """Retrieve detailed information about a specific SonarQube rule.

    Provides rule details, including description and active status in profiles if requested.

    Args:
        rule_key (str): The key of the rule. Must be non-empty.
        actives (bool, optional): If True, include active status in quality profiles. Defaults to False.

    Returns:
        Dict[str, Any]: A dictionary with rule details.
    """

    response = await sonar_client.get_rule_details(rule_key=rule_key, actives=actives)

    return response
