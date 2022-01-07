import requests
from bs4 import BeautifulSoup

title = 'ShakeDrop Regularization for Deep Residual Learning'
title.replace(' ', '+')
title.replace(':', '%3')
print('My search title is: ' + title)
payload = {'q_meta': '', 'q_type': '', 'q': title}
response = requests.get('https://paperswithcode.com/search', params=payload)

print(response.status_code)
print('current url: ' + response.url)

bs = BeautifulSoup(response.text, 'html.parser')
link = bs.find(name='a', attrs={'class': 'badge badge-light'})
print(link['href'])
# find paper page
next_link = 'https://paperswithcode.com' + link['href']
response = requests.get(next_link)
# check out
print(response.status_code)
print('current url: ' + response.url)
print('*' * 10)
bs = BeautifulSoup(response.text, 'html.parser')
impl_list = bs.find(name='div', attrs={'id': 'implementations-full-list'})
rows = impl_list.find_all(name='div', attrs={'class': 'row'})


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
        repo_name = get_repo(row)
        star = get_star(row)
        info = {'reponame': repo_name, 'star': star}
        all_info.append(info)
    return all_info


def add_txt(filename):
    code_impl = get_row_info(rows)
    with open(filename, 'w+') as f:
        f.write(title + '\n' + '-' * 50 + '\n')
        for i in code_impl:
            f.write(str(i))
            f.write('\n')


# TODO(2022-01-07): get tools
def get_tools(rows):
    pass


if __name__ == '__main__':
    add_txt('./dataset/result.txt')
