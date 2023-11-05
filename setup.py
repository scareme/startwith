#!\usr\bin\python
"""Setuptools-based installation."""
from pathlib import Path

from setuptools import find_packages, setup

from startwith.version import __version__

readme = Path(__file__).parent / "README.md"


with Path("requirements.txt").open() as file:
    dependencies = [line.rstrip() for line in file if not line.startswith("-") and "@git" not in line]


setup(
    name="startwith",
    packages=find_packages(include=["startwith"]),
    author="Kirill Ivanov",
    version=__version__,
    include_package_data=True,
    install_requires=dependencies,
)
