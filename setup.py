import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

install_requires = [
    "Django>=1.11.20,<2.0.0",
    "djangorestframework>=3.9.1",
    "djangorestframework-gis==0.14",
]

dependency_links=['http://github.com/OpenUpSA/wazimap_sa_boundaries.git/tarball/master#egg=package-1.0']

setup(
    name="Wazimap SA Boundaries",
    version="0.1",
    packages=find_packages(exclude=["project"]),
    include_package_data=True,
    install_requires=install_requires,
    dependency_links=dependency_links,
    licence="MIT",
    description="A Wazimap plugin for point in polygon lookups",
    long_description=README,
    url="https://github.com/OpenUpSA/wazimap_sa_boundaries",
    author="OpenUp",
    author_email="adi@openup.org.za",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 1.11",  # replace "X.Y" as appropriate
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT Licence",  # example license
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        # Replace these appropriately if you are stuck on Python 2.
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)
