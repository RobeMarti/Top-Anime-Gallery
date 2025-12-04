from app import app, db
from flask import render_template, request, redirect, url_for
from app.models import Anime, Gif
from sqlalchemy import func
import os

@app.route('/')
@app.route('/index')
def index():
    animes = Anime.query.all()
    return render_template('index.html', title='Top-Anime-Gallery', anime_list=animes)

@app.route('/add_anime', methods=['GET', 'POST'])
def add_anime():
    if request.method == 'POST':
        
        anime_title = request.form['anime_name']
        
        existing = Anime.query.filter(
            func.lower(Anime.title) == anime_title.lower()
        ).first()

        if not existing:
            anime = Anime(title=anime_title)
            db.session.add(anime)
            db.session.commit()
        else:
            anime = existing

        gif_files = request.files.getlist('gif_files')
        
        folder_name = anime_title.replace(" ", "_")
        base_path = os.path.join(app.root_path, 'static', 'public', folder_name)
        os.makedirs(base_path, exist_ok=True)

        for gif in gif_files:
            if gif.filename == "":
                continue  # file vuoto → skip
            
            # percorso sul server
            file_path = os.path.join(base_path, gif.filename)
            gif.save(file_path)

            # percorso da salvare nel DB (quello che userà HTML)
            db_path = f"public/{folder_name}/{gif.filename}"

            # creo l’entry nel database
            new_gif = Gif(path=db_path, anime_id=anime.id)
            db.session.add(new_gif)

        db.session.commit()

        return redirect(url_for('index'))

    return render_template('add_anime.html', title='Add New Anime')
