import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd
import datetime

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    userId = session["user_id"]
    userStocks = db.execute(
        "SELECT symbol, SUM(shares) AS shares, price, total FROM transactions WHERE user_id = :id GROUP BY symbol", id = userId)
    userCashDb = db.execute("SELECT cash FROM users WHERE id = ?", userId)
    userCash = userCashDb[0]["cash"]

    return render_template("index.html", database=userStocks, cash=userCash)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Define variables from user input
        symbol = request.form.get("symbol")
        stock = lookup(symbol.upper())

        try:
            shares = int(request.form.get("shares"))
        except:
            return apology("Please insert a valid number of shares k")

        # Check if symbol exists
        if not symbol:
            return apology("Must give a Symbol")

        if stock == None:
            return apology("Symbol does not exist")

        # check if shares are valid
        if shares == None or shares < 0:
            return apology("Please insert a valid number of shares")

        transactionValue = shares * stock["price"]

        userId = session["user_id"]
        userCashDb = db.execute("SELECT cash FROM users WHERE id = ?", userId)
        userCash = userCashDb[0]["cash"]
        if transactionValue > userCash:
            return apology("You have insuficient founds")
        else:
            updateCash = userCash - transactionValue
            db.execute("UPDATE users SET cash = ? WHERE id = ?", updateCash, userId)

            timestamp = datetime.datetime.now()
            db.execute(
                "INSERT INTO transactions (user_id,symbol,shares,price,date,total) VALUES (?,?,?,?,?,?)",
                userId, symbol.upper(), shares, stock["price"], timestamp, transactionValue)

            flash("Stocks bought!")
            return redirect("/")
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    userId = session["user_id"]
    transactions = db.execute("SELECT * FROM transactions WHERE user_id = :id", id=userId)
    userCashDb = db.execute("SELECT cash FROM users WHERE id = ?", userId)
    userCash = userCashDb[0]["cash"]

    return render_template("history.html", transactions=transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Define varibales with user input
        username = request.form.get("username")
        password = request.form.get("password")

        # Ensure username was submitted
        if not username:
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not password:
            return apology("must provide password", 400)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], password):
            return apology("invalid username and/or password", 400)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    if request.method == "POST":
        symbol = request.form.get("symbol")

        if not symbol:
            return apology("Must give a Symbol")

        stock = lookup(symbol.upper())

        if stock == None:
            return apology("Symbol does not exist")

        return render_template("quoted.html", name=stock["name"], price=stock["price"], symbol=stock["symbol"])

    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Define variables with user input
        username = request.form.get("username")
        password = request.form.get("password")
        passwordConfirmation = request.form.get("confirmation")
        hash = generate_password_hash(password)

        # Ensure username was submitted
        if not username:
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not password:
            return apology("must provide password", 400)

        # Ensure password and confirmation are equal
        elif password != passwordConfirmation:
            return apology("Passwords do not match", 400)

        # If username is new
        try:
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash)
            userId = db.execute("SELECT id FROM users WHERE username = ?", username)
            session["user_id"] = userId
            return render_template("quote.html")

        # If username aready exist
        except:
            return apology("Username not available ", 400)

    # User reached route not via POST
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = int(request.form.get("shares"))
        stock = lookup(symbol.upper())

        # Check if symbol exists
        if not symbol:
            return apology("Must give a Symbol")

        if stock == None:
            return apology("Symbol does not exist")

        # check if shares are valid
        if shares < 0 or shares == None:
            return apology("Please insert a valid number of shares")

        transactionValue = shares * stock["price"]
        userId = session["user_id"]
        userCashDb = db.execute("SELECT cash FROM users WHERE id = ?", userId)
        userCash = userCashDb[0]["cash"]
        userSharesDb = db.execute(
            "SELECT shares FROM transactions WHERE user_id=:id AND symbol= :symbol GROUP BY symbol", id=userId, symbol=symbol)
        userShares = userSharesDb[0]["shares"]

        if shares <= userShares:
            updateCash = userCash + transactionValue
            db.execute("UPDATE users SET cash = ? WHERE id = ?", updateCash, userId)

            timestamp = datetime.datetime.now()
            db.execute(
                "INSERT INTO transactions (user_id,symbol,shares,price,date) VALUES (?,?,?,?,?)", userId, symbol.upper(), (-1)*shares, stock["price"], timestamp)
            flash("Stocks Sold!")
            return redirect("/")

        else:
            return apology("More shares than you have!")

    else:
        userId = session["user_id"]
        userSymbols = db.execute(
            "SELECT symbol FROM transactions WHERE user_id = :id GROUP BY symbol HAVING SUM (shares) > 0", id=userId)
        return render_template("sell.html", symbols=[row["symbol"] for row in userSymbols])
