from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="dht11",
    version="0.1.0",
    author="Pavel Milanes",
    author_email="pavelm@gmail.com",
    description="Python library for reading DHT11 sensor on Orange Pi SBCs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/stdevPavelmc/DHT11_Python_OPi.GPIO",
    packages=find_packages(),
    install_requires=["OPi.GPIO"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

