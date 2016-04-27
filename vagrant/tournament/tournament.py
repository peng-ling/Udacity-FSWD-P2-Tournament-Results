#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
from contextlib import contextmanager


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


@contextmanager
def db_cursor():
"""defines the runtime context to be established when executing cursor
   operraions
"""

    db_connection = connect()
    cursor = db_connection.cursor()

    try:
        yield cursor
    except:
        raise
    finally:
        db_connection.commit()
        cursor.close()
        db_connection.close()


def deleteMatches():
    """Remove all the match records from the database."""
    with db_cursor() as db_query:
        db_query.execute("DELETE FROM Matches;")


def deletePlayers():
    """Remove all the player records from the database."""
    with db_cursor() as db_query:
        db_query.execute("DELETE FROM players;")


def countPlayers():
    """Returns the number of players currently registered."""
    with db_cursor() as db_query:
        db_query.execute("SELECT COUNT(id) FROM players;")
        numberofplayers = db_query.fetchone()[0]
    return numberofplayers


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    with db_cursor() as db_query:
        db_query.execute("INSERT INTO players (playername) VALUES (%s);",
                         ([name]))


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    with db_cursor() as db_query:
        db_query.execute("SELECT * FROM standings;")
        standings = db_query.fetchall()

    return standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    with db_cursor() as db_query:
        db_query.execute(
            "INSERT INTO Matches (winner, loser) VALUES (%s, %s)", (winner, loser))


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    pairing = []
    oponents = []

    with db_cursor() as db_query:
        db_query.execute("SELECT * FROM standings")
        standings = db_query.fetchall()

    # for a in range(0, 1):
    sortedstandings = sorted(standings, key=lambda tup: tup[2], reverse=True)

    for a in range(0, len(standings), 2):
        oponents.append([sortedstandings[a][0], sortedstandings[a][
                        1], sortedstandings[a + 1][0], sortedstandings[a + 1][1]])

    return oponents
