FROM mongo:7.0

# Set environment variables
ENV MONGO_INITDB_ROOT_USERNAME=admin
ENV MONGO_INITDB_ROOT_PASSWORD=password
ENV MONGO_INITDB_DATABASE=myapp

# Create a directory for MongoDB data
RUN mkdir -p /data/db

# Expose MongoDB port
EXPOSE 27017

# Set the default command to run MongoDB
CMD ["mongod", "--bind_ip_all"] 