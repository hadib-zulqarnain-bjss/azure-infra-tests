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
def app_insights_kind(request):
    return split_option(request, "app_insights_kind")


@pytest.fixture
def app_insights_retention(request):
    return split_option(request, "app_insights_retention")


@pytest.fixture
def app_insights_sampling(request):
    return split_option(request, "app_insights_sampling")


def pytest_generate_tests(metafunc):
    client = get_client_from_cli_profile(ResourceManagementClient)
    resources = client.resources.list(
        filter="resourceType eq 'Microsoft.Insights/components'"
    )
    resources = map(
        lambda x: client.resources.get_by_id(x.id, api_version="2015-05-01"), resources
    )
    if "resource" in metafunc.fixturenames:
        metafunc.parametrize(
            "resource",
            resources,
            ids=lambda x: x.name,
        )


def pytest_addoption(parser):
    parser.addoption(
        "--app-insights-kind",
        nargs=1,
        action="store",
        type=str,
        help="allowed minimum TLS versions",
        default=[os.environ.get("APP_INSIGHTS_KIND", "basic,web")]
    )
    parser.addoption(
        "--app-insights-retention",
        nargs=1,
        action="store",
        type=str,
        help="allowed minimum TLS versions",
        default=[os.environ.get("APP_INSIGHTS_RETENTION", "30")]
    )
    parser.addoption(
        "--app-insights-sampling",
        nargs=1,
        action="store",
        type=str,
        help="allowed minimum TLS versions",
        default=[os.environ.get("APP_INSIGHTS_SAMPLING", "100.0,None")]
    )
