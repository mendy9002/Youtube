import urllib
import json
from apiclient.discovery import build

# arguments to be passed to build function
DEVELOPER_KEY = "AIzaSyCDQHD9GIVtbuYDgorDef4fs0eihln_98E"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# creating youtube resource object for interacting with API
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)


def get_all_video_in_channel(channel_id):

    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    first_url = base_search_url+'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(DEVELOPER_KEY, channel_id)

    video_links = []
    url = first_url
    while True:
        # inp = urllib.urlopen(url)
        with urllib.request.urlopen(url) as url:
            s = url.read()
        resp = json.loads(s)

        for i in resp['items']:
            if i['id']['kind'] == "youtube#video":
                video_links.append(base_video_url + i['id']['videoId'])

        try:
            next_page_token = resp['nextPageToken']
            url = first_url + '&pageToken={}'.format(next_page_token)
        except:
            break
    return video_links
