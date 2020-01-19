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

## 3. Clean Code Development (at least 5 points + 10 cheat sheet)

## 4. Build Management

## 5. Testing integrated in the Build Management

## 6. Continous Delivery (show pipeline in Travis-CI)

## 7. IDE (favorite shortcuts)

## 8. Domain Specific Language (DSL) (create a small snippet, and apply functional programming)

## 9. Functional Programming 

Prove that you have covered the following:
 ..* only final data structures
 ..* side effects free functions
 ..* the use of higher order functions
 ..* functions as parameters and return values
 ..* use clojures / anonymous functions



