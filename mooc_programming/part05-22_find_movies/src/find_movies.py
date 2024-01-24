# Write your solution here
def find_movies(database: list, search_term: str):
    movie_list = []

    for dictionary in database:
      
        if search_term.lower() in dictionary["name"].lower():
            movie_list.append(dictionary)
           
    return movie_list
       
