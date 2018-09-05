import setuptools

with open('README.md') as fh:
	long_description = fh.read()

setuptools.setup(
	name="pyexample_psg",
	version="0.0.1",
	author="psg",
	author_email="pranavg456@gmail.com",
	description="A small python example project",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/Alexmhack/python_packaging",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	]
)
