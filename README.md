Poster Projects

## Requirements

For running this application with Docker, you will need:

- Docker version 20.10.14 (the project might work with other versions, but this one was used during development)
- Docker Compose version 2.5.0 (the project might work with other versions, but this one was used during development)

For running the service without Docker, you will need:

- Python version 3.9.12

## Running the Application

1. **Starting the Application:** Utilize the following command to run the application:

```
make run-app
```

2. **Executing Unit Tests:** The following commands are used to install the necessary tools and run the unit tests:

```
make install
make tests
```

## API Documentation

Once you've successfully started the app, you can access the API documentation via your browser by following this link:

```
http://localhost:8000/api/docs
```

If you'd rather view the documentation offline, you can find it in the `docs` folder.

# Critique

1. **Current State and Potential Enhancements:** If provided with additional time, the areas of focus would be setting up a separate testing environment and implementing integration tests and request mocks to improve the quality of tests. Emphasis would also be placed on unit testing to verify the functionality of individual code segments.

2. **Scaling Strategy:** To ensure independent scalability, the application could be divided into microservices. Specifically, separate services for /post and /request endpoints could be developed.

3. **Potential Bottlenecks:** As the project scales, potential points of failure could be the database and the web server, as these areas commonly become bottlenecks.

4. **Real Life Scaling:** In a real-life scenario, a microservices-based architecture would be adopted to allow different components of the system to scale independently. Other considerations for scalability would include database optimization, load balancing, the use of caching to boost response times, and the implementation of auto-scaling to adjust server numbers based on load. Message queues for asynchronous processing would also be implemented to increase system reliability. The specific application of these strategies would be dependent on the project's unique requirements.

### Future Refactoring and Improvement:

- **Error Handling:** Develop a robust error handling mechanism.

- **Testing:** Implement more unit, integration, and stress tests to enhance application reliability.

- **Logging:** Incorporate a logging system and APM instrumentation for effective monitoring and troubleshooting.

- **Database Optimization:** Proactively address potential database performance issues, especially as user and post count grow. Direct queries could be considered instead of an ORM.

- **System Caching:** Implement system caching to improve performance.

- **Worker Quantity:** Increase the number of workers to enhance the application's processing power.

In conclusion, a thorough analysis of the application revealed several areas for improvement and potential modifications, including the implementation of a caching system, cloud deployment for load balancing, and improvements to the gunicorn server. These enhancements will significantly increase the efficiency and reliability of the application.
