# FastAPI Example

This is a simple FastAPI application that provides a basic API endpoint.

## Installation

Ensure you have Python installed, then install FastAPI and Uvicorn:

```bash
pip install fastapi uvicorn
```

## Running the Application

Start the FastAPI server using Uvicorn:

```bash
uvicorn main:app --reload
```

- `main` refers to the filename (main.py) containing the FastAPI app instance.
- `app` is the FastAPI instance.
- `--reload` enables automatic reloading on code changes (useful for development).

## API Endpoints

### Root Endpoint

**URL:** `/`

**Method:** `GET`

**Response:**

```json
{
  "message": "Hellow Word"
}
```

> Note: There is a typo in the message. It should be "Hello World".

## Testing the API

Once the server is running, you can test the API using a web browser or a tool like `curl` or Postman:

```bash
curl -X GET "http://127.0.0.1:8000/"
```

Alternatively, you can access the interactive API documentation provided by FastAPI at:
- [Swagger UI](http://127.0.0.1:8000/docs)
- [ReDoc](http://127.0.0.1:8000/redoc)

## License

This project is licensed under the MIT License.

