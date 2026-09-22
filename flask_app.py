from flask import Flask, jsonify, render_template, redirect, url_for

from tester.runner import run_tests
from storage import save_run, list_runs, get_last_run


app = Flask(__name__)


@app.route("/")
def home():
    """Redirige vers le dashboard."""
    return redirect(url_for("dashboard"))


@app.route("/run")
def run():
    """Lance les tests et enregistre le résultat."""
    result = run_tests()
    save_run(result)

    return jsonify(result)


@app.route("/dashboard")
def dashboard():
    """Affiche le dashboard et l'historique."""
    runs = list_runs(20)
    last_run = get_last_run()

    return render_template(
        "dashboard.html",
        runs=runs,
        last_run=last_run
    )


@app.route("/health")
def health():
    """État de santé de notre solution."""
    last_run = get_last_run()

    if last_run is None:
        return jsonify({
            "status": "UNKNOWN",
            "message": "Aucun test n'a encore été exécuté"
        }), 200

    healthy = last_run["failed"] == 0

    return jsonify({
        "status": "UP" if healthy else "DEGRADED",
        "api": "Frankfurter",
        "last_run": last_run["timestamp"],
        "availability": last_run["availability"],
        "failed_tests": last_run["failed"]
    }), 200 if healthy else 503


if __name__ == "__main__":
    app.run(debug=True)
