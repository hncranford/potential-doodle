# Web Scraping Homework: Mission to Mars
Complete your initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

NASA Mars News--get the latest article and paragraph from the website.
JPL Mars Space Images - Featured Image--save the featured image
Mars Facts--get the table from the website
Mars Hemispheres--get the 4 pictures and titles of each


Then, use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

-Created a route called /scrape that will import the scrape_mars.py script and call the scrape function.

-Store the return value in Mongo as a Python dictionary.

-Created a root route / that will query your Mongo database and pass the mars data into an HTML template to display the data.

-Created a template HTML file called index.html that will take the mars data dictionary and display all of the data in the appropriate HTML elements.
