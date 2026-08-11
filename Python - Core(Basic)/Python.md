## what is Python 
-- Python is a high-level, general-purpose programming language known for its simplicity, readability, and versatility

It is widely used in:
--Web development (using frameworks like Django, Flask)
--Data science and analytics
--Machine learning and AI
--Automation and scripting
--Desktop applications
--APIs and backend development
--Cybersecurity and ethical hacking
--GUI 

## IDE : integrated Development Environment

## Key Features of Python
-- Simple Syntax – Easy to read and write
-- Interpreted Language – Runs code line-by-line
-- Cross-Platform – Works on Windows, macOS, Linux.
-- Huge Community – Tons of libraries and support.
-- Object-Oriented & Functional – Supports both paradigms.

## Why Should You Learn Python?
--Beginner-friendly
--High demand in job market (tech, finance, healthcare, etc.)
--Strong ecosystem (e.g., Pandas, NumPy, TensorFlow, Flask, FastAPI)
--Used by companies like Google, Netflix, NASA, etc.

## Variables in Python
--Variables are containers for storing data values.
--Python has no command for declaring a variable.
--A variable is created the moment you first assign a value to it.

## Variables Names rules in Python
-- A variable can have a short name (like x and y) or a more descriptive name (age, total_volume).

Rules for Python variables: 
-- A variable name must start with a letter or the underscore character
-- A variable name cannot start with a number
-- A variable name can only contain alphanumeric characters and underscores (A-z, 0-9, and _ )
-- Variable names are case-sensitive (age, Age and AGE are three different variables)
-- A variable name cannot be any of the Python keywords.

## DataTypes in Python
-- Variables can store data of different types, and different types can do different things.

1. String 
Note: string in python is immutable it means we can't change the value of given string

2. Numeric Types :int, double, float
Note: its mutable it means we can change value
3. Sequence Types: list, tuple, range
4. Mapping Types: dict
5. set Types: set, frozenset
6. Boolean Types: bool
7. Binary Types: bytes, bytearray, memory view
8. None Types: NoneType

Note: BODMAS Rule 
B - brackets
o - orders 
D - divide
M - multiply
A - Addition
S - subtract

## difference between append and insert
 - append means it will add something in the end
 - insert means it will add something in between

## Operators in python
1. Arithmetic Operator
2. Assignment Operator
3. Relational Operator or comparison operator
4. Logical Operator
5. Unary Operator
6. Bitwise operator

## IDLE Previous Command
-- IDLE (Integrated Development and Learning Environment) is the official Python IDE that comes pre-installed 
with Python. It allows you to write, run, and test Python code.

##Import Math Function in Python
-- In Python, the math module provides mathematical functions like square root, factorial, trigonometry,
logarithms, and more.

1. math.sqrt(x) - 	Square root	
2. math.pow(x, y) - x raised to the power y	
3. math.factorial(x) -	Factorial of x	
4. math.floor(x)-	Round down to nearest int	
5. math.ceil(x)- Round up to nearest int	
6. math.pi- Value of π 
7. math.sin(x)- Sine of x (in radians)	
8. math.log(x)- Natural logarithm (base e) 

## SWAP Variables in Python
-- Swapping means exchanging the values of two variables.

## User Input in Python
--we can take input from the user using the built-in input() function.
--input() always returns a string – even if the user types a number.

1. input() - Takes input as string
2. int(input()) - Converts input to integer
3. float(input()) -	Converts input to float
4. split() - Takes multiple inputs in one line
5. map() - Converts multiple inputs at once

## conditions in Python
1. if ...else 
2. else...
3. nested if...

## Loops in python
1. For Loop
2. For Loop
3. Break continue pass

## Patterns in Python
-- Pattern printing is a common exercise in Python for logic building, gaming platform, etc...

## what is NUMPY?
-- Dependency: pip install numpy

-- NumPy (Numerical Python) is a powerful open-source Python library used for scientific computing and data analysis.
Importance 
1. Fast and efficient array operations
2. Support for multidimensional arrays
3. Mathematical functions (like mean, median, matrix operations, etc.)
4. Basis for many libraries like Pandas, Matplotlib, TensorFlow

## Working with matrix using python
-- Working with matrices in Python is simple and efficient, especially using libraries like NumPy.

## Functions in Python
-- Functions in Python allow you to group code into reusable blocks. 
-- They improve readability, reduce redundancy, and make debugging easier.

## Function Arguments in Python
-- When you call a function, the values you give are called arguments.

## Types of Arguments in Python
1. Positional - Passed in order Ex: a, b	
2. Default - Used if not provided	Ex: b=2	
3. Arbitrary Positional	- Collects extra positional args into a tuple Ex: *args	
4. Arbitrary Keyword-Collects extra keyword args into a dictionary Ex: **kwargs

## what is Global Keyword in Python?
-- The global keyword is used to access and modify a variable outside a function (global scope) from inside a function.
-- Without global You can’t modify global variable inside function

## Why Use global?
-- When you want to update a global variable inside a function.
-- Useful in counters, flags, configurations, etc.

## Pass List to a Function in python
-- In Python, you can easily pass a list to a function just like any other variable.
 
## Fibonacci Sequence in Python
-- The Fibonacci series is a list of numbers where:
-- The first two numbers are always: 0 and 1
-- Every number after that is the sum of the previous two numbers

## Factorial in Python
Multiply all whole numbers from that number down to 1.
Ex: 5! = 5 × 4 × 3 × 2 × 1 = 120

## what is Recursion?
-- This is what recursion does — it keeps calling itself until a final condition is met (called the base case). 
-- Note - Without a base case, it runs forever or infinite 
-- Recursive call - When function calls itself

### Recursion is used in:
1. Math problems (like factorial, Fibonacci)
2. Data structures (trees, graphs)
3. Divide and conquer algorithms (like merge sort)

## what is lambda and how its work on python
-- In Python, a lambda is a short and simple way to write a function.
-- You can think of it as a one-line mini function — also called an anonymous function (because it doesn’t have a name).

## OOPs in Python
-- OOP (Object-Oriented Programming) is a programming paradigm based on the concept of "objects", 
which can contain data (attributes) and code (methods).

-- 4.Main OOP Concepts in Python
1. Class: Blueprint for creating objects
2. object: Instance of a class
3. Inheritance: One class can inherit properties from another class
4. Polymorphism: Same method behaves differently depending on context
5. Encapsulation: Hiding internal state; only exposing what’s necessary
6. Abstraction: Hiding implementation details, only showing functionality

## -------------------------------------  The Django Framework -----------------------------------------

1. What is Django Framework in Python
-- django is the free and open-source web framework
-- Django is a back-end server side web framework.

2. what is Framework 
--framework is the combination of the components and packages
--framework used for build a complex web application and handle or manage huge data

3. why we have to learn Django framework in python
--Django is a high-level web framework in Python that helps you build web applications quickly and efficiently.

-- Built for Speed and Simplicity

For Example: 
--- Login/logout
---Admin panel
---URL routing
---Database models
---Forms, Validation

** -- Secure: Django automatically handles many security issues:

For Example: SQL injection,
XSS (Cross-site scripting)
CSRF (Cross-site request forgery)
Password hashing

## How does Django Work?
-- Django follows the MVT design pattern (Model View Template).

1.Model - The data you want to present, usually data from a database.
2.View - A request handler that returns the relevant template and content - based on the request from the user.
3.Template - A text file (like an HTML file) containing the layout of the web page, with logic on how to display the data.

## --- Model 
-- The model provides data from the database.
-- In Django, the data is delivered as an Object Relational Mapping (ORM), which is a technique 
designed to make it easier to work with databases.
-- The most common way to extract data from a database is SQL. One problem with SQL is that you have to have a pretty 
good understanding of the database structure to be able to work with it.
-- Django, with ORM, makes it easier to communicate with the database, without having to write complex SQL statements.
-- The models are usually located in a file called models.py

## --- View
-- A view is a function or method that takes http requests as arguments, imports the relevant model(s),
and finds out what data to send to the template, and returns the final result.
-- The views are usually located in a file called views.py.

## --- Template
-- A template is a file where you describe how the result should be represented.

## what is Virtual Environment in Django  
-- A Virtual Environment (venv) is like a separate box/sandbox inside your computer where you install Python + Django
 + other project libraries without affecting your system-wide Python.

## why Virtual Environment is important for Django?
-- Isolation : Each Django project can have its own Django version.
Example:
Project A uses Django 4.2
Project B uses Django 5.0

→ Both can run without conflicts because each is inside its own venv (Virtual Environment).

-- No system mess: You don’t install packages globally on your machine → keeps system clean.
-- Portability: You can share requirements.txt (list of libraries in venv) with others → they can recreate
   same environment easily.
-- Easy to manage: You can delete the venv anytime → it won’t affect system Python.

## How Virtual Environment works (behind the scenes)
-- It creates a folder (e.g., .venv/) in your project.
Inside it:
-- A copy of Python interpreter
-- Local site-packages/ (where Django & libs are installed)
-- When you “activate” venv, your terminal switches to use this local Python instead of global Python.

-------------------------------- Cloud services (AWS) ----------------------------------------
## what is AWS ??
-- AWS: Amazon Web Service 
-- AWS is a cloud computing platform provided by Amazon.
-- It offers a wide range of on-demand services like computing power, storage, databases, networking, AI/ML,
and security—all accessible over the internet.
-- Instead of buying and maintaining your own servers, you can use AWS services and pay only for what you 
use (like electricity).

## Key Points of AWS 
1. Launched → 2006 by Amazon.
2. Type → Cloud Computing (IaaS, PaaS, SaaS).
3. Global Reach → Available across the world with Regions (locations) and Availability Zones (AZs) 
(data centers inside regions).
4. Billing → Pay-as-you-go model.
5. Users → Startups, enterprises, and governments use AWS.

## AWS Provides 3 Main Categories of Services
-- Compute (Processing Power): 
   Example: 1. EC2 (Elastic Compute Cloud) → Virtual servers in the cloud.
      2. Lambda → Run code without managing servers (serverless).

-- Storage (Save Data): 
Example: 
1. S3 (Simple Storage Service) → Store unlimited data (like Google Drive but for businesses).
2. EBS (Elastic Block Store) → Hard disk for EC2 instances.

-- Databases: 
1. RDS (Relational Database Service) → SQL databases.
2. DynamoDB → NoSQL database.

## Key Features of AWS and why companies use AWS 
1. Scalability → Increase or decrease resources anytime.
2. Cost-Effective → Pay only for what you use.
3. Reliability → Highly secure and available 24/7.
4. Flexibility → Wide range of services for any application (websites, mobile apps, ML, IoT).

##  ------------------ Introduction of EC2 ---------------------
1. Amazon EC2 is one of the most important services in AWS.
2. It provides virtual servers (called instances) in the cloud that you can use to run applications.
3. Think of it as renting a computer/server from Amazon that runs 24/7 in the cloud.
4. You don’t need to buy physical servers → just launch an EC2 instance and pay only for the time you use it.

## Key Points about EC2
1. Different Instance Types → For general purpose, compute-heavy, memory-heavy, or GPU workloads.
2. Operating System Choice → Linux, Windows, Ubuntu, Red Hat, etc.
3. Storage Options → Attach EBS (Elastic Block Store) or use S3 for backups.
4. Security → Secure with Key Pairs (SSH login) and Security Groups (firewall).
5. Scalability → Works with Auto Scaling to automatically add/remove servers.

## Common Uses of EC2
1. Hosting websites & web apps.
2. Running databases and enterprise software.
3. Machine Learning model training.
4. Gaming servers.
5. Backup and disaster recovery

## EC2 Example
Example in Simple Terms:
Imagine you want to launch a website.
Normally, you’d buy a physical server, install OS, configure network, etc.
With EC2, you just:
1. Go to AWS Console → Click Launch Instance.
2. Choose an OS (e.g., Ubuntu).
3. Select hardware (CPU, RAM size).
4. Set up security (firewall rules).
5. Launch → Your virtual server is ready within minutes 🚀.

EC2 = Cloud-based Virtual Server that gives you computing power without buying physical hardware.

## ------------------ Introduction of MongoDB Atlas --------------------- 
-- MongoDB Atlas is a cloud-based database service provided by MongoDB.
-- It is the managed version of MongoDB – meaning you don’t have to worry about installation, setup, backup, or scaling.
-- It runs on major cloud providers like AWS, Google Cloud, and Microsoft Azure.

## Key Factors of MongoDB Atlas
-- Type → NoSQL Database (Document-oriented).
-- Hosted → Fully managed in the cloud. 
-- Scalable → Can handle small apps to enterprise-level data.
-- Flexible Schema → Stores data as JSON-like documents (BSON) instead of rows and tables.
-- Multi-Cloud → You can even deploy across multiple cloud providers.

## Features of MongoDB Atlas
-- Automated Deployment → Just a few clicks, and your database is ready.
-- Automatic Backups & Security → In-built monitoring, encryption, and compliance. 
-- Global Clusters → Deploy data close to users for fast performance.
-- Serverless Option → Pay only for what you use (no need to manage servers).
-- Integration → Works with popular programming languages (Python, Java, Node.js, etc.).

## Why Use MongoDB Atlas?
-- You don’t need to install or maintain MongoDB yourself.
-- Built-in scalability → Can handle millions of users.
-- High availability → Runs on multiple servers automatically.
-- Easy connection → Provides a connection string (URI) you can use in your application.

## Introduction to AWS Elastic Beanstalk
-- AWS Elastic Beanstalk is a Platform as a Service (PaaS) on AWS.
It allows you to deploy, run, and manage web applications without worrying about the infrastructure
(servers, load balancers, scaling).

-- You just upload your code (Java, Python, Node.js, .NET, PHP, Go, Ruby, Docker, etc.),
and Elastic Beanstalk automatically:

1. Creates EC2 servers
2. Configures load balancers
3. Sets up auto-scaling
4. Monitors the health of your app

## Key Points
1. Service Type → PaaS (Platform as a Service).
2. Supports Multiple Languages → Java, Python, Node.js, .NET, PHP, Ruby, Go, Docker.
3. Fully Managed → AWS handles provisioning, scaling, and monitoring.
4. Customizable → You can still access EC2, S3, RDS, etc., if needed.
5. No Extra Cost → You only pay for the underlying AWS resources (EC2, S3, RDS), not for Beanstalk itself.

## Features of Elastic Beanstalk
1. Automatic Infrastructure Management → No need to manually set up servers.
2. Scalability → Built-in Auto Scaling.
3. Load Balancing → Handles traffic distribution automatically.
4. Monitoring → Integrated with CloudWatch.
5.Fast Deployment → Just upload your app package (ZIP or WAR).

## When to Use Elastic Beanstalk?
-- When you want to focus on writing code instead of managing infrastructure.
-- For web apps, APIs, and backend services.
-- For quick deployment and easy scaling.

**** Elastic Beanstalk = AWS service to deploy & manage web apps easily → you focus on code, AWS handles the rest.

## ----------- Amazon RDS (Managed Relational Database service) -----------
-- Amazon RDS (Relational Database Service) is a managed service by AWS that makes it easier to set up, operate,
and scale relational databases in the cloud.
-- Instead of installing, configuring, and managing a database manually, RDS automates most of the heavy tasks like:
1. Database provisioning (creating DB instances)
2. Patching the OS and database software
3. Backup and restore
4. Scaling (CPU, RAM, storage)
5. High availability & failover
6. Monitoring & security

## Supported Databases in Amazon RDS
-- Amazon RDS supports multiple relational database engines:
Amazon Aurora (AWS’s own highly optimized DB compatible with MySQL & PostgreSQL)

1. MySQL
2. PostgreSQL
3. MariaDB
4. Oracle
5. Microsoft SQL Server

## Key Features
1. Automated Backups → RDS automatically takes backups of your database.
2. Multi-AZ Deployment → Provides high availability and automatic failover.
3. Read Replicas → You can create read-only copies for scaling reads.
4. Scalability → You can increase compute and storage without downtime.
5. Monitoring & Security → Works with CloudWatch, IAM, KMS (encryption).
6. Pay-as-you-go → You only pay for what you use. 

## Amazon RDS = Relational Database + Fully Managed by AWS (No headache of maintenance).

## ------------------ Amazon DynamoDB (Managed NoSQL Database) -----------------
1. DynamoDB is a fully managed NoSQL database service provided by AWS.
2. It is designed for fast performance, high scalability, and low-latency access.

-- Amazon DynamoDB = A lightning-fast, fully managed, serverless NoSQL database that can handle huge amounts of 
data with zero admin effort.

-- Unlike Amazon RDS (Relational DB) which works with tables, rows, and SQL queries, DynamoDB is schema-less (NoSQL)
and stores data in key-value pairs or documents.

## Key Features of DynamoDB
1. Fully Managed → No need to manage servers, scaling, patching, or replication.
2. Serverless → You don’t worry about infrastructure. DynamoDB automatically scales.
3. High Performance → Single-digit millisecond response time.
4. Flexible Data Model → Supports key-value and document (JSON-like) storage.
5. Scalability → Automatically handles millions of requests per second.
6. High Availability → Data is replicated across multiple Availability Zones.
7. Backup & Restore → Continuous backups and point-in-time recovery.
8. Global Tables → Multi-region, multi-master database (write and read anywhere).

## Data Model in DynamoDB
1. Table → Collection of data.
2. Item → Equivalent to a row (but schema-less).
3. Attribute → Equivalent to a column.

## Difference between RDS (Relational Database system) and DynamoDB 
1. Data Model
 - RDS : Tables, rows, SQL queries
 - DynamoDB : Key-Value / Document
 - 
2. Schema 
 - RDS : Fixed schema
 - DynamoDB : Schema-less

3. Scaling
 - RDS : Vertical + Read replicas
 - DynamoDB: Horizontal (automatic)

Note: RDS best for Structured data like (ERP, Banking) and DynamoDB is best for Unstructured / high-speed apps 
(IoT, gaming, e-commerce)

## --------------- Amazon Simple Storage Service (S3) (Scalable storage in the cloud) -------------------
-- Amazon Simple Storage Service (S3) is a cloud-based storage service provided by AWS.
It allows you to store and retrieve any amount of data, anytime, from anywhere on the internet.

## Key Points about Amazon S3
1. Scalable → You can store unlimited data (from a few MBs to petabytes).
2. Durable & Reliable → Data is stored across multiple servers and locations, so chances of data loss are extremely low 
(99.999999999% durability = "11 nines").
3. Flexible Storage Classes → Different options based on how often you need the data:
- S3 Standard (frequently accessed)
- S3 Infrequent Access (less frequently used data)
- S3 Glacier (long-term, archival storage, very cheap).
4. Pay-as-you-go → You pay only for what you use (storage + requests + data transfer).
5. Secure → Supports encryption, access control, and integration with AWS Identity and Access Management (IAM)

Amazon S3 = Infinite hard drive on the cloud, secure, scalable, and reliable.
