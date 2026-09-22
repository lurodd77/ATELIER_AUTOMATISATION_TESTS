import time
import requests


BASE_URL = "https://api.frankfurter.dev"
TIMEOUT = 3
MAX_RETRIES = 1


def get(endpoint):
    """
    Effectue une requête GET vers l'API Frankfurter.
    Mesure la latence et gère un retry en cas d'erreur.
    """

    url = BASE_URL + endpoint

    for attempt in range(MAX_RETRIES + 1):
        start = time.perf_counter()

        try:
            response = requests.get(url, timeout=TIMEOUT)
            latency_ms = (time.perf_counter() - start) * 1000

            # Rate limit : petite attente avant un nouvel essai
            if response.status_code == 429 and attempt < MAX_RETRIES:
                time.sleep(1)
                continue

            # Erreur serveur : on effectue un retry
            if response.status_code >= 500 and attempt < MAX_RETRIES:
                time.sleep(1)
                continue

            return response, latency_ms

        except requests.exceptions.Timeout:
            if attempt >= MAX_RETRIES:
                raise

            time.sleep(1)

        except requests.exceptions.RequestException:
            if attempt >= MAX_RETRIES:
                raise

            time.sleep(1)
