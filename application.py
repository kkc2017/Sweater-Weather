from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp

from helpers import geo

# global variables
gender = None
latitude = None
longitude = None
val = None
temp_str = None
weather_str = None
noClothes = []

# Configure application
app = Flask(__name__)

# Ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///final.db")


@app.route("/", methods=["GET", "POST"])
# home page: user selects preference for male clothing or female clothing
def index():
    if request.method == "POST":
        global gender
        # verify that either "male clothing" or "female clothing" is selected; if neither is selected, the home page refreshes
        if "gender" in request.form:
            gender = request.form['gender']
            # go to next page: temperature/weather page
            return redirect("/temp")
    return render_template("index.html")


@app.route("/temp", methods=["GET", "POST"])
# temperature/weather page: gives temperature and weather data for your current location
def temp():
    # determine whether the weather from the table "temp_weather" should be snow, rain, or sunny, based on the current weather
    global weather_str
    global val
    if 'Snow' in val['weather'] or 'Ice' in val['weather'] or 'Hail' in val['weather']:
        weather_str = "snow"
    elif 'Rain' in val['weather'] or 'Thunderstorm' in val['weather'] or 'Drizzle' in val['weather']:
        weather_str = "rain"
    else:
        weather_str = "sunny"

    # determine what the temperature range from the table "temp_weather" should be, based on the current temperature
    global temp_str
    if val['temp_f'] > 80:
        temp_str = ">80"
    elif val['temp_f'] <= 80 and val['temp_f'] >= 60:
        temp_str = "60-80"
    elif val['temp_f'] <= 59 and val['temp_f'] >= 40:
        temp_str = "40-59"
    elif val['temp_f'] < 40 and weather_str == "snow":
        temp_str = "<40"
    elif val['temp_f'] <= 39 and val['temp_f'] >= 20:
        temp_str = "20-39"
    elif val['temp_f'] < 20:
        temp_str = "<20"

    clothes = db.execute("SELECT Clothing FROM temp_weather WHERE Temperature_Range_F = :temp_str AND Weather = :weather_str",
                         temp_str=temp_str, weather_str=weather_str)
    if request.method == "POST":
        # noClothes: array of clothes you don't have/want to buy
        global noClothes
        # set noClothes to empty list
        noClothes = []

        # check which checkboxes have been checked and add those clothes to noClothes
        if 'clothes1' in request.form:
            noClothes.append(clothes[0]['Clothing'])
        if 'clothes2' in request.form:
            noClothes.append(clothes[1]['Clothing'])
        if 'clothes3' in request.form:
            noClothes.append(clothes[2]['Clothing'])
        if 'clothes4' in request.form:
            noClothes.append(clothes[3]['Clothing'])

        # if no clothes are checked off, return to home page
        if noClothes == []:
            return redirect("/")

        # go to next page: links page
        return redirect("/links")
    return render_template("temp.html", temp=val['temperature_string'], weather=val['weather'],
                           precipitation=val['precip_today_string'], city_state=val['display_location']['full'],
                           country=val['display_location']['country'], observation_time=val['observation_time'],
                           clothes=clothes)


@app.route("/links", methods=["GET", "POST"])
# links page: tells user what clothes that do not have/need to buy and gives the shopping links (Amazon) to those clothes
def links():
    global noClothes
    global gender
    for i in range(len(noClothes)):
        links = db.execute("SELECT Link FROM clothing WHERE Gender = :gender AND Clothing IN (:noClothes)",
                           gender=gender, noClothes=noClothes)
    # if "Return to Home Page" button is clicked, return to home page
    if request.method == "POST":
        return redirect("/")
    return render_template("links.html", links=links, noClothes=noClothes, length=len(noClothes))


@app.route("/location", methods=["POST"])
# get the latitude and longitude of your location, then insert that information into the weather API
def location():
    global val
    # get the latitude and longitude of your current location
    latitude = request.form.get('latitude')
    longitude = request.form.get('longitude')

    # insert latitude and longitude information into weather API
    val = geo(latitude, longitude)
    return ("", 204)
