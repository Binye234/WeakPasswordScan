#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2023/2/26-15:32


class OcrError(Exception):
    def __init__(self, msg):
        super().__init__(msg)
