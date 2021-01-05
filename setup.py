import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "1.0.0"

setuptools.setup(
    name="planetterp",
    version=__version__,
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
