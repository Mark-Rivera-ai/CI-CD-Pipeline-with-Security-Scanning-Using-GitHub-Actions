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

## Usage Guide

1. Start the Flask server in a terminal:
```bash
python app.py
```
**Important:** Keep this terminal open and running. The server needs to stay running to process requests.

2. Open a new terminal window for executing API commands. In the new terminal, navigate to the project directory:
```bash
cd path/to/minimal-todo-api
```

3. Now you can execute commands in the new terminal window while the server runs in the first terminal.

**Note:** You cannot execute API commands in the same terminal where the Flask server is running. Always use a separate terminal for making requests.

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
- **Bash Example** (in new terminal):
```bash
curl -X POST http://127.0.0.1:5000/todo \
  -H "Content-Type: application/json" \
  -d '{"task": "Pick up kids"}'
```
- **PowerShell Alternative**:
```powershell
Invoke-WebRequest -Uri "http://127.0.0.1:5000/todo" -Method Post -ContentType "application/json" -Body '{"task": "Pick up kids"}'
```

### Get All Todo Items
- **URL**: `/todo`
- **Method**: `GET`
- **Bash Example** (in new terminal):
```bash
curl http://127.0.0.1:5000/todo
```
- **PowerShell Alternative**:
```powershell
Invoke-WebRequest -Uri "http://127.0.0.1:5000/todo" -Method Get
```

## Project Structure
```
minimal-todo-api/
├── .github/
│   └── workflows/     # GitHub Actions workflow configurations
├── src/              # Source code directory
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

## Troubleshooting

1. If you see an error when trying to execute commands, make sure:
   - The Flask server is running in a separate terminal
   - You're using a new terminal window for API requests
   - The server URL is correct (http://127.0.0.1:5000)
   - You're in the correct directory in your new terminal

2. Common Issues:
   - "Connection refused" - Check if the Flask server is running
   - "404 Not Found" - Verify the endpoint URL (/todo)
   - "Invalid JSON" - Check your JSON syntax in the POST request

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.
