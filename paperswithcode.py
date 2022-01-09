import os
import time
import json

import requests
from bs4 import BeautifulSoup


class PaperWithCode(object):
    """Class includes methods to crawl paperswithcode.com.

    Attributes:
        BaseLink: a constant string 'https://paperswithcode.com/search'

    """

    def __init__(self):
        self.BaseLink = 'https://paperswithcode.com/search'

    def title_process(self, title):
        # replace special symbols for searching
        title.replace(' ', '+')
        title.replace(':', '%3')
        # print('current search title is: ' + title)
        return title

    def search_by_title(self, title):
        # construct payload
        payload = {'q_meta': '', 'q_type': '', 'q': title}
        response = requests.get(self.BaseLink, params=payload)
        return response

    def page_parse(self, response):
        bs = BeautifulSoup(response.text, 'html.parser')
        # get paper page link
        partial_link = bs.find(name='a', attrs={'class': 'badge badge-light'})
        print(partial_link['href'])
        # find paper page
        paper_link = 'https://paperswithcode.com' + partial_link['href']
        response = requests.get(paper_link)
        # check status
        assert response.status_code == 200
        # print(response.status_code)
        print('current url: ' + response.url)
        # parse page
        bs = BeautifulSoup(response.text, 'html.parser')
        impl_list = bs.find(name='div', attrs={'id': 'implementations-short-list'})
        rows = impl_list.find_all(name='div', attrs={'class': 'row'})
        return rows

    def get_repo(self, row):
        """get repo name of a single row."""
        repo_name = row.find(name='a', attrs={'class': 'code-table-link'}).text
        repo_name = ''.join(repo_name.split())
        return repo_name

    def get_star(self, row):
        """get stars of a single row."""
        star = row.find(name='div', attrs={'class': 'paper-impl-cell text-nowrap'}).text
        star = ''.join(star.split()).replace(',', '')
        return int(star)

    def get_tools(self, row):
        tool_img = row.find(name='img')
        if tool_img is not None:
            src = tool_img['src']
            # only care about pytorch and tensorflow
            if 'pytorch' in str(src):
                return 'pytorch'
            elif 'data:image' in str(src):
                return 'tensorflow'
        else:
            return 'unknown'

    def get_repo_link(self, row):
        repo_link = row.find(name='a', attrs={'class': 'code-table-link'})['href']
        return repo_link

    def get_row_info(self, rows):
        """get all code list information."""
        all_info = []
        for row in rows:
            repo_name = self.get_repo(row)
            star = self.get_star(row)
            repo_link = self.get_repo_link(row)
            repo_tool = self.get_tools(row)
            info = {'repo name': repo_name, 'star': star,
                    'repo link': repo_link, 'repo tool:': repo_tool}
            all_info.append(info)
        return all_info

    def get_single_row_info(self, row):
        repo_name = self.get_repo(row)
        star = self.get_star(row)
        repo_link = self.get_repo_link(row)
        repo_tool = self.get_tools(row)
        row_info = {'repo name': repo_name, 'stars': star,
                'repo link': repo_link, 'repo tool:': repo_tool}
        return row_info

    def export_result(self, rows, title, path):
        """write all crawled information into a file."""
        filename = title.replace(' ', '_') + '.json'
        file = os.path.join(path, filename).replace('\\', '/')
        with open(file, 'w') as f:
            # save as json file
            for row in rows:
                row_info = self.get_single_row_info(row)
                row_info = json.dumps(row_info)
                f.write(row_info)
                f.write('\n')
            f.write('\n')

    # TODO(2021-01-08): crawl dataset

    def process_pipeline(self, title, path='./dataset'):
        """processing pipeline of crawling by title."""
        print('starting processing...')
        title = self.title_process(title)
        response = self.search_by_title(title)
        rows = self.page_parse(response)
        self.export_result(rows, title, path)
        print('ending processing...')

    def test(self, title):
        title = self.title_process(title)
        response = self.search_by_title(title)
        rows = self.page_parse(response)
        for row in rows:
            self.get_tools(row)


if __name__ == '__main__':
    # test sample
    test = PaperWithCode()
    title = 'deep residual learning for image recognition'
    test.process_pipeline(title)
    # test.test(title)
