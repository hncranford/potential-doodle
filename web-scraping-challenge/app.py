from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import Mars_Scrape

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/Missions_to_Mars_app"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/Missions_to_Mars_app")


@app.route("/")
def index():
    Mars_c = mongo.db.Mars_c.find_one()
    return render_template("index.html", Mars_html=Mars_c )


@app.route("/scrape")
def scraper():
    Mars_c = mongo.db.Mars_c
    Mars_data = Mars_Scrape.scrape()
    Mars_c.update({}, Mars_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
