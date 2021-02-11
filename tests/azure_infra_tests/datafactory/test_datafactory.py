def test_system_assigned_identity(resource):
    assert resource.identity.type == "SystemAssigned"


def test_location_allowed(resource, allowed_locations):
    assert resource.location in allowed_locations