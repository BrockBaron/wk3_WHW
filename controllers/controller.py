from rps import app
from flask import render_template
from models.player import Player
from models.game import Game
import random


@app.route('/rps')
def index():
    return render_template('index.html', title='Home')

@app.route('/rps/<p1_choice>/<p2_choice>')
def play(p1_choice, p2_choice):
    p1 = Player('Rodrigo', p1_choice)
    p2 = Player('Miguel', p2_choice)
    play_game = Game(p1, p2)
    winner =play_game.play_rps()
    return render_template('pvp.html', winner=winner, p1=p1, p2=p2)

