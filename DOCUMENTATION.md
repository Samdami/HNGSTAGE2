# FastAPI API DOCUMENTATION

**Version:** 0.1.0

---

## Available Endpoints

### Index

- **Objective:** Fetch index details.
- **HTTP Method:** GET
- **Path:** `/`
- **Responses:**
  - **200:** Successful Response (Content: JSON)

### Add User

- **Objective:** Establish a new user.
- **HTTP Method:** POST
- **Path:** `/api`
- **Request Body:** PersonCreate JSON object (Required)
- **Responses:**
  - **200:** Successful Response (Content: Person JSON object)
  - **422:** Validation Error (Content: HTTPValidationError JSON object)

### Retrieve User

- **Objective:** Get user data by name.
- **HTTP Method:** GET
- **Path:** `/api/user_id`
- **Query Parameter:**
  - `name` (string, required): User's name
- **Responses:**
  - **200:** Successful Response (Content: JSON)
  - **422:** Validation Error (Content: HTTPValidationError JSON object)

### Erase User

- **Objective:** Remove a user by name.
- **HTTP Method:** DELETE
- **Path:** `/api/user_id`
- **Query Parameter:**
  - `name` (string, required): User's name
- **Responses:**
  - **200:** Successful Response (Content: JSON)
  - **422:** Validation Error (Content: HTTPValidationError JSON object)

### Modify User

- **Objective:** Adjust user information by name.
- **HTTP Method:** PUT
- **Path:** `/api/user_id`
- **Query Parameter:**
  - `name` (string, required): Name of the user to update
- **Request Body:** PersonCreate JSON object (Required)
- **Responses:**
  - **200:** Successful Response (Content: Person JSON object)
  - **422:** Validation Error (Content: HTTPValidationError JSON object)

---

## Data Structures

### Person

- Attributes:
  - `name` (string, required): User's name
  - `id` (integer): User ID
  - `createdAt` (string): Creation timestamp
  - `updatedAt` (string): Last update timestamp

### PersonCreate

- Attributes:
  - `name` (string, required): User's name

### HTTPValidationError

- Attributes:
  - `detail` (array of ValidationError): Validation error details
    - `loc` (array of strings/integers): Location of the error
    - `msg` (string): Error message
    - `type` (string): Error type

### ValidationError

- Attributes:
  - `loc` (array of strings/integers): Location of the error
  - `msg` (string): Error message
  - `type` (string): Error type

---

This guide furnishes details about the accessible API endpoints, their functions, expected request/response structures, and data organization.
