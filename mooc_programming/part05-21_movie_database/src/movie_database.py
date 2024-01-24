# Write your solution here
def add_movie(database: list, name: str, director: str, year: int, runtime: int):

    entry = {}
    entry["name"] = name
    entry["director"] = director
    entry["year"] = year
    entry["runtime"] = runtime

    database.append(entry)

