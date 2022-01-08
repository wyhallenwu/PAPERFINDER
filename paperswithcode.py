import time

import requests
from bs4 import BeautifulSoup


class PaperWithCode(object):
    """Class includes methods to crawl paperswithcode.com.

    Attributes:
        SEARCH: a constant string 'https://paperswithcode.com/search'

    """
    def __init__(self):
        self.SEARCH = 'https://paperswithcode.com/search'

    def title_process(title):
        title.replace(' ', '+')
        title.replace(':', '%3')
        print('current search title is: ' + title)
        return title

    def search_by_title(title):
        payload = {'q_meta': '', 'q_type': '', 'q': title}
        response = requests.get('https://paperswithcode.com/search', params=payload)
        return response

    def page_parse(response):
        bs = BeautifulSoup(response.text, 'html.parser')
        link = bs.find(name='a', attrs={'class': 'badge badge-light'})
        print(link['href'])
        # find paper page
        next_link = 'https://paperswithcode.com' + link['href']
        response = requests.get(next_link)
        # check out
        print(response.status_code)
        print('current url: ' + response.url)
        bs = BeautifulSoup(response.text, 'html.parser')
        impl_list = bs.find(name='div', attrs={'id': 'implementations-full-list'})
        rows = impl_list.find_all(name='div', attrs={'class': 'row'})
        return rows

    def get_repo(row):
        repo_name = row.find(name='a', attrs={'class': 'code-table-link'}).text
        repo_name = ''.join(repo_name.split())
        return repo_name

    def get_star(row):
        star = row.find(name='div', attrs={'class': 'paper-impl-cell text-nowrap'}).text
        star = ''.join(star.split()).replace(',', '')
        return int(star)

    def get_row_info(rows):
        all_info = []
        for row in rows:
            repo_name = PaperWithCode.get_repo(row)
            star = PaperWithCode.get_star(row)
            info = {'repo name': repo_name, 'star': star}
            all_info.append(info)
        return all_info

    def add_txt(rows, title, filename):
        code_impl = PaperWithCode.get_row_info(rows)
        with open(filename, 'a+') as f:
            f.write(title + '  Time: ' + time.asctime(time.localtime()) + '\n' + '-' * 50 + '\n')
            for i in code_impl:
                f.write(str(i))
                f.write('\n')
            f.write('\n')

    def process_pipeline(title, download_file='./dataset/result.txt'):
        print('starting processing...')
        title = PaperWithCode.title_process(title)
        response = PaperWithCode.search_by_title(title)
        rows = PaperWithCode.page_parse(response)
        PaperWithCode.add_txt(rows, title, download_file)
        print('ending processing...')

    # TODO(2022-01-07): get tools
    def get_tools(rows):
        pass

    # TODO(2021-01-08): get repo link
    def get_repo_link(row):
        pass


if __name__ == '__main__':
    title = input('please input title: ')
    PaperWithCode.process_pipeline(title)
