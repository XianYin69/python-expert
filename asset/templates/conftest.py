import pytest

@pytest.fixture(scope="session")
def tmp_ws(tmp_path_factory):
    return tmp_path_factory.mktemp("ws")

@pytest.fixture
def data(request):
    return getattr(request, "param", {})

@pytest.mark.parametrize("case", [{"n": 1}, {"n": 10}], ids=lambda d: "n%s" % d["n"])
def test_shape(data, case, tmp_ws):
    assert (tmp_ws / "x").parent.exists()
