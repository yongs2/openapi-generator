#!/bin/sh

# git pull upstream master
# git push origin master
# maven cache 삭제 : mvn dependency:purge-local-repository

# Schema
# https://github.com/swagger-api/swagger-core/blob/cc9be286bc9ec41c24f15453a57cdb92474f358a/modules/swagger-models/src/main/java/io/swagger/v3/oas/models/media/Schema.java
# ComposedSchema
# https://github.com/swagger-api/swagger-core/blob/cc9be286bc9ec41c24f15453a57cdb92474f358a/modules/swagger-models/src/main/java/io/swagger/v3/oas/models/media/ComposedSchema.java

cd /root/src
mvn -am -pl "modules/openapi-generator-cli" package -DskipTests=true -Dmaven.javadoc.skip=true -Djacoco.skip=true
