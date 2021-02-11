from azure.common.client_factory import get_client_from_cli_profile
from azure.mgmt.storage import StorageManagementClient


def pytest_generate_tests(metafunc):
    client = get_client_from_cli_profile(StorageManagementClient)
    resources = client.storage_accounts.list()
    if "resource" in metafunc.fixturenames:
        metafunc.parametrize(
            "resource",
            filter(lambda x: not x.is_hns_enabled, resources),
            ids=lambda x: x.name,
        )
