#%%
from splinter import Browser
from bs4 import BeautifulSoup
import requests
import pandas as pd

#%%
#NASA Mars News
def Mars_News():
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.find('div', class_="content_title")
    title = results.text.strip()
    results = soup.find('div', class_="rollover_description_inner").text
    return title, results

#%%
#NASA Images 
def Mars_Image():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://www.jpl.nasa.gov/spaceimages/details.php?id=PIA02570'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    result = soup.find('figure', class_='lede')
    image = result.a['href']
    image_url = f"https://www.jpl.nasa.gov{image}"
    return image_url

#%%
#Mars Facts
def Mars_Facts():
    url = "https://space-facts.com/mars/"
    tables = pd.read_html(url)
    Mars_Fact_df = tables[1]
    Mars_Fact_HTML = Mars_Fact_df.to_html('Mars_Fact_HTML.html', classes = "html_table")    

#%%
#Mars Hemisphere
def Mars_Hemisphere_Cerberus():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    html = browser.html
    #soup = BeautifulSoup(html, 'html.parser')
    
    url_1 = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
    browser.visit(url_1)
    title_1 = browser.find_by_css('h2.title').text
    image_1 = browser.find_by_css('img.wide-image')['src']
    return title_1, image_1

#%%
def Mars_Hemisphere_Schiaperlli():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    url_2 = "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"
    browser.visit(url_2)
    title_2 = browser.find_by_css('h2.title').text
    image_2 = browser.find_by_css('img.wide-image')['src']
    return title_2, image_2

#%%    
def Mars_Hemisphere_Syrtis_Major():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    url_3 = "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"
    browser.visit(url_3)
    title_3 = browser.find_by_css('h2.title').text
    image_3 = browser.find_by_css('img.wide-image')['src']
    return title_3, image_3

#%%
def Mars_Hemisphere_Valles_Marineris():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    
    url_4 = "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"
    browser.visit(url_4)
    title_4 = browser.find_by_css('h2.title').text
    image_4 = browser.find_by_css('img.wide-image')['src']
    return title_4, image_4

#%%
def Mars_Hemisphere():  
    hemisphere_image_urls = [
            {"title": "title_4", "img_url":"Image_4"},
            {"title": "title_1", "img_url":"Image_1"},
            {"title": "title_2", "img_url":"Image_2"},
            {"title": "title_3", "img_url":"Image_3"}]
    return hemisphere_image_urls

#%%
def Scrape():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    title, results = Mars_News()
    image_url = Mars_Image()
    Mars_Facts_HTML = Mars_Facts()
    data = {
            "newstitle": title,
            "newstext": results,
            "featured_image":image_url,
            "facts":Mars_Facts_HTML
            }
    browser.quit()
    return data
#%%
def Scrape2():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    title_1, image_1 = Mars_Hemisphere_Cerberus()
    title_2, image_2 = Mars_Hemisphere_Schiaperlli()
    title_3, image_3 = Mars_Hemisphere_Syrtis_Major()
    title_4, image_4 = Mars_Hemisphere_Valles_Marineris()
    data = {
            "cerberus_title": title_1,
            "cerberus_image": image_1,
            "schiaperlli_title":title_2,
            "schiaperlli_image":image_2,
            "syrtis_major_title":title_3,
            "syrtis_major_image":image_3,
            "valles_marineris_title":title_4,
            "valles_marineris_image":image_4
            }
    browser.quit()
    return data
#%%
if __name__ == "__main__":
    print(Scrape2())
    
    
    