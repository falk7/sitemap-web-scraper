from bs4 import BeautifulSoup
import re
import requests

# 1. scrape sitemap.xml & get all urls
def scrape_sitemap():
    """
    scrapes sitemap and collects any links
    """

    string = '''
    <?xml version="1.0" encoding="UTF-8"?> 
    <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
        <url> 
        <loc>https://www.example.com/examplea</loc> 
        <priority>0.5</priority> 
        <lastmod>2019-03-14</lastmod> 
        <changefreq>daily</changefreq> 
    </url> 
    <url> 
        <loc>https://www.example.com/exampleb</loc> 
        <priority>0.5</priority> 
        <lastmod>2019-03-14</lastmod> 
        <changefreq>daily</changefreq> 
    </url> 
    </urlset>
    '''

    pattern = '(?<=<loc>)[a-zA-z]+://[^\s]*(?=</loc>)'

    return re.findall(pattern,string)


# 2. save new urls to queue - no doubles

# 3. save scraped urls to done - no doubles

# 4. scan all urls from queue for javascript and further urls 
def scrape_url(url):
    """
    scrapes url for js and other urls
    """
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    scraped_urls.append(url)


if __name__ == "__main__":

    ### funktionen funktional implementieren?!?!
    urls_queue = scrape_sitemap()
    scraped_urls = []

    while len(urls_queue) > 0:
        scrape_url(urls_queue.pop())
    
    print(scraped_urls)