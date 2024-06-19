# Using the latest ubuntu image as base image
FROM ubuntu:latest

# Update package lists and install required packages
# installing netcat-openbsd as netcat is not directly available in ubuntu base image
RUN apt update && apt install -y \
    fortune-mod \
    cowsay \
    netcat-openbsd

# Ensure /usr/games is in the PATH to use the cowsay package
ENV PATH="/usr/games:${PATH}"

WORKDIR /app

# Copying the server script
COPY wisecow.sh /app/wisecow.sh

# Making the server script executable by changing permissions
RUN chmod +x /app/wisecow.sh

# Exposing the port the server is running on
EXPOSE 4499

# Running the shell script ~
CMD ["./wisecow.sh"]
