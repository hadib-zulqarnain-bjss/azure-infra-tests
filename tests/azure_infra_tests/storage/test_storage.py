def test_encrypted_at_rest(resource):
    assert resource.encryption.services.blob.enabled


def test_encrypted_in_transit(resource):
    assert resource.enable_https_traffic_only


def test_minimum_tls(resource, allowed_tls_versions):
    assert resource.minimum_tls_version in allowed_tls_versions


def test_default_network_access(resource, allowed_network_access):
    assert resource.network_rule_set.default_action in allowed_network_access


def test_location_allowed(resource, allowed_locations):
    assert resource.location in allowed_locations
