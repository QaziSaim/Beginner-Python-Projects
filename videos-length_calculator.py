from moviepy.editor import VideoFileClip
import os

def calculate_total_duration(directory):
    total_duration = 0
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_file() and entry.name.endswith('.mp4'):
                video_path = os.path.join(directory, entry.name)
                try:
                    clip = VideoFileClip(video_path)
                    total_duration += clip.duration
                    clip.close()
                except Exception as e:
                    print(f"Error processing {entry.name}: {e}")
    
    total_duration = round(total_duration, 2)
    return total_duration

# Example usage:
if __name__ == "__main__":
    directory = 'path'
    # directory="https://www.youtube.com/playlist?list=PL6XT0grm_TfgP3OlZzmGh4Cq_rHtX8z7e"
    total_duration = calculate_total_duration(directory)
    print(f"Total duration of MP4 videos in {directory}: {total_duration*0.000277778} hours")
