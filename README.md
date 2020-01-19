# Smart scoring of contracts/quotations for companies

## Introduction

This is a simple code in python used to depict some concepts around the designing and development of software.

This code simulates a process from fictitious company ABC, from the definition of the criteria to score a quotation, passing through populating the purchase process, to the display of the results of providers selected by purchase process.

## 1. Unified Modeling Language (UML)

In this section, I will show some UML diagrams used for explaining to other people the sowftare elements for this excercise and also some sofwtare's behaviors. It is an excellent set of notation elements that help us to model business processes and linking them to our software.

In this excercise, I used [Visual Paradigm](https://www.visual-paradigm.com/) Community Edition v16.1 as the tool for creating these diagrams.

### Use Case Diagram

The following diagram shows how different type of users interact with the software.

<p align="center">
<img src="https://github.com/federueda/ASW/blob/master/UML/UseCase.jpg" width="400" height="300" title="Use Case">
</p>

### Activity Diagram

The following diagram models the business process and flow of different actions.

<p align="center">
<img src="https://github.com/federueda/ASW/blob/master/UML/BPM.jpg" width="300" height="400" title="Activity Diagram">
</p>

### Class Diagram

The following diagram shows some of the classes and relationships between them.

<p align="center">
<img src="https://github.com/federueda/ASW/blob/master/UML/Class.jpg" width="600" height="220" title="Class Diagram">
</p>

## 2. Metrics

For the metrics, I use [SonarCloud](https://sonarcloud.io/). Connecting this tool with GitHub, allows an automatic scanning of the code, letting the user configure which kind of measurements to be performed. 

In particular, it was a valuable tool for realizing some issues and points for improvement in the initial code. The Duplications metric was a focal-point for starting to make some changes, that results in a more efficient code. Also, the code smells gave me a good overview of the complexity and the level of code that is confusing and difficult to mantain.

In the following [link](https://sonarcloud.io/dashboard?id=federueda_ASW) you can find the dashboard displaying several metrics for the code.

Also this is a screenshot of a common SonarCloud dashboard:

<p align="center">
<img src="https://github.com/federueda/ASW/blob/master/Sonarcloud/SonarCloudDash.png" width="400" height="300" title="Activity Diagram">
</p>

## 3. Clean Code Development (at least 5 points + 10 cheat sheet)

For this excercise, I had been applying some best practices in terms of clean code development.

- Boy Scout Rule: "*Leave the campground cleaner than you found it.*". Clean code developers leave code in a better state than they found it. So after work accomplished code shall apply more to CCD values than before. What exactly to be done is specific to situation and code – and of course to the grade currently worked on. A CCD in read grade would for an instance move code into version control, if it wasn’t yet in there. And he would focus on eliminating any kind of redundancies which are violations of the DRY principle.

- Don’t Repeat Yourself (DRY): 

- Version Control: Version control eliminates fear to do something wrong and break the system.

- Single Responsibility Principle (SRP): Single Responsibility Principle (SRP) is one of the SOLID principles stating that a calls shall have only one responsibility.

- Automatized Integration Tests: When we do code changes we shall be sure not to break anything. This security can be only achieved by testing if the application still behaves same as before.

## 4. Build Management

## 5. Testing integrated in the Build Management

## 6. Continous Delivery (show pipeline in Travis-CI)

## 7. IDE

The IDE used for this project is [Pycharm](https://www.jetbrains.com/pycharm/). This is a very famous IDE and supports several programming languages and has great features as smart code completition, error highlighting, etc.

Very useful shortcuts that I used for coding in Pycharm:

- F2: Navigate between code issues
- Shift + Enter: start new line after
- Option + Command + Enter: start new line before (for Mac only)
- Option + Shift + Up/Down: move selected code (similar to cut but without disappearing text)
- Option + Command + L: reformat code, very useful to apply code styles quickly

## 8. Domain Specific Language (DSL) (create a small snippet, and apply functional programming)

## 9. Functional Programming 

Prove that you have covered the following:
- Only final data structures
- Side effects free functions
- The use of higher order functions
- Functions as parameters and return values
- Use clojures / anonymous functions



