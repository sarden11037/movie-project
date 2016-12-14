import webbrowser  # import webbrowser class to open webpage

""" class movie is the main classes from which all instance creation will
 recieve their information"""


class Movie():
    def __init__(self, movie_title, poster_image,
                 trailer_youtube):
        # initialization constructor for class Movie
        self.title = movie_title  # initialization of arguments
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
