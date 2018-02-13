The code in "layout.html" and "styles.css," which determined how the website looked
(including the design of the "Sweater Weather" logo at the top left of the page), was inspired by
Problem Set 7 (CS50 Finance)'s "layout.html" and "styles.css" code.

On the home page ("/"), the website first asks the user to allow the website to use the user's current location;
once the user clicks "allow," an HTML Geolocation API (implemented in "index.html") gets
information on the user's current position. A post request is sent to the "/location" route, which gets the
latitude and longitude of the user's location from the information on the user's current position. I then
defined a function (in "helpers.py"), geo(latitude, longitude), that takes in a latitude value and a longitude value and
inserts them into the Weather Underground API, which outputs a JSON file that lists a variety of temperature/weather
attributes of the location at the given latitude and longitude and at the current time. geo(latitude, longitude)
returns a dictionary with this information. Since def location() must return something, it just returns an empty string.

The home page's interface code (e.g. the question "Which type of clothing do you prefer to wear?") is written in "index.html."
In order to ensure that one of the radio buttons was selected (and the use of radio buttons ensures that the user
can only select one choice, either "male clothing" or "female clothing"), in "application.py", I used the if statement
"if "gender" in request.form:" (otherwise, return render_template("index.html"), or return to the home page). The gender
selected is saved in the global variable gender, which gets updated. The "Next" button takes the user to the page with route
"/temp" because of the statement "if request.method == "POST" (aka the button is clicked on): ... return redirect("/temp")".

On the temperature/weather page ("/temp"), the information on Last Updated, Location, Temperature, Weather, and Precipitation
Today all came from the Weather Underground API (and is passed into the HTML code "temp.html" using Jinja). I chose to use
checkboxes for the "Suggested Articles of Clothing" so the user could select more than one choice, de-select, and re-select
checkboxes. Once the user clicked the "Submit" button, a POST request was sent and I used "if clothes(1/2/3/4) in request.form:"
to check which boxes had been checked off. If a box was checked off, that article of clothing was added to the list noClothes
(a list of clothes that the user did not have). If no boxes were checked off, the user was returned to the home page, which
I implemented using "return redirect("/")". The articles of clothing in noClothes were passed into "temp.html" using
Jinja, so that each checkbox represented an article of clothing. I also saved the temperature and weather data
given by the Weather Underground API and used if statements to match the data to their equivalent elements in the
"Temperature_Range_F" and "Weather" fields of the "temp_weather" table in my database. Once the user clicked submit
(assuming at least one box was checked off), the user was redirected to the next page ("/links").

On the links page ("/links"), noClothes was once again passed in and printed on the web page using Jinja, so the user
can see what articles of clothing he/she selected on the previous page. The links to those articles of clothing were then
retrieved using a SELECT sql statement from the "clothing" table, and a Jinja for loop ensured that all the links (the
number of which varies, from 1-4) were printed on the links page. The <li></li> tags created the bullet point formatting, and
the <a href="url"></a> tags created the hyperlink, so the user could click on the text and go directly to the Amazon link.
If the user clicked on the "Return to Home Page" button, a POST request was sent and the user was redirected to the home page
via the code "return redirect("/")".