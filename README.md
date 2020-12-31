# socket-programming-python
Simple socket programs build with python

# ONE DRAWBACK OF A SINGLE THREADED SERVER AND HOW TO SOLVE IT

Here, I will be demonstrating how I used multithreading to solve one of the drawbacks of a single thread server. This is a task that was given to us by Mr. Vimal Daga during his Socket programming class under IIEC rise python.

The drawback we are looking at is how a single-threaded server processes requests from clients. Since a single-threaded server runs only one thread, it can only process one request at a time.

This is a drawback because most often, servers at a particular time receive multiple requests from clients and some of the requests require a lot of time to process. This means that if one client (say client C) makes a request that requires a lot of time to process, then, all other clients that sent or will send their request after client C has sent its request will have to wait for the server to finish processing client C’s request before theirs gets processed. 

To solve this problem, we have to program our server in such a way that it can handle/process multiple requests at the same time (Simultaneously). To achieve this, we will use the concept of multithreading.

Multithreading in a nutshell is simply the process of executing multiple threads at the same time. A thread is a path/unit of execution in a process. With multithreading, a program is capable of performing multiple operations like processing multiple requests at once (simultaneously).

Now, the above-stated drawback, what I did was, since we are never aware of the number of requests that will come into our server, for every new request that is received, a thread is created to handle that request. In this way, no request will have to wait for other requests before being processed.

The video below demonstrates the above drawback and solution. To demonstrate this, I have created three python programs (using the concept of socket programming) one client, and two servers. One server has the capability to run only one thread while the other has the capability to run multiple threads.

The setup here is, we have three computers one running the server program and the others running the client program. The server program receives Linux commands from the client and executes the commands. After processing each request (executing the command received), the server makes a log entry containing the client’s IP, command/request, date and time of the request, and output (return code and output) of the request.

The video below is divided into two parts;

## Part One: Demonstration of drawback (single-threaded server)

In part one, we will see how two clients are sending their request to the server and the server is processing the request but suddenly, one client sends a request that causes the server to sleep for some time (client sends a sleep command). Since our server is single-threaded, it can only execute the sleep command and while executing this command, other requests sent to the server are not processed until the sleep time gets exhausted. When the sleep time is exhausted, we will see the other requests being processed serially in the order they were sent.

## Part two: Multithreaded server.

In part two, we still have a similar setup as in part one, that is clients are sending their requests to the server and the server is processing the requests. The difference between part two and part one is that; in part two, when a sleep request is made to the server program, the server receives the request, and because of its multithreading nature, it gives the request to a thread that starts executing it but the full functioning of the server is not disturbed that is other clients requests are processed immediately as the requests are sent. Also, in the video, we will notice that as the sleep request is being handled, other requests are being handled as well.

End Of Post.

### Thank you for reading. Comments, suggestions, and other ways of solving the above problem are accepted.

### Code Here:  https://github.com/yobahBertrandYonkou/socket-programming-python/tree/main/singe%20and%20multi%20threaded%20servers



