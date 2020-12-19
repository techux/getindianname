import setuptools

with open("README.md", "r") as file:
    readme = file.read()

setuptools.setup(
	name="getindianname",
	version="1.0.2",
	author="Devesh Singh",
	author_email="connect.world12345@gmail.com",
	description="Get 30K+ random indian names",
	long_description=readme,
	long_description_content_type="text/markdown",
	url="https://github.com/devesh7272/getindianname",
	license="MIT",
	classifiers=["License :: OSI Approved :: MIT License"],
	packages=["getindianname"],
	include_package_data=True,
	python_requires='>=2.0',

)