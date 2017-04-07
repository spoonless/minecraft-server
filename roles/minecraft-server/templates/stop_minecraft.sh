#!/bin/sh

ps a | grep '-Dminecraft.server=true' | cut -f1 -d' ' | xargs kill
