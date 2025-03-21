import pathlib

import pkg_resources
from setuptools import setup

with pathlib.Path("requirements.txt").open() as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement in pkg_resources.parse_requirements(requirements_txt)
    ]


setup(
    name="mill_local",
    packages=["mill_local"],
    install_requires=install_requires,
    version="0.4.0",
    description="A python3 library to communicate with Mill heaters using local Gen 3 API",
    python_requires=">=3.8.0",
    author="Daniel Hjelseth Høyer",
    author_email="mail@dahoiv.net",
    url="https://github.com/Danielhiversen/pyMillLocal",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
