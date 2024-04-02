# 0x0E-web_stack_debugging_1
The `0-nginx_likes_port_80` script is a Bash script designed to ensure that Nginx, a popular web server, is installed, running, and configured to listen on port 80. Here's a detailed breakdown of its components:

1. **Shebang (`#!/usr/bin/env bash`)**: This line specifies that the script should be executed using the Bash shell. It's a common way to ensure that the script runs with the appropriate interpreter, regardless of the system's configuration.

2. **Comment (`# This script checks if Nginx is installed and running, and ensures it's configured to listen on port 80 using service instead of systemctl.`)**: This line provides a brief description of what the script does. It's a good practice to include comments like this to make the script's purpose clear to anyone reading it.

3. **Check if Nginx is Installed**:
    - The script first checks if Nginx is installed on the system. It does this by using the `which` command to search for the `nginx` executable. If `nginx` is not found, the script installs it using `apt-get`.
    - **`if ! which nginx > /dev/null; then`**: This line checks if the `nginx` command is available. The `!` negates the condition, so the script proceeds to install Nginx if it's not found.
    - **`apt-get update && apt-get install -y nginx`**: These commands update the package lists for upgrades and new package installations, and then install Nginx. The `-y` option automatically answers "yes" to prompts, allowing the installation to proceed without user intervention.

4. **Check if Nginx is Running**:
    - The script then checks if Nginx is currently running. It does this by using the `service nginx status` command and checking if the output contains the string 'active (running)'.
    - **`if ! service nginx status | grep -q 'active (running)'; then`**: This line checks if Nginx is running. If it's not, the script starts Nginx.
    - **`service nginx start`**: This command starts the Nginx service.

5. **Check if Nginx is Configured to Listen on Port 80**:
    - The script checks if Nginx is configured to listen on port 80 by searching the default Nginx configuration file for the string 'listen 80;'.
    - **`if ! grep -q 'listen 80;' /etc/nginx/sites-available/default; then`**: This line checks the Nginx configuration. If Nginx is not configured to listen on port 80, the script configures it.
    - **Configuration Block**: The script then writes a new configuration block to the default Nginx configuration file, specifying that Nginx should listen on port 80 and serve files from `/var/www/html`. It also sets up a basic server block with a location directive to handle requests.
    - **`service nginx reload`**: After updating the configuration, the script reloads Nginx to apply the changes.

6. **Final Message**:
    - **`echo "Nginx is now configured to listen on port 80."`**: This line prints a message to the console indicating that Nginx is now configured to listen on port 80.

In summary, the `0-nginx_likes_port_80` script is a utility script for ensuring that Nginx is installed, running, and configured to listen on port 80. It automates the process of installing and configuring Nginx, making it easier to set up a web server on a Linux system.
