from googleapiclient.discovery import build
import pandas as pd
def get_playlist_videos(api_key, playlist_id):
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Fetch playlist items
    request = youtube.playlistItems().list(
        part='snippet',
        playlistId=playlist_id,
        maxResults=50  # Maximum number of items per page
    )
    
    videos = []
    while request:
        response = request.execute()
        for item in response['items']:
            title = item['snippet']['title']
            videos.append(title)

        request = youtube.playlistItems().list_next(request, response)

    return videos

def main():
    api_key = "" # Replace with your actual API key
    playlist_url = ""

    # Extract the playlist ID from the URL
    playlist_id = playlist_url.split('list=')[-1].split('&')[0]

    videos = get_playlist_videos(api_key, playlist_id)
    df = pd.DataFrame(videos, columns=['Video Title'])
    output_file = 'playlist_videos.txt'
    df.to_csv(output_file, index=False)

    print(f'Course list of topics saved to {output_file}')


    

if __name__ == "__main__":
    main()
