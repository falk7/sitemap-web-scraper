from bs4 import BeautifulSoup
# from xml.etree.ElementTree import parse
from defusedxml.ElementTree import parse

# 1. scrape sitemap.xml & get all urls
def scrapeSitemap(sitemap_file):
    """
    scrapes sitemap and collects any links
    """
    et = parse(sitemap_file)
    root = et.getroot()
    # print(dir(root))
    # print(dir(root[0][0]))

    print(root.findall("./loc"))
    print(root[0][0].text)
    # for child in root:
    #     print("newCh")
    #     print(child.tag, child.attrib)


# 2. save new urls to queue - no doubles

# 3. save scraped urls to done - no doubles

# 4. scan all urls from queue for javascript and further urls 
def scrapeUrl(url):
    """
    scrapes url for js and other urls
    """
    soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
    print(soup.prettify())
    pass

if __name__ == "__main__":
    scrapeSitemap("sitemap.xml")
    # scrapeUrl("any")
    