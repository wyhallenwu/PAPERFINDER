from scholarly import scholarly
from connectedpapers import download_with_title


# from scholarly import ProxyGenerator
# pg = ProxyGenerator()
# pg.FreeProxies()
# scholarly.use_proxy(pg)

def search_by_name(search_name):
    # Retrieve the author's data, fill-in, and print
    print('running')
    search_query = scholarly.search_author(search_name)
    author = scholarly.fill(next(search_query))
    print(author)
    print('*' * 10)
    # Print the titles of the author's publications
    print([pub['bib']['title'] for pub in author['publications']])
    print('*' * 10)
    # Take a closer look at the first publication
    pub = scholarly.fill(author['publications'][0])
    title = pub['bib']['title']

    # download prior and derivative works
    download_with_title(title)
    print('end')


if __name__ == '__main__':
    name = input('please input author name:')
    search_by_name(name)
