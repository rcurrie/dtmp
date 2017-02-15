import requests

server = "http://localhost:5000/"


def test_hello():
    """
    Test hello endpoint
    """
    r = requests.get(server + "hello")
    assert(r.status_code == requests.codes.ok)
    assert(r.text == "hello")
