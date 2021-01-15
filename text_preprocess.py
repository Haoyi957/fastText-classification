import re
import pkuseg
import jieba
from zhon.hanzi import punctuation


class TextProcess:

    def word_split(self, text):
        seg = pkuseg.pkuseg()
        seg_list = jieba.lcut(text, cut_all=True)
        return seg_list

    def word_space_split(self, text):
        return ' '.join(text)

    def remove_punctuation(self, text):
        return re.sub("[{}]+".format(punctuation), "", text)

    def word_preprocess(self, text):
        text = text.replace('\n', '')
        text = self.remove_punctuation(text)
        text = self.word_split(text)
        text = self.word_space_split(text)
        return text
