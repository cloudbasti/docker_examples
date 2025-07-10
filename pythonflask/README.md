# Python Flask Backend

This folder contains a Python Flask backend application configured to run in a Docker container.

## Features

- **Flask 3.0.0** - Modern web framework
- **Python 3.11** - Latest stable Python version
- **Test Function** - Simple function to verify Python code execution
- **Health Check** - Endpoint to verify container health
- **Development Mode** - Debug enabled for development

## Endpoints

- `GET /` - Home endpoint
- `GET /test` - Test Python function execution
- `GET /health` - Health check

## Usage

### Build the image:
```bash
docker build -t flask-backend .
```

### Run the container:
```bash
docker run -d --name flask-backend -p 5000:5000 flask-backend
```

### Test the endpoints:
```bash
# Home endpoint
curl http://localhost:5000/

# Test Python function
curl http://localhost:5000/test

# Health check
curl http://localhost:5000/health
```

## Test Function

The `test_python_function()` demonstrates:
- Python code execution
- System information retrieval
- Simple calculations
- Container identification
- Timestamp generation

## Container Information

The application will print:
- Python version
- Platform information
- Container ID
- Test function results

## Development

The Flask app runs in development mode with:
- Debug enabled
- Auto-reload on code changes
- Detailed error messages 