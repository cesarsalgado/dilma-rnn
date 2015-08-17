import os
from os.path import join
from bs4 import BeautifulSoup
import glob
import random
import urllib2

dataset_root_path = 'datasets/discursos_dilma'
htmls_dir_path = join(dataset_root_path, 'htmls')
texts_dir_path = join(dataset_root_path, 'texts')

def download_htmls_wget():
    if not os.path.isdir(htmls_dir_path):
        os.makedirs(htmls_dir_path)
    os.system("wget -i dilma_discursos_urls.txt -P %s"%htmls_dir_path)

def download_htmls_urllib2():
    if not os.path.isdir(htmls_dir_path):
        os.makedirs(htmls_dir_path)
    with open('dilma_discursos_urls.txt', 'r') as f:
        urls = f.read().strip().split('\n')
        n = len(urls)
        for i,url in enumerate(urls):
            save_path = join(htmls_dir_path, os.path.basename(url))
            if not os.path.isfile(save_path):
                print '%d/%d files downloaded'%(i+1,n)
                response = urllib2.urlopen(url)
                html = response.read()
                with open(save_path, 'w') as f2:
                    f2.write(html)

def get_content_from_soup(soup):
    complete = soup.find(id='parent-fieldname-text').text.strip()
    lines = complete.split('\n')
    return '\n'.join(lines[1:-1]).strip()

def convert_htmls_to_txt():
    if not os.path.isdir(texts_dir_path):
        os.makedirs(texts_dir_path)
    paths = glob.glob(join(htmls_dir_path, '*'))
    for path in paths:
        with open(path, 'r') as f:
            html_doc = f.read()
        soup = BeautifulSoup(html_doc, 'html.parser')
        text = get_content_from_soup(soup)
        name_txt = os.path.basename(path)+'.txt'
        with open(join(texts_dir_path, name_txt), 'w') as f:
            f.write(text.encode('utf8'))

def concatenate_texts():
    paths = glob.glob(join(texts_dir_path, '*'))
    texts = []
    for path in paths:
        with open(path, 'r') as f:
            text = f.read()
        texts.append(text)
    random.shuffle(texts)
    with open(join(dataset_root_path, 'input.txt'), 'w') as f:
        f.write("\n\n*************\n\n".join(texts))

use_wget = True # or use urllib2 otherwise. The later is slower in my experience.
def main():
    if use_wget:
        download_htmls_wget()
    else:
        download_htmls_urllib2()
    convert_htmls_to_txt()
    random.seed(1)
    concatenate_texts()

if __name__ == "__main__":
    main()
