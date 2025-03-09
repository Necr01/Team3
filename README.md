# Team3
Panganiban, Bangki, Niñeza

Summary of Database System Architectures
**1. Single-Tier Architecture**
Description: The database and application reside on the same system.
Example: SQLite with a Python script for a local note-taking app.
Pros: Simple setup, fast access, no network dependency.
Cons: Limited scalability, not ideal for multi-user applications.
**2. Two-Tier Architecture**
Description: A client-server model where the database is on a separate server, and the client communicates directly with it.
Example: MySQL database with a Python client performing CRUD operations.
Pros: Better scalability, multiple clients can connect.
Cons: Increased complexity, potential performance bottlenecks.
**3. Three-Tier Architecture**
Description: Introduces an intermediate application server between the client and database, handling business logic.
Example: A Flask-based web app with MySQL and a web interface.
Pros: Greater scalability, security, and flexibility.
Cons: More complex setup and maintenance.
Each architecture is suited for different use cases, balancing complexity, performance, and scalability.


Instructions for Running or Testing the Code
**1. Single-Tier Architecture (SQLite + Python)**
Prerequisites:

Install Python (if not already installed).
Install SQLite (included with Python by default).
Steps:

Create an SQLite database (notes.db).
Write a Python script to interact with the database (e.g., add, delete, view notes).
Run the script using:
_python script.py_
Verify database updates using an SQLite viewer or Python queries.

**2. Two-Tier Architecture (SQLite + Python Client)**
Prerequisites:

Install Python (if not already installed).
SQLite is included with Python by default.
Steps:

Create an SQLite database (notes.db).
Write a Python script to interact with the database using SQL queries.
Run the script using:
_python client.py_
Verify database changes by checking the SQLite database.

**3. Three-Tier Architecture (SQLite + Python + HTML, CSS, JavaScript)**
Prerequisites:

Install Python (if not already installed).
SQLite is included with Python by default.
A web browser (Chrome, Firefox, etc.).
Steps:

Database Setup:

Create an SQLite database (notes.db).
Backend (Python):

Write a Python script to handle database interactions (e.g., adding, retrieving, deleting notes).
Start a simple HTTP server using Python’s http.server to serve the frontend.
Frontend (HTML, CSS, JavaScript):

Develop an HTML, CSS, and JavaScript-based web interface.
Use JavaScript (Fetch API) to send requests to the Python backend.
Running the Application:

Start the Python server:
_python -m http.server 8000_

Open a web browser and go to:
_http://localhost:8000_

Perform CRUD operations using the web interface, which communicates with the Python backend.

**This project explores database system architectures by implementing Single-Tier, Two-Tier, and Three-Tier models using SQLite, Python, HTML, CSS, and JavaScript.**

Single-Tier: A standalone Python script interacts directly with an SQLite database.
Two-Tier: A Python client connects to an SQLite database, separating logic from data storage.
Three-Tier: A web-based application with a frontend (HTML, CSS, JavaScript), a backend (Python server), and an SQLite database for data management.
The project demonstrates CRUD operations, separation of concerns, and local hosting using Python’s built-in HTTP server. It provides hands-on experience with scalability, performance, and complexity in database architectures.
