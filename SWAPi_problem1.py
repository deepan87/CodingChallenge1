import requests

starship_list = []
films_list = []

#definition - get json data
def get_response(url):
    json_data = requests.get(url).json()
    return json_data

#definition - get starship names
def get_starship_name(url):
    starship_result = get_response(url)
    starship_list.extend(starship_result['results'])
    if starship_result['next'] is not None:
        get_starship_name(starship_result['next'])

# definition - get film names
def get_film_names(url):
    film_result = get_response(url)
    films_list.extend(film_result['results'])
    if film_result['next'] is not None:
        print(film_result['next'])
        get_film_names(film_result['next'])

# Hyperdrive Rating
def ships_hyperdrive_rating_condition():
    starships_hyper_drive = [starships['name'] for starships in starship_list if starships['hyperdrive_rating'] != "unknown" and float(starships['hyperdrive_rating']) >= 1.0]
    return starships_hyper_drive

# Crew Condition
def ships_with_crew_condition():
    starships_crew_condition = [starships['name'] for starships in starship_list if (starships['crew'] != "unknown" and "-" not in str(starships['crew'])) and (int(starships['crew'].replace(",", "")) > 3 and int(starships['crew'].replace(",", "")) < 100)]
    return starships_crew_condition

# Return of Jedi
def ships_in_return_of_jedi():
    starships_in_return_of_jedi = [films['starships'] for films in films_list if films['title'] == 'Return of the Jedi']
    starships_return_of_jedi = [starships['name'] for starships in starship_list if starships['url'] in starships_in_return_of_jedi[0]]
    return starships_return_of_jedi

if __name__ == '__main__':
    get_starship_name("https://swapi.dev/api/starships/")
    get_film_names("https://swapi.dev/api/films/")

    print("Hyperdrive Rating result: ")
    print("Ships that have a hyperdrive rating >= 1.0 :")
    print(ships_hyperdrive_rating_condition())   # Hyperdrive Rating result

    print("Crew Condition result: ")
    print("Ships that have crews between 3 and 100 :")
    print(ships_with_crew_condition())  # Crew Condition result
    print("Return of Jedi result: ")

    print("Ships appeared in Return of the Jedi :")
    print(ships_in_return_of_jedi())   # Return of Jedi result
    
   
