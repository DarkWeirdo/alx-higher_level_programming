# 0x14-javascript-web_scraping

## Task 0

- Line 1: The shebang line specifies that this script should be run with Node.js.
- Line 3: Import the `fs` module, which is used for file system operations.
- Line 4: Retrieve the file path from the command line arguments.
- Line 6-12: Read the file asynchronously with `fs.readFile`. The encoding `utf-8` ensures the file's content is treated as text. If an error occurs (e.g., file not found), it is caught and printed; otherwise, the content of the file is printed.

## Task 1

- Line 1: The shebang line #!/usr/bin/node makes the script executable with Node.js.
- Line 3: The fs module is imported, which provides filesystem-related functionality.
- Line 5-6: process.argv is used to retrieve the command-line arguments. process.argv[2] is the file path, and process.argv[3] is the string to write.
- Line 8-12: fs.writeFile is used to write the string to the file specified by filePath. The content is written in utf-8 encoding. If an error occurs during the write operation, it is caught in the callback and printed to the console.

## Task 2

- Shebang Line: The script starts with `#!/usr/bin/node` to specify that it should be executed using Node.js.
- Module Import: Uses `const` to import the `request` module, which is necessary for making HTTP requests.
- Command Line Arguments: `process.argv[2]` is used to get the URL from the command line argument.
- Request Handling: The `request` function is called with the URL. It takes a callback function that handles the response. The callback checks for - errors and prints the status code.
- Error Handling: If an error occurs during the request (e.g., network issues, invalid URL), it logs the error.
- Output: Prints the status code in the format `code: <status code>`.

## Task 3

## Task 4

## Task 5

In this JavaScript script, we utilize the request module to send an HTTP request to a specified URL and then save the response body to a file using the fs module.

Here's a breakdown of the script:

1. We require the necessary modules fs and request.
2. The script retrieves the URL and file path from the command line arguments.
3. It sends a request to the specified URL using request.
4. Upon receiving a response, it checks for errors and verifies if the status code is 200 (OK).
5. If there are no errors and the status code is 200, it writes the body of the response to the specified file path using fs.writeFileSync.
6. The file is encoded in UTF-8.
7. If an error occurs during the request or the status code is not 200, an error message is logged.

- This script essentially fetches the contents of a webpage from a given URL and saves it to a file specified by the user in UTF-8 encoding.

## Task 6

This script will fetch the data from the provided API URL, filter out the completed tasks, count the number of completed tasks per user id, and then print the result as shown in the example output you provided.
