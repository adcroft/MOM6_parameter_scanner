""" mom6_parameter_scanner setup """
from setuptools import setup, find_packages
import os

setup(
    name="mom6_parameter_scanner",
    version="0.0.2",
    author="Alistair Adcroft",
    author_email="alistair.adcroft@noaa.gov",
    description=("A tool to digest and difference MOM parameter files"),
    license="GPLv3",
    keywords="",
    url="https://github.com/adcroft/MOM6_parameter_scanner",
    packages=find_packages(),
    scripts=["scripts/MOM6param_scan.py"],
)
