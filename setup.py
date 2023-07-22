#!\usr\bin\python
"""Setuptools-based installation."""
from pathlib import Path

from setuptools import find_packages, setup

readme = Path(__file__).parent / "README.md"


with Path("requirements.txt").open() as file:
    dependencies = [line.rstrip() for line in file if not line.startswith("-") and "@git" not in line]


setup(
    name="src",
    packages=find_packages(include=["src"]),
    author="Kirill Ivanov",
    version="1.0",
    include_package_data=True,
    install_requires=dependencies
)
