import pytest
import os


def split_option(request, name, default=[]):
    option = request.config.getoption(name)
    if option is None:
        return default
    else:
        return [None if x == "None" else x for x in option[0].split(",")]


@pytest.fixture
def allowed_locations(request):
    return split_option(request, "allowed_locations")


@pytest.fixture
def allowed_network_access(request):
    return split_option(request, "network_access")


@pytest.fixture
def allowed_tls_versions(request):
    return split_option(request, "tls_versions")


def pytest_addoption(parser):
    parser.addoption(
        "--allowed-locations",
        nargs=1,
        action="store",
        type=str,
        help="allowed locations for resources",
        default=[os.environ.get("ALLOWED_LOCATIONS", "uksouth,ukwest,UK South,UK West")]
    )
    parser.addoption(
        "--network-access",
        nargs=1,
        action="store",
        type=str,
        help="allowed default network access",
        default=[os.environ.get("NETWORK_ACCESS", "Deny")]
    )
    parser.addoption(
        "--tls-versions",
        nargs=1,
        action="store",
        type=str,
        help="allowed minimum TLS versions",
        default=[os.environ.get("TLS_VERSIONS", "TLS1_2")]
    )

