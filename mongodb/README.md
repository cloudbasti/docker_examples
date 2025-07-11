# MongoDB Database

This folder contains the MongoDB database configuration for the Docker stack.

## Dockerfile

The Dockerfile sets up MongoDB 7.0 with the following configuration:

- **Database**: myapp
- **Username**: admin
- **Password**: password
- **Port**: 27017

## Usage

### Build the image:
```bash
docker build -t mongodb-app .
```

### Run the container:
```bash
docker run -d --name mongodb -p 27017:27017 -v mongodb_data:/data/db mongodb-app
```

### Connect to MongoDB:
```bash
# Using MongoDB shell
docker exec -it mongodb mongosh -u admin -p password

# Or connect from your application
mongodb://admin:password@localhost:27017/myapp
```

## Environment Variables

You can override the default environment variables:

- `MONGO_INITDB_ROOT_USERNAME`: Root username (default: admin)
- `MONGO_INITDB_ROOT_PASSWORD`: Root password (default: password)
- `MONGO_INITDB_DATABASE`: Initial database name (default: myapp)

## Data Persistence

The MongoDB data is persisted using a Docker volume named `mongodb_data`. 