#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import codecs
import pysrt

def srt_to_txt(srt_path, txt_path):
    """
    将srt字幕文件转换成纯文本txt文件
    去掉时间码、index等信息
    """
    txt_file = codecs.open(txt_path, 'w+', encoding='utf-8')
    srt_file = codecs.open(srt_path, encoding='utf-8')
    
    for sub in pysrt.stream(srt_file):
        txt_file.write(sub.text+'\n')

    srt_file.close()
    txt_file.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print >>sys.stderr, "{0} srt_path [txt_path]".format(__file__)
        sys.exit(1)
    
    srt_path=sys.argv[1]
    txt_path=srt_path+'.txt'
    if len(sys.argv) > 2:
        txt_path=sys.argv[2]
    srt_to_txt(srt_path,txt_path)