class SumWeb():
    @classmethod
    def scrape_and_sum(cls, url):
        import requests
        from bs4 import BeautifulSoup
        from gensim.summarization import summarize
        from gensim.summarization import keywords
        from collections.abc import Mapping

        page = requests.get(url)
        html = page.text

        soup = BeautifulSoup(html, "html.parser")

        headline = soup.find('h1').get_text()

        print(headline)

        p_tags = soup.find_all('p')

        p_tags_text = [tag.get_text().strip() for tag in p_tags]

        sentence_list = [sentence for sentence in p_tags_text if not '\n' in sentence]

        sentence_list = [sentence for sentence in sentence_list if '.' in sentence]

        article = ''.join(sentence_list)

        article_summary = summarize(article, ratio = 0.3)

        # creating/opening a file
        f = open(headline + ".txt", "w")

        # writing in the file
        f.write(article_summary)

        # closing the file
        #f.close()