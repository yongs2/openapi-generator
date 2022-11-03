#!/bin/sh

# IN_YAML=TS29502_Nsmf_PDUSession.yaml
# OUT_DIR=/out/smf_pdus/server_ntels

# IN_YAML=TS29514_Npcf_PolicyAuthorization.yaml
# OUT_DIR=/out/pcf_pa/server_ntels

IN_YAML=TS29512_Npcf_SMPolicyControl.yaml
OUT_DIR=/out/pcf_smpc/server_ntels

# IN_YAML=TS32291_Nchf_ConvergedCharging.yaml
# OUT_DIR=/out/chf_cc/server_ntels

# IN_YAML=TS29520_Nnwdaf_EventsSubscription.yaml
# OUT_DIR=/out/nwdaf_es/server_ntels

# IN_YAML=TS29503_Nudm_MT.yaml
# OUT_DIR=/out/udm_mt/server_ntels

# IN_YAML=TS29518_Namf_EventExposure.yaml
# OUT_DIR=/out/amf_ee/server_ntels

# IN_YAML=TS29518_Namf_MT.yaml
# OUT_DIR=/out/amf_mt/server_ntels

# IN_YAML=TS29503_Nudm_NIDDAU.yaml
# OUT_DIR=/out/udm_niddau/server_ntels

# IN_YAML=TS29503_Nudm_UEAU.yaml
# OUT_DIR=/out/udm_ueau/server_ntels

# IN_YAML=TS29503_Nudm_UECM.yaml
# OUT_DIR=/out/udm_uecm/server_ntels

# IN_YAML=TS29503_Nudm_EE.yaml
# OUT_DIR=/out/udm_ee/server_ntels

# IN_YAML=TS29503_Nudm_SDM.yaml
# OUT_DIR=/out/udm_sdm/server_ntels

# IN_YAML=TS29503_Nudm_PP.yaml
# OUT_DIR=/out/udm_pp/server_ntels

# IN_YAML=TS29519_Application_Data.yaml
# OUT_DIR=/out/udr_ad/server_ntels

# IN_YAML=TS29519_Policy_Data.yaml
# OUT_DIR=/out/udr_pd/server_ntels

# IN_YAML=TS29519_Exposure_Data.yaml
# OUT_DIR=/out/udr_ed/server_ntels

# IN_YAML=TS29505_Subscription_Data.yaml
# OUT_DIR=/out/udr_sd/server_ntels

# IN_YAML=TS29521_Nbsf_Management.yaml
# OUT_DIR=/out/bsf_m/server_ntels

# IN_YAML=TS29531_Nnssf_NSSelection.yaml
# OUT_DIR=/out/nssf_nss/server_ntels

# IN_YAML=TS29542_Nsmf_NIDD.yaml
# OUT_DIR=/out/smf_nidd/server_ntels

mkdir -p ${OUT_DIR};
java -Dlog.level=debug \
    -jar /root/src/modules/openapi-generator-cli/target/openapi-generator-cli.jar \
    generate -i /local/${IN_YAML} \
    -g go-gin-server \
    --additional-properties=enumClassPrefix=true \
    -o${OUT_DIR} >${OUT_DIR}/ogc_java.log 2>&1
