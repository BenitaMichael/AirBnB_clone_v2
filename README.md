# AIRBNB CLONE PROJECT
## Project Description:
This is the first section of the AirBnB clone project where we worked on the backend of the project with the help of the cmd module in python.

Data (python objects) stored in files generated are stored in a json file and can be accessed with the json module in python

## Description of the command interpreter:
A command line interpreter allows the user to interact with a program using commands in the form of text lines. Our command line interpreter functions like the Bash shell except that it recognizes a limited number of commands that were solely defined and implemented for the purposes of the AirBnB website.
This command line interpreter  serves as the frontend of the web app where users can interact with the backend which was developed with python OOP programming.

Some of the commands available are:
- create
- show ( read )
- count
- update
- destroy

And as part of the implementation of the command line interpreter coupled with the backend and file storage system, the folowing actions can be performed:
-   Creating new objects (ex: a new User or a new Place)
-   Retrieving or reading an object from a file, a database etc…
-   executing several operations(count, compute stats, etc…)
-   Updating of an object
-   Destroying an object

## Console.py
### How it works
- The program starts by importing the cmd module, which provides a framework for building interactive command-line applications.
- This class is where you define the behavior of the command-line console and its inherits from cmd.Cmd.
- The "(hbnb)" appears as the command prompt is executed, indicating that the console is ready to accept user input.
- To exit the console, the user can either type "quit" or use Ctrl+D (EOF). In both cases, the program returns True, which signals the console to exit.


# AIRBNB CLONE PROJECT
## Project Description:
This is the first section of the AirBnB clone project where we worked on the backend of the project with the help of the cmd module in python.

Data (python objects) stored in files generated are stored in a json file and can be accessed with the json module in python

## Description of the command interpreter:
A command line interpreter allows the user to interact with a program using commands in the form of text lines. Our command line interpreter functions like the Bash shell except that it recognizes a limited number of commands that were solely defined and implemented for the purposes of the AirBnB website.
This command line interpreter  serves as the frontend of the web app where users can interact with the backend which was developed with python OOP programming.

Some of the commands available are:
- create
- show ( read )
- count
- update
- destroy

And as part of the implementation of the command line interpreter coupled with the backend and file storage system, the folowing actions can be performed:
-   Creating new objects (ex: a new User or a new Place)
-   Retrieving or reading an object from a file, a database etc…
-   executing several operations(count, compute stats, etc…)
-   Updating of an object
-   Destroying an object

## How to start it
These instructions will get you a copy of the project up and running on your local machine (Linux distro) for development and testing purposes.

```
Clone the repository using:
git clone https://github.com/Benita_Michael/AirBnB_clone.git
```
After cloning the repository you will have a folder called AirBnB_clone. In here there will be several files that allow the program to run

## How to use it
It can work in two different modes:


**Interactive** and **Non-interactive**.

In **Interactive mode**, the console will display a prompt (hbnb) indicating that the user can write and execute a command. After the command has run, the prompt will appear again a wait for a new command. This is a continous process unless the user exits the program.

In **Non-interactive mode**, the console will need to be run with a command input piped into its execution so that the command is run as soon as the Shell starts. In this mode no prompt will appear, and the program exits.

## Format of Command Input

In order to give commands to the console, these will need to be piped through an echo in case of  **Non-interactive mode**.

In  **Interactive Mode**  the commands will need to be written with a keyboard when the prompt appears and will be recognized when an enter key is pressed (new line). As soon as this happens, the console will attempt to execute the command through several means or will show an error message if the command didn't run successfully. In this mode, the console can be exited using the **CTRL + D** combination,  **CTRL + C**, or the command **quit** or **EOF**.

## Arguments

Most commands have several options or arguments that can be used when executing the program. In order for the Shell to recognize those parameters, the user must separate everything with spaces.

Example:

```

user@ubuntu:~/AirBnB$ ./console.py
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
user@ubuntu:~/AirBnB$ ./console.py

```

or

```
user@ubuntu:~/AirBnB$ ./console.py $ echo "create BaseModel" | ./console.py
(hbnb)
e37ebcd3-f8e1-4c1f-8095-7a019070b1fa
(hbnb)
user@ubuntu:~/AirBnB$ ./console.py
```

## Available commands and what they do

The recognizable commands by the interpreter are the following:

|Command| Description |
|--|--|
| **quit or EOF** | Exits the program |
| **Usage** | By itself |
| **-----** | **-----** |
| **help** | Provides a text describing how to use a command.  |
| **Usage** | By itself --or-- **help <command\>** |
| **-----** | **-----** |
| **create** | Creates a new instance of a valid `Class`, saves it (to the JSON file) and prints the `id`.  Valid classes are: BaseModel, User, State, City, Amenity, Place, Review. |
| **Usage** | **create <class name\>**|
| **-----** | **-----** |
| **show** | Prints the string representation of an instance based on the class name and `id`  |
| **Usage** | **show <class name\> <id\>** --or-- **<class name\>.show(<id\>)**|
| **-----** | **-----** |
| **destroy** | Deletes an instance based on the class name and `id` (saves the change into a JSON file).  |
| **Usage** | **destroy <class name\> <id\>** --or-- **<class name>.destroy(<id>)** |
| **-----** | **-----** |
| **all** | Prints all string representation of all instances based or not on the class name.  |
| **Usage** | By itself or **all <class name\>** --or-- **<class name\>.all()** |
| **-----** | **-----** |
| **update** | Updates an instance based on the class name and `id` by adding or updating attribute (saves the changes into a JSON file).  |
| **Usage** | **update <class name\> <id\> <attribute name\> "<attribute value\>"** ---or--- **<class name\>.update(<id\>, <attribute name\>, <attribute value\>)** --or-- **<class name\>.update(<id\>, <dictionary representation\>)**|
| **-----** | **-----** |
| **count** | Retrieve the number of instances of a class.  |
| **Usage** | **<class name\>.count()** |



## Overview Of Classes Created
BaseModel: Parent class that defines all common attributes/methods for other classes. It handles Public attributes including:
- id: created using uuid
- created_at: using the date object
- updated_at: using the date object
and Public instance methods:
- save(self): updates the public instance attribute updated_at with the current datetime
to_dict(self): returns a dictionary containing all keys/values of __dict__ of the Public instance

# User: Class that inherits from BaseModel. It handles Public Attributes including:
- email: string object
- password: string object
- first_name: string object
- last_name: string object

# State Public class attributes:
- name: string - empty string

# City Public class attributes:
state_id: string - empty string
- name: string - empty string

# Amenity Public class attributes:
- name: string - empty string

# Place Public class attributes:
- city_id: string - empty string
- user_id: string - empty string
- name: string - empty string
- description: string
- number_rooms: integer - 0
- number_bathrooms: integer - 0
- max_guest: integer - 0
- price_by_night: integer - 0
- latitude: float - 0.0
- longitude: float - 0.0
- amenity_ids: list of string


# Review Public class attributes:
- place_id: string - empty string
- user_id: string - empty string
- text: string - empty string



## Overview of Unittest
Unit tests are essential for ensuring the correctness of code. Every possible edge cases have been covered by working with a wide range of students participating in this project.
Unittest can be found in test/test_models directory, Handling test cases for:
- BaseModel
- Amenity
- City
- Place
- Review
- State
- User
- File storage (test/test_models/engine)

