from resources.auth import Register, Login
from resources.hall import Hall
from resources.movie import Movie
from resources.ticket import Ticket

routes = (
    (Register, '/register'),
    (Login, '/login'),
    (Hall, '/create-hall'),
    (Movie, '/create-movie'),
    (Ticket, '/purchase-ticket'),
)
