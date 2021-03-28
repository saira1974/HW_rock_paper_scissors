from app import app
from models.game import *
from models.player import *
from flask import render_template, request

@app.route('/<hand1>/<hand2>')
def play(hand1, hand2):
    rps = game()
    player1 = Player("Player 1", hand1)
    player2 = Player("Player 2", hand2)
    winner = rps.check_win(player1, player2)
    return render_template('result.html', **locals())