import codecs
import pysrt


subs=pysrt.open(u'Alexis Ohanian - How to make a splash in social media.zh-cn.srt')
print(len(subs))
subs.clean_indexes()
subs.save('Alexis Ohanian - How to make a splash in social media.zh-cn.srt2', encoding='utf-8')