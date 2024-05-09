#!/bin/bash

# http methods the server
curl -sI "$1" | grep "ALLOW" | cut -d " " -f 2-
