#!/bin/bash

pandoc -f html-native_divs-native_spans -t markdown test.html -o test.md
