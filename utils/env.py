"""Detect where a lesson is running and where it may write files.

This is the canonical copy. The setup cell of every lesson notebook
(marked `# COMPPATH-SETUP`) contains an inlined copy of these functions.
"""
import os
import sys
from pathlib import Path


def detect_environment() -> str:
    """Return "kaggle", "colab" or "local"."""
    if os.environ.get("KAGGLE_KERNEL_RUN_TYPE") or Path("/kaggle/working").exists():
        return "kaggle"
    if "google.colab" in sys.modules or os.environ.get("COLAB_RELEASE_TAG"):
        return "colab"
    return "local"


def smoke_test_enabled() -> bool:
    """True when CI asks for a quick run on tiny synthetic data."""
    return os.environ.get("COMPPATH_SMOKE_TEST", "0") == "1"


def work_dir(env: str | None = None) -> Path:
    """A writable folder for downloads, models and outputs."""
    env = env or detect_environment()
    if env == "kaggle":
        path = Path("/kaggle/working")
    elif env == "colab":
        path = Path("/content")
    else:
        path = Path(os.environ.get("COMPPATH_WORK_DIR", Path.cwd() / "work"))
    path.mkdir(parents=True, exist_ok=True)
    return path
