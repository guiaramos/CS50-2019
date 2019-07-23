import cs50
import csv

from flask import Flask, jsonify, redirect, render_template, request


# Configure application
app = Flask(__name__)


# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# This application directs the user to the form page once the website is clicked on


@app.route("/", methods=["GET"])
def get_index():
    return redirect("/form")


# This loads the actual form.html page


@app.route("/form", methods=["GET"])
def get_form():
    return render_template("form.html")


@app.route("/form", methods=["POST"])
def post_form():
    if not request.form.get("firstName"):
        return render_template("error.html", message="You must state your first name.")
    if not request.form.get("lastName"):
        return render_template("error.html", message="You must state your last name.")
    if not request.form.get("career"):
        return render_template("error.html", message="You must state your career.")
    if not request.form.get("language"):
        return render_template("error.html", message="You must state your language.")
    if not request.form.get("email"):
        return render_template("error.html", message="You must provide your email address.")
    with open("survey.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow((request.form.get("firstName"), request.form.get("lastName"), request.form.get("career"),
                         request.form.get("language"), request.form.get("email")))
    return redirect("/sheet")



@app.route("/sheet")
def get_sheet():
    with open("survey.csv", "r") as file:
        reader = csv.reader(file)
        people = list(reader)
    return render_template("sheet.html", people=people)