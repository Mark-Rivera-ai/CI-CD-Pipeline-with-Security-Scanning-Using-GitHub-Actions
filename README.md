Minimal To-Do List API

This project provides a simple REST API built with Flask that allows users to manage to-do items. It also includes automated CI/CD workflows using GitHub Actions, integrating static code analysis with SonarCloud and security vulnerability scanning with OWASP Dependency-Check.

Table of Contents
  - Setup
  - Endpoints
  - CI/CD Pipeline
  - Dependencies

Setup
-Prerequisites
   - Python 3.7+ installed on your local machine.
   - Java 17 installed for Maven-based security scanning (for the CI/CD pipeline).
   - SonarCloud account for code analysis.
   - OWASP Dependency-Check for vulnerability scanning (integrated in the pipeline).

Installation
1. Clone the repository:
   git clone https://github.com/Mark-Rivera-ai/minimal-todo-api.git
   cd minimal-todo-api
2. Install Python dependencies:
   pip install -r requirements.txt
3. Run the application:
   python app.py

The server should start running on http://127.0.0.1:5000.

Endpoints
- POST /todo: Add a new to-do item.
    - Request:
      { "task": "Buy groceries" }
    - Response:
      { "message": "To-do item added", "task": "Buy groceries" }
 - GET /todo: Retrieve all to-do items.
    - Response:
      { "todo": ["Buy groceries", "Read a book"] }

CI/CD Pipeline
This project uses GitHub Actions for continuous integration and security analysis. The pipeline includes:
1. Static Code Analysis:
   - SonarCloud is used to analyze code quality and maintainability.
   - Configured via pom.xml and the build.yml workflow.
2. Dependency Vulnerability Scanning:
   - OWASP Dependency-Check scans for known security vulnerabilities in dependencies.
   - The scan report is uploaded as an artifact in GitHub Actions.

Workflow Files
   - build.yml: Contains the setup for testing, building, and SonarCloud analysis.
   - security.yml: Runs the OWASP Dependency-Check for vulnerability scanning.

Dependencies
All required Python packages are listed in the requirements.txt file. Key dependencies include:
   - Flask: Lightweight WSGI web application framework.
   - SonarCloud: For code quality analysis (configured in pom.xml and build.yml).
   - OWASP Dependency-Check: For identifying vulnerabilities in dependencies.
