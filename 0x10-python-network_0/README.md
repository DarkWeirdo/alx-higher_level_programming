# python network 0 late submission
## task 0
The code you're looking at is a simple shell script written in Bash. It's designed to send a request to a specified URL and then display the size of the body of the response. Let's break down each line of the script:

1. `#!/bin/bash`
   - This is called a shebang. It tells the system that this script should be executed using the Bash shell.

2. `# sends a request an URL, and displays the size of the body of the response`
   - This is a comment. It's not executed as part of the script but provides information to anyone reading the script about what it does.

3. `curl -s "$1" | wc -c`
   - This line is the core of the script. It performs two main operations:
     - `curl -s "$1"`: This command sends a request to the URL specified as the first argument (`$1`) to the script. The `-s` option makes `curl` operate in silent mode, which means it won't show progress or error messages. The output of this command (the body of the response from the URL) is then piped (`|`) to the next command.
     - `wc -c`: This command counts the number of bytes in the input it receives. Since the input is the body of the response from the `curl` command, `wc -c` effectively counts the size of the response body.

In summary, when you run this script with a URL as an argument, it sends a request to that URL and then displays the size of the response body in bytes.

## task 1:
The script is a Bash script designed to send a GET request to a specified URL and then display the body of the response. Here's a breakdown of its contents:

1. `#!/bin/bash`
   - This line is known as a shebang. It specifies that the script should be executed using the Bash shell. This is necessary for the system to understand how to run the script.

2. `# sends a GET request to an URL, and displays the body of the response`
   - This is a comment line. It provides a brief description of what the script does. Comments in Bash scripts start with a `#` symbol and are ignored by the shell when executing the script.

3. `curl -sL "$1"`
   - This line is the core of the script. It uses the `curl` command to send a GET request to the URL provided as the first argument (`$1`) to the script. The `-sL` options have specific meanings:
     - `-s` makes `curl` operate in silent mode, which suppresses the progress meter and error messages.
     - `-L` tells `curl` to follow redirects if the server responds with a redirect status code.
   - The output of this command, which is the body of the HTTP response, is then displayed in the terminal.

In summary, when you run this script with a URL as an argument, it sends a GET request to that URL and displays the body of the response. This script is useful for quickly fetching and viewing the content of a webpage or API endpoint directly from the command line.

## task 2
The script is a Bash script designed to send a DELETE request to a specified URL and then display the body of the response. Here's a breakdown of its contents:

1. `#!/bin/bash`
   - This line is known as a shebang. It specifies that the script should be executed using the Bash shell. This is necessary for the system to understand how to run the script.

2. `# sends a DELETE request to an URL and displays the body of the response`
   - This is a comment line. It provides a brief description of what the script does. Comments in Bash scripts start with a `#` symbol and are ignored by the shell when executing the script.

3. `curl -sX DELETE "$1"`
   - This line is the core of the script. It uses the `curl` command to send a DELETE request to the URL provided as the first argument (`$1`) to the script. The `-sX` options have specific meanings:
     - `-s` makes `curl` operate in silent mode, which suppresses the progress meter and error messages.
     - `-X` specifies the request method to use when communicating with the HTTP server. In this case, `DELETE` is specified, indicating that a DELETE request should be sent.
   - The output of this command, which is the body of the HTTP response, is then displayed in the terminal.

In summary, when you run this script with a URL as an argument, it sends a DELETE request to that URL and displays the body of the response. This script is useful for interacting with web services or APIs that support the DELETE method, allowing you to remove resources or data specified by the URL.
