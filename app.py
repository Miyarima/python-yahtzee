#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
This is the main file of the application
"""
import os
import re
import traceback
from flask import Flask, render_template, request, redirect, url_for, session
from src.hand import Hand
from src.scoreboard import Scoreboard
from src.rules import Ones, Twos, Threes, Fours, Fives, Sixes
from src.rules import ThreeOfAKind, FourOfAKind, FullHouse
from src.rules import SmallStraight, LargeStraight, Yahtzee, Chance
from src.leaderboard import Leaderboard
from src.unorderedlist import UnorderedList
from src.sort import recursive_insertion
from src.queue import Queue

app = Flask(__name__)
app.secret_key = re.sub(r"[^a-z\d]", "", os.path.realpath(__file__))

@app.route("/")
def main():
    """ Main route """
    return render_template("index.html")

@app.route("/init", methods=["POST"])
def init():
    """ Intialize values needed in session """
    hand = Hand()
    que = Queue()
    players = int(request.form.get("players"))
    for i in range(players):
        hand = Hand()
        que.enqueue([hand.to_list(), {}, f"Player {i+1}"])
    print(que.to_list())
    session["scoreboard"] = {}
    session["rerolls"] = 2
    session["players"] = que.to_list()
    return redirect(url_for('yahtzee'))

@app.route("/yahtzee", methods=["GET"])
def yahtzee():
    """
    This route is for the index page, where five random dices will be shown
    """
    hand = Hand(session["players"][0][0])
    sb = Scoreboard().from_dict(session["players"][0][1])

    rules = [
        Ones(), Twos(), Threes(), Fours(), Fives(), Sixes(),
        ThreeOfAKind(), FourOfAKind(), FullHouse(), SmallStraight(),
        LargeStraight(), Yahtzee(), Chance()
    ]

    points = [rule.points(hand) for rule in rules]
    names = [n.name for n in rules]

    if sb.finished() and len(session["players"][-1][1]) == 13:
        max_points = 0
        winning_player = ""
        player_and_score = []
        for i in range(len(session["players"])):
            sb = Scoreboard().from_dict(session["players"][i][1])
            player_and_score.append([session["players"][i][2], sb.get_total_points()])
            if sb.get_total_points() > max_points:
                max_points = sb.get_total_points()
                winning_player = session["players"][i][2]
        return render_template(
            "winner.html",
            title="Fem Tärningar",
            max_points=max_points,
            winning_player=winning_player,
            players=player_and_score
        )

    used_rules = sb.get_used_rules().keys()
    rerolls = session["rerolls"]
    return render_template(
        "yahtzee.html",
        title="Fem Tärningar",
        hand=hand,
        used_rules=used_rules,
        points=points,
        names=names,
        sb=sb,
        rerolls=rerolls,
        player=session["players"][0][2]
    )

@app.route("/game-choice", methods=["POST"])
def game_choice():
    """
    Extracting the selected value
    """

    if request.form.get("value") is not None:
        data = str(request.form.get("value"))
        sb = Scoreboard().from_dict(session["players"][0][1])
        sb.add_points(data, Hand(session["players"][0][0]))
        session["players"][0][1] = sb.get_used_rules()
        hand = Hand()
        session["players"][0][0] = hand.to_list()
        que = Queue()
        for player in session["players"]:
            que.enqueue(player)
        player = que.peek()
        que.dequeue()
        que.enqueue(player)
        session["players"] = que.to_list()
        session["rerolls"] = 2
    elif request.form is not None and session["rerolls"] > 0:
        data = request.form
        dies_to_reroll = []
        for d in data:
            dies_to_reroll.append(int(d))
        hand = Hand(session["players"][0][0])
        session["players"][0][0] = hand.roll(dies_to_reroll).to_list()
        session["rerolls"] -= 1
    return redirect(url_for('yahtzee'))

@app.route("/leaderboard", methods=["GET"])
def show_leaderboard():
    """
    This route is for the leaderboard
    """

    lb = Leaderboard().load("scores.txt")
    ul = UnorderedList()
    lb_list = []
    # retrieve the score and name pair
    for i in range(lb.entries.size()):
        name = lb.entries.get(i).replace(",", "").split(" ")
        name.append(lb.entries.get(i))
        lb_list.append(name)
    # retriving the scores
    for score in lb_list:
        ul.append(int(score[1]))
    # sorting the scores
    recursive_insertion(ul)
    sorted_list = []
    # matching the sorted scores with the score and name pairs
    for i in range(lb.entries.size()):
        for pair in lb_list:
            if ul.get(i) == int(pair[1]):
                sorted_list.append(pair)
    return render_template(
        "leaderboard.html",
        title="Topplista",
        lb=lb,
        lb_list=sorted_list
    )

@app.route("/leaderboard-remove", methods=["POST"])
def leaderboard_remove():
    """
    Extracting the selected value and update the leaderboard
    """
    lb = Leaderboard().load("scores.txt")
    data = str(request.form.get("value"))
    lb.remove_entry(lb.entries.index_of(data))
    lb.save("scores.txt")
    return redirect(url_for('show_leaderboard'))

@app.route("/leaderboard-add", methods=["POST"])
def leaderboard_add():
    """
    Extracting the selected value and update the leaderboard
    """
    lb = Leaderboard().load("scores.txt")
    name = str(request.form.get("name")).replace(" ", "_")
    points = str(request.form.get("points"))
    lb.add_entry(name, points)
    lb.save("scores.txt")
    return redirect(url_for('show_leaderboard'))

@app.route("/about")
def show_about():
    """
    This route is for the about page
    """
    return render_template("about.html", title="Om")

@app.route("/reset")
def reset():
    """
    Route for reset session
    """
    _ = [session.pop(key) for key in list(session.keys())]

    return redirect(url_for('main'))

@app.errorhandler(404)
def page_not_found(e):
    """
    Handler for page not found 404
    """
    #pylint: disable=unused-argument
    return "Flask 404 here, but not the page you requested."


@app.errorhandler(500)
def internal_server_error(e):
    """
    Handler for internal server error 500
    """
    #pylint: disable=unused-argument
    return "<p>Flask 500<pre>" + traceback.format_exc()

if __name__ == "__main__":
    app.run(debug=True)
