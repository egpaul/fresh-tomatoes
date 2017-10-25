import webbrowser


class Movie ():
    """This class provides a way to store movie related information"""

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

# Instances that share,movie title, storyline, poster art and, youtube trailer.
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

# This is the instance that opens the youtube URL for the movie trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
