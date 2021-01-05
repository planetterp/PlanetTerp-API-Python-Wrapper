import setuptools
import re

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# https://stackoverflow.com/a/7071358
VERSION = "Unknown"
VERSION_RE = r"^__version__ = ['\"]([^'\"]*)['\"]"

with open("planetterp/version.py") as f:
    match = re.search(VERSION_RE, f.read())
    if match:
        VERSION = match.group(1)
    else:
        raise RuntimeError("Unable to find version string in planetterp/version.py")


setuptools.setup(
    name="planetterp",
    version=VERSION,
    author="PlanetTerp",
    author_email="admin@planetterp.com",
    description="PlanetTerp API Python wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/planetterp/PlanetTerp-API-Python-Wrapper",
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
    	"requests"
    ]
)
