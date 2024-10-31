# Minimal TODO API

A simple REST API built with Flask that allows you to manage todo items. This project demonstrates basic CRUD operations and RESTful API design.

## About

CI/CD Pipeline with Security Scanning using GitHub Actions integrating SonarCube for static code analysis and OWASP Dependency-Check for vulnerability scanning.

## Features

- Create new todo items
- Retrieve all todo items
- Simple and lightweight
- JSON-based API responses
- Integrated security scanning
  - SonarCube static code analysis
  - OWASP Dependency-Check
- Automated CI/CD pipeline with GitHub Actions

## Prerequisites

- Python 3.x
- Flask
- Git Bash (for running curl commands)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Mark-Rivera-ai/minimal-todo-api.git
cd minimal-todo-api
```

2. Install Flask:
```bash
pip install flask
```

## API Endpoints

### Create a Todo Item
- **URL**: `/todo`
- **Method**: `POST`
- **Content-Type**: `application/json`
- **Body**:
```json
{
    "task": "Your task description"
}
```
- **Example Command**:
```bash
curl -X POST http://127.0.0.1:5000/todo \
  -H "Content-Type: application/json" \
  -d '{"task": "Pick up kids"}'
```

### Get All Todo Items
- **URL**: `/todo`
- **Method**: `GET`
- **Example Command**:
```bash
curl http://127.0.0.1:5000/todo
```

## Usage Guide

1. Start the Flask server:
```bash
python app.py
```

2. Add a new todo item:
```bash
curl -X POST http://127.0.0.1:5000/todo \
  -H "Content-Type: application/json" \
  -d '{"task": "Pick up kids"}'
```

3. View all todo items:
```bash
curl http://127.0.0.1:5000/todo
```

## Project Structure
```
minimal-todo-api/
├── .github/
│   └── workflows/     # GitHub Actions workflow configurations
├── app.py            # Main application file
├── pom.xml          # Maven configuration for security scanning
├── requirements.txt  # Python dependencies
└── README.md        # Project documentation
```

## Security Features

This project includes:
- SonarCube integration for static code analysis
- OWASP Dependency-Check for vulnerability scanning
- Automated security checks via GitHub Actions

## Development Note

This is a development server and should not be used in production. For production deployment, use a proper WSGI server and implement appropriate security measures.

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
