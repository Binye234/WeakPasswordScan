#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2023/2/26-9:40


from modules import code_ocr


def run():
    ocr = code_ocr.CodeOcr()
    s = ocr.ocr('../image/1.jpg')
    print(s)


if __name__ == "__main__":
    run()
