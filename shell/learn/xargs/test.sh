#!/bin/bash

ls -1 | sort -R | head -n 2 | xargs -I {} cp -r {} /tmp
