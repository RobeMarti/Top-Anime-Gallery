from app import app
from flask import render_template, request

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Top-Anime-Gallery')

@app.route('/add_anime', methods=['GET', 'POST'])
def add_anime():
    if request.method == 'POST':
        anime_title = request.form['anime_name']
        gif_files = request.files.getlist('gif_files')

        con = db.engine.connect()
        exist = con.execute(
            "SELECT * FROM anime WHERE title = :title",
            {"title": anime_title}
        )

        if exist == []:
            pass
        else:
            pass
    return render_template('add_anime.html', title='Add New Anime')
