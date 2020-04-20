#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import pysrt


subs=pysrt.open(u'不能说的秘密.zh-cn.srt')
print(len(subs))
subs.clean_indexes()
subs.save(u'不能说的秘密.zh-cn.srt2', encoding='utf-8')