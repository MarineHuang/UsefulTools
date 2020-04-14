# Subtitles

一些关于字幕的小工具

[pysrt](https://github.com/byroot/pysrt)是第三方的字幕文件解析库

srt2txt.py 将srt字幕文件转成纯文本txt文件，去掉时间戳信息

`python srt2txt.py input_srt_path [output_txt_path]`

clean_index.py 将srt字幕文件中的序号重新排序，从1开始

`python clean_index.py input_srt_path` 