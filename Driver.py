from Listing_Page import Listing_Page

MAIN = 'https://allhay.com/listing/'
HEAD = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) \
         AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 \
         Safari/537.36'}
# allhay requires header to access the page
OUT = './1-3-2020_Scrape.txt'

def page_navigator(start_url, number_pages):
    for i in range(1, number_pages+1):
        yield '{}page/{}'.format(start_url, i)

def page_scraper(pages, headers):
    for page in pages:
        yield Listing_Page(page, headers)

# scraper driver code
with open(OUT, 'w') as o:
    for page in page_scraper(page_navigator(MAIN, 20), HEAD):
        for listing in page:
            for article in listing.articles:
                o.write(article.__str__())
