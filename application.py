import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():
    return render_template("VisitMysore.html")

@app.route("/history")
def history():
    return render_template("history.html")

@app.route("/opportunities")
def opportunities():
    return render_template("opportunities.html")

@app.route("/attractions")
def attractions():
    return render_template("attractions.html")

@app.route("/temples")
def temples():
    return render_template("temples.html")

@app.route("/parks")
def markets():
    return render_template("parks.html")

@app.route("/hotels")
def accmd():
    return render_template("hotels.html")

@app.route("/placestovisit")
def ptv():
    return render_template("ptv.html")

@app.route("/joinus")
def volunteer():
    return render_template("joinus.html")

@app.route("/thanks")
def thanks():
    return render_template("thanks.html")

@app.route("/prevention")
def prevention():
    return render_template("prevention.html")