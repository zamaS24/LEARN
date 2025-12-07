import requests

HOST = "http://localhost:5000"

# 1. uploading a excel file  to aliment the BDD
url = "http://localhost:5000/upload"
file_path = '../movies.xls'
with open(file_path, "rb") as file: 

    print('file opened successfuly ...')
    files = {"file":("data.xlsx", file, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")}

    print('making post request now ... ')
    response = requests.post(url, files=files)

    print('response : ', response.text)



# 2. /top-movies - This route should return the top 10 movies based on IMDB Score
url = HOST + "/top-movies"
response = requests.get(url)
print(response.text)


# 3. /movies-by-year
url = HOST +'/movies-by-year?' +'year=1997'
response = requests.get(url)
print(response.text)


# 4. /movies-by-language - This route should return the movies released in the given language 
url = HOST +'/movies-by-language?' +'language=German'
response = requests.get(url)
print(response.text)


# 5. /movies-by-country - This route should return the movies released in the given country 
url = HOST +'/movies-by-country?' +'country=France'
response = requests.get(url)
print(response.text)


# 6. /update-movie - This route should update the User Votes for the given movie
url = HOST +'/update-movie'
data = {
    'title': 'The Train',
    'user_votes': 10120
}
response = requests.put(url, data=data)
print(response.text)


#  7. /delete-movie - This route should delete the given movie from the database
url = HOST +'/delete-movie?' + 'title=The Train'  
response = requests.delete(url)
print(response.text)

