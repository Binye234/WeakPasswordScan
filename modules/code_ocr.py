#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2023/2/26-9:41

import ddddocr
from error import file_io_error, ocr_error


class CodeOcr:
    def __init__(self):
        self.__ocr = ddddocr.DdddOcr()

    def ocr(self, image_path):
        with open(image_path, "rb") as f:
            try:
                buff = f.read()
            except IOError as e:
                raise file_io_error.FileIoError('图片读取异常')
            try:
                result = self.__ocr.classification(buff)
            except Exception as e:
                raise ocr_error.OcrError('验证码识别异常')
        return result



