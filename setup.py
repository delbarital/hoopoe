from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup (
    name='hoopoe',
    version='0.0.11',
    description='Hoopoe is a data enrichment service that makes it easy to improve your data-centric services and increase the accuracy of your ML models.',
    py_modules=["hoopoe", "us_states", "international_phone_prefixes", "units_conversion", "canonicalization"],
    package_dir={'': 'src'},
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    long_description =long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        #TODO: Check if can be reduced
        "pandas>=1",
    ],
    extra_requires={
        #TODO: Check if can be reduced
        "dev": [
            "pytest>=3.7",
            "check-manifest>=0.45"
        ],
    },
    url="https://github.com/delbarital/hoopoe",
    author="Tal Delbari",
    author_email="delbarital@gmail.com",
)