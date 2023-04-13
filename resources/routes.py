from resources.auth import Register, Login
from resources.hall import Hall
from resources.movie import CreateMovie, UpdateMovie, BrowseMovies, DeleteMovie
from resources.ticket import TicketPurchase, UserTickets

routes = (
    (Register, '/register'),
    (Login, '/login'),
    (Hall, '/create-hall'),
    (CreateMovie, '/create-movie'),
    (TicketPurchase, '/purchase-ticket'),
    (UserTickets, '/my-tickets'),
    (UpdateMovie, '/update-movie/<int:pk>'),
    (BrowseMovies, '/browse-movies'),
    (DeleteMovie, '/delete-movie/<int:pk>'),
    # TODO: add route delete movie, etc
)
