/*
OpenAPI Petstore

This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\

API version: 1.0.0
*/

// Code generated by OpenAPI Generator (https://openapi-generator.tech); DO NOT EDIT.

package petstore

import (
	"encoding/json"
	"reflect"
	"strings"
)

// Cat struct for Cat
type Cat struct {
	Animal
	Declawed *bool `json:"declawed,omitempty"`
	AdditionalProperties map[string]interface{}
}

type _Cat Cat

// NewCat instantiates a new Cat object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewCat(className string) *Cat {
	this := Cat{}
	this.ClassName = className
	var color string = "red"
	this.Color = &color
	return &this
}

// NewCatWithDefaults instantiates a new Cat object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewCatWithDefaults() *Cat {
	this := Cat{}
	return &this
}

// GetDeclawed returns the Declawed field value if set, zero value otherwise.
func (o *Cat) GetDeclawed() bool {
	if o == nil || isNil(o.Declawed) {
		var ret bool
		return ret
	}
	return *o.Declawed
}

// GetDeclawedOk returns a tuple with the Declawed field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Cat) GetDeclawedOk() (*bool, bool) {
	if o == nil || isNil(o.Declawed) {
		return nil, false
	}
	return o.Declawed, true
}

// HasDeclawed returns a boolean if a field has been set.
func (o *Cat) HasDeclawed() bool {
	if o != nil && !isNil(o.Declawed) {
		return true
	}

	return false
}

// SetDeclawed gets a reference to the given bool and assigns it to the Declawed field.
func (o *Cat) SetDeclawed(v bool) {
	o.Declawed = &v
}

func (o Cat) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]interface{}{}
	serializedAnimal, errAnimal := json.Marshal(o.Animal)
	if errAnimal != nil {
		return []byte{}, errAnimal
	}
	errAnimal = json.Unmarshal([]byte(serializedAnimal), &toSerialize)
	if errAnimal != nil {
		return []byte{}, errAnimal
	}
	if !isNil(o.Declawed) {
		toSerialize["declawed"] = o.Declawed
	}

	for key, value := range o.AdditionalProperties {
		toSerialize[key] = value
	}

	return json.Marshal(toSerialize)
}

func (o *Cat) UnmarshalJSON(bytes []byte) (err error) {
	type CatWithoutEmbeddedStruct struct {
		Declawed *bool `json:"declawed,omitempty"`
	}

	varCatWithoutEmbeddedStruct := CatWithoutEmbeddedStruct{}

	err = json.Unmarshal(bytes, &varCatWithoutEmbeddedStruct)
	if err == nil {
		varCat := _Cat{}
		varCat.Declawed = varCatWithoutEmbeddedStruct.Declawed
		*o = Cat(varCat)
	} else {
		return err
	}

	varCat := _Cat{}

	err = json.Unmarshal(bytes, &varCat)
	if err == nil {
		o.Animal = varCat.Animal
	} else {
		return err
	}

	additionalProperties := make(map[string]interface{})

	if err = json.Unmarshal(bytes, &additionalProperties); err == nil {
		delete(additionalProperties, "declawed")

		// remove fields from embedded structs
		reflectAnimal := reflect.ValueOf(o.Animal)
		for i := 0; i < reflectAnimal.Type().NumField(); i++ {
			t := reflectAnimal.Type().Field(i)

			if jsonTag := t.Tag.Get("json"); jsonTag != "" {
				fieldName := ""
				if commaIdx := strings.Index(jsonTag, ","); commaIdx > 0 {
					fieldName = jsonTag[:commaIdx]
				} else {
					fieldName = jsonTag
				}
				if fieldName != "AdditionalProperties" {
					delete(additionalProperties, fieldName)
				}
			}
		}

		o.AdditionalProperties = additionalProperties
	}

	return err
}

type NullableCat struct {
	value *Cat
	isSet bool
}

func (v NullableCat) Get() *Cat {
	return v.value
}

func (v *NullableCat) Set(val *Cat) {
	v.value = val
	v.isSet = true
}

func (v NullableCat) IsSet() bool {
	return v.isSet
}

func (v *NullableCat) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableCat(val *Cat) *NullableCat {
	return &NullableCat{value: val, isSet: true}
}

func (v NullableCat) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableCat) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}


