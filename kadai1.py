#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 課題URL: https://github.com/marutoraman/study-07-translate
# 参照URL: https://qiita.com/_yushuu/items/83c51e29771530646659

from googletrans import Translator

class CustomTranslator():

    def __init__(self):
        print("【翻訳機】英語→日本語")
        self.tr = Translator(service_urls=['translate.googleapis.com'])
        self.src = None

    def get_input(self):
        self.src = input("英語の文章を入力ください")

    def validate_input(self):
        if self.src is None:
            print("文章が入力されていません。")
            return False
        elif len(self.src) == 0:
            print("文章が空です。")
            return False
        return True 

    def translate(self):
        try:
            text = self.tr.translate(self.src, dest="ja").text
            print(text)
        except Exception as e:
            print(e)


def main():
    translator = CustomTranslator()
    translator.get_input()
    validated = translator.validate_input()
    if validated:
        translator.translate()

if __name__ == "__main__":
    main()
