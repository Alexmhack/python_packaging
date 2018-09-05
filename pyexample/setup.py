import setuptools

with open('README.md') as fh:
	long_description = fh.read()

setuptools.setup(
	name="pyexample",
	version="0.0.1",
	author="PSG",
	author_email="author@example.com",
	description="A small python example project",
	long_description=long_description,
	long_description_content_type="text/markdown"
)
