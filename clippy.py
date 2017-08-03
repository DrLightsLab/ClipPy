import sys
from moviepy.editor import *

# Take in an array of objects from command line
# This should be an array and consist of the following pattern:
# {filepath, start time, end time}

create_clip_array(sys.argv)

def create_clip_array(command_list):
clips = []
for clip in command_list:
    clip_list = clip.split('-')
    print clip_list
    clip_object = {'file_path' : clip_list[0], 'start_time' : clip_list[1], 'end_time' : clip_list[2]}
    clips.append(clip_object)
return clips

def create_clips(clip_array):
    for clip in clip_array:
        new_clip = VideFileClip(clip['file_path'])
        