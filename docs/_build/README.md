## 4. Build Management

Build Automation or Management is the process of scripting and automating the retrieval of software code from a repository, compiling it into a binary artifact, executing automated functional tests, and publishing it into a shared and centralized repository ([from: AemCorp](https://www.aemcorp.com/devops/build-automation)).

For the build automation of this project, I used the PyBuilder that is a "software build tool written in pure Python which mainly targets Python applications. It is based on the concept of dependency based programming but also comes along with powerful plugin mechanism that allows the construction of build life cycles similar to those known from other famous build tools like Apache Maven" (extracted from [Pybuilder homepage](https://pybuilder.github.io/)).

<p align="center">
<img src="https://github.com/federueda/ASW/blob/master/figures/builder/pybuilder_intro.png" width="700" height="100" title="BuildIntro">
</p>

The python version supported by this tool is Python 3.6.10, so it is installed and used with virtualenv, check that was sucessfully created the venv, activate it and assign variables to ./bash_profile.

$ pyenv virtualenv 3.6.10 <name-to-give-it>\
$ pyenv virtualenvs\
$ pyenv activate <name>\
$ pyenv deactivate

Install PyBuilder

$ pip install pybuilder

The following are the main steps to setting up the project for building automation using PyBuilder.

### Step 1: Start configuration of PyBuilder
PyBuilder is configured using a Python file that is named build.py. This is the main file to set up, starting with the instruction to build the project, going through measuring test coverage and finishing with building the whole distribution to make the code available to 3rd parties for example. You can check the [build.py](https://github.com/federueda/ASW/tree/master/build.py) file for details.

### Step 2: Add the source files
PyBuilder separates source files. The default location for python sources is: src/main/python

### Step 3: Adding Scripts
For adding scripts you just put them in the directory src/main/scripts.

### Step 4: Write Unit Tests
For adding scripts you just put them in the directory src/unittest/python. You can check the [tests folder](https://github.com/federueda/ASW/tree/master/src/unittest/python).

### Step 5: Installing needed dependencies
$ pyb install_dependencies

### Step 6: Building the distribution
In Python, the usual way to do this is using distutils. PyBuilder automatically discovers the  modules, packages and scripts and writes configuration for the setup script. As the final step the following command gives us the building for the project: $ pyb -v

In the reports directory you can find some reports each containing detailed information on a tool or command, pyb invoked during the build. Also you can check the unittest and coverage report. A second directory is the dist directory which contains the distribution. The distribution directory contains the same sources but in a Python-typical directory layout. 
