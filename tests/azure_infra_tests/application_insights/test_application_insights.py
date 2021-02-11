def test_kind_basic(resource, app_insights_kind):
    assert resource.kind in app_insights_kind


def test_retention(resource, app_insights_retention):
    assert str(resource.properties["RetentionInDays"]) in app_insights_retention


def test_sampling_percentage(resource, app_insights_sampling):
    sampling = resource.properties["SamplingPercentage"]
    if sampling is None:
        assert sampling in app_insights_sampling
    else:
        assert str(sampling) in app_insights_sampling


def test_location_allowed(resource, allowed_locations):
    assert resource.location in allowed_locations
