from resources.auth import Register, Login
from resources.hall import Hall
from resources.movie import CreateMovie, UpdateMovie, BrowseMovies, DeleteMovie, UpcomingMovies, SearchMovie
from resources.ticket import TicketPurchase, UserTickets

routes = (
    (Register, '/register'),
    (Login, '/login'),
    (Hall, '/create-hall'),
    (CreateMovie, '/create-movie'),
    (TicketPurchase, '/purchase-ticket'),
    (UserTickets, '/my-tickets'),
    (UpdateMovie, '/update-movie/<int:pk>'),
    (DeleteMovie, '/delete-movie/<int:pk>'),
    (BrowseMovies, '/browse-movies'),
    (UpcomingMovies, '/upcoming-movies'),
    (SearchMovie, '/search-movie/<string:query>'),
)
