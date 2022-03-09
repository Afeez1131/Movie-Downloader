import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def get_videos(url):
    ''' will get videos from the urlpath /videos, which has the category'''
    url = requests.get(url)
    soup = BeautifulSoup(url.content, 'html.parser')
    videos = soup.find("div", class_="video-files")
    # print('Video List :', videos_list)
    video_list = videos.find_all('article', class_='file-one shadow')
    video_dict = {}
    for video in video_list:
        video_info = video.find('div', class_='info')
        movie_type = video_info.find('div', class_="category").text.replace('\n', '')
        link = video_info.find('h2').find(href=True)
        title = video_info.find('h2').text.replace('\n','')
        # meta = video_info.find('div', class_='inner')
        # timestamp = meta.find('span').text.replace('\n','')

        video_dict[title] = [link['href'], movie_type]
        # video_dict[title] = link['href']
        # video_dict['movie_type'] = movie_type
        # video_dict['timestamp'] = timestamp

    return video_dict


def get_videos_genre(url):
    ''' This will get videos from a url path e.g. videos/movies, videos/nollywood .
    Since this is a path for a genre, the category is not included
    will also get the episode of a series of movie'''
    '''https://www.thenetnaija.co/videos/series/11725-snowpiercer/season-1
        https://www.thenetnaija.co/videos/series'''
    url = requests.get(url)
    soup = BeautifulSoup(url.content, 'html.parser')
    videos = soup.find("div", class_="video-files")
    # print('Video List :', videos_list)
    video_list = videos.find_all('article', class_='file-one shadow')
    video_dict = {}
    for video in video_list:
        video_info = video.find('div', class_='info')
        link = video_info.find('h2').find(href=True)
        title = video_info.find('h2').text.replace('\n','')

        video_dict[title] = link['href']
    return video_dict


def category_movie(url):
    ''' this will only download the "movie" category'''
    '''
        https://www.thenetnaija.co/videos/series/11725-snowpiercer/season-1/episode-1
        
        '''
    url = requests.get(url)
    soup = BeautifulSoup(url.content, 'html.parser')
    title = soup.find('h1', class_='page-h1').text.strip().replace('\n', '')
    download_links = soup.find_all('div', class_='db-one')
    movie_link_href = download_links[0].find(href=True)['href']
    if len(download_links) > 1:
        subtitle_link_href = download_links[1].find(href=True)['href']
    else:
        subtitle_link_href = None

    host = 'https://www.thenetnaija.co'
    movie_link = host + movie_link_href
    if subtitle_link_href == None:
        subtitle_link = None
    else:
        subtitle_link = host + subtitle_link_href
    return title, movie_link, subtitle_link#, para


def category_series(url):
    ''' will get all seasons in a series and the return the title and link to each season'''
    ''' path = https://www.thenetnaija.co/videos/series/11725-snowpiercer
                /videos/series/series_title
    '''
    url = requests.get(url)
    soup = BeautifulSoup(url.content, 'html.parser')
    series_title = soup.find('h1', class_='page-h1')
    seasons = soup.find('article', class_='vs-many')
    season = seasons.find_all('div', class_='vs-one')
    seasons_dict = {}
    for seas in season:
        season_title = seas.find('h3', class_='title')
        season_link = seas.find('h3', class_='title').find(href=True)['href']
        seasons_dict[season_title] =  season_link
    return seasons_dict

def category_nollywood(url):
    ''' will get all seasons in a series and the return the title and link to each season'''
    ''' path = https://www.thenetnaija.co/videos/nollywood/11725-snowpiercer
                /videos/series/series_title
    '''
    url = requests.get(url)
    soup = BeautifulSoup(url.content, 'html.parser')
    seasons = soup.find('article', class_='ve-many')
    season = seasons.find_all('div', class_='ve-one')
    seasons_dict = {}
    for seas in season:
        season_title = seas.find('h3', class_='title').text.strip()
        season_link = seas.find('h3', class_='title').find(href=True)['href']
        seasons_dict[season_title] =  season_link
    return seasons_dict

'''url = 'https://www.thenetnaija.co/videos/movies/15784-te-jing-dui-2019-chinese/download'
download_page = requests.get(url)
soup = BeautifulSoup(download_page.content, 'html.parser')
button = soup.find('button', class_='btn shadow-sm download mt-3 mt-sm-0')
print(button['onclick'])'''



# series = category_series('https://www.thenetnaija.co/videos/series/14768-the-good-doctor')
# for season, link in series.items():
#     a_season = get_videos_genre(link)
#     for title, link2 in a_season.items():
#         print(category_movie(link2))


# single_movie_url = 'https://www.thenetnaija.co/videos/movies/15781-the-girl-on-the-mountain-2022'
# # for season, link in series.items():
# #     a_season = get_videos_genre(link)
# #     for title, link2 in a_season.items():
# print(category_movie(single_movie_url))



# series = category_nollywood('https://www.thenetnaija.co/videos/nollywood/15692-two-wives-one-husband-2022')
# for season, link in series.items():
#     # a_season = get_videos_genre(link)
#     # for title, link2 in a_season.items():
#     print(category_movie(link))

'''window.__NUXT__=(function(a,b,c,d,e,f,g,h,i,j){return {layout:"default",data:[{file:{id:"GSkMuJFdZ14",name:"Te Jing Dui (2019) (NetNaija.com).mp4",about:c,datetime:{atom:"2022-03-08T14:49:26+00:00",pretty:"3 hours ago",last:{atom:"2022-03-08T18:38:58+00:00",pretty:"Just Now"}},downloads:{number:3903,pretty:"3.9k"},plays:{number:d,pretty:"0"},private:b,password:c,protected:b,folder:{id:f,name:"Movies",count:{files:3141,folders:d},datetime:{atom:"2020-11-15T13:13:33+00:00",pretty:"Nov 15, 2020"},size:{number:805647462248,pretty:"750.32GB"},user:{id:g,username:h,suffix:i},parent:{id:e,name:"Videos",permalink:"folder\u002Fxl4ql8-XK"},ancestors:{id:[e]},permalink:"folder\u002FjveiR7mkj",private:j},ancestors:{id:[e,f]},user:{id:g,username:h,suffix:i},format:"mp4",busy:b,thumb:d,img:c,size:{number:391138664,pretty:"373.02MB"},mod:c,permalink:"file\u002FGSkMuJFdZ14-te-jing-dui-2019-netnaija-com-mp4",slug:"GSkMuJFdZ14-te-jing-dui-2019-netnaija-com-mp4",path:"2022\u002F03\u002FGerardcole\u002F1646750966_Te_Jing_Dui_(2019)_(NetNaija.com).mp4_1b2fa05d538622ff89446bc251f55d85.nnf",meta:{duration:6587.875},captions:[],supports:[],clusters:["njide","fresh"],hash:{md5:"4c80f50b1dd439b26709ff2061838b1c",sha256:"c4593f93cbb50532713fdefd3c43a35e81288fea928f794c6e0983140a10b657"},forced_private:b},isM:b}],fetch:[],error:a,state:{access:a,apiUrl:"https:\u002F\u002Fapi.sabishare.com\u002F",imgUrl:"https:\u002F\u002Fimg.sabishare.com\u002F",appHost:"https:\u002F\u002Fwww.sabishare.com\u002F",appRoot:"\u002F",userData:{id:a,username:a,usage:a,plan:a,count:a},languages:{}},serverRendered:j,routePath:"\u002Ffile\u002FGSkMuJFdZ14-te-jing-dui-2019-netnaija-com-mp4",config:{}}}(null,false,"",0,"xl4ql8-XK","jveiR7mkj","8fOS3iq","Gerardcole","(NetNaija.com)",true));'''