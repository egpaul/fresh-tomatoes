import fresh_tomatoes
import media

goodfellas = media.Movie ("Goodfellas",
                         "A young man grows up in the mob and works very hard to advance himself through the ranks",
                         "https://s-media-cache-ak0.pinimg.com/originals/17/34/15/173415b43512c20f4ec490909b81a82c.jpg",
                         "https://youtu.be/qWhS8Pjf-9c")
# This is an instance for the class movie that provides information for the movie Goodfellas.

casino = media.Movie ("Casino",
                     "In early-1970s Las Vegas, low-level mobster Sam Ace Rothstein (Robert De Niro) gets tapped by his bosses to head the Tangiers Casino. ",
                     "http://www.impawards.com/1995/posters/casino_ver1.jpg",
                     "https://youtu.be/EGNx3ilNB80")
# This is an instance for the class movie that provides information for the movie Casino.

a_bronx_tale = media.Movie ("A Bronx Tale",
                           "As he grows into a teenager on the streets of the Bronx in the socially turbulent 1960s, Calogero (Lillo Brancato) gets taken under the wing of neighborhood mobster Sonny (Chazz Palminteri).",
                           "http://is1.mzstatic.com/image/thumb/Video52/v4/7c/ed/9b/7ced9bfb-50f7-ca84-2757-3d53adf48d1e/source/1200x630bb.jpg",
                           "https://youtu.be/iPaMz7DkGdw")
# This is an instance for the class movie that provides information for the movie A Bronx Tale.

donnie_brasco = media.Movie ("Donnie Brasco",
                            "Joseph Pistone (Johnny Depp) is an FBI agent who has infiltrated one of the major New York Mafia families and is living under the name Donnie Brasco.",
                            "https://s-media-cache-ak0.pinimg.com/originals/7f/99/8d/7f998df079fc950a9779ca23ff9b5836.jpg",
                            "https://youtu.be/-LxfpyZXJiI")
# This is an instance for the class movie that provides information for the movie Donnie Brasco.

the_godfather = media.Movie ("The Godfather",
                            "The aging patriarch of an organized crime dynasty transfers control of his clandestine",
                            "http://static.metacritic.com/images/products/movies/3/47c2b1f35087fc23c5ce261bbc3ad9e0.jpg",
                            "https://youtu.be/8V2k2YQEQJ4")
# This is an instance for the class movie that provides information for the movie The Godfather.

the_departed = media.Movie ("The Departed",
                           "An undercover cop and a mole in the police attempt to identify each other.",
                           "http://static.rogerebert.com/uploads/movie/movie_poster/the-departed-2007/large_tGLO9zw5ZtCeyyEWgbYGgsFxC6i.jpg",
                           "https://youtu.be/SGWvwjZ0eDc")
# This is an instance for the class movie that provides information for the movie The Departed.

movies = [goodfellas, casino, a_bronx_tale, donnie_brasco, the_godfather, the_departed]
fresh_tomatoes.open_movies_page(movies)

#print (media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)
