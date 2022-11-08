#!/bin/bash

IN_YAMLS=()
OUT_DIRS=()

##------------------ 3GPP -----------------------------------
init_3GPP() {
    # TS 29.571
    IN_YAMLS+=(/local/TS29571_CommonData.yaml)
    OUT_DIRS+=(/out/common_571/client)

    # TS 29.122
    IN_YAMLS+=(/local/TS29122_CommonData.yaml)
    OUT_DIRS+=(/out/common_122/client)

    # TS 29.502
    IN_YAMLS+=(/local/TS29502_Nsmf_PDUSession.yaml)
    OUT_DIRS+=(/out/smf_pdus/client)

    # TS 29.503
    IN_YAMLS+=(/local/TS29503_Nudm_EE.yaml)
    OUT_DIRS+=(/out/udm_ee/client)

    # TS 29.503
    IN_YAMLS+=(/local/TS29503_Nudm_MT.yaml)
    OUT_DIRS+=(/out/udm_mt/client)

    # TS 29.503
    IN_YAMLS+=(/local/TS29503_Nudm_NIDDAU.yaml)
    OUT_DIRS+=(/out/udm_niddau/client)

    # TS 29.503
    IN_YAMLS+=(/local/TS29503_Nudm_PP.yaml)
    OUT_DIRS+=(/out/udm_pp/client)

    # TS 29.503
    IN_YAMLS+=(/local/TS29503_Nudm_SDM.yaml)
    OUT_DIRS+=(/out/udm_sdm/client)

    # TS 29.503
    IN_YAMLS+=(/local/TS29503_Nudm_UEAU.yaml)
    OUT_DIRS+=(/out/udm_ueau/client)

    # TS 29.503
    IN_YAMLS+=(/local/TS29503_Nudm_UECM.yaml)
    OUT_DIRS+=(/out/udm_uecm/client)

    # TS 29.505
    IN_YAMLS+=(/local/TS29505_Subscription_Data.yaml)
    OUT_DIRS+=(/out/udr_sd/client)

    # TS 29.512
    IN_YAMLS+=(/local/TS29512_Npcf_SMPolicyControl.yaml)
    OUT_DIRS+=(/out/pcf_smpc/client)

    # TS 29.514
    IN_YAMLS+=(/local/TS29514_Npcf_PolicyAuthorization.yaml)
    OUT_DIRS+=(/out/pcf_pa/client)

    # TS 29.518
    IN_YAMLS+=(/local/TS29518_Namf_EventExposure.yaml)
    OUT_DIRS+=(/out/amf_ee/client)

    # TS 29.518
    IN_YAMLS+=(/local/TS29518_Namf_MT.yaml)
    OUT_DIRS+=(/out/amf_mt/client)

    # TS 29.518
    IN_YAMLS+=(/local/TS29518_Namf_Communication.yaml)
    OUT_DIRS+=(/out/amf_c/client)

    # TS 29.519
    IN_YAMLS+=(/local/TS29519_Application_Data.yaml)
    OUT_DIRS+=(/out/udr_ad/client)

    # TS 29.519
    IN_YAMLS+=(/local/TS29519_Policy_Data.yaml)
    OUT_DIRS+=(/out/udr_pd/client)

    # TS 29.519
    IN_YAMLS+=(/local/TS29519_Exposure_Data.yaml)
    OUT_DIRS+=(/out/udr_ed/client)

    # TS 29.520
    IN_YAMLS+=(/local/TS29520_Nnwdaf_EventsSubscription.yaml)
    OUT_DIRS+=(/out/nwdaf_es/client)

    # TS 29.521
    IN_YAMLS+=(/local/TS29521_Nbsf_Management.yaml)
    OUT_DIRS+=(/out/bsf_m/client)

    # TS 29.531
    IN_YAMLS+=(/local/TS29531_Nnssf_NSSelection.yaml)
    OUT_DIRS+=(/out/nssf_nss/client)

    # TS 29.542
    IN_YAMLS+=(/local/TS29542_Nsmf_NIDD.yaml)
    OUT_DIRS+=(/out/smf_nidd/client)

    # TS 32.291
    IN_YAMLS+=(/local/TS32291_Nchf_ConvergedCharging.yaml)
    OUT_DIRS+=(/out/chf_cc/client)
}

##------------------ test cases -----------------------------------
init_testCases() {
    # ts_allof_pattern
    IN_YAMLS+=(/root/src/samples/yaml/ts_allof_pattern.yaml)
    OUT_DIRS+=(/out/ts_allof_pattern/client)

    # ts_allof_ref
    IN_YAMLS+=(/root/src/samples/yaml/ts_allof_ref.yaml)
    OUT_DIRS+=(/out/ts_allof_ref/client)

    # ts_anyof_ref
    IN_YAMLS+=(/root/src/samples/yaml/ts_anyof_ref.yaml)
    OUT_DIRS+=(/out/ts_anyof_ref/client)

    # ts_anyof_required
    IN_YAMLS+=(/root/src/samples/yaml/ts_anyof_required.yaml)
    OUT_DIRS+=(/out/ts_anyof_required/client)

    # ts_callbacks
    IN_YAMLS+=(/root/src/samples/yaml/ts_callbacks.yaml)
    OUT_DIRS+=(/out/ts_callbacks/client)

    # ts_nullable_map
    IN_YAMLS+=(/root/src/samples/yaml/ts_nullable_map.yaml)
    OUT_DIRS+=(/out/ts_nullable_map/client)

    # ts_number_prefix
    IN_YAMLS+=(/root/src/samples/yaml/ts_number_prefix.yaml)
    OUT_DIRS+=(/out/ts_number_prefix/client)

    # ts_oneof
    IN_YAMLS+=(/root/src/samples/yaml/ts_oneof.yaml)
    OUT_DIRS+=(/out/ts_oneof/client)

    # ts_ref_array
    IN_YAMLS+=(/root/src/samples/yaml/ts_ref_array.yaml)
    OUT_DIRS+=(/out/ts_ref_array/client)
}

getVersion() {
    MVN_VERSION=$(mvn -q \
        -Dexec.executable=echo \
        -Dexec.args='${project.version}' \
        --non-recursive \
        exec:exec)
    echo "MVN_VERSION=[${MVN_VERSION}]"
}

generate_all() {
    echo "Number of elements in IN_YAMLS: ${#IN_YAMLS[@]}"
    echo "Number of elements in OUT_DIRS: ${#OUT_DIRS[@]}"

    for (( i=0; i<${#IN_YAMLS[@]}; i++ )); do
        # input YAML
        IN_YAML="${IN_YAMLS[$i]}"
        # version 별로 OUT_DIR 생성
        OUT_DIR="${OUT_DIRS[$i]}_${MVN_VERSION}"
        echo "IN_YAML=[${IN_YAML}],OUT_DIR=[${OUT_DIR}]"

        # input 파일이 없다면, 다음 진행
        if [ ! -f ${IN_YAML} ] ; then
            continue
        fi

        # 디렉토리 생성
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
    done
}

# Run
init_3GPP
init_testCases
getVersion
generate_all

# end of script
