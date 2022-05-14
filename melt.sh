#!/bin/bash
#
#melt intro.mlt -consumer avformat:output.mov f=mov acodec=pcm_s16le vcodec=libxvid s=1920x1080 b=6000k pix_fmt=uyvy422 vtag=yuvs acodec=pcm_s16le

melt intro.mlt -consumer avformat:output.mov f=mov acodec=pcm_s16le vcodec=prores_ks vendor="apl0" s=1920x1080 b=6000k pix_fmt=uyvy422


# -c:v prores_ks -profile:v 2 -vendor apl0 -bits_per_mb 8000 -pix_fmt yuv422p10le -r 29.97 -s 1920x1080 -video_track_timescale 30000
