from pprint import pprint

from dataset import randomuser_data

def get_fullname(user: dict):
    return f'{user["name"]["first"]} {user["name"]["last"]}'

def get_full_names(data: dict) -> list[str]:  #1
    """

    Returns a list of users' full names in 'First Last' format.


    Args:

        data (dict): JSON data containing user records.


    Returns:

        list[str]: List of full names.
    """

    result = []

    for user in data["results"]:

        full_name = user["name"]["first"] + " " + user["name"]["last"]

        result.append(full_name)

    return result

#get_full_names(randomuser_data) # 1

def get_users_by_country(data: dict, country_name: str) -> list[dict]:  #2
    """

    Filters and returns users who live in a specific country.


    Args:

        data (dict): JSON data containing user records.

        country (str): Country name to filter by.


    Returns:

        list[dict]: List of dictionaries containing full name and email of matching users.
    """    

    result = []
    for user in data['results']:
        if user['location']['country']  == country:
            result.append({
                'fullname': user['name']['first'] + ' ' + user['name']['last'],
                'email': user['email'],
                'country': user['location']['country']
            })
    return result

#get_users_by_country(data=randomuser_data, country_name='India') # 2

def count_users_by_gender(data: dict) -> dict:  #3
    """

    Counts the number of users by gender.


    Args:

        data (dict): JSON data containing user records.


    Returns:

        dict: Dictionary with gender as keys and count as values.
    """

    result = {'male': 0, 'female': 0}
    
    for user in data['results']:
        if user['gender'] == 'male':
            result['male'] += 1
        elif user['gender'] == 'female':
            result['female'] += 1
            

    return result

# count_users_by_gender(randomuser_data) # 3

def get_emails_of_older_than(data: dict, age: int) -> list[str]:   #4
    """

    Returns a list of emails of users older than the given age.


    Args:

        data (dict): JSON data containing user records.

        age (int): Age threshold.


    Returns:

        list[str]: List of email addresses.
    """
    result = []
    for user in data['results']:
        if user['dob']['age']  > age:
            result.append({
                'full_age': user['dob']['age'],
                'email': user['email']
            })
    return result

    
# get_emails_of_older_than(data=randomuser_data, age=60) # 4

def sort_users_by_age(data: dict, descending: bool = False) -> list[dict]:   #5
    """

    Sorts users by age in ascending or descending order.


    Args:

        data (dict): JSON data containing user records.

        descending (bool, optional): Whether to sort in descending order. Defaults to False.


    Returns:

        list[dict]: List of users with name and age sorted accordingly.
    """

    result1 = sorted(data['results'], key=lambda x: x['dob']['age'], reverse=descending)
    result2 = map(
        lambda x: {'fullname': get_fullname(x), 'age': x['dob']['age']},
        result1
    )
    return list(result2)

# pprint(sort_users_by_age(randomuser_data)) #5

def get_usernames_starting_with(data: dict, letter: str) -> list[str]:   #6

    """

    Returns a list of usernames starting with a given letter.


    Args:

        data (dict): JSON data containing user records.

        letter (str): The starting letter to filter usernames.


    Returns:

        list[str]: List of matching usernames.
    """

    filt_data = filter(
        lambda user: user['login']['username'].startswith(letter),
        data['results']
    )
    result = map(
        lambda user: user['login']['username'],
        filt_data
    )

    return list(result)

# pprint(get_usernames_starting_with(randomuser_data, "g"))  # 6

def get_average_age(data: dict) -> float:   #7
    """

    Calculates and returns the average age of users.


    Args:

        data (dict): JSON data containing user records.


    Returns:

        float: Average age.
    """
    total_age = sum(map(
        lambda user: user['dob']['age'],
        data['results']
    ))
    n = len(data['results'])
        
    return total_age / n

# pprint(get_average_age(randomuser_data)) # 7

def group_users_by_nationality(data: dict) -> dict:   #8
    """

    Groups and counts users by their nationality.


    Args:

        data (dict): JSON data containing user records.


    Returns:

        dict: Dictionary with nationality as keys and count as values.
    """
    group = {}
    for user in data['results']:
        group.setdefault(user['nat'], 0)

        group[user['nat']] += 1

    return group

# pprint(group_users_by_nationality(randomuser_data)) # 8

def get_all_coordinates(data: dict) -> list[tuple[str, str]]:   #9
    """

    Extracts all users' coordinates as tuples of (latitude, longitude).


    Args:

        data (dict): JSON data containing user records.


    Returns:

        list[tuple[str, str]]: List of coordinate tuples.
    # """
    return [(user['location']['coordinates']['latitude'], user['location']['coordinates']['longitude']) for user in data['results']]

# pprint(get_all_coordinates(randomuser_data)) # 9

def get_oldest_user(data: dict) -> dict:  #10
    """

    Finds and returns the oldest user's name, age, and email.


    Args:

        data (dict): JSON data containing user records.


    Returns:

        dict: Dictionary containing 'name', 'age', and 'email' of the oldest user.
    """

    result = max(
    data['results'], key=lambda user: user['dob']['age']
    )
    return {
        'name': get_fullname(result),
        'age': result['dob']['age'],
        'email': result['email']
    }


# pprint(get_oldest_user(randomuser_data)) # 10

def find_users_in_timezone(data: dict, offset: str) -> list[dict]:   #11
    """

    Returns users whose timezone offset matches the given value.


    Args:

        data (dict): JSON data containing user records.

        offset (str): Timezone offset (e.g. '+5:30').


    Returns:

        list[dict]: List of users with full name and city.
    """
    return list(map(
        lambda user: {"name": get_fullname(user), "city": user['location']['city']},
        filter(
            lambda user: user['location']['timezone']['offset'] == offset,
            data['results']
        )
    ))


# pprint(find_users_in_timezone(randomuser_data, '+5:30')) # 11

def get_registered_before_year(data: dict, year: int) -> list[dict]:  #12
    """

    Returns users who registered before a given year.


    Args:

        data (dict): JSON data containing user records.

        year (int): Year threshold.


    Returns:

        list[dict]: List of users with full name and registration date.
    """
    return list(map(
        lambda user: {'name': get_fullname(user),'city': user['registered']['date']},
        filter(
            lambda user: user['registered']['date'] == date,
            data['results']
        )
    ))
    # return list(result_filt)

pprint(get_registered_before_year(randomuser_data, 2010)) # 12