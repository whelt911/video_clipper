# This program extracts and saves a clip from a .mp4 file

# downloads ffmpeg if not already downloaded
import imageio.plugins.ffmpeg

imageio.plugins.ffmpeg.download()

# import necessary modules
from moviepy.editor import VideoFileClip, concatenate_videoclips
from moviepy.editor import CompositeVideoClip
from moviepy.editor import ColorClip
from moviepy.editor import TextClip

# this function can randomly clip a file into a specified number of clips
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


# loads a file clipped from start to end
def clipper(file, start, end):
    clip = VideoFileClip(file).subclip(int(start),int(end))
    return clip
    

# creates a text and overlays over black screen
def description (info):
    text_clip = TextClip(info, fontsize=70,color='white')
    text_clip = text_clip.set_pos('center').set_duration(5)
    # video frame is: 1280x720
    background = ColorClip((1280,720), (0,0,0), False, 5)
    intro_clip = CompositeVideoClip([background,text_clip])
    return intro_clip

def overlay (clip, eureka_dat_list):

    info = [TextClip(text, fontsize = 32, color='green').
            set_pos('top').set_duration(5)
            for text in eureka_dat_list]
    overlay = concatenate_videoclips(info)
    overlayed_clip = CompositeVideoClip([boat, overlay])
    return overlayed_clip

ex_data = ["sample1","sample2","sample3","sample4","sample5"]
clip = "C:/Prov_River_Project/video_clipper/Encode_10.mp4"
boat = clipper(clip,10,40)
boat = overlay(boat,ex_data)
text = description("Conimicut: 10s - 40s")
video = concatenate_videoclips((text,boat))
video.write_videofile("C:/Prov_River_Project/video_clipper/test.mp4", fps = 60)
#text.write_videofile("C:/Prov_River_Project/video_clipper/test.mp4", fps = 60)



'''
GOOD SOURCE CODE FOR ADDING TEXT THAT CHANGES EVERY FEW SECONDS TO A VIDEO
messages = ["Dog", "Cat", "Duck", "Wolf"]
clips = [ mp.TextClip(txt, fontsize=170, color='green', size=(500,300))
            .set_duration(1)
          for txt in  messages]
concat_clip = mp.concatenate_videoclips(clips)
'''
