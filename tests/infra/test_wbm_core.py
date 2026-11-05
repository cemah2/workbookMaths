"""Tests of wbm.setup and the environment helpers."""

import random
import re
from pathlib import Path

import numpy as np
import pytest

import wbm
from wbm import core
from wbm._versions import DIST_NAMES, EXPECTED_VERSIONS

ROOT = Path(__file__).resolve().parents[2]


def test_repo_root_found_from_anywhere(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    assert wbm.repo_root() == ROOT
    monkeypatch.setenv("WBM_ROOT", str(ROOT))
    assert wbm.repo_root() == ROOT


def test_setup_seeds_are_reproducible(capsys):
    wbm.setup(seed=123, verbose=False, style=False)
    a = (random.random(), np.random.rand())
    wbm.setup(seed=123, verbose=False, style=False)
    b = (random.random(), np.random.rand())
    assert a == b


def test_setup_seeds_torch():
    torch = pytest.importorskip("torch")
    wbm.setup(seed=7, verbose=False, style=False)
    a = torch.rand(3)
    wbm.setup(seed=7, verbose=False, style=False)
    assert torch.equal(a, torch.rand(3))


def test_setup_report_and_config(capsys):
    cfg = wbm.setup(seed=1, fast=True)
    out = capsys.readouterr().out
    assert "FAST_MODE : True" in out and "Python" in out
    assert cfg.device in ("cpu", "cuda") and cfg.seed == 1 and cfg.fast is True
    assert cfg.root == ROOT


def test_fast_mode_env_override(monkeypatch):
    monkeypatch.setenv("WBM_FAST_MODE", "0")
    cfg = wbm.setup(fast=True, verbose=False, style=False)
    assert cfg.fast is False and wbm.by_mode(1, 10) == 10
    monkeypatch.setenv("WBM_FAST_MODE", "1")
    cfg = wbm.setup(fast=False, verbose=False, style=False)
    assert cfg.fast is True and wbm.by_mode(1, 10) == 1


def test_timer(capsys):
    with wbm.timer("bloc") as t:
        sum(range(1000))
    assert t["seconds"] >= 0 and "bloc" in capsys.readouterr().out


def test_expected_versions_match_requirements():
    pins = {}
    for line in (ROOT / "requirements.txt").read_text().splitlines():
        line = line.split("#")[0].strip()
        if "==" in line:
            name, version = line.split("==")
            pins[name.strip().lower()] = version.strip()
    for module, version in EXPECTED_VERSIONS.items():
        dist = DIST_NAMES.get(module, module)
        pinned = version if isinstance(version, str) else version[0]     # the first accepted version is the pin
        assert pins.get(dist) == pinned, f"{dist}: requirements.txt and _versions.py disagree"


def test_expected_versions_match_bible():
    bible = (ROOT / "docs" / "BIBLE.md").read_text(encoding="utf-8")
    section = bible.split("## 22.")[1].split("## 23.")[0]
    for module, versions in EXPECTED_VERSIONS.items():
        for version in (versions,) if isinstance(versions, str) else versions:
            assert re.search(re.escape(version), section), f"{module} {version} missing from BIBLE §22"


def test_ensure_does_nothing_when_installed():
    assert wbm.ensure("numpy", "scikit-learn") == []


def test_is_colab_false_here():
    assert core.is_colab() is False


def test_setup_never_imports_torch(monkeypatch):
    """workbookMaths does not need PyTorch: setup() must not import it (seconds lost in every notebook)."""
    import sys as _sys

    monkeypatch.delitem(_sys.modules, "torch", raising=False)
    cfg = wbm.setup(seed=1, style=False, verbose=False)
    assert "torch" not in _sys.modules and cfg.device == "cpu" and cfg.torch_available is False
