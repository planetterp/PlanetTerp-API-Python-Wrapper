import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="planetterp", # Replace with your own username
    version="1.0.3",
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
