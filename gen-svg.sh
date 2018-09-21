#!/bin/sh

# dot classes.gv -Tsvg -o classes.svg

python main.py > tmp.gv \
  && dot tmp.gv -Tsvg -o tmp.svg
