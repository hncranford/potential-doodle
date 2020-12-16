from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd

def init_browser():
    executable_path = {"executable_path":"/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless = False)  

def scrape():
    browser = init_browser()
    mars_dictionary = {}

    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    html = browser.html
    Soup = BeautifulSoup(html, "html.parser")
    slide = Soup.select_one("ul.item_list li.slide")
    title = slide.find('div', class_='content_title').get_text()
    news_p = Soup.find('div', class_='article_teaser_body').get_text()
    
    mars_dictionary["title"] = title
    mars_dictionary["news_p"] = news_p
    
    featured_image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(featured_image_url)
    hmtl_img = browser.html
    soup = BeautifulSoup(hmtl_img, "html.parser")
    image_url  = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]
    main_url = "https://www.jpl.nasa.gov"
    image_url = main_url + image_url

    mars_dictionary["image_url"]= image_url

    url = "https://space-facts.com/mars/"
    browser.visit(url)
    tables = pd.read_html(url)
    df = tables[0]
    df = df.rename(columns={0:"Description",1:"Values"})
    newdf = df.set_index(["Description"])
    tabledf= newdf.to_html(index = True, header =True)

    mars_dictionary["tabledf"]=tabledf


    hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemispheres_url)
    html_hemispheres = browser.html
    Soup = BeautifulSoup(html_hemispheres, 'html.parser')
    items = Soup.find_all('div', class_='item')
    hemisphere_image_urls =[]
    hemisphere_main_url = "https://astrogeology.usgs.gov/"
    for item in items:
        title2 = item.find('h3').text
        image_url = item.find("a")["href"]
        browser.visit(hemisphere_main_url + image_url)
        image_html = browser.html
        Soup = BeautifulSoup(image_html, 'html.parser')
        downloads = Soup.find("div", class_="downloads")
        image_url = downloads.find("a")["href"]
        hemisphere_image_urls.append({"Title": title2, "Image_URL": image_url})

    mars_dictionary["image_url"]=image_url
    mars_dictionary["Title"] = title2






    return mars_dictionary
