#!/bin/sh

# git pull upstream master
# git push origin master

cd /root/src
mvn -am -pl "modules/openapi-generator-cli" package -DskipTests=true -Dmaven.javadoc.skip=true -Djacoco.skip=true
