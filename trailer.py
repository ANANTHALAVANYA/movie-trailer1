import webbrowser

class Favouritemovies():
    def __init__(self,movie_title,movie_story,movie_picture,movie_trailer):
        self.title=movie_title
        self.storyline=movie_story
        self.poster_image_url=movie_picture
        self.trailer_youtube_url=movie_trailer
    def show_film_trailer(self):
         webbrowser.open(self,trailer_youtube_url)
        
