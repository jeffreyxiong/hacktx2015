from apiclient.discovery import build
from secret import secret_key

DEVELOPER_KEY = 'AIzaSyCkTsiDORr0CeVAITisYAxw8EU3G4Zqqps'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


def youtube_search(url):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    video_id = url.split('v=')[1].split('&')[0]

    return youtube.videos().list(
        part='snippet',
        id=video_id
    ).execute()['items'][0]['snippet']['title']

    return search_response

print youtube_search('https://www.youtube.com/watch?v=Ea9_nwcN37I')
