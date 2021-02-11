from azure.common.client_factory import get_client_from_cli_profile
from azure.mgmt.resource import ResourceManagementClient

import pytest
import os


def split_option(request, name, default=[]):
    option = request.config.getoption(name)
    if option is None:
        return default
    else:
        return [None if x == "None" else x for x in option[0].split(",")]


@pytest.fixture
def log_analytics_retention(request):
    return split_option(request, "log_analytics_retention")


def pytest_generate_tests(metafunc):
    client = get_client_from_cli_profile(ResourceManagementClient)
    resources = client.resources.list(
        filter="resourceType eq 'Microsoft.OperationalInsights/workspaces'"
    )
    resources = map(
        lambda x: client.resources.get_by_id(x.id, api_version="2015-11-01-preview"), resources
    )
    if "resource" in metafunc.fixturenames:
        metafunc.parametrize(
            "resource",
            resources,
            ids=lambda x: x.name,
        )


def pytest_addoption(parser):
    parser.addoption(
        "--log-analytics-retention",
        nargs=1,
        action="store",
        type=str,
        help="allowed minimum TLS versions",
        default=[os.environ.get("LOG_ANALYTICS_RETENTION", "730")]
    )
