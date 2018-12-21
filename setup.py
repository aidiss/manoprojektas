import os
from setuptools import setup


setup(
    name="an_example_pypi_project",
    version="0.0.4",
    author="Andrew Carter",
    author_email="andrewjcarter@gmail.com",
    description=("An demonstration of how to create, document, and publish "
                 "to the cheese shop a5 pypi.org."),
    license="BSD",
    keywords="example documentation tutorial",
    url="http://packages.python.org/an_example_pypi_project",
    packages=['bad_example'],
    long_description="Long description",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
