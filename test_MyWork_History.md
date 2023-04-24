# openapi-generator
## 작업 일지

### git history 관리

```sh
git remote add upstream https://github.com/OpenAPITools/openapi-generator
git pull upstream master
git push origin master
```

### 2022/11/11

- ts_allof_pattern.yaml 을 수정
  - allof 하위 항목에 pattern 만 가지는 경우에는 무시하도록 수정, FIX
- ts_allof_ref
  - allof, anyof 하위 항목 무시됨, FIX
- ts_anyof_ref
  - NewEventsSubscPutData(v string) 으로 생성자에 대해 v string 이 제거되어야 함, TODO:
- ts_anyof_required
  - anyOf 하위 항목 무시됨, FIX
- ts_callbacks
  - callback api 생성되어야 함, TODO:
- ts_nullable_map
  - GoClientCodegen.java 의 postProcessModels 수정, FIX
- ts_number_prefix
  - 3GPPPSDataOffStatus 모델 생성 안됨, TODO:
- ts_oneof
- ts_ref_array
  - EnhancedDiagnostics5G 모델 생성 안됨, TODO:
- TS29542_Nsmf_NIDD
  - DeliverRequest 
    - multipart/related 에 대한 처리, TODO:
    - contentType 에 대한 처리, TODO:
    - model 에 mutlpart: 로 추가 여부, TODO:

### 2022/12/02

- upstream 의 Commits on Dec 1, 2022 까지 반영

### 2022/12/07

- upstream 의 Commits on Dec 7, 2022 까지 반영

### 2023/02/17

- upstream 의 Commits on Feb 17, 2023 까지 반영

### 2023/02/21

- upstream 의 Commits on Feb 21, 2023 까지 반영
- ParameterAddToHeaderOrQuery 확인은 udr_ad/client/api_influence_data_store.go

### 2023/04/24

- upstream 의 Commits on Apr 22, 2023 까지 반영
