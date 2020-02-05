# Smart scoring of contracts/quotations for companies
## Advance Software Programming - Concepts

## Introduction

This is a simple code in python used to depict some concepts around the designing and development of software.

This code simulates a process from fictitious company ABC, from the definition of the criteria to score a quotation, passing through populating the purchase process, to the display of the results of providers selected by purchase process.

## 1. Unified Modeling Language (UML)

In this section, I will show some UML diagrams used for explaining to other people the sowftare elements for this excercise and also some sofwtare's behaviors. It is an excellent set of notation elements that help us to model business processes and linking them to our software.

In this excercise, I used [Visual Paradigm](https://www.visual-paradigm.com/) Community Edition v16.1 as the tool for creating these diagrams.

### Use Case Diagram

The following diagram shows how different type of users interact with the software.

<p align="center">
<img src="https://github.com/federueda/ASW/blob/master/doc/uml/UseCase.jpg" width="400" height="300" title="Use Case">
</p>

### Activity Diagram

The following diagram models the business process and flow of different actions.

<p align="center">
<img src="https://github.com/federueda/ASW/blob/master/doc/uml/BPM.jpg" width="300" height="400" title="BPM">
</p>

### Class Diagram

The following diagram shows some of the classes and relationships between them.

<p align="center">
<img src="https://github.com/federueda/ASW/blob/master/doc/uml/Class.jpg" width="480" height="180" title="Class Diagram">
</p>

## 2. Metrics

For the metrics, I used [SonarCloud](https://sonarcloud.io/). Connecting this tool with GitHub, allows an automatic scanning of the code, letting the user configure which kind of measurements to be performed. 

In particular, it was a valuable tool for realizing some issues and points for improvement in the initial code. The Duplications metric was a focal-point for starting to make some changes, that results in a more efficient code. Also, the code smells gave me a good overview of the complexity and the level of code that is confusing and difficult to mantain.

In the following [link](https://sonarcloud.io/dashboard?id=federueda_ASW) you can find the dashboard displaying several metrics for the code.

Also this is a screenshot of a common SonarCloud dashboard:

<p align="center">
<img src="https://github.com/federueda/ASW/blob/master/doc/sonarcloud/SonarCloudDash.png" width="400" height="300" title="SC">
</p>

## 3. Clean Code Development (at least 5 points + 10 cheat sheet)

For this excercise, I had been applying some best practices in terms of clean code development.

- Boy Scout Rule: "*Leave the campground cleaner than you found it.*". Clean code developers leave code in a better state than they found it. So after work accomplished code shall apply more to CCD values than before. What exactly to be done is specific to situation and code – and of course to the grade currently worked on. A CCD in read grade would for an instance move code into version control, if it wasn’t yet in there. And he would focus on eliminating any kind of redundancies which are violations of the DRY principle.

- Don’t Repeat Yourself (DRY): 

- Version Control: Version control eliminates fear to do something wrong and break the system.

- Single Responsibility Principle (SRP): Single Responsibility Principle (SRP) is one of the SOLID principles stating that a calls shall have only one responsibility.

- Automatized Integration Tests: When we do code changes we shall be sure not to break anything. This security can be only achieved by testing if the application still behaves same as before.

## 4. Build Management

Build Automation or Management is the process of scripting and automating the retrieval of software code from a repository, compiling it into a binary artifact, executing automated functional tests, and publishing it into a shared and centralized repository ([from: AemCorp](https://www.aemcorp.com/devops/build-automation)).

For the build automation of this project, I used the PyBuilder that is a "software build tool written in pure Python which mainly targets Python applications. It is based on the concept of dependency based programming but also comes along with powerful plugin mechanism that allows the construction of build life cycles similar to those known from other famous build tools like Apache Maven" (extracted from [Pybuilder homepage](https://pybuilder.github.io/)). 

<p align="center">
<img src="https://github.com/federueda/ASW/blob/master/doc/builder/pybuilder_intro.png" width="900" height="131" title="BuildIntro">
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

PyBuilder is configured using a Python file that is named build.py. This is the main file to set up, starting with the instruction to build the project, going through measuring test coverage and finishing with building the whole distribution to make the code available to 3rd parties for example.

You can check the [build.py](https://github.com/federueda/ASW/tree/master/build.py) file for details.

### Step 2: Add the source files

PyBuilder separates source files. The default location for python sources is:

src/main/python

### Step 3: Adding Scripts

For adding scripts you just put them in the directory src/main/scripts. You can chech the [contracts-pybuilder.py](https://github.com/federueda/ASW/tree/master/src/main/scripts/contracts-pybuilder.py) file.

### Step 4: Write Unit Tests

For adding scripts you just put them in the directory src/unittest/python. You can check the [contracts_tests.py](https://github.com/federueda/ASW/tree/master/src/unittest/python/contracts_tests.py) file. 

### Step 5: Installing needed dependencies

$ pyb install_dependencies

### Step 6: Building the distribution

In Python, the usual way to do this is using distutils. PyBuilder automatically discovers the  modules, packages and scripts and writes configuration for the setup script. As the final step the following command gives us the building for the project (in verbose mode):

$ pyb -v

In the reports directory you can find some reports each containing detailed information on a tool or command, pyb invoked during the build. Also you can check the unittest and coverage report.

A second directory is the dist directory which contains the distribution. The distribution directory contains the same sources but in a Python-typical directory layout. You can also find the setup.py

## 5. Testing integrated in Build Management

PyBuilder is used to integrate the testing into the build management. Steps were explained in the section before, but details of configuration could be find in the [PyBuilder Tutorial](https://pybuilder.github.io/documentation/tutorial.html#.XjrZ-RNKj6C).

You can check again the [contracts_tests.py](https://github.com/federueda/ASW/tree/master/src/unittest/python/contracts_tests.py) file.

## 6. Continous Delivery (show pipeline in Travis-CI)

Python projects need to provide the script key in their .travis.yml to specify what command to run tests with.

For example, if your project uses pytest:

- command to run tests
- script: pytest

## 7. IDE

The IDE used for this project is [Pycharm](https://www.jetbrains.com/pycharm/). This is a very famous IDE and supports several programming languages and has great features as smart code completition, error highlighting, etc.

Very useful shortcuts that I used for coding in Pycharm:

- F2: Navigate between code issues
- Shift + Enter: start new line after
- Option + Command + Enter: start new line before (for Mac only)
- Option + Shift + Up/Down: move selected code (similar to cut but without disappearing text)
- Option + Command + L: reformat code, very useful to apply code styles quickly

## 8. Domain Specific Language (DSL)

In this example, you will see a DSL designed to interact with a player for a little "matrix-type" game. The main idea is to use a language that could interact in a easy way, just entering "intuitive commands" in order to arrive from initial postion on the matrix to the desired destination in the matrix. This is achieved through a transformation engine inside the General Purpose Programming Language, in this case Python.

To see the code please go to src folder and find [dsl-rev2.py](src/dsl_rev2.py) file. If you run it, then you find a small game where you need to move the "number 1" until arrive to the "number 2" position in the matrix, using commands as up, down, left or right. A screenshot is shown:

<p align="center">
<img src="https://github.com/federueda/ASW/blob/master/doc/dsl/dsl_matrix3.png" width="500" height="300" title="DSL_Matrix">
</p>


The main advantages of a DSL are:
- It is a portable code that you could use inside several general-purpose languages
- Designed for a limited scope and specific domain expertise, that makes it easier to understand for the non-technical users
- Easier to find issues or errors because of its limited scope
- Higher expressiveness compared to general purpouse programming language

In the following diagram is possible to understand the basic DSL functionalities that interact between the player and the matrix through the command validator.

<p align="center">
<img src="https://github.com/federueda/ASW/blob/master/doc/dsl/DSL.jpg" width="400" height="280" title="DSL_Diagram">
</p>

## 9. Functional Programming 

Prove that you have covered the following:
- Only final data structures
- Side effects free functions
- The use of higher order functions
- Functions as parameters and return values
- Use clojures / anonymous functions



