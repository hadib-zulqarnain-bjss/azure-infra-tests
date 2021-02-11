def test_encrypted_in_transit(resource):
    assert resource.properties["vaultUri"].startswith("https://")


def test_is_default_network_access(resource, allowed_network_access):
    assert (
        resource.properties.get("networkAcls", {}).get("defaultAction", None)
        in allowed_network_access
    )


def test_location_allowed(resource, allowed_locations):
    assert resource.location in allowed_locations
