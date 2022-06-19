from googleapiclient.discovery import build
from api_constants import api_key

youtube = build('youtube', 'v3', developerKey=api_key)

def fetchApiResults():
    request = youtube.search().list(
        q='cricket',
        part='snippet',
        type='video',
        maxResults=10
        )

    response = request.execute()

    videoDataList = []

    for item in response['items']:
        videoId = item['id']['videoId']

        snippet = item['snippet']

        # Item snippet
        publishedAt = snippet['publishedAt']
        title = snippet['title']
        description = snippet['description']
        thumbnails = snippet['thumbnails']
        channelTitle = snippet['channelTitle']
        publishTime = snippet['publishTime']

        # Thumbnail urls
        defaultUrl = thumbnails['default']['url']
        mediumUrl = thumbnails['medium']['url']
        highUrl = thumbnails['high']['url']
        urlList = []
        urlList.append(defaultUrl)
        urlList.append(mediumUrl)
        urlList.append(highUrl)

        videoDataList.append({
            "video_id": videoId,
            "title": title,
            "description": description,
            "thumbnails": urlList,
            "channel_title": channelTitle,
            "published_at": publishedAt
            })

    return(videoDataList)
