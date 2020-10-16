# -*- coding: utf-8 -*-

from {{ cookiecutter.project_name.lower().replace("-", "_") }} import version


def test_version():
    """Double check version."""
    assert version.pkg_version == "20.1"
