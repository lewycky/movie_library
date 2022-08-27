


class Movie():
    
    def __init__(self, title, year_of_publishment, type, number_of_plays):
        self.title = title
        self.year_of_publishment = year_of_publishment
        self.type = type
        self.number_of_plays = number_of_plays

    def __str__(self):
        return f'{self.title} ({self.year_of_publishment})' 
    
    def __repr__(self) -> str:
        pass     

    def play(self):
        return self.title + 1  



class Series(Movie):

    def __init__(self, episode_number, season_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_number = episode_number
        self.season_number = season_number

    def __str__(self):
        return f'{self.title} {self.season_number}{self.episode_number}'   


    

movie_1=Movie(title="Pulp Fiction", year_of_publishment="1994", type="Thriller", number_of_plays=82173901)
series_1=Series(title="Vikings", year_of_publishment="2013",season_number= "S01", episode_number="E01", type="Historical drama", number_of_plays=5621231 )
series_2=Series(title="Vikings", year_of_publishment="2013",season_number= "S03", episode_number="E02", type="Historical drama", number_of_plays=43213 )
series_3=Series(title="Vikings", year_of_publishment="2013",season_number= "S04", episode_number="E03", type="Historical drama", number_of_plays=321321 )
series_4=Series(title="Vikings", year_of_publishment="2013",season_number= "S03", episode_number="E04", type="Historical drama", number_of_plays=321213 )
series_5=Series(title="Vikings", year_of_publishment="2013",season_number= "S07", episode_number="E05", type="Historical drama", number_of_plays=4532322 )

print(movie_1)
print(series_1,series_2,series_3,series_4,series_5)


list=[series_1,series_2,series_3,series_4,series_5,movie_1]


for i in list:
    print(i)