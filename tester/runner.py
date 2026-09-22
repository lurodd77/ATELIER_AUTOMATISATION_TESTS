from datetime import datetime, timezone
import math

from .tests import TESTS


def percentile_95(values):
    """Calcule le percentile 95 des latences."""
    if not values:
        return 0

    values = sorted(values)
    index = math.ceil(0.95 * len(values)) - 1

    return values[index]


def run_tests():
    """Exécute tous les tests et calcule les métriques QoS."""

    results = []

    for test in TESTS:
        try:
            test_result = test()
            results.append(test_result)

        except Exception as error:
            results.append({
                "name": test.__name__,
                "status": "FAIL",
                "latency_ms": 0,
                "details": str(error)
            })

    total = len(results)

    passed = sum(
        1 for test in results
        if test["status"] == "PASS"
    )

    failed = total - passed

    latencies = [
        test["latency_ms"]
        for test in results
        if test["latency_ms"] > 0
    ]

    average_latency = (
        sum(latencies) / len(latencies)
        if latencies else 0
    )

    p95_latency = percentile_95(latencies)

    error_rate = failed / total if total else 0

    availability = (
        (passed / total) * 100
        if total else 0
    )

    return {
        "api": "Frankfurter",
        "timestamp": datetime.now(timezone.utc).isoformat(),

        "summary": {
            "total": total,
            "passed": passed,
            "failed": failed,
            "error_rate": round(error_rate, 3),
            "availability": round(availability, 2),
            "latency_ms_avg": round(average_latency, 2),
            "latency_ms_p95": round(p95_latency, 2)
        },

        "tests": results
    }
