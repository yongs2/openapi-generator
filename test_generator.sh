#!/bin/sh

# IN_YAML=/local/TS29571_CommonData.yaml
# OUT_DIR=/out/common_571/client

# IN_YAML=/local/TS29122_CommonData.yaml
# OUT_DIR=/out/common_122/client

# IN_YAML=/local/TS29502_Nsmf_PDUSession.yaml
# OUT_DIR=/out/smf_pdus/client

# IN_YAML=/local/TS29514_Npcf_PolicyAuthorization.yaml
# OUT_DIR=/out/pcf_pa/client

# IN_YAML=/local/TS29512_Npcf_SMPolicyControl.yaml
# OUT_DIR=/out/pcf_smpc/client

# IN_YAML=/local/TS32291_Nchf_ConvergedCharging.yaml
# OUT_DIR=/out/chf_cc/client

# IN_YAML=/local/TS29520_Nnwdaf_EventsSubscription.yaml
# OUT_DIR=/out/nwdaf_es/client

# IN_YAML=/local/TS29503_Nudm_MT.yaml
# OUT_DIR=/out/udm_mt/client

# IN_YAML=/local/TS29518_Namf_EventExposure.yaml
# OUT_DIR=/out/amf_ee/client

# IN_YAML=/local/TS29518_Namf_MT.yaml
# OUT_DIR=/out/amf_mt/client

# IN_YAML=/local/TS29518_Namf_Communication.yaml
# OUT_DIR=/out/amf_c/client

# IN_YAML=/local/TS29503_Nudm_NIDDAU.yaml
# OUT_DIR=/out/udm_niddau/client

# IN_YAML=/local/TS29503_Nudm_UEAU.yaml
# OUT_DIR=/out/udm_ueau/client

# IN_YAML=/local/TS29503_Nudm_UECM.yaml
# OUT_DIR=/out/udm_uecm/client

# IN_YAML=/local/TS29503_Nudm_EE.yaml
# OUT_DIR=/out/udm_ee/client

# IN_YAML=/local/TS29503_Nudm_SDM.yaml
# OUT_DIR=/out/udm_sdm/client

# IN_YAML=/local/TS29503_Nudm_PP.yaml
# OUT_DIR=/out/udm_pp/client

# IN_YAML=/local/TS29519_Application_Data.yaml
# OUT_DIR=/out/udr_ad/client

# IN_YAML=/local/TS29519_Policy_Data.yaml
# OUT_DIR=/out/udr_pd/client

# IN_YAML=/local/TS29519_Exposure_Data.yaml
# OUT_DIR=/out/udr_ed/client

# IN_YAML=/local/TS29505_Subscription_Data.yaml
# OUT_DIR=/out/udr_sd/client

# IN_YAML=/local/TS29521_Nbsf_Management.yaml
# OUT_DIR=/out/bsf_m/client

# IN_YAML=/local/TS29531_Nnssf_NSSelection.yaml
# OUT_DIR=/out/nssf_nss/client

# IN_YAML=/local/TS29542_Nsmf_NIDD.yaml
# OUT_DIR=/out/smf_nidd/client

### unit test for test cases
IN_YAML=/root/src/samples/yaml/ts_allof_pattern.yaml
OUT_DIR=/out/ts_allof_pattern/client

# IN_YAML=/root/src/samples/yaml/ts_allof_ref.yaml
# OUT_DIR=/out/ts_allof_ref/client

# IN_YAML=/root/src/samples/yaml/ts_anyof_required.yaml
# OUT_DIR=/out/ts_anyof_required/client

# IN_YAML=/root/src/samples/yaml/ts_anyof_ref.yaml
# OUT_DIR=/out/ts_anyof_ref/client

# IN_YAML=/root/src/samples/yaml/ts_oneof.yaml
# OUT_DIR=/out/ts_oneof/client

# IN_YAML=/root/src/samples/yaml/ts_number_prefix.yaml
# OUT_DIR=/out/ts_number_prefix/client

# IN_YAML=/root/src/samples/yaml/ts_ref_array.yaml
# OUT_DIR=/out/ts_ref_array/client

# IN_YAML=/root/src/samples/yaml/ts_callbacks.yaml
# OUT_DIR=/out/ts_callbacks/client

mkdir -p ${OUT_DIR};
java -Dlog.level=debug \
    -jar /root/src/modules/openapi-generator-cli/target/openapi-generator-cli.jar \
    generate -i ${IN_YAML} \
    -g go \
    --additional-properties=enumClassPrefix=true \
    --additional-properties=generateAliasAsModel=true \
    -o${OUT_DIR} >${OUT_DIR}/ogc_java.log 2>&1

# anyOf 의 New 함수에서 string 에 대해 변환 오류가 있어서, 후처리 작업 진행
sed -i 's/if varstring, err := NewstringFromValue(v); err == nil {/if true {/g' ${OUT_DIR}/model_*.go
sed -i 's/this.string = varstring/this.string = \&v/g' ${OUT_DIR}/model_*.go
