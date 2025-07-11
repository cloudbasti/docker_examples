# Use official Node.js image
FROM node:18

# Set working directory
WORKDIR /usr/src/app

# Install dependencies
COPY package*.json ./
RUN npm install && npm install -g nodemon

# Copy source code (only app.js and src directory)
COPY src ./src

# Expose port 3000 (default for many Node.js apps)
EXPOSE 3000

# Start the app with nodemon for hot reloading
CMD ["nodemon", "--legacy-watch", "--watch", "src", "src/app.js"]