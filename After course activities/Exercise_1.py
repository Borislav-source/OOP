def check_imdb_score_of_a_movie(movie):
    if movie['imdb'] >= 5.5:
        return True
    return False


def sublist_movies_high_score(sequence):
    inner_list = []
    for movie in sequence:
        if movie['imdb'] >= 5.5:
            inner_list.append(movie)
    return inner_list


def sort_by_category(sequence, category):
    inner_list = []
    for movie in sequence:
        if movie['category'] == category:
            inner_list.append(movie)
    return inner_list


def compute_the_average_score(sequence):
    result = 0
    for movie in sequence:
        result += movie['imdb']
    result /= len(sequence)
    return result


def compute_the_average_score_by_category(sequence, category):
    inner_list = sort_by_category(sequence, category)
    result = compute_the_average_score(inner_list)
    return result


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

print(check_imdb_score_of_a_movie({
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
}))

print(sublist_movies_high_score(movies))

print(sort_by_category(movies, 'Thriller'))
print(compute_the_average_score(movies))
print(compute_the_average_score_by_category(movies, 'Thriller'))