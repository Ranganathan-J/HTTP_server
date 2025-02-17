Python HTTP Server
This project implements a simple HTTP server using Python. The server listens for incoming HTTP requests, handles basic HTTP methods like GET and POST, and responds with appropriate content.

Features
GET Requests: Handles basic GET requests to serve static content.
POST Requests: Handles POST requests to receive and process data.
Custom Headers: Allows sending custom headers with HTTP responses.
Basic Routing: Implements routing for specific URLs.
Requirements
Python 3.9 or higher
Installation
1. Clone this Repository
Clone the repository to your local machine:

bash
Copy
Edit
git clone https://github.com/Ranganathan-J/HTTP_server.git
2. Navigate into the Project Directory
bash
Copy
Edit
cd http-server-python
3. Run the Server
Run the Python server script:

bash
Copy
Edit
python server.py
By default, the server will run on localhost (127.0.0.1) and listen on port 8080.

4. Access the Server
Open your web browser and go to:

cpp
Copy
Edit
http://127.0.0.1:8080
Usage
The server will respond to a variety of HTTP requests. Here's an example of how to make a simple GET request using curl or your browser:

bash
Copy
Edit
curl http://127.0.0.1:8080
If you have a POST handler implemented, you can send data like this:

bash
Copy
Edit
curl -X POST -d "name=JohnDoe" http://127.0.0.1:8080
Example Response
Here’s an example response for a GET request to the root endpoint (/):

makefile
Copy
Edit
HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8
Content-Length: 17

Hello, World!
For a POST request, the server might respond with the data it receives or a success message.

Customizing the Server
Change Port: Modify the port number by changing the PORT variable in the server.py file.

python
Copy
Edit
PORT = 8081
Add Routes: To handle more routes, simply add more conditions in the handle_request function to check for different paths (e.g., /about, /contact).

python
Copy
Edit
if "GET /about" in request:
    response = "<html><body><h1>About Us</h1></body></html>"
Serve Static Files: To serve HTML, CSS, and JS files, you can read the file content and send it as the response.

python
Copy
Edit
def serve_file(filepath):
    with open(filepath, 'r') as file:
        return file.read()
Contributing
Feel free to fork this repository and submit pull requests! Any contributions to improve the functionality of the server are welcome.

License
This project is licensed under the MIT License - see the LICENSE file for details.

