from azure.common.client_factory import get_client_from_cli_profile
from azure.mgmt.resource import ResourceManagementClient


def pytest_generate_tests(metafunc):
    client = get_client_from_cli_profile(ResourceManagementClient)
    resources = client.resources.list(
        filter="resourceType eq 'Microsoft.DataFactory/factories'"
    )
    resources = map(
        lambda x: client.resources.get_by_id(x.id, api_version="2018-06-01"), resources
    )
    if "resource" in metafunc.fixturenames:
        metafunc.parametrize(
            "resource",
            resources,
            ids=lambda x: x.name,
        )
