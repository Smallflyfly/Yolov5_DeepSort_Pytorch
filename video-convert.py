#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@author:fangpf
@time: 2021/03/15
"""

import argparse

import cv2


def convert(video_file, dest_file):
    try:
        cap = cv2.VideoCapture(video_file)
    except:
        print('读取视频文件出错')
        return
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    fps = cap.get(cv2.CAP_PROP_FPS)
    size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    out = cv2.VideoWriter(dest_file, fourcc, fps, size)
    while cap.isOpened():
        print('fang')
        _, frame = cap.read()
        cv2.imshow('im', frame)
        cv2.waitKey(1)
        out.write(frame)
    cv2.destroyAllWindows()
    cap.release()
    out.release()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=str, default='', help='要转换的视频源文件')
    parser.add_argument('--dest', type=str, default='test.mp4', help='转换后的视频文件')
    args = parser.parse_args()
    video_file = args.file
    dest_file = args.dest
    convert(video_file, dest_file)
