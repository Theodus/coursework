#!/bin/sh

python main.py > classes.gv \
  && dot classes.gv -Tsvg -o classes.svg

