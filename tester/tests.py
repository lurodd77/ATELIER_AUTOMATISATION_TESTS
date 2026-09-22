from .client import get


def result(name, passed, latency_ms=0, details=""):
    """Crée le résultat standardisé d'un test."""
    return {
        "name": name,
        "status": "PASS" if passed else "FAIL",
        "latency_ms": round(latency_ms, 2),
        "details": details
    }


def test_http_200():
    response, latency = get("/v2/rate/eur/usd")

    return result(
        "HTTP 200",
        response.status_code == 200,
        latency,
        f"HTTP {response.status_code}"
    )


def test_content_type_json():
    response, latency = get("/v2/rate/eur/usd")
    content_type = response.headers.get("Content-Type", "")

    return result(
        "Content-Type JSON",
        "application/json" in content_type.lower(),
        latency,
        content_type
    )


def test_required_fields():
    response, latency = get("/v2/rate/eur/usd")
    data = response.json()

    required_fields = ["date", "base", "quote", "rate"]
    passed = all(field in data for field in required_fields)

    return result(
        "Champs obligatoires",
        passed,
        latency,
        f"Champs reçus : {list(data.keys())}"
    )


def test_field_types():
    response, latency = get("/v2/rate/eur/usd")
    data = response.json()

    passed = (
        isinstance(data.get("date"), str)
        and isinstance(data.get("base"), str)
        and isinstance(data.get("quote"), str)
        and isinstance(data.get("rate"), (int, float))
    )

    return result(
        "Types des champs",
        passed,
        latency,
        "Vérification date/base/quote/rate"
    )


def test_currency_values():
    response, latency = get("/v2/rate/eur/usd")
    data = response.json()

    passed = (
        data.get("base", "").upper() == "EUR"
        and data.get("quote", "").upper() == "USD"
        and data.get("rate", 0) > 0
    )

    return result(
        "Valeurs EUR/USD",
        passed,
        latency,
        f"{data.get('base')} -> {data.get('quote')} : {data.get('rate')}"
    )


def test_invalid_currency():
    response, latency = get("/v2/rate/INVALID/USD")

    passed = response.status_code in (400, 404, 422)

    return result(
        "Devise invalide",
        passed,
        latency,
        f"HTTP {response.status_code}"
    )


TESTS = [
    test_http_200,
    test_content_type_json,
    test_required_fields,
    test_field_types,
    test_currency_values,
    test_invalid_currency,
]
