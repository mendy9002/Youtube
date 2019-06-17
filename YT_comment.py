from apiclient.discovery import build

# arguments to be passed to build function
DEVELOPER_KEY = "AIzaSyCDQHD9GIVtbuYDgorDef4fs0eihln_98E"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# creating youtube resource object for interacting with API
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)


def video_details(video_id):

    # Call the videos.list method to retrieve video info
    result = youtube.videos().list(
        id = video_id,
        part = "id,snippet,contentDetails,statistics",
    ).execute()
    
    # Extracting required info about video
    video = {}
    video['title'] = result['items'][0]['snippet']['title']
    video['tags'] = result['items'][0]['snippet']['tags']
    video['descr'] = result['items'][0]['snippet']['description']
    video['content'] = result['items'][0]['contentDetails']
    video['stats'] = result['items'][0]['statistics']
    
    return video
    

def video_comments(video_id, max_results = 1000):
    
    # Call the comments.list method to retrieve video comments
    results = youtube.commentThreads().list(
        videoId = video_id,
        part = "id,snippet",
        order = "relevance",
        textFormat = "plainText",
        maxResults = max_results%101
    ).execute()

    comments = []
    
    # Extracting required info from each result
    for result in results['items']:
        comment = {}
        comment['id'] = result['id']
        comment['authorDisplayName'] = result['snippet']['topLevelComment']['snippet']['authorDisplayName']
        comment['text'] = result['snippet']['topLevelComment']['snippet']['textOriginal']
        comment['likes'] = result['snippet']['topLevelComment']['snippet']['likeCount']
        comment['publishedtime'] = result['snippet']['topLevelComment']['snippet']['publishedAt']
        comment['updatedttime'] = result['snippet']['topLevelComment']['snippet']['updatedAt']
        comments.append(comment)
    
    return comments
    

if __name__ == "__main__":
    video_id = "gdhYD1WQKyM"
    
    details = video_details(video_id)
    comments = video_comments(video_id)
    
     print(comments)