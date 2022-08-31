
from turtle import title

from operator import attrgetter


class Movie():
    
    def __init__(self, title, year_of_publishment, type, number_of_plays):
        self.title = title
        self.year_of_publishment = year_of_publishment
        self.type = type
        self.number_of_plays = number_of_plays

    def __str__(self):
        return f'{self.title} ({self.year_of_publishment})' 
    
    def __repr__(self): 
        return f'Title = {self.title} Year_of_publishment = {self.year_of_publishment}'     

    def play(self):
        return self.title + 1  



class Series(Movie):

    def __init__(self, episode_number, season_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_number = episode_number
        self.season_number = season_number

    def __str__(self):
        return f'{self.title} {self.season_number}{self.episode_number}'
    def __repr__(self): 
        return f'Title = {self.title} Year_of_publishment = {self.year_of_publishment}'      


    

movie_1=Movie(title="Pulp Fiction", year_of_publishment="1994", type="Thriller", number_of_plays=173901)
movie_2=Movie(title="Gladiator", year_of_publishment="2000", type="Historical drama", number_of_plays=2781221)
movie_3=Movie(title="Forrest Gump", year_of_publishment="1994", type="Drama/Comedy", number_of_plays=2712671)
movie_4=Movie(title="Avatar", year_of_publishment="2009", type="2009", number_of_plays=16128111)
movie_5=Movie(title="Matrix", year_of_publishment="1994", type="Sci-Fi", number_of_plays=12032122)
series_1=Series(title="Vikings", year_of_publishment="2013", season_number= "S01", episode_number="E01", type="Historical drama", number_of_plays=5621231 )
series_2=Series(title="Vikings", year_of_publishment="2013", season_number= "S03", episode_number="E02", type="Historical drama", number_of_plays=43213 )
series_3=Series(title="Vikings", year_of_publishment="2013", season_number= "S04", episode_number="E03", type="Historical drama", number_of_plays=321321 )
series_4=Series(title="Vikings", year_of_publishment="2013", season_number= "S03", episode_number="E04", type="Historical drama", number_of_plays=321213 )
series_5=Series(title="Vikings", year_of_publishment="2013", season_number= "S07", episode_number="E05", type="Historical drama", number_of_plays=4532322 )



list=[series_1,series_2,series_3,series_4,series_5,movie_1,movie_2,movie_3,movie_4,movie_5]


#result = sorted(list, key=lambda views: views.number_of_plays) # sortowanie na podstawie liczby wyświetleń

#result = filter(lambda item: item[1] == series_1, list)

#result = sorted(list, key=attrgetter(title) )

def e_sort(emp):
    return emp.title

result = sorted(list, key=lambda e: e.title )  

print(result)

#for i in list:
 #   print(i)

#def get_movies(arg):

    #result=[]

    #for i in arg:
     #   if i == "Vikings":
      #      result.append(i)

    #return result       


#def search(list, str):
        
    

#search(list, "Avatar (2009)")
    

#print(get_movies(list))   