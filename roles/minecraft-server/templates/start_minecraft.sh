#!/bin/sh

/usr/lib/jvm/java-8-openjdk-amd64/bin/java -Dminecraft.server=true -Xmx1024M -Xms1024M -jar {{minecraft_home}}/minecraft_server.{{minecraft_version}}.jar nogui
