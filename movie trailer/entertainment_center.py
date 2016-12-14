import media  # import the media.py file with class Movie
import fresh_tomatoes  # import the html build file

# declaration of new class instances
revolver = media.Movie("Revolver",
                       "http://bit.ly/2hxvYlx",
                       "https://youtu.be/M9JAYfZOHms")
body_of_lies = media.Movie("Body of Lies",
                           "http://bit.ly/2hwQzGm",
                           "https://youtu.be/A4noCwwEUBA")
watchmen = media.Movie("Watchmen",
                       "http://bit.ly/2gMkDPJ",
                       "https://youtu.be/PVjA0y78_EQ")
the_social_network = media.Movie("The Social Network",
                                 "http://bit.ly/1MR9iHJ",
                                 "https://youtu.be/lB95KLmpLR4")
the_girl_dragon_tattoo = media.Movie(" The Girl with the Dragon Tattoo",
                                     "http://bit.ly/1KSmKeM",
                                     "https://youtu.be/DqQe3OrsMKI")
fight_club = media.Movie("Fight Club",
                         "http://bit.ly/2hGa2Yr",
                         "https://youtu.be/SUXWAEX2jlg")
# array used to consolidate all class instances
movies = [revolver, body_of_lies, watchmen, the_social_network,
          the_girl_dragon_tattoo, fight_club]
# pass the array into the html file
fresh_tomatoes.open_movies_page(movies)




