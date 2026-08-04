import runpy
from pathlib import Path
from unittest.mock import patch


def test_signup_route_is_registered_before_server_starts():
    app_path = Path(__file__).resolve().parents[1] / "src" / "app.py"

    with patch("uvicorn.run") as mock_run:
        runpy.run_path(str(app_path), run_name="__main__")

    app = mock_run.call_args[0][0]
    route_paths = [route.path for route in app.routes if hasattr(route, "path")]

    assert "/activities/{activity_name}/signup" in route_paths


def test_unregister_participant_route_is_registered():
    app_path = Path(__file__).resolve().parents[1] / "src" / "app.py"

    with patch("uvicorn.run") as mock_run:
        runpy.run_path(str(app_path), run_name="__main__")

    app = mock_run.call_args[0][0]
    route_paths = [route.path for route in app.routes if hasattr(route, "path")]

    assert "/activities/{activity_name}/participants/{email}" in route_paths
