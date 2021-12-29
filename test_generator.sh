#!/bin/sh

# IN_YAML=TS29571_CommonData.yaml
# OUT_DIR=/out/common_571/client_ntels

# IN_YAML=TS29122_CommonData.yaml
# OUT_DIR=/out/common_122/client_ntels

# IN_YAML=TS29502_Nsmf_PDUSession.yaml
# OUT_DIR=/out/smf_pdus/client_ntels

# IN_YAML=TS29514_Npcf_PolicyAuthorization.yaml
# OUT_DIR=/out/pcf_pa/client_ntels

# IN_YAML=TS29512_Npcf_SMPolicyControl.yaml
# OUT_DIR=/out/pcf_smpc/client_ntels

# IN_YAML=TS32291_Nchf_ConvergedCharging.yaml
# OUT_DIR=/out/chf_cc/client_ntels

# IN_YAML=TS29520_Nnwdaf_EventsSubscription.yaml
# OUT_DIR=/out/nwdaf_es/client_ntels

# IN_YAML=TS29503_Nudm_MT.yaml
# OUT_DIR=/out/udm_mt/client_ntels

# IN_YAML=TS29518_Namf_EventExposure.yaml
# OUT_DIR=/out/amf_ee/client_ntels

# IN_YAML=TS29518_Namf_MT.yaml
# OUT_DIR=/out/amf_mt/client_ntels

IN_YAML=TS29518_Namf_Communication.yaml
OUT_DIR=/out/amf_c/client_ntels

# IN_YAML=TS29503_Nudm_NIDDAU.yaml
# OUT_DIR=/out/udm_niddau/client_ntels

# IN_YAML=TS29503_Nudm_UEAU.yaml
# OUT_DIR=/out/udm_ueau/client_ntels

# IN_YAML=TS29503_Nudm_UECM.yaml
# OUT_DIR=/out/udm_uecm/client_ntels

# IN_YAML=TS29503_Nudm_EE.yaml
# OUT_DIR=/out/udm_ee/client_ntels

# IN_YAML=TS29503_Nudm_SDM.yaml
# OUT_DIR=/out/udm_sdm/client_ntels

# IN_YAML=TS29503_Nudm_PP.yaml
# OUT_DIR=/out/udm_pp/client_ntels

# IN_YAML=TS29519_Application_Data.yaml
# OUT_DIR=/out/udr_ad/client_ntels

# IN_YAML=TS29519_Policy_Data.yaml
# OUT_DIR=/out/udr_pd/client_ntels

# IN_YAML=TS29519_Exposure_Data.yaml
# OUT_DIR=/out/udr_ed/client_ntels

# IN_YAML=TS29505_Subscription_Data.yaml
# OUT_DIR=/out/udr_sd/client_ntels

# IN_YAML=TS29521_Nbsf_Management.yaml
# OUT_DIR=/out/bsf_m/client_ntels

# IN_YAML=TS29531_Nnssf_NSSelection.yaml
# OUT_DIR=/out/nssf_nss/client_ntels

# IN_YAML=TS29542_Nsmf_NIDD.yaml
# OUT_DIR=/out/smf_nidd/client_ntels

# unit test for test cases
#YAML_NAME=ts_allof_pattern
#YAML_NAME=ts_allof_ref
#YAML_NAME=ts_anyof_nfprofile
#YAML_NAME=ts_callbacks
#IN_YAML=/out/${YAML_NAME}.yaml
#OUT_DIR=/out/${YAML_NAME}

mkdir -p ${OUT_DIR};
java -Dlog.level=debug \
    -jar /root/src/modules/openapi-generator-cli/target/openapi-generator-cli.jar \
    generate -i /local/${IN_YAML} \
    -g go \
    --additional-properties=enumClassPrefix=true \
    -o${OUT_DIR} >${OUT_DIR}/ogc_java.log 2>&1

# anyOf 의 New 함수에서 string 에 대해 변환 오류가 있어서, 후처리 작업 진행
sed -i 's/if varstring, err := NewstringFromValue(v); err == nil {/if true {/g' ${OUT_DIR}/model_*.go
sed -i 's/this.string = varstring/this.string = \&v/g' ${OUT_DIR}/model_*.go
