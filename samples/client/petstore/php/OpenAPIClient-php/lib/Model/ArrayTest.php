<?php
/**
 * ArrayTest
 *
 * PHP version 7.4
 *
 * @category Class
 * @package  OpenAPI\Client
 * @author   OpenAPI Generator team
 * @link     https://openapi-generator.tech
 */

/**
 * OpenAPI Petstore
 *
 * This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\
 *
 * The version of the OpenAPI document: 1.0.0
 * Generated by: https://openapi-generator.tech
 * OpenAPI Generator version: 6.1.0-SNAPSHOT
 */

/**
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

namespace OpenAPI\Client\Model;

use \ArrayAccess;
use \OpenAPI\Client\ObjectSerializer;

/**
 * ArrayTest Class Doc Comment
 *
 * @category Class
 * @package  OpenAPI\Client
 * @author   OpenAPI Generator team
 * @link     https://openapi-generator.tech
 * @implements \ArrayAccess<string, mixed>
 */
class ArrayTest implements ModelInterface, ArrayAccess, \JsonSerializable
{
    public const DISCRIMINATOR = null;

    /**
      * The original name of the model.
      *
      * @var string
      */
    protected static $openAPIModelName = 'ArrayTest';

    /**
      * Array of property to type mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $openAPITypes = [
        'array_of_string' => 'string[]',
        'array_array_of_integer' => 'int[][]',
        'array_array_of_model' => '\OpenAPI\Client\Model\ReadOnlyFirst[][]'
    ];

    /**
      * Array of property to format mappings. Used for (de)serialization
      *
      * @var string[]
      * @phpstan-var array<string, string|null>
      * @psalm-var array<string, string|null>
      */
    protected static $openAPIFormats = [
        'array_of_string' => null,
        'array_array_of_integer' => 'int64',
        'array_array_of_model' => null
    ];

    /**
      * Array of nullable properties. Used for (de)serialization
      *
      * @var boolean[]
      */
    protected static array $openAPINullables = [
        'array_of_string' => false,
		'array_array_of_integer' => false,
		'array_array_of_model' => false
    ];

    /**
      * If a nullable field gets set to null, insert it here
      *
      * @var boolean[]
      */
    protected array $openAPINullablesSetToNull = [];

    /**
     * Array of property to type mappings. Used for (de)serialization
     *
     * @return array
     */
    public static function openAPITypes()
    {
        return self::$openAPITypes;
    }

    /**
     * Array of property to format mappings. Used for (de)serialization
     *
     * @return array
     */
    public static function openAPIFormats()
    {
        return self::$openAPIFormats;
    }

    /**
     * Array of nullable properties
     *
     * @return array
     */
    protected static function openAPINullables(): array
    {
        return self::$openAPINullables;
    }

    /**
     * Array of nullable field names deliberately set to null
     *
     * @return boolean[]
     */
    private function getOpenAPINullablesSetToNull(): array
    {
        return $this->openAPINullablesSetToNull;
    }

    /**
     * Checks if a property is nullable
     *
     * @param string $property
     * @return bool
     */
    public static function isNullable(string $property): bool
    {
        return self::openAPINullables()[$property] ?? false;
    }

    /**
     * Checks if a nullable property is set to null.
     *
     * @param string $property
     * @return bool
     */
    public function isNullableSetToNull(string $property): bool
    {
        return in_array($property, $this->getOpenAPINullablesSetToNull(), true);
    }

    /**
     * Array of attributes where the key is the local name,
     * and the value is the original name
     *
     * @var string[]
     */
    protected static $attributeMap = [
        'array_of_string' => 'array_of_string',
        'array_array_of_integer' => 'array_array_of_integer',
        'array_array_of_model' => 'array_array_of_model'
    ];

    /**
     * Array of attributes to setter functions (for deserialization of responses)
     *
     * @var string[]
     */
    protected static $setters = [
        'array_of_string' => 'setArrayOfString',
        'array_array_of_integer' => 'setArrayArrayOfInteger',
        'array_array_of_model' => 'setArrayArrayOfModel'
    ];

    /**
     * Array of attributes to getter functions (for serialization of requests)
     *
     * @var string[]
     */
    protected static $getters = [
        'array_of_string' => 'getArrayOfString',
        'array_array_of_integer' => 'getArrayArrayOfInteger',
        'array_array_of_model' => 'getArrayArrayOfModel'
    ];

    /**
     * Array of attributes where the key is the local name,
     * and the value is the original name
     *
     * @return array
     */
    public static function attributeMap()
    {
        return self::$attributeMap;
    }

    /**
     * Array of attributes to setter functions (for deserialization of responses)
     *
     * @return array
     */
    public static function setters()
    {
        return self::$setters;
    }

    /**
     * Array of attributes to getter functions (for serialization of requests)
     *
     * @return array
     */
    public static function getters()
    {
        return self::$getters;
    }

    /**
     * The original name of the model.
     *
     * @return string
     */
    public function getModelName()
    {
        return self::$openAPIModelName;
    }


    /**
     * Associative array for storing property values
     *
     * @var mixed[]
     */
    protected $container = [];

    /**
     * Constructor
     *
     * @param mixed[] $data Associated array of property values
     *                      initializing the model
     */
    public function __construct(array $data = null)
    {
        $this->setIfExists('array_of_string', $data ?? [], null);
        $this->setIfExists('array_array_of_integer', $data ?? [], null);
        $this->setIfExists('array_array_of_model', $data ?? [], null);
    }

    /**
    * Sets $this->container[$variableName] to the given data or to the given default Value; if $variableName
    * is nullable and its value is set to null in the $fields array, then mark it as "set to null" in the
    * $this->openAPINullablesSetToNull array
    *
    * @param string $variableName
    * @param array  $fields
    * @param mixed  $defaultValue
    */
    private function setIfExists(string $variableName, array $fields, $defaultValue): void
    {
        if (self::isNullable($variableName) && array_key_exists($variableName, $fields) && is_null($fields[$variableName])) {
            $this->openAPINullablesSetToNull[] = $variableName;
        }

        $this->container[$variableName] = $fields[$variableName] ?? $defaultValue;
    }

    /**
     * Show all the invalid properties with reasons.
     *
     * @return array invalid properties with reasons
     */
    public function listInvalidProperties()
    {
        $invalidProperties = [];

        if (!is_null($this->container['array_of_string']) && (count($this->container['array_of_string']) > 3)) {
            $invalidProperties[] = "invalid value for 'array_of_string', number of items must be less than or equal to 3.";
        }

        if (!is_null($this->container['array_of_string']) && (count($this->container['array_of_string']) < 0)) {
            $invalidProperties[] = "invalid value for 'array_of_string', number of items must be greater than or equal to 0.";
        }

        return $invalidProperties;
    }

    /**
     * Validate all the properties in the model
     * return true if all passed
     *
     * @return bool True if all properties are valid
     */
    public function valid()
    {
        return count($this->listInvalidProperties()) === 0;
    }


    /**
     * Gets array_of_string
     *
     * @return string[]|null
     */
    public function getArrayOfString()
    {
        return $this->container['array_of_string'];
    }

    /**
     * Sets array_of_string
     *
     * @param string[]|null $array_of_string array_of_string
     *
     * @return self
     */
    public function setArrayOfString($array_of_string)
    {

        if (!is_null($array_of_string) && (count($array_of_string) > 3)) {
            throw new \InvalidArgumentException('invalid value for $array_of_string when calling ArrayTest., number of items must be less than or equal to 3.');
        }
        if (!is_null($array_of_string) && (count($array_of_string) < 0)) {
            throw new \InvalidArgumentException('invalid length for $array_of_string when calling ArrayTest., number of items must be greater than or equal to 0.');
        }

        if (is_null($array_of_string)) {
            throw new \InvalidArgumentException('non-nullable array_of_string cannot be null');
        }

        $this->container['array_of_string'] = $array_of_string;

        return $this;
    }

    /**
     * Gets array_array_of_integer
     *
     * @return int[][]|null
     */
    public function getArrayArrayOfInteger()
    {
        return $this->container['array_array_of_integer'];
    }

    /**
     * Sets array_array_of_integer
     *
     * @param int[][]|null $array_array_of_integer array_array_of_integer
     *
     * @return self
     */
    public function setArrayArrayOfInteger($array_array_of_integer)
    {

        if (is_null($array_array_of_integer)) {
            throw new \InvalidArgumentException('non-nullable array_array_of_integer cannot be null');
        }

        $this->container['array_array_of_integer'] = $array_array_of_integer;

        return $this;
    }

    /**
     * Gets array_array_of_model
     *
     * @return \OpenAPI\Client\Model\ReadOnlyFirst[][]|null
     */
    public function getArrayArrayOfModel()
    {
        return $this->container['array_array_of_model'];
    }

    /**
     * Sets array_array_of_model
     *
     * @param \OpenAPI\Client\Model\ReadOnlyFirst[][]|null $array_array_of_model array_array_of_model
     *
     * @return self
     */
    public function setArrayArrayOfModel($array_array_of_model)
    {

        if (is_null($array_array_of_model)) {
            throw new \InvalidArgumentException('non-nullable array_array_of_model cannot be null');
        }

        $this->container['array_array_of_model'] = $array_array_of_model;

        return $this;
    }
    /**
     * Returns true if offset exists. False otherwise.
     *
     * @param integer $offset Offset
     *
     * @return boolean
     */
    public function offsetExists($offset): bool
    {
        return isset($this->container[$offset]);
    }

    /**
     * Gets offset.
     *
     * @param integer $offset Offset
     *
     * @return mixed|null
     */
    #[\ReturnTypeWillChange]
    public function offsetGet($offset)
    {
        return $this->container[$offset] ?? null;
    }

    /**
     * Sets value based on offset.
     *
     * @param int|null $offset Offset
     * @param mixed    $value  Value to be set
     *
     * @return void
     */
    public function offsetSet($offset, $value): void
    {
        if (is_null($offset)) {
            $this->container[] = $value;
        } else {
            $this->container[$offset] = $value;
        }
    }

    /**
     * Unsets offset.
     *
     * @param integer $offset Offset
     *
     * @return void
     */
    public function offsetUnset($offset): void
    {
        unset($this->container[$offset]);
    }

    /**
     * Serializes the object to a value that can be serialized natively by json_encode().
     * @link https://www.php.net/manual/en/jsonserializable.jsonserialize.php
     *
     * @return mixed Returns data which can be serialized by json_encode(), which is a value
     * of any type other than a resource.
     */
    #[\ReturnTypeWillChange]
    public function jsonSerialize()
    {
       return ObjectSerializer::sanitizeForSerialization($this);
    }

    /**
     * Gets the string presentation of the object
     *
     * @return string
     */
    public function __toString()
    {
        return json_encode(
            ObjectSerializer::sanitizeForSerialization($this),
            JSON_PRETTY_PRINT
        );
    }

    /**
     * Gets a header-safe presentation of the object
     *
     * @return string
     */
    public function toHeaderValue()
    {
        return json_encode(ObjectSerializer::sanitizeForSerialization($this));
    }
}


