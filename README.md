# python_packaging
This tutorial walks you through how to package a simple Python project. It will show you how to add the necessary files and structure to create the package, how to build the package, and how to upload it to the Python Package Index.

# Introduction
This tutorial uses a simple project named **pyexample**

Throughout this tutorial we will be creating necessary files and structure to create the 
package, how to build the package, and how to upload it the to python packaging index.

This tutorial will be starter for our large python email package which will be used to 
send emails using command line by setting in the sender's email address, a file for
our email template and another file that will have the receiver's email or emails. But 
more on that later.

[SOURCE](https://packaging.python.org/tutorials/packaging-projects/) FOR THIS TUTORIAL

# A simple project
You can name your project a unique name which does not already exists on [pypi.org](https://pypi.org)

Since this is a example python package so we name it **pyexample** that is [unique](https://pypi.org/search/?q=pyexample)

Okay enough of the chit chat. Let's begin with our package project structure.

Create the structure for your project

```
C:.
└───pyexample
    └───pyexample
```

Inside the inner **pyexample** folder create a new file named ```__init__.py``` and place 
this piece of code in it.

```
name = "pyexample"
```

Once you have this structure ready **cd** into the outer or the main project folder

```
.../pyexample> dir

05-09-2018  14:43    <DIR>          .
05-09-2018  14:43    <DIR>          ..
05-09-2018  14:43    <DIR>          pyexample
               0 File(s)              0 bytes
               3 Dir(s)  211,912,638,464 bytes free
```

# Create the package files
For distributing our project we need to create some files.

Create the files as listed below


**+ is a folder and - is a file and space represents path**
```
+ example_pkg
	+ example_pkg
		- __init__.py
	- setup.py
	- LICENSE
	- README.md
```

# Create setup.py file
```setup.py``` is the build script for [setuptools](https://packaging.python.org/key_projects/#setuptools). According to setuptools,

**
setuptools (which includes easy_install) is a collection of enhancements to the Python distutils that allow you to more easily build and distribute Python distributions, especially ones that have dependencies on other packages.

[distribute](https://pypi.org/project/distribute) was a fork of setuptools that was merged back into setuptools (in v0.7), thereby making setuptools the primary choice for Python packaging.
**

The ```setup.py``` is the file which tells setuptools about the name and version and also 
the files to include.

Open ```setup.py``` and enter the below code in it, you can customize the code as you want

**setup.py**
```
import setuptools
```

Now we will set the several arguments that ```setuptools.setup()``` takes, we will set the 
name, version, description etc. for our package in this file only

```
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
	long_description_content_type="text/markdown",
	url="https://github.com/Alexmhack/python_packaging",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	]
)
```

1. **name** is the name of the python package which be as long and contain any letters 
including *-*, *_*, *numbers*

2. **version** is the package version for example ```django==2.0```

3. **author** and **author_email** are the details of the package author

4. **description** is the small single line summary of the package.

5. **long_description** is a detailed description of the package. This is shown on the 
package detail package on the Python Package Index. In this case, the long 
description is loaded from README.md which is a common pattern.

	```
	with open('README.md') as fh:
		long_description = fh.read()
	...
	author_email="author@example.com",
	description="A small python example project",
	long_description=long_description,
	...
	```

6. **long_description_content_type** tells the index what type of markup is used for the long 
description. In this case, it’s Markdown.

7. **url** is the link to the project homepage which usually is on github like our project
or bitbucket.

8. **packages** is a list of all Python import packages that should be included in the 
distribution package. Instead of listing each package manually, we can use find_
packages() to automatically discover all packages and subpackages. In this case, the list 
of packages will be **pyexample** as that’s the only package present.

9. **classifiers** tell the index and pip some additional metadata about your package. In 
our project, the package is only compatible with Python 3, is licensed under the MIT 
license, and is OS-independent. You should always include at least which version(s) of 
Python your package works on, which license your package is available under, and which 
operating systems your package will work on. Visit [link](https://pypi.org/classifiers/) 
for a complete list of classifiers.

# README and LICENSE
Your package README.md and LICENSE file should contain relevant information for your 
particular package.

README.md file contents will be dispalyed on the pypi.org package homepage and github 
package homepage.

And LICENSE should be included with every python package, the most common license is the 
MIT LICENSE, checkout the [LICENSE](https://github.com/Alexmhack/python_packaging/blob/master/pyexample/LICENSE
) and [README.md](https://github.com/Alexmhack/python_packaging/blob/master/pyexample/README.md) file.

# Generating distribution archives
In this section we will be generating distribution packages for our package. These are 
the files which are uploaded to the Package Index and this enables anyone with a internet
connection and python install that package with [pip](https://packaging.python.org/key_projects/#pip)

Install the latest version of **setuptools** and **wheel** by running

```
> pip install --user --upgrade setuptools wheel
```

OR

```
> python3 -m pip install --user --upgrade setuptools wheel
```

Now run this command from the same directory where setup.py is located

```
.../pyexample> python3 setup.py sdist bdist_wheel

...
adding 'pyexample\__init__.py'
adding 'pyexample-0.0.1.dist-info\top_level.txt'
adding 'pyexample-0.0.1.dist-info\WHEEL'
adding 'pyexample-0.0.1.dist-info\METADATA'
adding 'pyexample-0.0.1.dist-info\RECORD'
removing build\bdist.win-amd64\wheel
```

The process after completion should create some new folders -- ```build``` ```dist``` ```pyexample.egg-info``` and many files inside them. inside the main 
folder.


For more Information visit the [official](https://packaging.python.org/tutorials/packaging-projects/) tutorial

# Uploading the distribution archives
Finally, we will upload our package onto Python Package Index

First thing we need to do is create an account on [Test PyPi](https://test.pypi.org/). Well the yellow highlighted text on the homepage
of TestPypi says this but just for clarity Test Pypi is **Test PyPI is a 
separate instance of the package index intended for testing and 
experimentation.**

You might be wondering why this but this ensures that we test our package
on an instance here without affecting the real python package index.

To register an account, go to https://test.pypi.org/account/register/ and 
complete the steps on that page. You will also need to verify your email 
address before you’re able to upload any packages. For more details on Test 
PyPI, see Using TestPyPI.

Now that you are registered and verified your account you can upload your
distributions using [twine](https://packaging.python.org/key_projects/#twine)

Install twine locally using 

```
> pip install --user --upgrade twine
```

Or if that doesn't work

```
python3 -m pip install --user --upgrade twine
```

Once installed you can upload your distributions well uploading your archives
inside **dist** folder using twine

You should get errors like

```
The user '[your username]' isn't allowed to upload to project 'example-pkg'...
```

**NOTE:**To solve this problem which is basically caused due to package name 
conflicts you need to change the name of the package inside the ```setup.py``` 
file

I renmaed the file to **your_package_username**

```
setuptools.setup(
	name="<your_package_username>",
	version="0.0.1",
	author="psg",
```

After renaming the package inside ```setup.py``` file you need to delete the 
folder that the ```python setup.py sdist bdist_wheel``` and run this command 
again because we made changes in the name of the package and twine will upload the
same archives until we delete or upadte them.

```
twine upload --repository-url https://test.pypi.org/legacy/ dist/*

upload --repository-url https://test.pypi.org/legacy/ dist/*
Uploading distributions to https://test.pypi.org/legacy/
Enter your username: [username]
Enter your password: [password]
Uploading pyexample-0.0.1-py3-none-any.whl
100%|██████████████████████████████████████████| 4.66k/4.66k [00:06<00:00, 66234B/s]
...
```

# Installing your test package
run the pip install but with a simple tweak

I would prefer to install our example package in a virtualenv

```
(env)> python3 -m pip install --index-url https://test.pypi.org/simple/ pyexample_psg

Looking in indexes: https://test.pypi.org/simple/
Collecting pyexample-psg
  Downloading https://test-files.pythonhosted.org/packages/55/99/690744d9eba00f94cdf0631d36a36254b3537309e6311b926943fbe4694d/pyexample_psg-0.0.1-py3-none-any.whl
Installing collected packages: pyexample-psg
Successfully installed pyexample-psg-0.0.1
```

You can check if the package is actually installed and works like the other python
packages do,

**testing.py**
```
import pyexample_psg

print(pyexample_psg.name)
```

Congratulations on your first python package. This was a very simple project and
we uploaded our project on Test PyPi not on PyPi, the process for that is same
but we need to upload the archives on the pypi site which can be done by

```
twine upload dist/*
```

The same credentials will be asked but this time enter in pypi.org details and
install the package using the simple ```pip isntall your-package```
