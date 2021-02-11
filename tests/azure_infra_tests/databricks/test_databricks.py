def test_sku_is_premium(resource):
    assert resource.sku.name == "premium"


def test_virtual_network_exists(resource):
    vnet_id = resource.properties.get("parameters", {}).get("customVirtualNetworkId")
    public_subnet_name = (
        resource.properties.get("parameters", {})
        .get("customPublicSubnetName", {})
        .get("value")
    )
    private_subnet_name = (
        resource.properties.get("parameters", {})
        .get("customPrivateSubnetName", {})
        .get("value")
    )
    assert vnet_id is not None
    assert public_subnet_name is not None
    assert private_subnet_name is not None


def test_location_allowed(resource, allowed_locations):
    assert resource.location in allowed_locations
