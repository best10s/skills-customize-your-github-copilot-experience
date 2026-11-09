# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API with FastAPI by creating routes, handling JSON data, and validating request payloads. This assignment introduces students to the basics of building web services in Python.

## 📝 Tasks

### 🛠️ Create a Basic API

#### Description
Build a small FastAPI application that exposes endpoints for managing a collection of tasks or items.

#### Requirements
Completed program should:

- Create a FastAPI app instance
- Define at least one `GET` endpoint that returns a list of items in JSON format
- Define a `POST` endpoint that accepts input data and adds it to the collection
- Return clean JSON responses using Python dictionaries or Pydantic models
- Start the app locally with `uvicorn` and test the endpoints in a browser or API client

### 🛠️ Add Dynamic Routes and Validation

#### Description
Extend the API so it can work with individual resources and validate incoming data.

#### Requirements
Completed program should:

- Add a `GET /items/{item_id}` endpoint that returns one item by ID
- Return a helpful error response when the item is not found
- Use a Pydantic model to validate incoming request data
- Include at least one field such as `title`, `description`, or `completed`
- Demonstrate both successful requests and invalid input handling

### 🛠️ Build a Small API Project

#### Description
Make the API more realistic by organizing it into a simple, complete project structure.

#### Requirements
Completed program should:

- Use meaningful route names and resource data
- Keep the app easy to read and organized into clear sections
- Add a few sample items so the API has initial data to return
- Show how the API responds with JSON for both listing and creating resources
- Include a brief description of how the API works and what each route does
