import sys
from moviepy.editor import *

if __name__ = '__main__':
    clips = create_clip_array(sys.argv)
    create_clips(clips)


# Take in an array of objects from command line
# This should be an array and consist of the following pattern:
# {filepath, start time, end time}

#create_clip_array(sys.argv)
complete = false
method_input = raw_input('Enter [I]nteractive or [O]bject mode [I/O]: ')
if(method_input == 'I'):
    task_input = raw_input('[E]dit clip or [C]reate clip [E/C]?:')
    if(task_input == 'E'):
        clips_array = interactive_create_clip_array()
        new_clips = create_new_clips_array(clip_array)
        while(!complete):
            status = write_clips(new_clips)
        
# I'm thinking that these could probably be their own module that
# I can import and call these methods on.
def interactive_create_clip_array():
    clips = []
    done = false
    while(!done):
        file_path = raw_input('Enter path to file: ')
        start_time = raw_input('Enter clip start time (format: hh:mm:ss): ')
        end_time = raw_input('Enter clip end time (format: hh:mm:ss): ')
        new_filename = raw_input('Enter a name for this clip: ')
        clip_object = {'file_path': file_path, 'start_time': str(start_time), 'end_time': str(end_time), 'new_filename' : new_filename}
        clips.append(clip_object)
        finished = raw_input('Are there more clips you would like to edit? [Y/N]: ')
        if(finished == 'Y'):
            done = true
    return clips


def create_clip_array(command_list):
clips = []
for clip in command_list:
    clip_list = clip.split('-')
    print clip_list
    clip_object = {'file_path' : clip_list[0], 'start_time' : clip_list[1], 'end_time' : clip_list[2]}
    clips.append(clip_object)
return clips

# Currently, I am hardcoding certain things like target_resolution because I'm assuming
# that no one wants a video file that isn't 1920x1080, and that isn't 60fps.  However, I
# should make it possible for someone to change that, but make the default 1920x1080, 60fps
def create_new_lips_array(clip_array):
    new_clips = []
    for clip in clip_array:
        original_clip = VideoFileClip(clip['file_path'], target_resolution=(1080,1920))
        new_clip = original_clip.subclip(clip['start_time'], clip['end_time'])
        new_clip_object = {'new_clip' : new_clip, 'new_filename' : clip['new_filename']}
        new_clips.append(new_clip_object)
    return new_clips

def write_clips(clips):
    for(clip in clips):
        clip['new_clip'].write_videofile(clip['new_filename'], fps=60)
    return true