class Article():


    def __init__(self, article_html):
        self.title = Article.get_title(article_html)
        self.pfl = Article.get_price_fert_location(article_html)
        self.discription = Article.get_description(article_html)

    def __str__(self):
        return '{}, {}, {}, {}, {}\n'.format(self.title, self.pfl[0],
                                             self.pfl[1], self.pfl[2],
                                             self.discription)

    def get_title(article):
        return str(article.select('h2 a')[0]).split('>')[-2][0:-3]

    def get_price_fert_location(article):
        line = str(article.find_all('div', class_='listing-details')[0])
        pfl = line.split('\n\t\t\t')[1].split('\u2002')
        p, f, l = pfl[0], pfl[2], pfl[4].split('\t')[0]
        return (p, f, l)

    def get_description(article):
        return str(article.select('div p')[0])[3:-4].replace('\n', ' ')
