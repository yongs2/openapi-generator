/*
OpenAPI Petstore

This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\

API version: 1.0.0
*/

// Code generated by OpenAPI Generator (https://openapi-generator.tech); DO NOT EDIT.

package petstore

import (
	"encoding/json"
)

// Client struct for Client
type Client struct {
	Client *string `json:"client,omitempty"`
	AdditionalProperties map[string]interface{}
}

type _Client Client

// NewClient instantiates a new Client object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewClient() *Client {
	this := Client{}
	return &this
}

// NewClientWithDefaults instantiates a new Client object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewClientWithDefaults() *Client {
	this := Client{}
	return &this
}

// GetClient returns the Client field value if set, zero value otherwise.
func (o *Client) GetClient() string {
	if o == nil || isNil(o.Client) {
		var ret string
		return ret
	}
	return *o.Client
}

// GetClientOk returns a tuple with the Client field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Client) GetClientOk() (*string, bool) {
	if o == nil || isNil(o.Client) {
    return nil, false
	}
	return o.Client, true
}

// HasClient returns a boolean if a field has been set.
func (o *Client) HasClient() bool {
	if o != nil && !isNil(o.Client) {
		return true
	}

	return false
}

// SetClient gets a reference to the given string and assigns it to the Client field.
func (o *Client) SetClient(v string) {
	o.Client = &v
}

func (o Client) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]interface{}{}
	if !isNil(o.Client) {
		toSerialize["client"] = o.Client
	}

	for key, value := range o.AdditionalProperties {
		toSerialize[key] = value
	}

	return json.Marshal(toSerialize)
}

func (o *Client) UnmarshalJSON(bytes []byte) (err error) {
	varClient := _Client{}

	if err = json.Unmarshal(bytes, &varClient); err == nil {
		*o = Client(varClient)
	}

	additionalProperties := make(map[string]interface{})

	if err = json.Unmarshal(bytes, &additionalProperties); err == nil {
		delete(additionalProperties, "client")
		o.AdditionalProperties = additionalProperties
	}

	return err
}

type NullableClient struct {
	value *Client
	isSet bool
}

func (v NullableClient) Get() *Client {
	return v.value
}

func (v *NullableClient) Set(val *Client) {
	v.value = val
	v.isSet = true
}

func (v NullableClient) IsSet() bool {
	return v.isSet
}

func (v *NullableClient) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableClient(val *Client) *NullableClient {
	return &NullableClient{value: val, isSet: true}
}

func (v NullableClient) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableClient) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}


