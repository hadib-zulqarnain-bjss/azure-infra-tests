def test_threat_intel_mode_alert(resource):
    assert resource.properties["threatIntelMode"] == "Alert"


def test_network_rule(resource):
    pass


def test_application_rule_collection(resource):
    pass


def test_location_allowed(resource, allowed_locations):
    assert resource.location in allowed_locations
