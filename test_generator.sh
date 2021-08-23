#!/bin/sh

# OUT_DIR=/out/smf_nidd/client_ntels
# mkdir -p ${OUT_DIR};
# java -Dlog.level=debug \
#     -jar /root/src/modules/openapi-generator-cli/target/openapi-generator-cli.jar \
#     generate -i /local/TS29542_Nsmf_NIDD.yaml \
#     -g go \
#     -o${OUT_DIR} >${OUT_DIR}/ogc_java.log 2>&1

OUT_DIR=/out/pcf_smpc/client_ntels2
mkdir -p ${OUT_DIR};
java -Dlog.level=debug \
    -jar /root/src/modules/openapi-generator-cli/target/openapi-generator-cli.jar \
    generate -i /local/TS29512_Npcf_SMPolicyControl.yaml \
    -g go \
    --additional-properties=enumClassPrefix=true \
    -o${OUT_DIR} >${OUT_DIR}/ogc_java.log 2>&1
