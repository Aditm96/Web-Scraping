# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:23:22 2020

@author: aditm
"""
#%%
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
#%%
app = Flask(__name__)

#%%
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

#%%
@app.route("/")
def index():
    mars_db = mongo.db.mars_db.find_one()
    return render_template("index.html", mars_db=mars_db)
#%%
@app.route("/scrape")
def scrapper():
    mars_db = mongo.db.mars_db
    mars_data = scrape_mars.Scrape()
    mars_db.update({}, mars_data, upsert=True)
    return "Scraping Successful"
#%%
 #%%
@app.route("/index")
def index2():
    mars = mongo.db.mars.update_one()
    return render_template("index.html", mars = mars)
#%%
@app.route("/scrape2")
def scrapper2():
    mars = mongo.db.mars
    mars_data2 = scrape_mars.Scrape2()
    mars.update({}, mars_data2, upsert=True)
    return "Scraping Successful"
   
#%%
if __name__ == "__main__":
    app.run(debug=True)
