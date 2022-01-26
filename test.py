import subprocess
import json
import pathlib

REPO_ROOT = pathlib.Path(__file__).resolve().parent


def test_ping_failures():
    reviewers_script = REPO_ROOT / "ping_on_failure.py"

    def run():
        data = {}
        proc = subprocess.run(
            [str(reviewers_script), "--statuses", json.dumps(data)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding="utf-8",
        )
        if proc.returncode != 0:
            raise RuntimeError(f"Process failed:\nstdout:\n{proc.stdout}\n\nstderr:\n{proc.stderr}")

    run()
