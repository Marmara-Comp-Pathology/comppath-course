"""Shared helper code for the course (maintainers, CI and local use).

Lesson notebooks cannot import this package when opened on Kaggle or Colab,
so each lesson's setup cell carries a copy of the logic in `env.py`.
Keep the two in sync.
"""
from .env import detect_environment, smoke_test_enabled, work_dir

__all__ = ["detect_environment", "smoke_test_enabled", "work_dir"]
