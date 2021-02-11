from azure.common.client_factory import get_client_from_cli_profile
from azure.mgmt.resource import ResourceManagementClient
from azure.core.exceptions import ResourceNotFoundError


def pytest_generate_tests(metafunc):
    client = get_client_from_cli_profile(ResourceManagementClient)
    resources = client.resources.list(
        filter="resourceType eq 'Microsoft.EventHub/namespaces'"
    )
    resources = map(
        lambda x: client.resources.get_by_id(x.id, api_version="2018-01-01-preview"),
        resources,
    )
    if "resource" in metafunc.fixturenames:
        metafunc.parametrize(
            "resource",
            resources,
            ids=lambda x: x.name,
        )

    def get_network_rules_for_namespace(x):
        try:
            return client.resources.get_by_id(
                f"{x.id}/networkRuleSet/default",
                api_version="2018-01-01-preview",
            )
        except ResourceNotFoundError:
            return None

    networks = map(get_network_rules_for_namespace, resources)
    if "network" in metafunc.fixturenames:
        metafunc.parametrize("network", networks, ids=lambda x: x.name)
