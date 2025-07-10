from flask import Flask, jsonify
import datetime
import platform
import os

app = Flask(__name__)

def test_python_function():
    """Simple test function to verify Python code execution"""
    result = {
        "message": "Python is working inside the container!",
        "timestamp": datetime.datetime.now().isoformat(),
        "python_version": platform.python_version(),
        "platform": platform.platform(),
        "container_id": os.environ.get('HOSTNAME', 'unknown'),
        "test_calculation": 2 + 2 * 3  # Simple math test
    }
    return result

@app.route('/')
def home():
    """Home endpoint"""
    return jsonify({
        "message": "Flask Backend is running!",
        "status": "success"
    })

@app.route('/test')
def test():
    """Test endpoint to verify Python code execution"""
    return jsonify(test_python_function())

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.datetime.now().isoformat()
    })

if __name__ == '__main__':
    print("Starting Flask application...")
    print("Python version:", platform.python_version())
    print("Platform:", platform.platform())
    print("Container ID:", os.environ.get('HOSTNAME', 'unknown'))
    
    # Test the function
    test_result = test_python_function()
    print("Test function result:", test_result)
    
    app.run(host='0.0.0.0', port=5000, debug=True) 