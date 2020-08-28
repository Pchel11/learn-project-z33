import pytest

from custom_types import Endpoint


@pytest.mark.unit
def test_endpoint():
    data_set = {
        "": Endpoint(original="", normal="/"),
        "/": Endpoint(original="/", normal="/"),
        "/images": Endpoint(original="/images", normal="/images/"),
        "/images/": Endpoint(original="/images/", normal="/images/"),
        "/images/a": Endpoint(original="/images/a", normal="/images/a/"),
        "/images/a/": Endpoint(original="/images/a/", normal="/images/a/"),
        "/images/image.jpg": Endpoint(
            original="/images/image.jpg", normal="/images/", file_name="image.jpg"
        ),
        "/images/image.jpg/": Endpoint(
            original="/images/image.jpg/", normal="/images/", file_name="image.jpg"
        ),
        "/images/x/image.jpg": Endpoint(
            original="/images/x/image.jpg", normal="/images/x/", file_name="image.jpg"
        ),
        "/images/x/image.jpg/": Endpoint(
            original="/images/x/image.jpg/", normal="/images/x/", file_name="image.jpg"
        ),
    }

    for path, expected_endpoint in data_set.items():
        got_endpoint = Endpoint.from_path(path)

        assert (
            got_endpoint == expected_endpoint
        ), f"mismatch for `{path}`: expected {expected_endpoint}, got {got_endpoint}"
