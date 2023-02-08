# Dictionary of movies

movies = [
{
"name": "Usual Suspects",
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
#Write a function that takes a single movie and returns True if its IMDB score is above 5.5
"""def scorecheck(movie):
    for n in movies:
        if n["imdb"]>5.5:
            return True
        else:
            return False"""
#Write a function that returns a sublist of movies with an IMDB score above 5.5.
"""def movies55score(movies):
    movies55score = []
    for n in movies:
        if n["imdb"]>5.5:
            movies55score.append(n["name"])
    return movies55score
movies55score(movies)"""
#Write a function that takes a category name and returns just those movies under that category.
"""def mcategory(category):
    mcategory = []
    for n in movies:
        if n["category"] == category:
            mcategory.append(n["name"])
    return mcategory
moviescat = mcategory(str(input('Enter movie category: ')))
print(moviescat)"""
#Write a function that takes a list of movies and computes the average IMDB score.
"""def avgscore(movielist):
    scores = []
    for n in movielist:
        score = n["imdb"]
        scores.append(score)
    averagescore = sum(scores)/len(scores)
    return averagescore
average = avgscore(movies)
print(average)"""
#Write a function that takes a category and computes the average IMDB score.
def avgscore(category):
    scores = []
    for n in movies:
        if n["category"] == category:
            scores.append(n["imdb"])
    averagescore = sum(scores)/len(scores)
    return averagescore
average=avgscore(str(input('Enter movie category: ')))
print('Average score in that category is', average)