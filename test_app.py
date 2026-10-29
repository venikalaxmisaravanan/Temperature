from app import app


def test_home():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert response.data == b"Temperature Converter"


def test_celsius_to_fahrenheit():
    client = app.test_client()
    response = client.get("/convert?type=c_to_f&value=100")

    assert response.status_code == 200
    assert response.json["result"] == 212.0


def test_fahrenheit_to_celsius():
    client = app.test_client()
    response = client.get("/convert?type=f_to_c&value=212")

    assert response.status_code == 200
    assert response.json["result"] == 100.0


def test_invalid_value():
    client = app.test_client()
    response = client.get("/convert?type=c_to_f&value=abc")

    assert response.status_code == 400


def test_invalid_type():
    client = app.test_client()
    response = client.get("/convert?type=invalid&value=100")

    assert response.status_code == 400