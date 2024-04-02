# python network 0 late submission

## Related topics:
1. HTTP basics
2. cURL command basics
3. Bash scripting review

### task 0
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

### task 1:
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

### task 2
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

### task 3
The script is a Bash script designed to display all HTTP methods the server will accept for a specified URL. Here's a breakdown of its contents:

1. `#!/bin/bash`
   - This line is known as a shebang. It specifies that the script should be executed using the Bash shell. This is necessary for the system to understand how to run the script.

2. `# displays all HTTP methods the server will accept.`
   - This is a comment line. It provides a brief description of what the script does. Comments in Bash scripts start with a `#` symbol and are ignored by the shell when executing the script.

3. `curl -sI "$1" | grep "Allow" | cut -d " " -f 2-`
   - This line is the core of the script. It performs several operations:
     - `curl -sI "$1"`: This command sends a HEAD request to the URL provided as the first argument (`$1`) to the script. The `-sI` options have specific meanings:
       - `-s` makes `curl` operate in silent mode, which suppresses the progress meter and error messages.
       - `-I` tells `curl` to only fetch the HTTP-header. This is useful for retrieving meta-information written in headers, without having to download the entire body content.
     - The output of this command, which includes the headers of the HTTP response, is then piped (`|`) to the next command.
     - `grep "Allow"`: This command filters the output to only include lines that contain the word "Allow". The "Allow" header in an HTTP response specifies the methods that are allowed for the resource identified by the URL.
     - `cut -d " " -f 2-`: This command splits the line at each space character (`-d " "`) and then selects all fields starting from the second field (`-f 2-`). This effectively removes the "Allow:" part of the header, leaving only the list of allowed methods.

In summary, when you run this script with a URL as an argument, it sends a HEAD request to that URL, retrieves the "Allow" header from the response, and displays the list of HTTP methods that the server will accept for that URL. This script is useful for quickly determining which HTTP methods are supported by a web service or API endpoint.

### task 4
The file `4-header.sh` is a Bash script designed to send a GET request to a specified URL and then display the body of the response. It includes a custom HTTP header, `X-School-User-Id`, with a value of `98`. Here's a breakdown of its contents:

1. `#!/bin/bash`
   - This line is known as a shebang. It specifies that the script should be executed using the Bash shell. This is necessary for the system to understand how to run the script.

2. `# sends a GET request to the URL, and displays the body of the response`
   - This is a comment line. It provides a brief description of what the script does. Comments in Bash scripts start with a `#` symbol and are ignored by the shell when executing the script.

3. `curl -sH "X-School-User-Id: 98" "$1"`
   - This line is the core of the script. It uses the `curl` command to send a GET request to the URL provided as the first argument (`$1`) to the script. The `-sH` options have specific meanings:
     - `-s` makes `curl` operate in silent mode, which suppresses the progress meter and error messages.
     - `-H` specifies an additional HTTP header to include in the request. In this case, it adds the header `X-School-User-Id: 98`.
   - The output of this command, which is the body of the HTTP response, is then displayed in the terminal.

In summary, when you run this script with a URL as an argument, it sends a GET request to that URL with the custom header `X-School-User-Id: 98` and displays the body of the response. This script is useful for interacting with web services or APIs that require specific headers for authentication or other purposes.

### task 5:
The `5-post_params.sh` script is a simple Bash script designed to send a POST request to a specified URL and display the body of the response. Here's a breakdown of its components:

1. **Shebang (`#!/bin/bash`)**: This line tells the system that this script should be executed using the Bash shell. It's the first line of the script and is necessary for the system to know how to run the script.

2. **Comment (`# sends a POST request to the passed URL, and displays the body of the response`)**: This line is a comment that describes what the script does. It's not executed by the shell but serves as documentation for anyone reading the script.

3. **`curl` Command**: This is the main command of the script. `curl` is a command-line tool used for transferring data with URLs. It supports various protocols, including HTTP and HTTPS.

    - **`-s`**: This option makes `curl` silent or quiet mode. It means that it won't show progress meter or error messages.
    - **`-X POST`**: This option specifies the request method to use when communicating with the HTTP server. In this case, it's set to POST, which is used to send data to the server.
    - **`-d "email=test@gmail.com&subject=I will always be here for PLD"`**: The `-d` option sends the specified data in a POST request to the HTTP server. Here, it's sending two pieces of data: an email address and a subject line. The data is formatted as a query string, which is a common way to send data in HTTP requests.
    - **`"$1"`**: This is a positional parameter that represents the first argument passed to the script. In the context of this script, it should be the URL to which the POST request is sent.

4. **Empty Line**: The last line of the script is empty. It's not necessary for the script to function but can be used for readability or to separate sections of the script.

In summary, when you run this script with a URL as an argument, it sends a POST request to that URL with the specified data (`email=test@gmail.com&subject=I will always be here for PLD`) and displays the response body.

### task 6:
The `6-peak.py` script is a Python program that defines a function to find a peak in a list of unsorted integers. A peak is an element that is greater than or equal to its neighbors. Here's a detailed explanation of the script:

1. **Shebang (`#!/usr/bin/python3`)**: This line specifies that the script should be executed using Python 3. It's not strictly necessary for running the script in a Python environment but is useful for running the script directly from the command line.

2. **Docstring (`"""Defines a peak-finding algorithm."""`)**: This is a multi-line string that serves as documentation for the script. It briefly describes the purpose of the script.

3. **Function Definition (`def find_peak(list_of_integers):`)**: This line defines a function named `find_peak` that takes one argument, `list_of_integers`. This function is designed to find a peak in the given list of integers.

4. **Base Cases**:
    - **Empty List Check (`if (not list_of_integers):`)**: If the list is empty, the function returns `None`, indicating that there is no peak.
    - **Single or Two Elements Check (`if (len(list_of_integers) <= 2):`)**: If the list contains one or two elements, the function returns the maximum of these elements, which is the peak.

5. **Initial Peak Check**:
    - The script checks if the first or last element of the list is a peak by comparing them with their neighbors. If either is greater than or equal to its neighbor, it is considered a peak, and the function returns it.

6. **Iterative Peak Search**:
    - If the list has more than two elements and neither the first nor the last element is a peak, the script enters a while loop to search for a peak.
    - The loop starts from the second element (`i = 1`) and iterates through the list until it finds a peak or reaches the end of the list.
    - Inside the loop, it checks if the current element is greater than or equal to both its neighbors. If so, it returns the current element as the peak.
    - If the current element is not a peak, the loop increments `i` by 1 to move to the next element.

7. **Return Statement for No Peak Found**:
    - If the loop completes without finding a peak, the function returns the last checked peak (which could be `None` if no peak was found in the initial checks).

In summary, the `find_peak` function in `6-peak.py` is designed to find a peak in a list of unsorted integers. It handles various edge cases, such as empty lists, lists with one or two elements, and lists where the peak is not at the beginning or end. It uses a combination of direct checks and an iterative search to find the peak.
