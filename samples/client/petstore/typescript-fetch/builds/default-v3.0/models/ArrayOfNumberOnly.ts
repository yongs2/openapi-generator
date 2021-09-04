/* tslint:disable */
/* eslint-disable */
/**
 * OpenAPI Petstore
 * This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { exists, mapValues } from '../runtime';
/**
 * 
 * @export
 * @interface ArrayOfNumberOnly
 */
export interface ArrayOfNumberOnly {
    /**
     * 
     * @type {Array<number>}
     * @memberof ArrayOfNumberOnly
     */
    arrayNumber?: Array<number>;
}

export function ArrayOfNumberOnlyFromJSON(json: any): ArrayOfNumberOnly {
    return ArrayOfNumberOnlyFromJSONTyped(json, false);
}

export function ArrayOfNumberOnlyFromJSONTyped(json: any, ignoreDiscriminator: boolean): ArrayOfNumberOnly {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'arrayNumber': !exists(json, 'ArrayNumber') ? undefined : json['ArrayNumber'],
    };
}

export function ArrayOfNumberOnlyToJSON(value?: ArrayOfNumberOnly | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'ArrayNumber': value.arrayNumber,
    };
}

