def test_sku_per_gb_billing(resource):
    assert resource.properties["sku"]["name"] == "pergb2018"


def test_retention_730_days(resource, log_analytics_retention):
    assert str(resource.properties["retentionInDays"]) in log_analytics_retention


def test_location_allowed(resource, allowed_locations):
    assert resource.location in allowed_locations
