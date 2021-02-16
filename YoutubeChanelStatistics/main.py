import requests

# 1)Like to dislike ratio , percentage of likes on video, absolute number of likes on video ...
# 2)total number of Subscribers
# 3) subscribers growth over time ( relative and absolute)
# 3)total views of all videos over time
# 4)total numbers of videos


API_KEY = 'AIzaSyD_BzAH50QaQA38ioHYmTEJb_1CSFdMV-c'
VIDEO_STATS_URL = 'https://www.googleapis.com/youtube/v3/videos'
CHANNEL_STATS_URL = 'https://www.googleapis.com/youtube/v3/channels'
PLAYLIST_ITEMS_URL = 'https://www.googleapis.com/youtube/v3/playlistItems'
SEARCH_CHANNEL_URL = 'https://www.googleapis.com/youtube/v3/search'


def get_stats_for_video(id_block):
    video_id = id_block['videoId']

    vid_result = requests.get(
        VIDEO_STATS_URL,
        params={
            'part': 'statistics',
            'id': video_id,
            'key': API_KEY
        }
    ).json()

    stats = vid_result['items'][0]['statistics']
    likes_count = int(stats.get('likeCount', 0))
    dislikes_count = int(stats.get('dislikeCount', 0))
    return {'video_id': video_id, 'likes_count': likes_count, 'dislikes_count': dislikes_count}


def get_chanel_info(channel_id):
    res = requests.get(
        CHANNEL_STATS_URL,
        params={
            'part': 'statistics,contentDetails',
            'id': channel_id,
            'key': API_KEY
        }
    )
    res = res.json()
    stats = res['items'][0]['statistics']
    total_subscribers = stats['subscriberCount']
    total_views = stats['viewCount']
    total_videos = stats['videoCount']
    total_comments = stats['commentCount']
    result = {
        'total_subscribers': total_subscribers,
        'total_views': total_views,
        'total_videos': total_videos,
        'total_comments': total_comments,
    }

    videos = []
    page_token = ''
    playlist_id = res['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    while True:
        params = {
            'part': 'snippet,contentDetails',
            'playlistId': playlist_id,
            'maxResults': 50,
            'key': API_KEY
        }
        if len(page_token) > 0:
            params['pageToken'] = page_token

        res_videos = requests.get(PLAYLIST_ITEMS_URL, params).json()

        for obj in res_videos['items']:
            id_block = obj['contentDetails']
            if 'videoId' in id_block:
                stats = get_stats_for_video(id_block)
                videos.append(stats)
        if 'nextPageToken' not in res_videos:
            break
        page_token = res_videos['nextPageToken']
    result['videos'] = videos
    return result


def get_channel_id(channel_name):
    params = {
        'part': 'snippet',
        'type': 'channel',
        'q': channel_name,
        'key': API_KEY
    }

    res = requests.get(SEARCH_CHANNEL_URL, params=params).json()
    if len(res["items"]) == 0:
        return None
    else:
        return res["items"][0]["snippet"]["channelId"]


def main():
    res = requests.get('https://www.googleapis.com/youtube/v3/videos')


    # channel_name = 'VSAUCE'
    # channel_id = get_channel_id(channel_name)
    # channel_info = get_chanel_info(channel_id)
    # print(channel_info)


if __name__ == '__main__':
    main()
