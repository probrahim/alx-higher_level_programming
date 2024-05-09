#!/bin/bash

# http methods the server
curl -sI "$1" | grep "AllOW" | cut -d " " -f 2-
