import setuptools
from setuptools import setup, find_packages, Extension

# with open("README.md", "r") as fh:
#     long_description = fh.read()


setuptools.setup(
    name="mypylib", 
    version="0.1",
    author="schwarzam",
    author_email="gustavo.b.schwarz@gmail.com",
    description="A simple 'dynamic' library used to save any function with a decorator and import it later from any script.",
    url="https://github.com/schwarzam/mypylib",
    packages= setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.6',
    include_package_data=True
)
