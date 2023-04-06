from resources.auth import Register, Login
from resources.hall import Hall
from resources.movie import Movie
from resources.ticket import TicketPurchase, UserTickets

routes = (
    (Register, '/register'),
    (Login, '/login'),
    (Hall, '/create-hall'),
    (Movie, '/create-movie'),
    (TicketPurchase, '/purchase-ticket'),
    (UserTickets, '/my-tickets'),
)
