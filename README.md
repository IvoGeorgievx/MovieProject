#The Movie Project

This is a REST project for my Web Applications with Flask course.

To use this API, follow these steps:


#Usage

1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Start the server by running app.py.
4. Import the Postman collection located in the `docs` directory to test the API endpoints.
5. Enjoy!

#Endpoints

Here is a list of the available endpoints:

1. '/register': Registers a new user
2. '/login': Login an existing user 
3. '/create-hall': Create a hall for movies screening.
4. '/create-movie': Admin creates a movie.
5. '/purchase-ticket': User can purchase a ticket for a movie of his choice.
6. '/my-tickets': User can see his ticket purchases.
7. '/update-movie/<int:pk>': An admin can update existing movie.
8. '/browse-movies': Gets all the movies in the database.
9. '/delete-movie/<int:pk>': Admin deletes a movie.
10. '/upcoming-movies': Connects to the Movie Database API, to get the upcoming movies.
11. '/search-movie/<string:query>': Connects to the Movie Database API, to get movie information set by the query.
