from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in development/__init__.py
from development import __version__ as version

setup(
	name="development",
	version=version,
	description="somthing",
	author="rahul",
	author_email="rahulpraj4121@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
