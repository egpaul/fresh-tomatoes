import fresh_tomatoes
import media

# Goodfellas Movie: Movie title, storyline, poster image, and trailer
goodfellas = media.Movie(
    "Goodfellas",
    "A young man grows up in the mob and works very hard to advance himself"
    "through the ranks",
    "https://s-media-cache-ak0.pinimg.com/originals/17/34/15/173415b43512c20f4ec490909b81a82c.jpg",  # NOQA
    "https://youtu.be/qWhS8Pjf-9c"
)

# Casino Movie: Movie title, storyline, poster image, and trailer
casino = media.Movie(
    "Casino",
    "In early-1970s Las Vegas, low-level mobster Sam Ace Rothstein (Robert De"
    "Niro) gets tapped by his bosses to head the Tangiers Casino. ",
    "http://www.impawards.com/1995/posters/casino_ver1.jpg",
    "https://youtu.be/EGNx3ilNB80"
)

# A Bronx Tale Movie: Movie title, storyline, poster image, and trailer
a_bronx_tale = media.Movie(
    "A Bronx Tale",
    "As he grows into a teenager on the streets of the Bronx in the socially"
    "turbulent 1960s, Calogero (Lillo Brancato) gets taken under the wing of"
    "neighborhood mobster Sonny (Chazz Palminteri).",
    "http://is1.mzstatic.com/image/thumb/Video52/v4/7c/ed/9b/7ced9bfb-50f7-ca84-2757-3d53adf48d1e/source/1200x630bb.jpg",  # NOQA
    "https://youtu.be/iPaMz7DkGdw"
    )

# Donnie Brasco Movie: Movie title, storyline, poster image, and trailer
donnie_brasco = media.Movie(
    "Donnie Brasco",
    "Joseph Pistone (Johnny Depp) is an FBI agent who has infiltrated one of"
    "the major New York Mafia families and is living under the name Donnie"
    "Brasco.",
    "https://s-media-cache-ak0.pinimg.com/originals/7f/99/8d/7f998df079fc950a9779ca23ff9b5836.jpg",  # NOQA
    "https://youtu.be/-LxfpyZXJiI"
    )

# The Godfather: Movie title, storyline, poster image, and trailer
the_godfather = media.Movie(
    "The Godfather",
    "The aging patriarch of an organized crime dynasty transfers control of"
    "his clandestine",
    "http://static.metacritic.com/images/products/movies/3/47c2b1f35087fc23c5ce261bbc3ad9e0.jpg",  # NOQA
    "https://youtu.be/8V2k2YQEQJ4"
    )

# The Departed: Movie title, storyline, poster image, and trailer
the_departed = media.Movie(
    "The Departed",
    "An undercover cop and a mole in the police attempt to identify each"
    "other.",
    "http://static.rogerebert.com/uploads/movie/movie_poster/the-departed-2007/large_tGLO9zw5ZtCeyyEWgbYGgsFxC6i.jpg",  # NOQA
    "https://youtu.be/SGWvwjZ0eDc")
# The Departed: Movie title, storyline, poster image, and trailer

# Sets the movies to be passed to the media file
movies = [
    goodfellas,
    casino,
    a_bronx_tale,
    donnie_brasco,
    the_godfather,
    the_departed
]

# Opens the HTML file in a webbrowser
fresh_tomatoes.open_movies_page(movies)

# print (media.Movie.VALID_RATINGS)
# print(media.Movie.__doc__)
