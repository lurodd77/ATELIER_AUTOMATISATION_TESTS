import json
import sqlite3
from pathlib import Path


DB_PATH = Path(__file__).parent / "runs.db"


def get_connection():
    """Ouvre une connexion à la base SQLite."""
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    """Crée la table des runs si elle n'existe pas."""
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS runs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                api TEXT NOT NULL,
                passed INTEGER NOT NULL,
                failed INTEGER NOT NULL,
                error_rate REAL NOT NULL,
                availability REAL NOT NULL,
                latency_avg REAL NOT NULL,
                latency_p95 REAL NOT NULL,
                details TEXT NOT NULL
            )
        """)


def save_run(run):
    """Enregistre un run de tests dans SQLite."""
    init_db()

    summary = run["summary"]

    with get_connection() as connection:
        connection.execute("""
            INSERT INTO runs (
                timestamp,
                api,
                passed,
                failed,
                error_rate,
                availability,
                latency_avg,
                latency_p95,
                details
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            run["timestamp"],
            run["api"],
            summary["passed"],
            summary["failed"],
            summary["error_rate"],
            summary["availability"],
            summary["latency_ms_avg"],
            summary["latency_ms_p95"],
            json.dumps(run["tests"], ensure_ascii=False)
        ))


def list_runs(limit=20):
    """Retourne les derniers runs enregistrés."""
    init_db()

    with get_connection() as connection:
        rows = connection.execute("""
            SELECT *
            FROM runs
            ORDER BY id DESC
            LIMIT ?
        """, (limit,)).fetchall()

    return [dict(row) for row in rows]


def get_last_run():
    """Retourne le dernier run enregistré."""
    init_db()

    with get_connection() as connection:
        row = connection.execute("""
            SELECT *
            FROM runs
            ORDER BY id DESC
            LIMIT 1
        """).fetchone()

    return dict(row) if row else None
