#!/bin/sh

jps | grep minecraft_server | cut -d' ' -f 1 | xargs kill
