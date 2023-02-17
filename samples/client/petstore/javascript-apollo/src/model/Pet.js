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
 *
 */

import ApiClient from '../ApiClient';
import Category from './Category';
import Tag from './Tag';

/**
 * The Pet model module.
 * @module model/Pet
 * @version 1.0.0
 */
class Pet {
    /**
     * Constructs a new <code>Pet</code>.
     * @alias module:model/Pet
     * @param name {String} 
     * @param photoUrls {Array.<String>} 
     */
    constructor(name, photoUrls) { 
        
        Pet.initialize(this, name, photoUrls);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, name, photoUrls) { 
        obj['name'] = name;
        obj['photoUrls'] = photoUrls;
    }

    /**
     * Constructs a <code>Pet</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Pet} obj Optional instance to populate.
     * @return {module:model/Pet} The populated <code>Pet</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Pet();

            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('category')) {
                obj['category'] = Category.constructFromObject(data['category']);
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('photoUrls')) {
                obj['photoUrls'] = ApiClient.convertToType(data['photoUrls'], ['String']);
            }
            if (data.hasOwnProperty('tags')) {
                obj['tags'] = ApiClient.convertToType(data['tags'], [Tag]);
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Pet</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Pet</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Pet.RequiredProperties) {
            if (!data[property]) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `category`
        if (data['category']) { // data not null
          Category.validateJSON(data['category']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['photoUrls'])) {
            throw new Error("Expected the field `photoUrls` to be an array in the JSON data but got " + data['photoUrls']);
        }
        if (data['tags']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['tags'])) {
                throw new Error("Expected the field `tags` to be an array in the JSON data but got " + data['tags']);
            }
            // validate the optional field `tags` (array)
            for (const item of data['tags']) {
                Tag.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }

        return true;
    }


}

Pet.RequiredProperties = ["name", "photoUrls"];

/**
 * @member {Number} id
 */
Pet.prototype['id'] = undefined;

/**
 * @member {module:model/Category} category
 */
Pet.prototype['category'] = undefined;

/**
 * @member {String} name
 */
Pet.prototype['name'] = undefined;

/**
 * @member {Array.<String>} photoUrls
 */
Pet.prototype['photoUrls'] = undefined;

/**
 * @member {Array.<module:model/Tag>} tags
 */
Pet.prototype['tags'] = undefined;

/**
 * pet status in the store
 * @member {module:model/Pet.StatusEnum} status
 */
Pet.prototype['status'] = undefined;





/**
 * Allowed values for the <code>status</code> property.
 * @enum {String}
 * @readonly
 */
Pet['StatusEnum'] = {

    /**
     * value: "available"
     * @const
     */
    "available": "available",

    /**
     * value: "pending"
     * @const
     */
    "pending": "pending",

    /**
     * value: "sold"
     * @const
     */
    "sold": "sold"
};



export default Pet;

