# -*- coding: utf-8 -*-
import os
import subprocess
# use ffmpeg to convert images into video
# detect images with path:/users/18004/Desktop/ec601/project1/
# convert the image into proper size, and convert them into a mp4 vedio named 'Myvedio.mp4'
subprocess.call('ffmpeg', '-f', 'image2', '-framerate', '1', '-s', '1920*1080', '-i', 'r/users/18004/Desktop/ec601/project1/', '-crf', '25', '-pix_fmt', 'yuv420p', 'Myvideo.mp4')
