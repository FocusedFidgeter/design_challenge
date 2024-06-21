

## Overview

Welcome to the 30-Day Design Challenge!

In this course, you'll get plenty of practice with a wide variety of software design problems. There's a new problem for you every day, but you can go through the challenges at your own pace.

Don't hesitate to ask questions and give feedback about the challenges by posting a comment. Your feedback is extremely helpful to improve the challenges for everyone - so thank you in advance!

I'm really excited for you to start with the challenges. Good luck!

**Table of Contents**

- [Overview](#overview)
- [Introduction](#introduction)
- [Challenges](#challenges)
  - [Day 1: KISS](#day-1-kiss)
    - [Resources](#resources)
  - [Day 2: Type Annotations](#day-2-type-annotations)
    - [Resources](#resources-1)
  - [Day 3: Decoupling](#day-3-decoupling)
    - [Resources](#resources-2)
  - [Day 4: DRY](#day-4-dry)
    - [Resources](#resources-3)
  - [Day 5: String Formatting](#day-5-string-formatting)
    - [Resources](#resources-4)
  - [Day 6: Demeter](#day-6-demeter)
    - [Resources](#resources-5)
  - [Day 7: Better Discounts](#day-7-better-discounts)
  - [Day 8: Payment Strategy](#day-8-payment-strategy)
    - [Resources](#resources-6)
  - [Day 9: Plugins](#day-9-plugins)
    - [Resources](#resources-7)
  - [Day 10: OO to Functional](#day-10-oo-to-functional)
    - [Resources](#resources-8)
  - [Day 11: Cohesion](#day-11-cohesion)
    - [Resources](#resources-9)
  - [Day 12: MVP](#day-12-mvp)
    - [Resources](#resources-10)
  - [Day 13: Inheritance](#day-13-inheritance)
    - [Resources](#resources-11)
  - [Day 14: Abstraction](#day-14-abstraction)
    - [Resources](#resources-12)
  - [Day 15: Higher-Order Functions](#day-15-higher-order-functions)
    - [Resources](#resources-13)
  - [Day 16: Configuration](#day-16-configuration)
  - [Day 17: Concurrency](#day-17-concurrency)
    - [Resources](#resources-14)
  - [Day 18: Refactoring](#day-18-refactoring)
  - [Day 19: Itertools](#day-19-itertools)
    - [Resources](#resources-15)
  - [Day 20: Inappropriate Intimacy](#day-20-inappropriate-intimacy)
    - [Resources](#resources-16)
  - [Day 21: Undo/Redo](#day-21-undoredo)
      - [Resources](#resources)
  - [Day 22: SQL to ORM](#day-22-sql-to-orm)
      - [Resources](#resources-1)
  - [Day 23: Unit tests (Basic)](#day-23-unit-tests-basic)
  - [Day 24: Unit tests (Advanced)](#day-24-unit-tests-advanced)
  - [Day 25: Operations Layer](#day-25-operations-layer)
  - [Day 26: Ticket Cancellation](#day-26-ticket-cancellation)
  - [Day 27: Messaging](#day-27-messaging)
      - [Resources](#resources-2)
  - [Day 28: Validation](#day-28-validation)
      - [Resources](#resources-3)
  - [Day 29: Bridge](#day-29-bridge)
      - [Resources](#resources-4)
  - [Day 30: Mixins](#day-30-mixins)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)

## Introduction

Each challenge is based on a code example that you can download at the top. To complete a challenge, read through the challenge text and work on the code to solve the problem. Some challenges might be quite short, others are going to take you a bit more time. You'll also see some challenges work on the same codebase. I've done this on purpose so that on the one hand you will recognize the code sooner so it takes you less time to get into the material, and reusing code also made it easier for me to create more complex challenges.

## Challenges

### Day 1: KISS
Count the frequency of each type of fruit and return a dictionary where the keys are the names of the fruits and the values are their respective counts. Write a Python function named count_fruits that accomplishes this task in the simplest possible way. Follow the KISS principle to avoid unnecessary complexity in your solution.

After completing the function, write tests to ensure that it's working correctly. You can use Python's built-in unittest package for this, or you can simply add a couple of assertions to the main function.

After you've completed the tasks, reflect on your solution and ask yourself the following questions:

* Is your solution as simple as it could be, or is there a simpler approach?
* Does your solution use language features and constructs appropriately and effectively?

#### Resources
* [KISS](https://en.wikipedia.org/wiki/KISS_principle) (Website)
  
### Day 2: Type Annotations
Type annotations in Python allow you to explicitly specify the data types of constants, variables, function parameters and return values. This helps to improve code clarity, readability, and maintainability, especially in large-scale projects where multiple developers may be working on the same codebase.

By using type annotations, you can catch potential bugs early on in the development process, and on top of that they help your IDE provide better code suggestions and error detection.

For this challenge, you will need to add type annotations to the code given in the `type_annotations\before.py`. Before you start working on the code, make sure your VS Code editor has the Python language extension installed and also make sure that you've set type checking mode to "strict". You can do this by adding the following line to your settings.json file:

```
"python.analysis.typeCheckingMode": "strict"
```

Once you've done that and you open `type_annotations\before.py`, you should see a bunch of errors related to the types missing (even though you can still run the code).

The challenge is to write the type annotations so that:

* All type errors identified by the IDE are gone
* The type annotations are a generic as possible - in other words, the type annotations shouldn't impose any extra limitations on how you can use the functions

You're not allowed to use the Any type in this challenge. You can make minor modifications to the code if needed. However, the functionality should stay the same and you're not allowed to change things like function arguments and return types.

#### Resources
* [PEP 0484](https://peps.python.org/pep-0484/) (Website)


### Day 3: Decoupling
In this challenge, you're going to work on a banking service.

The problem with the current code is that the `BankService` class in `bank.py` is highly coupled with the payment service and the different account types. Also, the code has quite a bit of duplication. Your job is to refactor this code so that it's less coupled and has less duplicate code.

You have quite a bit of freedom in this challenge: it's okay to introduce new classes or replace existing classes by functions, feel free to experiment! However, the goal remains that banking operations should be decoupled from payment operations as much as possible.

#### Resources
* [Reducing coupling](https://www.youtube.com/watch?v=qR4-PBLUZNw) (Video)
  
  
### Day 4: DRY
The Don't Repeat Yourself (DRY) principle is a coding principle that aims to reduce repetition in code. It suggests that when writing code, you should avoid duplicating code logic or functionality in multiple places, and instead, create reusable code elements that can be called and reused throughout your codebase.

There are at least 3 places where there's a lot of code repetition. The challenge is to identify these places and refactor the code so that the repetition is removed.

#### Resources
* [DRY principle](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) (Wikipedia)
  
### Day 5: String Formatting

String formatting is a way of constructing a string that includes dynamic or variable values. It allows you to insert values into a string and control how those values are displayed. You can use string formatting to replace placeholders in a string with actual values, such as numbers or strings, and also specify how those values should be formatted.

This can help make your code more readable and easier to maintain, especially when you need to output complex or formatted strings. In Python, there are different ways to perform string formatting, including using the % operator, the format() method, or f-strings. 

The starting point of this challenge is a code example that creates a shopping cart and prints an overview of the shopping cart contents to the console. Currently, this is what the program produces, which is unfortunately quite hard to read:

```
Shopping Cart:
Item, Price, Qty, Total
Apple, 1.50, 10, 15.00
Banana, 2.00, 2, 4.00
Pizza, 11.90, 5, 59.50
========================================
Total: $78.50
```
The goal is to use string formatting to make the output easier to read by better aligning the values. Ultimately, the table look something like this:
```
Shopping Cart:
Item           Price    Qty        Total
Apple       $   1.50     10     $  15.00
Banana      $   2.00      2     $   4.00
Pizza       $  11.90      5     $  59.50
========================================
Total: $ 78.50
```

The exact number of spaces between each column is not important. However, the dollar signs as well as the prices need to be correctly aligned.

#### Resources
* [PEP 498](https://peps.python.org/pep-0498/) (Website)
* [f-strings](https://www.youtube.com/watch?v=Mfmr_Puhtew) (Video)

### Day 6: Demeter
The Law of Demeter, also known as the Principle of Least Knowledge, is a software design guideline that suggests that an object should avoid direct interaction with other objects that are not directly related to its primary purpose.

In simpler words, this law states that an object should only communicate with its immediate friends and not with the friends/attributes of its friends. Violating this principle can result in tightly coupled and brittle code that is difficult to maintain and modify over time.

A typical violation of the law is that one object directly interacts with an instance variable of another object. The code belonging to this challenge has several violations of the Law of Demeter. Refactor the code to remove these violations.

#### Resources
* [Law of Demeter](https://en.wikipedia.org/wiki/Law_of_Demeter) (Wikipedia)

### Day 7: Better Discounts
A new feature has been added to the shopping cart system: discounts!

Unfortunately, the developer who coded this (let's call him "Arjan"), didn't do a very good job! He used inheritance to add the discount feature and set things up in such a way that the discount codes and discount handling is all hardcoded in a single method.

You've been hired to redesign the discounts system so that it's easier to add new discount codes on the fly and simplify the code. Feel free to change anything you like in the code, but make sure there's still a ShoppingCart class since that's what the customer needs to integrate into their webshop.

### Day 8: Payment Strategy
The Strategy pattern is a design pattern that allows you to define a family of algorithms (strategies) and make them interchangeable within an object at runtime. In other words, it lets you define a set of related algorithms and encapsulate each one in a separate class.

An object can then use one of these algorithms (strategies) without knowing the details of how the algorithm works or how it's implemented. This pattern promotes the principle of "composition over inheritance", which means that behavior should be composed dynamically at runtime rather than being hard-coded into classes through inheritance. This makes the code more flexible, extensible, and easy to maintain.

The example code allows you to pay by credit card, PayPal or Apple Pay. This is handled by the `process_payment` method in the ShoppingCart class. In this version of the code though, the shopping cart and in particular the `process_payment` method needs to know all the implementation details of each payment processing option. 

For this challenge you need to refactor this code and use the Strategy pattern to remove the coupling between the shopping cart and the different payment methods. You don't have to follow the pattern exactly by the book, you can also use a variety of the pattern, as long as it accurately removes the coupling.

#### Resources
* [Strategy design pattern](https://www.youtube.com/watch?v=WQ8bNdxREHU) (Video)
* [Follow up on Strategy design pattern](https://www.youtube.com/watch?v=n2b_Cxh20Fw) (Video)
* [Strategy design pattern](https://en.wikipedia.org/wiki/Strategy_pattern) (Wikipedia)

### Day 9: Plugins
In this challenge, we're going to take the Strategy pattern you implemented in the previous challenge to the next level.

When you take a look at the code, you see that at the moment, adding a new payment processor means we have to change the application code. For example, if you wanted to add a Google Pay option, you'll need to add a function to the main.py file. This is not ideal, because that file will get larger and larger as you add more payment methods. Additionally, it would be ideal if adding a new payment method requires only minimal changes in the rest of the code so that things are nicely decoupled and it's really easy to extend the code in the future.

The aim of this challenge is to modify the code so that we can add additional payment methods without having to change anything at all in the main file. This is what's also called a plugin mechanism.

Modify the code so that you can add more payment methods by going through these simple steps:

* Create a new Python script containing the code for the payment method that you'd like to add.
* Put the script in a dedicated plugins folder.
* Now run main.py - it should recognize the new payment method in the plugins folder and make it available automatically to the user.

Once you've refactored the code so that it supports a plugin interface, test it by creating a new payment method and verify that you can use it without having to change anything in the rest of the code.

<details>
<summary>Hints</summary>

* You can use importlib to dynamically load Python scripts and you can use os.walk to retrieve the files in a particular folder.
* Feel free to split things up into separate files. For example, you could create a separate file that manages loading and getting access to the plugins, so your main.py file remains relatively small.

#### Resources
* [Plugin Architecture](https://www.youtube.com/watch?v=iCE1bDoit9Q)
  
</details>

### Day 10: OO to Functional

The debate over functional vs object-oriented programming has been ongoing for decades, and both paradigms have their proponents and detractors. At a high level, object-oriented programming (OOP) is a programming paradigm that models real-world objects and their relationships, while functional programming (FP) is a programming paradigm that focuses on the evaluation of functions and their application to data.

Even though I'm using more and more concepts from the functional paradigm in my own projects, I find that in some cases an object-oriented approach is a better solution. Fortunately for us, Python supports both object-oriented and functional programming!

This challenge is aimed at helping you understand the difference between object-oriented (OO) programming and functional programming. As you can see, the code has been setup as an object-oriented program. There are various Shape classes as well as a ShapeCalculator class.

Change the code to follow a functional coding style. Make sure the refactored code has the following properties:

* There are zero classes in the new version of the code, you're only allowed to use functions.
* There are zero variables and variable assignments in the new version of the code - arguments to functions are allowed.

#### Resources
* [Functional programming](https://en.wikipedia.org/wiki/Functional_programming) (Wikipedia)
* [Comparing functions versus classes](https://www.youtube.com/watch?v=txRTzljmV0Q) (Video)

### Day 11: Cohesion
It is very common when coding and especially for beginners that people write very big functions with lots of different functionalities inside. Although this might look very appealing approach because you can write the code faster, it creates unnecessary coupling of functionalities, that becomes a headache later on when you try to test, debug, or further develop your application.

In the code belonging to this challenge, you'll see that there is a single `main()` function that contains everything. Refactor this function into several smaller ones without - of course - affecting the overall functionality. There are many ways in which you can split up the single large function, but try to come up with a solution that makes sure the separate functions are not too large, that they're easy to test, and that there's not too much duplication.

#### Resources
* [cohesion and coupling](https://www.youtube.com/watch?v=eiDyK_ofPPM) (Video)
* [Cohesion](https://en.wikipedia.org/wiki/Cohesion_(computer_science)) (Wikipedia)


### Day 12: MVP

When you create a GUI application, it's a good thing to consider separating the GUI-specific code such as creating frames, buttons, text fields, and so on, from the logic of your application (what should happen when you press a button), as well as from the data that your application relies on or modifies.

There are different architectural patterns that address this. The most well-known one is Model-View-Controller, but there are several varieties including Model-View-Presenter or Model-View-Viewmodel.

The code that you'll use as a starting point in this challenge has a single `main()` function containing everything, although it does rely on the functions you created in the previous challenge that process data.

Refactor this code by using a GUI architectural pattern such as Model-View-Controller or Model-View-Presenter. Consider:

* What code should be part of each element of the pattern?
* Where should we create and connect the Model, View, and Controller/Presenter objects?
* Which object needs to have a reference to which other object?


#### Resources
* [Model-view-controller](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller) (Wikipedia)
* [Model-view-presenter](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93presenter) (Wikipedia)
* [GUI architectures](https://www.youtube.com/watch?v=eHhXoCNCI1c) (Video)

### Day 13: Inheritance

I've learned that you should use inheritance sparingly in your code. It can be a really helpful tool to decouple your code, especially if you use inheritance with Abstract Base Classes or Protocols in Python.

Unfortunately, many developers abuse inheritance to do other things than decoupling your code. The code belonging to this challenge is a good example of that.

The code retrieves the weather information from a free-to-use weather API and prints it to the console. To run the code, you'll need to obtain a free API key from the OpenWeather service. That requires creating an account and you automatically receive one after you confirm your e-mail address. To create an account, [follow these instructions](https://openweathermap.org/appid#signup). Note that it might take some few minutes before the API key is activated on their servers.

* After you've created the free account and you have an API key, download the code and replace the key in the code with your API key. Run the code to see what it does.
* Analyze the code, and take a look at how it's organized. In particular, think about how inheritance is being used in the code.
* Refactor the code so that inheritance is no longer used.
* Compare your second version with the original code and consider in what ways the new version is better. How did you remove the inheritance relationship? Did it lead you to change other things as well in the code?

#### Resources
* [Composition vs. Inheritance](https://www.youtube.com/watch?v=0mcP8ZpUR38) (Video)

### Day 14: Abstraction

Introducing (levels of) abstraction allows classes to need less knowledge of each other, thus reducing coupling. This makes code more readable, maintainable and understood better both in depth, but also from a higher (conceptual) level.

For this challenge you need to refactor the given code so that the `WeatherService` becomes agnostic to the requests module.

In the current setup, `WeatherService` fetches the current weather forecast of a given city using the OpenWeather API. However, the `WeatherService` class is coupled to the requests library. This makes it hard to change the request module in the future to something else, or to replace it by a mock http request when testing the code.

The challenge is to use abstraction to separate the `WeatherService` class from the requests module.

<details>
<summary>Hints</summary>

You can create a separate `RequestsClient` class that defines a get method for fetching data from an API, and then let the WeatherService depend on an abstraction.

</details>


#### Resources
* [Dependency Injection and Dependency Inversion](https://www.youtube.com/watch?v=2ejbLVkCndI)


### Day 15: Higher-Order Functions

A higher-order function is a function that takes one or more functions as arguments, and/or returns a function as  its result. In other words, a higher-order function is a function that operates on functions.

Higher-order functions are a key feature of functional programming, which is a programming paradigm that emphasizes the use of functions to perform computations. They enable a more declarative and expressive style of programming, where functions can be composed, combined, and manipulated like any other value.

Some common examples of higher-order functions in Python include map, filter, and reduce. These functions take one or more functions as arguments and apply them to some input data to produce a new output.

The goal of this challenge is to take the object-oriented weather service code from the previous challenge (see the Downloads section at the top) and change it to functional code that relies on a higher-order function, as follows:

* First, turn the `WeatherService` class into separate functions. Specifically, create a `get_forecast` function that takes an `HttpClient`, a city and an API key and then returns the forecast object.
* Turn the properties that retrieve temperature, humidity, etc, into separate functions that get the forecast object as an argument and then extract the relevant information.
* Now, change the `RequestsClient` class into a get function, and then pass that function to the `get_forecast` function (this turns it into a higher-order function!)

As a bonus, can you define another function that allows you to get a weather forecast without having to provide the http getter function and the API key?

#### Resources
* [Higher-order functions](https://en.wikipedia.org/wiki/Higher-order_function) (Wikipedia)
* [Functools in Python](https://www.youtube.com/watch?v=ph2HjBQuI8Y) (Video)

### Day 16: Configuration

A configuration file allows you to store settings or parameters separately from the code. This makes it easier to  modify or manage these settings without changing the code itself, and also allows you to use the same code with different configurations, easier than when you need to find that value in the code itself.

In the weather service example, specifically the API url and the API key are things that are good candidates to move to a config file.

Extend so the information is now read from a config file (in JSON format). Consider the following things while refactoring the code:

* What values should we store in the config file and how do we structure it?
* Where do we define the config file path?
* Where should be load the config file?
* How should we pass data that is read from the config file to the code that needs it?

### Day 17: Concurrency

Using coroutines and the async/await syntax makes it easy to write concurrent code, which is code that can perform multiple tasks concurrently without blocking the execution of other code. Concurrent code is especially useful for applications that perform I/O-bound operations that the application needs to wait on.

I've extended the weather service application to now automatically provide the current weather for the capital cities of a number of countries. It relies on another free API to retrieve the capital of a country first, and then it retrieves the weather information.

Currently, the application doesn't use concurrent programming at the moment. When you run the code (make sure to insert your OpenWeather API key first!), you'll see that it actually runs quite slowly. The challenge is to refactor this code so it relies on concurrency to make it respond faster. Use the asyncio module together with async and await. There are a few different ways in which you can structure the API calls, but only one of them is optimal!

Note that for this challenge, you don't need to worry about rate limits, even though that is a nice bonus to consider if you want to dive in deeper.

#### Resources
* [Python's asyncio package](https://www.youtube.com/watch?v=2IW-ZEui4h4) (Video)
* [Concurrent programming](https://www.youtube.com/watch?v=GpqAQxH1Afc) (Video)

### Day 18: Refactoring

While running code directly from its script is quite common, especially when developing, sometimes it's (necessary or) useful to run the application through the command line. This simplifies the interface for the user and allows for extra functionality such as documentation for all the available commands and examples of how to use the interface.

I have (again) extended the weather service application to now include a command-line interface. Refactor the command-line interface code in the main.py file to solve these design problems:

* There's a lot of duplication in the CLI code.
* Everything is in a single main function.
* Translating the CLI to display another language (for example, Dutch instead of English) would be a nightmare.

### Day 19: Itertools
Python has excellent built in libraries that can simplify many process without you having to re-invent the wheel every time. A great example of this is the itertools package. This has many functionalities for iterating over lists or any other iterable object and performing a variety of operations on the data.

In the code for this challenge, a random list of persons is created. Then, the list of the persons is filtered by age. Finally, a summary is printed that groups the persons by country and shows how many persons live in each country.

Refactor the code in the main function by replacing the for-loops by functions from the itertools package.

#### Resources
* [Itertools package](https://www.youtube.com/watch?v=aumxFs2DO5o) (Video)
  
### Day 20: Inappropriate Intimacy

In programming, inappropriate intimacy refers to a situation where different parts of code become too dependent on each other, making changes or fixes difficult and causing potential issues. For example, imagine a Python class that directly accesses and modifies variables of another class, instead of using methods to interact with it, or a function that requests a lot of information without actually needing it. This tight coupling creates a brittle system that is hard to maintain and test. Inappropriate intimacy is an example of a code smell: if you see it in a piece of code, it's an indication that you need to fix something in the design.

An example of inappropriate intimacy is in the code for this challenge. Can you detect what it is? Refactor the code to fix the problem.

#### Resources
* [Code smells](https://en.wikipedia.org/wiki/Code_smell) (Wikipedia)

### Day 21: Undo/Redo

This is a simple text editor. It's not a complete text editor, but it does provide a basic system underlying a text editor that allows for text operations like inserting and deleting text. Obviously, a real text editor will have a way more complex system underlying it, but that's out of the scope of this challenge (though feel free to extend this code if you like).

The goal of this challenge is to extend the text editor to have undo and redo operations. However, when you write the code, make sure to think about how to add undo and redo behavior in such a way that it's independent of the text editing operations. For example, if you want to add a new text editing feature "boldface" in the future, you should be able to do it without having to change the undo/redo system.

#### Resources

[](https://github.com/ArjanCodes/30-day-design-challenge-21-30#resources)

- [Command design pattern](https://www.youtube.com/watch?v=FM71_a3txTo) (Video)

### Day 22: SQL to ORM

SQL queries and SQLAlchemy ORM queries are two ways of querying relational databases, but they differ in their syntax and approach.

SQL queries involve writing SQL statements directly in the code to retrieve data from the database. On the other hand, SQLAlchemy ORM queries are written in Python and use an object-oriented approach to interact with the database.

Rather than writing SQL statements, developers define classes and their attributes that map to database tables and columns. These classes are known as ORM models, and they provide an abstraction layer between the application code and the database.

In summary, while SQL queries require knowledge of SQL syntax and are more focused on the database structure, SQLAlchemy ORM queries provide a higher level of abstraction and can make database interactions more intuitive and Pythonic.

In this challenge you're going to work on an API that allows you to manage events and book tickets for events. The starting point is an API that's already been implemented for you, using FastAPI in combination with a SQLite database. Currently, it's not setup ideally: the API routes contain all of the code and directly interact with the SQLite database using SQL queries. Next to needing to know SQL syntax, there's also the risk of accidentally creating a security risk (SQL injection) when you write code for this API.

Refactor the code to use SQLAlchemy instead of direct SQL queries. For now, there's no need to refactor the actual API logic or extend the capabilities - this will be addressed in the upcoming challenges. However, I do recommend you split up the code into separate files at the same time, so that the main.py file remains small and your code remains manageable.

#### Resources

[](https://github.com/ArjanCodes/30-day-design-challenge-21-30#resources-1)

- [SQL queries vs. ORM systems](https://www.youtube.com/watch?v=x1fCJ7sUXCM) (Video)

### Day 23: Unit tests (Basic)

Although test driven development (TDD) has some strong advantages when it comes to code integrity and maintainability, there are quite some cases that you will need to write tests for code that has been written already (either by you or others) and cannot/should not be changed or refactored.

In this case that is the code of the events API we have created. Since APIs, are almost always designed with a universal architecture and structure, an attempt to refactor its components only for the sake of testing, might create more problems that it solves.

Being able to write test code for existing software, is equally useful to writing tests together with the code itself.

For this challenge you need to create test to check if the create_event API route works as it is supposed to: it is supposed to create an event in the database through a POST method.

The complication is that this is a function with side effects, since it writes data to the database. The challenge is to write the test in such a way that:

It doesn't interact with or change the database in any way. You should be able to run the test as often as you like, and it shouldn't be possible that a test is different due to a previously run test.

Hints

### Day 24: Unit tests (Advanced)

For this challenge you will need to further test the API (see the Downloads section at the top for the code). Think about the possible edge cases that you should cover in the unit tests. You don't have to be complete (that would be a lot of work), but test at least for these two cases:

- Event id doesn't exist when getting or deleting an event.
- There are no more tickets available when buying a ticket.

What other test cases can you think of? Write them down.

### Day 25: Operations Layer

Do you remember the GUI example where you had to use the Model-View-Controller/Presenter pattern? Or the CLI example where you had to separate the CLI-specific code from the actual logic?

Similarly, when you write an API application, it's also good practice to separate the interface to the outside world (= the API routes) from the API logic.

The best way to do this is to introduce an 'operations layer' that performs the actual database operations. The API routes then map to this operations layer, so that the logic is no longer directly in the route functions themselves.

Refactor the code (see the Downloads) to incorporate an operations layer. Think about what the interface between the operations layer and the API routing functions should look like.

Bonus: also rewrite the unit tests!

### Day 26: Ticket Cancellation

For this challenge you will need to add some extra functionality to the API. The extra functionality should implement the following:

- Add a feature to allow for ticket cancellation. That should be for a single ticket based on its id. Also make sure that if an event is deleted, all the related tickets are deleted as well.
- Add a feature to be able to change the name on a ticket.

For both of these features, the API should make sure that the event for which the ticket is for hasn't started yet. In other words: you can only cancel a ticket or change the name on a ticket if an event hasn't started yet.

### Day 27: Messaging

The observer pattern is a design pattern in which an object, called the subject, maintains a list of its dependents, called observers, and notifies them automatically of any state changes, usually by calling one of their methods. This pattern is useful in situations where multiple objects need to be informed of changes to the state of another object, without tightly coupling them.

For this challenge you should add a feature to the API to be able to send confirmations/notifications to the customer. You should design it in such a way that you can easily add different types of confirmation (email, SMS, or both). Switching between different confirmation methods should be modular and without changing the code, itself.

Note that you don't have to integrate the code with an actual SMS or email notification system. For this challenge, it's enough if you simply print the message to the console. For example, you could simply write this print statement when an SMS is supposed to be sent:

```python
print(f"SMS: Your ticket has been reserved under id {ticket.id}!")
```

Add the following notifications/confirmations to the API:

- When a ticket is booked, both a notification email and SMS are sent.
- When an event is created, a notification email is sent.

#### Resources

[](https://github.com/ArjanCodes/30-day-design-challenge-21-30#resources-2)

- [Observer pattern](https://www.youtube.com/watch?v=oNalXg67XEE) (Video)

### Day 28: Validation

Data validation is something you definitely need when users fill in data into a system. This will sanitize your data, preventing weird and unpredictable behavior later on that might cause very difficult and complicated bugs.

For this challenge you should add some validation checks for both the event and the tickets in our API. You should add at least the following checks:

- The available_tickets upon event creation can not be negative.
- The end date of an event can not be before the starting date.
- The customer email address should be a valid email address (meaning that it contains a @ etc - you don't have to check that the email address actually exists).

Since we are using Pydantic classes for the EventCreate and TicketCreate classes, I recommend that you use the Pydantic built-in validation functionality.

#### Resources

[](https://github.com/ArjanCodes/30-day-design-challenge-21-30#resources-3)

- [Pydantic](https://www.youtube.com/watch?v=Vj-iU-8_xLs) (Video)
- [Comparison to dataclasses and attrs](https://www.youtube.com/watch?v=zN4VCb0LbQI) (Video)

### Day 29: Bridge

You're getting close to completing the challenge. Only two more challenges to go and you''ll be there!

As you can see, this seems to be part of some sort of media/streaming system (I promise, I didn't steal this from Netflix!).

In the application, you can define different types of media (movies, series, etc). You can also define different types of views such as a full view, preview, or a list view. Each of these views needs different information. For example, the list view needs only the heading, whereas the full view needs the heading, subheading and a description text.

The view function handles all of this, which is not ideal. The main problem is that if you add a different type of media (for example a Documentary), you need to make a lot of changes to the view function. If you add a different type of view (such as a teaser that only shows the first 10 characters of the description text), you need to add that everywhere throughout the view function. As a result, this leads to a combinatorial explosion of views and media items.

Your task is to refactor the code so that you can add more media items without having to change anything in the part dealing with the views, and vice versa. Use the Bridge design pattern to achieve this.

To test whether your solution actually works, add a Documentary media item and check that you don't need to change anything in the code dealing with viewing media items. Also add a "teaser" view that prints just the first 10 characters of the description text and check that you don't need to change anything in the media item classes.

#### Resources

[](https://github.com/ArjanCodes/30-day-design-challenge-21-30#resources-4)

- [Bridge design pattern](https://en.wikipedia.org/wiki/Bridge_pattern) (Wikipedia)
- [Bridge pattern](https://www.youtube.com/watch?v=mM2-FPm1EhI) (Video)

### Day 30: Mixins

I'm not a big fan of using mixins for several reasons. You have to be careful as a developer when you use them because they can result in strange bugs related to multiple inheritance, they can break IDE autocompletion and suggestions, and they don't translate well outside of the Python world, since most programming languages forbid multiple inheritance, or only allow a very limited version of it using interfaces or abstract classes.

On top of that, you can often replace mixins by composition. Instead of inheriting from a class, you simply get an instance of that class. Composition often leads to shorter code that easier to read and maintain. And it doesn't break your IDE!

To illustrate this, take a look at the code for this (final!) challenge. It relies on mixins to model the game characters. Refactor the code so that it relies on composition instead. Think about how you would organize the data and the methods to achieve this. This is not an easy refactor. You're going to have to make a few tradeoffs to solve this, but it's well worth the effort and it will show you how composition helps you write cleaner and simpler code!

Resources

- [Mixins](https://en.wikipedia.org/wiki/Mixin) (Wikipedia)


## Prerequisites

* Basic understanding of Python

## Getting Started

Each challenge contains an poetry configuration. Before each challenge navigate to the challenge directory and run the following command to initate an python virtual enviroment in your current shell session.

```
poetry install && poetry shell
```
