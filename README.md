The website "Sweater Weather" should be used to find out the temperature and weather conditions of the
user's current location at the current time. The clothing recommendations given are based on the current
temperature and weather; they are targeted at a user who is about to go outside and needs to figure out what
would be appropriate to wear. For example, if it is not raining now but will rain later, the website
will not recommend that you either bring an umbrella or wear a rain jacket, since it is not currently raining,
so rain attire would not be appropriate at the current time. The information "Precipitation Today" is merely
for the user's benefit, in order to give the user a heads up about whether today has been a rainy day;
it does not factor into the clothing recommendations given.

Note: In order for the website to load, Flask must be running (type "flask run" into the terminal, then hit enter).
The user first goes to the home page, which is https://ide50-karenchen.cs50.io:8080/. The browser then states,
"The website “https://ide50-karenchen.cs50.io:8080” would like to use your current location," to which the
user must allow the website to use his/her current location by clicking "allow". Then, at the
home page, the user selects what gender clothing he/she
prefers. If the user does not select any gender clothing, the home page will be refreshed. Then, the user
clicks the "Next" button to go to the next page (temperature/weather data page). At this page, the user
will be able to view his/her current location, the amount of precipitation in that location today, and the
temperature and weather condition of that current location. The checkboxes for "Suggested Articles of Clothing"
pertain to the four articles of clothing in the "Clothing" field of the "temp_weather" table that
have the same temperature range and weather as the current location's temperature range and weather condition.
The user can then check off all the articles of clothing that they do not have and would like to buy.
The user can also un-check and re-check the boxes if he/she makes a mistake when checking off clothing.
If the user does not check off any boxes, the user is brought back to the home page after clicking the "Submit" button.
If the user does check off anywhere between one and four boxes, when
the user presses the "Submit" button, the user is directed to the next page (the links page), where the
Amazon links (either the male or female version of the clothes, depending on what preference the user selected
on the home page) to all the articles of clothing that the user checked off are listed. The links page lists
the articles of clothing that the user wants to buy, and then lists the Amazon shopping links to those articles
of clothing. Finally, the user can click the "Return to home page" button to return to the home page (and
re-select preferred gender type of clothing). At any time that the user wants to return to the home page,
the user can click on the "Sweater Weather" logo at the top left of the web page, which will take the user
back to the home page.

If the time under "Last Updated on..." (given on the temperature/weather web page, which is the second
web page that the user visits) does not update, the user should go back to the home page and try again
(this should only take a few tries of going back to the home page, selecting "male clothing" or
"female clothing", then clicking the "Next" button) until the time, location, and weather information updates.