from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in pharmacy/__init__.py
from pharmacy import __version__ as version

setup(
	name="pharmacy",
	version=version,
	description="Pharmacy Store",
	author="Mubashir Bashir",
	author_email="bashirmubashir798@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
