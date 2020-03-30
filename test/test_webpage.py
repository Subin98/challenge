from bs4 import BeautifulSoup
import pytest
import pickle
import requests

class TestWebpage:
    @pytest.fixture(autouse=True)
    def get_soup(self):
        index_page = requests.get("http://localhost:8000/index.html")
        soup_index = BeautifulSoup(index_page.content, 'html.parser')
        self._index = soup_index
        
    # testing index.html
    def test_indexpage(self):
        site = self._index.find_all('video')
        count = 0
        for audio in site:
            count +=1
        assert count==3
         
        site1 = self._index.find('source',{'src':'video.mp4'})
        count = 0
        for site1 in self._index.find_all('source',{'src':'video.mp4'}):
            count +=1
        assert count==3
  
        assert self._index.find('video', {'autoplay': ''})
        assert self._index.find('video', {'controls': '', 'preload': ''})
        assert self._index.find('video', {'poster': 'https://cdn12.picryl.com/photo/2016/12/31/lego-stones-plastic-education-8b9a7d-1024.jpg'})