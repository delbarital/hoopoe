from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup (
    name='hoopoe',
    version='0.0.1',
    description='Hoopoe is a data enrichment service that makes it easy to improve your data-centric services and increase the accuracy of your ML models.',
    py_modules=["hoopoe"],
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
)