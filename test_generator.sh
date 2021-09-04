#!/bin/sh

# OUT_DIR=/out/smf_nidd/client_ntels
# mkdir -p ${OUT_DIR};
# java -Dlog.level=debug \
#     -jar /root/src/modules/openapi-generator-cli/target/openapi-generator-cli.jar \
#     generate -i /local/TS29542_Nsmf_NIDD.yaml \
#     -g go \
#     --additional-properties=isGoSubmodule=true,enumClassPrefix=true,generateInterfaces=true \
#     -o${OUT_DIR} >${OUT_DIR}/ogc_java.log 2>&1

# OUT_DIR=/out/pcf_smpc/client_ntels2
# mkdir -p ${OUT_DIR};
# java -Dlog.level=debug \
#     -jar /root/src/modules/openapi-generator-cli/target/openapi-generator-cli.jar \
#     generate -i /local/TS29512_Npcf_SMPolicyControl.yaml \
#     -g go \
#     --additional-properties=isGoSubmodule=true,enumClassPrefix=true,generateInterfaces=true \
#     -o${OUT_DIR} >${OUT_DIR}/ogc_java.log 2>&1

# unit test for test cases
# YAML_NAME=ts_allof_pattern
# YAML_NAME=ts_allof_ref
# YAML_NAME=ts_anyof_nfprofile
YAML_NAME=ts_callbacks
IN_YAML=/out/${YAML_NAME}.yaml
OUT_DIR=/out/${YAML_NAME}

mkdir -p ${OUT_DIR}/;
rm -f  ${OUT_DIR}/*.go ; rm -f ${OUT_DIR}/docs/*.md;
java -Dlog.level=debug \
    -jar /root/src/modules/openapi-generator-cli/target/openapi-generator-cli.jar \
    generate -i ${IN_YAML} \
    -g go \
    --additional-properties=isGoSubmodule=true,enumClassPrefix=true,generateInterfaces=true \
    -o ${OUT_DIR} >${OUT_DIR}/oag.log 2>&1
