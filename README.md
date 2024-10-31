# Minimal TODO API

A simple REST API built with Flask that allows you to manage todo items. This project demonstrates basic CRUD operations and RESTful API design.

## Features

- Create new todo items
- Retrieve all todo items
- Simple and lightweight
- JSON-based API responses

## Prerequisites

- Python 3.x
- Flask
- PowerShell or Command Prompt (for testing API endpoints)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Mark-Rivera-ai/minimal-todo-api.git
cd minimal-todo-api
```

2. Install Flask (if not already installed):
```bash
pip install flask
```

## Running the Application

1. Start the Flask server:
```bash
python app.py
```

2. The server will start running at `http://127.0.0.1:5000`

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
- **Bash Example**:
```bash
curl -X POST http://127.0.0.1:5000/todo \
  -H "Content-Type: application/json" \
  -d '{"task": "Pick up kids"}'
```

### Get All Todo Items
- **URL**: `/todo`
- **Method**: `GET`
- **Bash Example**:
```bash
curl http://127.0.0.1:5000/todo
```

## Example Usage

1. Start the server:
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
├── app.py              # Main application file
├── README.md           # Project documentation
└── requirements.txt    # Project dependencies
```

## Technical Stack

- Python 3.x
- Flask (Web Framework)
- JSON for data formatting
- In-memory storage for todos

## Security Note

This is a development server and should not be used in production. For production deployment, use a proper WSGI server and implement appropriate security measures.

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
