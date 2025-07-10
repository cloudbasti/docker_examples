# PostgreSQL Database

This folder contains the PostgreSQL database configuration for the Docker stack.

## Dockerfile

The Dockerfile sets up PostgreSQL 15 with the following configuration:

- **Database**: myapp
- **Username**: admin
- **Password**: password
- **Port**: 5432

## Usage

### Build the image:
```bash
docker build -t postgresql-app .
```

### Run the container:

#### Option 1: Using Docker Compose (Recommended)
```bash
# Start the container (builds image if needed, uses existing if available)
docker-compose up -d

# Stop the container
docker-compose down

# View logs
docker-compose logs -f
```

#### Option 2: Using Docker commands directly
```bash
docker run -d --name postgresql -p 5432:5432 -v postgresql_data:/var/lib/postgresql/data postgresql-app
```

**Note for Windows users:** If you encounter volume name errors with direct Docker commands, use this command instead:
```bash
docker run -d --name postgresql -p 5432:5432 -v "postgresql_data:/var/lib/postgresql/data" postgresql-app
```

### Connect to PostgreSQL:
```bash
# Using psql client
docker exec -it postgresql psql -U admin -d myapp

# Or connect from your application
postgresql://admin:password@localhost:5432/myapp
```

## Environment Variables

You can override the default environment variables:

- `POSTGRES_DB`: Database name (default: myapp)
- `POSTGRES_USER`: Username (default: admin)
- `POSTGRES_PASSWORD`: Password (default: password)

## Data Persistence

The PostgreSQL data is persisted using a Docker volume named `postgresql_data`.

## Initial Setup

The database will be automatically created when the container starts for the first time. You can add initialization scripts by placing `.sql` files in a `docker-entrypoint-initdb.d/` directory if needed. 