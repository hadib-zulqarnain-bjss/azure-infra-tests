def test_zone_redundant(resource):
    assert resource.properties["zoneRedundant"]


def test_encrypted_in_transit(resource):
    assert resource.properties["serviceBusEndpoint"].startswith("https://")


def test_default_network_access(resource, network, allowed_network_access):
    skip = None in allowed_network_access and network is None
    if not skip:
        assert network.id.split("/")[-3] == resource.id.split("/")[-1]
        assert (
            network.properties["networkAcl"]["defaultAction"] in allowed_network_access
        )


def test_location_allowed(resource, allowed_locations):
    assert resource.location in allowed_locations
