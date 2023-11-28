from resources.auth import Register, Login, GetUser
from resources.hall import Hall
from resources.movie import (
    MovieResource,
    UpcomingMovies,
    SearchMovie,
    BrowseMovies,
    CreateMovie,
)
from resources.ticket import TicketPurchase, UserTickets

routes = (
    (Register, "/register"),
    (Login, "/login"),
    (GetUser, "/get-user"),
    (Hall, "/create-hall"),
    (CreateMovie, "/create-movie"),
    (TicketPurchase, "/purchase-ticket"),
    (UserTickets, "/my-tickets"),
    (MovieResource, "/movie/<int:pk>"),
    (BrowseMovies, "/browse-movies"),
    (UpcomingMovies, "/upcoming-movies"),
    (SearchMovie, "/search-movie/<string:query>"),
)
