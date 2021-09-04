/*
OpenAPI Petstore

This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\

API version: 1.0.0
*/

// Code generated by OpenAPI Generator (https://openapi-generator.tech); DO NOT EDIT.

package petstore

import (
	"bytes"
	_context "context"
	_ioutil "io/ioutil"
	_nethttp "net/http"
	_neturl "net/url"
)

// Linger please
var (
	_ _context.Context
)

type AnotherFakeApi interface {

	/*
	Call123TestSpecialTags To test special tags

	To test special tags and operation ID starting with number

	 @param ctx _context.Context - for authentication, logging, cancellation, deadlines, tracing, etc. Passed from http.Request or context.Background().
	 @return ApiCall123TestSpecialTagsRequest
	*/
	Call123TestSpecialTags(ctx _context.Context) ApiCall123TestSpecialTagsRequest

	// Call123TestSpecialTagsExecute executes the request
	//  @return Client
	Call123TestSpecialTagsExecute(r ApiCall123TestSpecialTagsRequest) (Client, *_nethttp.Response, error)
}

// AnotherFakeApiService AnotherFakeApi service
type AnotherFakeApiService service

type ApiCall123TestSpecialTagsRequest struct {
	ctx _context.Context
	ApiService AnotherFakeApi
	body *Client
}

// client model
func (r ApiCall123TestSpecialTagsRequest) Body(body Client) ApiCall123TestSpecialTagsRequest {
	r.body = &body
	return r
}

func (r ApiCall123TestSpecialTagsRequest) Execute() (Client, *_nethttp.Response, error) {
	return r.ApiService.Call123TestSpecialTagsExecute(r)
}

/*
Call123TestSpecialTags To test special tags

To test special tags and operation ID starting with number

 @param ctx _context.Context - for authentication, logging, cancellation, deadlines, tracing, etc. Passed from http.Request or context.Background().
 @return ApiCall123TestSpecialTagsRequest
*/
func (a *AnotherFakeApiService) Call123TestSpecialTags(ctx _context.Context) ApiCall123TestSpecialTagsRequest {
	return ApiCall123TestSpecialTagsRequest{
		ApiService: a,
		ctx: ctx,
	}
}

// Execute executes the request
//  @return Client
func (a *AnotherFakeApiService) Call123TestSpecialTagsExecute(r ApiCall123TestSpecialTagsRequest) (Client, *_nethttp.Response, error) {
	var (
		localVarHTTPMethod   = _nethttp.MethodPatch
		localVarPostBody     interface{}
		localVarFormFileName string
		localVarFileName     string
		localVarFileBytes    []byte
		localVarReturnValue  Client
	)

	localBasePath, err := a.client.cfg.ServerURLWithContext(r.ctx, "AnotherFakeApiService.Call123TestSpecialTags")
	if err != nil {
		return localVarReturnValue, nil, GenericOpenAPIError{error: err.Error()}
	}

	localVarPath := localBasePath + "/another-fake/dummy"

	localVarHeaderParams := make(map[string]string)
	localVarQueryParams := _neturl.Values{}
	localVarFormParams := _neturl.Values{}
	if r.body == nil {
		return localVarReturnValue, nil, reportError("body is required and must be specified")
	}

	// to determine the Content-Type header
	localVarHTTPContentTypes := []string{"application/json"}

	// set Content-Type header
	localVarHTTPContentType := selectHeaderContentType(localVarHTTPContentTypes)
	if localVarHTTPContentType != "" {
		localVarHeaderParams["Content-Type"] = localVarHTTPContentType
	}

	// to determine the Accept header
	localVarHTTPHeaderAccepts := []string{"application/json"}

	// set Accept header
	localVarHTTPHeaderAccept := selectHeaderAccept(localVarHTTPHeaderAccepts)
	if localVarHTTPHeaderAccept != "" {
		localVarHeaderParams["Accept"] = localVarHTTPHeaderAccept
	}
	// body params
	localVarPostBody = r.body
	req, err := a.client.prepareRequest(r.ctx, localVarPath, localVarHTTPMethod, localVarPostBody, localVarHeaderParams, localVarQueryParams, localVarFormParams, localVarFormFileName, localVarFileName, localVarFileBytes)
	if err != nil {
		return localVarReturnValue, nil, err
	}

	localVarHTTPResponse, err := a.client.callAPI(req)
	if err != nil || localVarHTTPResponse == nil {
		return localVarReturnValue, localVarHTTPResponse, err
	}

	localVarBody, err := _ioutil.ReadAll(localVarHTTPResponse.Body)
	localVarHTTPResponse.Body.Close()
	localVarHTTPResponse.Body = _ioutil.NopCloser(bytes.NewBuffer(localVarBody))
	if err != nil {
		return localVarReturnValue, localVarHTTPResponse, err
	}

	if localVarHTTPResponse.StatusCode >= 300 {
		newErr := GenericOpenAPIError{
			body:  localVarBody,
			error: localVarHTTPResponse.Status,
		}
		return localVarReturnValue, localVarHTTPResponse, newErr
	}

	err = a.client.decode(&localVarReturnValue, localVarBody, localVarHTTPResponse.Header.Get("Content-Type"))
	if err != nil {
		newErr := GenericOpenAPIError{
			body:  localVarBody,
			error: err.Error(),
		}
		return localVarReturnValue, localVarHTTPResponse, newErr
	}

	return localVarReturnValue, localVarHTTPResponse, nil
}
