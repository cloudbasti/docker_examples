FROM postgres:15

# Set environment variables
ENV POSTGRES_DB=myapp
ENV POSTGRES_USER=admin
ENV POSTGRES_PASSWORD=password

# Create a directory for PostgreSQL data
RUN mkdir -p /var/lib/postgresql/data

# Expose PostgreSQL port
EXPOSE 5432

# Set the default command to run PostgreSQL
CMD ["postgres"] 