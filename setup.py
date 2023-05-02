import setuptools
from setuptools import setup, find_packages, Extension

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="pymylib", 
    version="1",
    author="schwarzam",
    author_email="gustavo.b.schwarz@gmail.com",
    description=long_description,
    url="https://github.com/schwarzam/pymylib",
    packages= setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.6',
    include_package_data=True
)
