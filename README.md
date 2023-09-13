# Person REST API

This project introduces a streamlined API for overseeing "person" resources, which encompasses the creation, retrieval, modification, and deletion of individual records. Crafted using FastAPI, this API seamlessly interfaces with diverse databases. It dynamically adapts to user-provided input, such as a person's name, allowing for versatile operations.

## Table of Contents

- [Person Management API](#person-management-api)
  - [Table of Contents](#table-of-contents)
  - [Key Features](#key-features)
  - [Initiating the System](#initiating-the-system)
    - [Prerequisites](#prerequisites)
    - [Set-Up Process](#set-up-process)
  - [Application Flow](#application-flow)
    - [Introducing a Fresh Person](#introducing-a-fresh-person)
    - [Accessing Person Particulars](#accessing-person-particulars)
    - [Adjusting Person Details](#adjusting-person-details)
    - [Eliminating a Person](#eliminating-a-person)
  - [Database Blueprint (Extra)](#database-blueprint-extra)
  - [Verification](#verification)
  - [Parameter Flexibility](#parameter-flexibility)
  - [Detailed Reference Guide](#detailed-reference-guide)
  - [GitHub Repository](#github-repository)
  - [Hosting](#hosting)
  - [Adhering to Criteria](#adhering-to-criteria)

## Key Features

- **CRUD Operations:** The API empowers users to Create, Read, Update, and Delete person resources.
- **Secure Database Interaction:** All interactions with the database are fortified, safeguarding against common vulnerabilities like SQL injections.
- **Dynamic Parameter Handling:** The API adeptly processes operations based on user-supplied parameters, such as a person's name.
- **Comprehensive Documentation:** A detailed documentation file outlines request/response formats, setup instructions, and sample API usage.

## Initiating the System

### Prerequisites

Before launching the API, ensure you have the following prerequisites:

- Python (3.7+)
- FastAPI (automatically installed)

### Set-Up Process

1. Clone the GitHub repository to your local machine:

   ```bash
   git clone https://github.com/samdami/HNGTASK2.git
   cd HNG_CRUD
   ```

2. Optionally, create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Application Flow

### Run the application

```bash
uvicorn src.main:app --reload
```

### Introducing a Fresh Person

To introduce a new person, dispatch a POST request to `/api` with a JSON payload containing the person's name.

**Example Request:**

```bash
curl -X POST -H "Content-Type: application/json" -d '{"name": "Samdami"}' http://localhost:8000/api
```

### Accessing Person Particulars

To acquire details of a person by name, initiate a GET request to `/api/user_id` with the `name` query parameter.

**Example Request:**

```bash
curl http://localhost:8000/api/user_id?name=Samdami
```

### Adjusting Person Details

To modify a person's details by name, dispatch a PUT request to `/api/user_id` with the `name` query parameter and a JSON payload containing the updated information.

**Example Request:**

```bash
curl -X PUT -H "Content-Type: application/json" -d '{"name": "David"}' http://localhost:8000/api/user_id?name=Samdami
```

### Eliminating a Person

To erase a person by name, send a DELETE request to `/api/user_id` with the `name` query parameter.

**Example Request:**

```bash
curl -X DELETE http://localhost:8000/api/user_id?name=Samdami
```

### Verification

To verify the API, you can employ tools like Postman or write scripts in Python utilizing the requests library. Ensure you test each CRUD operation:

1. Adding a new person (e.g., "David").
2. Retrieving details of a person.
3. Adjusting the details of an existing person.
4. Removing a person.

```bash
pytest
```

### Database Blueprint (Extra)

As an added feature, we present a UML diagram illustrating the database structure and relationships. Consult the provided diagram for a visual representation of the database schema and entity interconnections.

### Parameter Flexibility

The API is adaptive and can accommodate dynamic input. You can furnish a name (or other specifics) to perform operations linked to that name. For instance, if you provide "David," you can execute all CRUD operations pertaining to "David."

### Detailed Reference Guide

For a comprehensive reference on the API, which includes:

- Standardized formats for requests and responses for each endpoint.
- Demonstrations of API utilization.
- Any recognized limitations or presumptions made during development.
- Directions for establishing and deploying the API either locally or on a server.

Please consult the [DOCUMENTATION](DOCUMENTATION.md) file.

# HNGSTAGE2

# HNGSTAGE2

"# HNGSTAGE2"
# HNGSTAGE2
