# Smart scoring of contracts/quotations for companies
## Advanced Software Programming - Concepts

## Introduction

This is a simple code in python used to depict some concepts around the designing and development of software.

This code simulates a process from fictitious company ABC, from the definition of the criteria to score a quotation, passing through populating the purchase process, to the display of the results of providers selected by purchase process.

For running the code you need to enter the path of every file needed for the system to work, in this case the list of providers, purchase processes, quotations and the scoring policy as follows (assuming the files are in the same folder as contracts.py). Yopu can find these example files in the [data folder](https://github.com/federueda/ASW/tree/master/data).

$ python3 contracts.py --providers Providers.csv --purchase Purchase_Process.csv --quotations Quotations.csv --scoring Scoring_Policy.csv

<p align="center">
<img src="https://github.com/federueda/ASW/blob/master/figures/others/Code.png" width="400" height="220" title="Code">
</p>

## 1. Unified Modeling Language (UML)

In this section, I will show some UML diagrams used for explaining to other people the sowftare elements for this excercise and also some sofwtare's behaviors. It is an excellent set of notation elements that help us to model business processes and linking them to our software.

In this excercise, I used [Visual Paradigm](https://www.visual-paradigm.com/) Community Edition v16.1 as the tool for creating these diagrams.

### 1.1 Use Case Diagram

The following diagram shows how different type of users interact with the software.

<p align="center">
<img src="https://github.com/federueda/ASW/blob/master/figures/uml/UseCase.jpg" width="400" height="300" title="Use Case">
</p>

### 1.2 Activity Diagram

The following diagram models the business process and flow of different actions.

<p align="center">
<img src="https://github.com/federueda/ASW/blob/master/figures/uml/BPM.jpg" width="300" height="400" title="BPM">
</p>

### 1.3 Class Diagram

The following diagram shows some of the classes and relationships between them.

<p align="center">
<img src="https://github.com/federueda/ASW/blob/master/figures/uml/Class.jpg" width="480" height="180" title="Class Diagram">
</p>

## 2. Metrics
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=federueda_ASW&metric=alert_status)](https://sonarcloud.io/dashboard?id=federueda_ASW)[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=federueda_ASW&metric=security_rating)](https://sonarcloud.io/dashboard?id=federueda_ASW)[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=federueda_ASW&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=federueda_ASW)

For the metrics, I used [SonarCloud](https://sonarcloud.io/). Connecting this tool with GitHub, allows an automatic scanning of the code, letting the user configure which kind of measurements to be performed.

In particular, it was a valuable tool for realizing some issues and points for improvement in the initial code. The Duplications metric was a focal-point for starting to make some changes, that results in a more efficient code. Also, the code smells gave me a good overview of the complexity and the level of code that is confusing and difficult to mantain.

See the [SonarCloud Dashboard](https://sonarcloud.io/dashboard?id=federueda_ASW) displaying main metrics for the code.

## 3. Clean Code Development (at least 5 points + 10 cheat sheet)

### 3.1 CCD Principles:

- **3.1.1 Don’t Repeat Yourself (DRY):** Try to avoid the copy and paste practice and instead encapsulate this repeated code for example in functions. You can check the examples in the code [here](https://github.com/federueda/ASW/blob/master/src/main/python/models/provider.py#L1).
- **3.1.2 Automated Unit Tests:** Automation simply saves time. And the more complex the code, the greater the reduction in fear. You can check automated unit tests [here](https://github.com/federueda/ASW/tree/master/src/unittest/python).
- **3.1.3 Code Coverage Analysis:** it is automated inside the pybuilder (builder automation) process using Python-Coverage plugin. You can check the code and plugin inside the [build.py](https://github.com/federueda/ASW/blob/master/build.py) file. You can see the result of the test coverage in section 3.16
- **3.1.4 Continuous Integration:** for this project is used the Travis-CI tool, you can the CI [dashboard](https://travis-ci.org/federueda/ASW).
- **3.1.5 Version Control:** for this project is used the Git tool, you can check releases [here](https://github.com/federueda/ASW/releases).
- **3.1.6 Use a Buildmanagement Tool:** nowadays, documentation generation, testing, creating the binaries, etc. cannot be done manually. It is used pybuilder tool for performing these actions. You can check the [build.py](https://github.com/federueda/ASW/blob/master/build.py) file used for build automation.

### 3.2 Clean Code Cheat Sheet:

Now, the following are examples of best practices applied to the project from the [clean code cheat sheet](https://github.com/federueda/ASW/blob/master/figures/cleancode/cheatsheet.pdf):

- **3.2.1 Boy Scout Rule:** leave the campground cleaner than you found it.
- **3.2.2 Don´t manage multiple languages in one source file:** reference to python code [contracts.py](https://github.com/federueda/ASW/blob/master/src/main/python/contracts.py).
- **3.2.3 Project Build Requires Only One Step:** Check out and then build with a single command, in this case pyb command from pybuilder, check the [build.py](https://github.com/federueda/ASW/blob/master/build.py).
- **3.2.4 Executing tests requires only one step:** Run all unit tests with a single command, in this case using the unittest plugin in pybuilder. See unit [test files](https://github.com/federueda/ASW/tree/master/src/unittest/python).
- **3.2.5 Dead Comment, Code:** delete unused things.
- **3.2.6 Poorly Written Comment:** comment does not add any value (redundant to code), is not well formed, not correct grammar/spelling.
- **3.2.7 Single Responsibility Principle (SRP):** single Responsibility Principle (SRP) is one of the SOLID principles stating that a calls shall have only one responsibility.
- **3.2.8 Understand the Algorithm:** Just working is not enough, make sure you understand why it works.
- **3.2.9 Test Method Naming:** Names reflect what is tested, an example in the python file [contracts.py](https://github.com/federueda/ASW/blob/master/src/main/python/contracts.py#L304).

## 4. Build Management

Build Automation or Build Management is the process of scripting and automating the retrieval of software code from a repository, compiling it into a binary artifact, executing automated functional tests, and publishing it into a shared and centralized repository ([from: AemCorp](https://www.aemcorp.com/devops/build-automation)).

For this project, I used the PyBuilder that is a software build tool written in pure Python which mainly targets Python applications. It is based on the concept of dependency based programming but also comes along with powerful plugin mechanism that allows the construction of build life cycles similar to those known from other famous build tools like Apache Maven. (extracted from [Pybuilder homepage](https://pybuilder.github.io/)).

<p align="center">
<img src="https://github.com/federueda/ASW/blob/master/figures/builder/pybuilder_intro.png" width="700" height="100" title="BuildIntro">
</p>

PyBuilder is configured using a Python file that is named build.py. This is the main file to set up, starting with the instruction to build the project, going through measuring test coverage and finishing with building the whole distribution to make the code available to 3rd parties for example. You can check the [build.py](https://github.com/federueda/ASW/tree/master/build.py) file for details.

I used pybuilder for several tasks including unit testing, you can check the [unit tests](https://github.com/federueda/ASW/tree/master/src/unittest/python). Also, generating documentation for the project using [sphinx](https://www.sphinx-doc.org/en/master/) and also automatically generating files as [requirements.txt](https://github.com/federueda/ASW/blob/master/requirements.txt) using pipreqs as pybuilder tasks. The following is the pybuilder process executing:

<p align="center">
<img src="https://github.com/federueda/ASW/blob/master/figures/builder/Build_Auto.png" width="600" height="450" title="BA">
</p>

In the reports directory you can find some reports each containing detailed information on a tool or command, pyb invoked during the build. Also you can check the unittest and coverage report. A second directory is the dist directory which contains the distribution. The distribution directory contains the same sources but in a Python-typical directory layout.

## 5. Testing integrated in Build Management

PyBuilder is used to integrate the testing into the build management. Steps were explained in the section before, but details of configuration could be find in the [PyBuilder Tutorial](https://pybuilder.github.io/documentation/tutorial.html#.XjrZ-RNKj6C).

## 6. Continous Delivery (show pipeline in Travis-CI)
[![Build Status](https://travis-ci.org/federueda/ASW.svg?branch=master)](https://travis-ci.org/federueda/ASW)

I used Travis-CI to manage some tasks around continous integration creating the .travis.yml. In this case the Travis Pipeline tasks were executed in the build automation section, but we could see the [Travis-CI dashboard](https://travis-ci.org/federueda/ASW) where requirements.txt is executed.

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

To see the code please go to src folder and find [dsl.py](src/main/python/dsl.py) file. If you run it, then you find a small game where you need to move the "number 1" until arrive to the "number 2" position in the matrix, using commands as up, down, left or right. A screenshot is shown:

<p align="center">
<img src="https://github.com/federueda/ASW/blob/master/figures/dsl/dsl_matrix3.png" width="500" height="300" title="DSL_Matrix">
</p>

The main advantages of a DSL are:
- It is a portable code that you could use inside several general-purpose languages
- Designed for a limited scope and specific domain expertise, that makes it easier to understand for the non-technical users
- Easier to find issues or errors because of its limited scope
- Higher expressiveness compared to general purpouse programming language

In the following diagram is possible to understand the basic DSL functionalities that interact between the player and the matrix through the command validator.

<p align="center">
<img src="https://github.com/federueda/ASW/blob/master/figures/dsl/DSL.jpg" width="691" height="299" title="DSL_Diagram">
</p>

## 9. Functional Programming

Prove that you have covered the following:

- **9.1 Only final data structures:** variables are Immutable. The immutable nature of variables in a functional programming language benefits in the form of preserving the state throughout the execution of a program. See example in the [code](https://github.com/federueda/ASW/blob/master/src/main/python/dsl.py#L7).

- **9.2 Side effects free functions:** pure functions always produce the same output with the same arguments disregard of other factors and they are also deterministic. You can see a side effects free functions example in the [code](https://github.com/federueda/ASW/blob/master/src/main/python/dsl.py#L72).

- **9.3 The use of higher order functions:** functions in the functional programming style are treated as variables. These first-class functions are allowed to be passed to other functions as parameters or returned from functions or stored in data structures. A higher-order function is a function that takes other functions as arguments and/or returns functions. You can see an example in the [code](https://github.com/federueda/ASW/blob/master/src/main/python/dsl.py#L86).

- **9.4 Use clojures / anonymous functions:** anonymous functions are not defined as standard functions, is not bound to an identifier and they are used once. You can see an example in the [code](https://github.com/federueda/ASW/blob/master/src/main/python/dsl.py#L34).

- **9.5 Functions as parameters and return values:** You can see an example in the [code](https://github.com/federueda/ASW/blob/master/src/main/python/dsl.py#L66).

