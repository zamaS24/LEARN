"""énoncé: 
    Use the movies for this exercise
    Create a flask api with the following routes
        1. /upload - This route should take the movies excel file and insert all of its rows into a MYSQL database having a table with the same columns as the excel file
        2. /top-movies - This route should return the top 10 movies based on IMDB Score
        3. /movies-by-year - This route should return the movies released in the given year
        4. /movies-by-language - This route should return the movies released in the given language 
        5. /movies-by-country - This route should return the movies released in the given country 
        6. /update-movie - This route should update the User Votes for the given movie
        7. /delete-movie - This route should delete the given movie from the database

"""

from flask import Flask, redirect, url_for, request, jsonify
import mysql.connector
import pandas as pd 
from utils import get_query_create_table, insert_df2sql
import io 


app = Flask(__name__)



# init db connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="assignement_db"
)
cursor = db.cursor()


# init dataframe 
df = pd.read_excel('../movies.xls')


# creating the movies table if not already created
cursor.execute('show tables')
tablenames = [row[0] for row in cursor.fetchall()]
if 'movies' not in tablenames:
    q_create_table = get_query_create_table('movies', df)
    cursor.execute(q_create_table)



# default root route
@app.route('/') 
def hello_world():
    return '<h1>Hello to assignement 2</h1><br><h2>Pandas</h2>'


# 1 : /upload - This route should take the movies excel file and insert all of its rows into a MYSQL database having a table with the same columns as the excel file
@app.route('/upload', methods=['POST']) # POST REQUEST
def fill_table():
    
    # check if the request contains a file
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']

    # check if a file was selected (this is for filename, I don't need it)
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    try:
        # Read the Excel file into a pandas DataFrame

        # TODO: add to notes this below
        file_stream = io.BytesIO(file.read()) # this is necessary so I can work with dataframe directly 

        df = pd.read_excel(file_stream)
        insert_df2sql(db, 'movies', df)
        return jsonify({"message": "Rows added to the database successfully!"}), 200

    except Exception as e:
        return ['Error happeneed', str(e)], 404



# 2. /top-movies - This route should return the top 10 movies based on IMDB Score
@app.route('/top-movies')
def get_top_movies(): 
    query = """
        select `Title`, `IMDB SCORE`
        from movies
        order by `IMDB score`
        desc
        limit 10
    """
    cursor.execute(query)
    
    return cursor.fetchall()


# 3. /movies-by-year - This route should return the movies released in the given year
@app.route('/movies-by-year') #/movie-by-year&year=2000
def get_movies_by_year(): 

    year = int(request.args.get('year'))

    query = f"""
        select `Title`
        from movies
        where year = {year}
    """
    cursor.execute(query)
    return cursor.fetchall()


# 4. /movies-by-language - This route should return the movies released in the given language 
@app.route('/movies-by-language') 
def get_movies_by_language(): 

    language = str(request.args.get('language'))

    query = f"""
        select `Title`
        from movies
        where Language = '{language}'
    """
    cursor.execute(query)
    return cursor.fetchall()


# 5. /movies-by-country - This route should return the movies released in the given country 
@app.route('/movies-by-country') 
def get_movies_by_country(): 

    country = str(request.args.get('country'))

    query = f"""
        select Title
        from movies
        where country = '{country}'
    """
    cursor.execute(query)
    return cursor.fetchall()



# 6. /update-movie - This route should update the User Votes for the given movie
@app.route('/update-movie', methods=['PUT'])
def update_movie_user_votes(): 
    try: 
        title = str(request.form.get('title'))
        user_votes = int(request.form.get('user_votes'))

        query = f"""
            update movies
            set `User Votes` = {user_votes}
            where Title = '{title}'
        """
        cursor.execute(query)
        db.commit()

        return 'success'
    except Exception as e:
            return  str(e)



#  7. /delete-movie - This route should delete the given movie from the database
@app.route('/delete-movie', methods=['DELETE'])
def delte_movie_by_title(): 

    title = request.args.get('title')

    query = f"""
    delete 
    from movies 
    where Title = '{title}'
    """
    cursor.execute(query)
    db.commit()

    return 'success'


if __name__ == '__main__':
    app.run(debug=True) 