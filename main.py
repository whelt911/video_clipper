# This program extracts and saves a clip from a .mp4 file

# downloads ffmpeg if not already downloaded
import imageio.plugins.ffmpeg

imageio.plugins.ffmpeg.download()


from moviepy.editor import VideoFileClip

def rand_generator(num_clips):
    import random
    clip_start = list()
    while len(clip_start) < int(num_clips):
        rand = random.randint(0,clip_length - 10)
        if len(clip_start) == 0:
            clip_start.append(rand)
        else:
            for j in clip_start:
                if abs(j-rand) > 10 :
                    clip_start.append(rand)
                    break

    print(clip_start)

video = VideoFileClip("C:/Users/william.helt/My Documents/video_clipper/Encode_10.mp4")
video_length = int(video.duration)




# loads subclip of the file
# clip = VideoFileClip("E:/video_clipper/Boat_13.mp4").subclip(1,5)
clip = VideoFileClip("C:/Users/william.helt/My Documents/video_clipper/Encode_10.mp4")

clip_length = int(clip.duration)



# clip.write_videofile("C:/Users/william.helt/My Documents/video_clipper/Encode_10.mp4")



print(clip_length)
rand_generator(5)
