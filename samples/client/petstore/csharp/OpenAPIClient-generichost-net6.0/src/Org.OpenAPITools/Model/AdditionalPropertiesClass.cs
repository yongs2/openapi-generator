// <auto-generated>
/*
 * OpenAPI Petstore
 *
 * This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\
 *
 * The version of the OpenAPI document: 1.0.0
 * Generated by: https://github.com/openapitools/openapi-generator.git
 */

using System;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;
using System.Text.Json;
using System.Text.Json.Serialization;
using System.ComponentModel.DataAnnotations;
using OpenAPIClientUtils = Org.OpenAPITools.Client.ClientUtils;

namespace Org.OpenAPITools.Model
{
    /// <summary>
    /// AdditionalPropertiesClass
    /// </summary>
    public partial class AdditionalPropertiesClass : IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="AdditionalPropertiesClass" /> class.
        /// </summary>
        /// <param name="emptyMap">an object with no declared properties and no undeclared properties, hence it&#39;s an empty map.</param>
        /// <param name="mapOfMapProperty">mapOfMapProperty</param>
        /// <param name="mapProperty">mapProperty</param>
        /// <param name="mapWithUndeclaredPropertiesAnytype1">mapWithUndeclaredPropertiesAnytype1</param>
        /// <param name="mapWithUndeclaredPropertiesAnytype2">mapWithUndeclaredPropertiesAnytype2</param>
        /// <param name="mapWithUndeclaredPropertiesAnytype3">mapWithUndeclaredPropertiesAnytype3</param>
        /// <param name="mapWithUndeclaredPropertiesString">mapWithUndeclaredPropertiesString</param>
        /// <param name="anytype1">anytype1</param>
        [JsonConstructor]
        public AdditionalPropertiesClass(Object emptyMap, Dictionary<string, Dictionary<string, string>> mapOfMapProperty, Dictionary<string, string> mapProperty, Object mapWithUndeclaredPropertiesAnytype1, Object mapWithUndeclaredPropertiesAnytype2, Dictionary<string, Object> mapWithUndeclaredPropertiesAnytype3, Dictionary<string, string> mapWithUndeclaredPropertiesString, Object anytype1 = default)
        {
            EmptyMap = emptyMap;
            MapOfMapProperty = mapOfMapProperty;
            MapProperty = mapProperty;
            MapWithUndeclaredPropertiesAnytype1 = mapWithUndeclaredPropertiesAnytype1;
            MapWithUndeclaredPropertiesAnytype2 = mapWithUndeclaredPropertiesAnytype2;
            MapWithUndeclaredPropertiesAnytype3 = mapWithUndeclaredPropertiesAnytype3;
            MapWithUndeclaredPropertiesString = mapWithUndeclaredPropertiesString;
            Anytype1 = anytype1;
            OnCreated();
        }

        partial void OnCreated();

        /// <summary>
        /// an object with no declared properties and no undeclared properties, hence it&#39;s an empty map.
        /// </summary>
        /// <value>an object with no declared properties and no undeclared properties, hence it&#39;s an empty map.</value>
        [JsonPropertyName("empty_map")]
        public Object EmptyMap { get; set; }

        /// <summary>
        /// Gets or Sets MapOfMapProperty
        /// </summary>
        [JsonPropertyName("map_of_map_property")]
        public Dictionary<string, Dictionary<string, string>> MapOfMapProperty { get; set; }

        /// <summary>
        /// Gets or Sets MapProperty
        /// </summary>
        [JsonPropertyName("map_property")]
        public Dictionary<string, string> MapProperty { get; set; }

        /// <summary>
        /// Gets or Sets MapWithUndeclaredPropertiesAnytype1
        /// </summary>
        [JsonPropertyName("map_with_undeclared_properties_anytype_1")]
        public Object MapWithUndeclaredPropertiesAnytype1 { get; set; }

        /// <summary>
        /// Gets or Sets MapWithUndeclaredPropertiesAnytype2
        /// </summary>
        [JsonPropertyName("map_with_undeclared_properties_anytype_2")]
        public Object MapWithUndeclaredPropertiesAnytype2 { get; set; }

        /// <summary>
        /// Gets or Sets MapWithUndeclaredPropertiesAnytype3
        /// </summary>
        [JsonPropertyName("map_with_undeclared_properties_anytype_3")]
        public Dictionary<string, Object> MapWithUndeclaredPropertiesAnytype3 { get; set; }

        /// <summary>
        /// Gets or Sets MapWithUndeclaredPropertiesString
        /// </summary>
        [JsonPropertyName("map_with_undeclared_properties_string")]
        public Dictionary<string, string> MapWithUndeclaredPropertiesString { get; set; }

        /// <summary>
        /// Gets or Sets Anytype1
        /// </summary>
        [JsonPropertyName("anytype_1")]
        public Object Anytype1 { get; set; }

        /// <summary>
        /// Gets or Sets additional properties
        /// </summary>
        [JsonExtensionData]
        public Dictionary<string, JsonElement> AdditionalProperties { get; } = new Dictionary<string, JsonElement>();

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            sb.Append("class AdditionalPropertiesClass {\n");
            sb.Append("  EmptyMap: ").Append(EmptyMap).Append("\n");
            sb.Append("  MapOfMapProperty: ").Append(MapOfMapProperty).Append("\n");
            sb.Append("  MapProperty: ").Append(MapProperty).Append("\n");
            sb.Append("  MapWithUndeclaredPropertiesAnytype1: ").Append(MapWithUndeclaredPropertiesAnytype1).Append("\n");
            sb.Append("  MapWithUndeclaredPropertiesAnytype2: ").Append(MapWithUndeclaredPropertiesAnytype2).Append("\n");
            sb.Append("  MapWithUndeclaredPropertiesAnytype3: ").Append(MapWithUndeclaredPropertiesAnytype3).Append("\n");
            sb.Append("  MapWithUndeclaredPropertiesString: ").Append(MapWithUndeclaredPropertiesString).Append("\n");
            sb.Append("  Anytype1: ").Append(Anytype1).Append("\n");
            sb.Append("  AdditionalProperties: ").Append(AdditionalProperties).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }

        /// <summary>
        /// To validate all properties of the instance
        /// </summary>
        /// <param name="validationContext">Validation context</param>
        /// <returns>Validation Result</returns>
        IEnumerable<System.ComponentModel.DataAnnotations.ValidationResult> IValidatableObject.Validate(ValidationContext validationContext)
        {
            yield break;
        }
    }

    /// <summary>
    /// A Json converter for type <see cref="AdditionalPropertiesClass" />
    /// </summary>
    public class AdditionalPropertiesClassJsonConverter : JsonConverter<AdditionalPropertiesClass>
    {
        /// <summary>
        /// Deserializes json to <see cref="AdditionalPropertiesClass" />
        /// </summary>
        /// <param name="utf8JsonReader"></param>
        /// <param name="typeToConvert"></param>
        /// <param name="jsonSerializerOptions"></param>
        /// <returns></returns>
        /// <exception cref="JsonException"></exception>
        public override AdditionalPropertiesClass Read(ref Utf8JsonReader utf8JsonReader, Type typeToConvert, JsonSerializerOptions jsonSerializerOptions)
        {
            int currentDepth = utf8JsonReader.CurrentDepth;

            if (utf8JsonReader.TokenType != JsonTokenType.StartObject && utf8JsonReader.TokenType != JsonTokenType.StartArray)
                throw new JsonException();

            JsonTokenType startingTokenType = utf8JsonReader.TokenType;

            Object emptyMap = default;
            Dictionary<string, Dictionary<string, string>> mapOfMapProperty = default;
            Dictionary<string, string> mapProperty = default;
            Object mapWithUndeclaredPropertiesAnytype1 = default;
            Object mapWithUndeclaredPropertiesAnytype2 = default;
            Dictionary<string, Object> mapWithUndeclaredPropertiesAnytype3 = default;
            Dictionary<string, string> mapWithUndeclaredPropertiesString = default;
            Object anytype1 = default;

            while (utf8JsonReader.Read())
            {
                if (startingTokenType == JsonTokenType.StartObject && utf8JsonReader.TokenType == JsonTokenType.EndObject && currentDepth == utf8JsonReader.CurrentDepth)
                    break;

                if (startingTokenType == JsonTokenType.StartArray && utf8JsonReader.TokenType == JsonTokenType.EndArray && currentDepth == utf8JsonReader.CurrentDepth)
                    break;

                if (utf8JsonReader.TokenType == JsonTokenType.PropertyName && currentDepth == utf8JsonReader.CurrentDepth - 1)
                {
                    string propertyName = utf8JsonReader.GetString();
                    utf8JsonReader.Read();

                    switch (propertyName)
                    {
                        case "empty_map":
                            if (utf8JsonReader.TokenType != JsonTokenType.Null)
                                emptyMap = JsonSerializer.Deserialize<Object>(ref utf8JsonReader, jsonSerializerOptions);
                            break;
                        case "map_of_map_property":
                            if (utf8JsonReader.TokenType != JsonTokenType.Null)
                                mapOfMapProperty = JsonSerializer.Deserialize<Dictionary<string, Dictionary<string, string>>>(ref utf8JsonReader, jsonSerializerOptions);
                            break;
                        case "map_property":
                            if (utf8JsonReader.TokenType != JsonTokenType.Null)
                                mapProperty = JsonSerializer.Deserialize<Dictionary<string, string>>(ref utf8JsonReader, jsonSerializerOptions);
                            break;
                        case "map_with_undeclared_properties_anytype_1":
                            if (utf8JsonReader.TokenType != JsonTokenType.Null)
                                mapWithUndeclaredPropertiesAnytype1 = JsonSerializer.Deserialize<Object>(ref utf8JsonReader, jsonSerializerOptions);
                            break;
                        case "map_with_undeclared_properties_anytype_2":
                            if (utf8JsonReader.TokenType != JsonTokenType.Null)
                                mapWithUndeclaredPropertiesAnytype2 = JsonSerializer.Deserialize<Object>(ref utf8JsonReader, jsonSerializerOptions);
                            break;
                        case "map_with_undeclared_properties_anytype_3":
                            if (utf8JsonReader.TokenType != JsonTokenType.Null)
                                mapWithUndeclaredPropertiesAnytype3 = JsonSerializer.Deserialize<Dictionary<string, Object>>(ref utf8JsonReader, jsonSerializerOptions);
                            break;
                        case "map_with_undeclared_properties_string":
                            if (utf8JsonReader.TokenType != JsonTokenType.Null)
                                mapWithUndeclaredPropertiesString = JsonSerializer.Deserialize<Dictionary<string, string>>(ref utf8JsonReader, jsonSerializerOptions);
                            break;
                        case "anytype_1":
                            if (utf8JsonReader.TokenType != JsonTokenType.Null)
                                anytype1 = JsonSerializer.Deserialize<Object>(ref utf8JsonReader, jsonSerializerOptions);
                            break;
                        default:
                            break;
                    }
                }
            }

            if (emptyMap == null)
                throw new ArgumentNullException(nameof(emptyMap), "Property is required for class AdditionalPropertiesClass.");

            if (mapOfMapProperty == null)
                throw new ArgumentNullException(nameof(mapOfMapProperty), "Property is required for class AdditionalPropertiesClass.");

            if (mapProperty == null)
                throw new ArgumentNullException(nameof(mapProperty), "Property is required for class AdditionalPropertiesClass.");

            if (mapWithUndeclaredPropertiesAnytype1 == null)
                throw new ArgumentNullException(nameof(mapWithUndeclaredPropertiesAnytype1), "Property is required for class AdditionalPropertiesClass.");

            if (mapWithUndeclaredPropertiesAnytype2 == null)
                throw new ArgumentNullException(nameof(mapWithUndeclaredPropertiesAnytype2), "Property is required for class AdditionalPropertiesClass.");

            if (mapWithUndeclaredPropertiesAnytype3 == null)
                throw new ArgumentNullException(nameof(mapWithUndeclaredPropertiesAnytype3), "Property is required for class AdditionalPropertiesClass.");

            if (mapWithUndeclaredPropertiesString == null)
                throw new ArgumentNullException(nameof(mapWithUndeclaredPropertiesString), "Property is required for class AdditionalPropertiesClass.");

            return new AdditionalPropertiesClass(emptyMap, mapOfMapProperty, mapProperty, mapWithUndeclaredPropertiesAnytype1, mapWithUndeclaredPropertiesAnytype2, mapWithUndeclaredPropertiesAnytype3, mapWithUndeclaredPropertiesString, anytype1);
        }

        /// <summary>
        /// Serializes a <see cref="AdditionalPropertiesClass" />
        /// </summary>
        /// <param name="writer"></param>
        /// <param name="additionalPropertiesClass"></param>
        /// <param name="jsonSerializerOptions"></param>
        /// <exception cref="NotImplementedException"></exception>
        public override void Write(Utf8JsonWriter writer, AdditionalPropertiesClass additionalPropertiesClass, JsonSerializerOptions jsonSerializerOptions)
        {
            writer.WriteStartObject();

            WriteProperties(ref writer, additionalPropertiesClass, jsonSerializerOptions);
            writer.WriteEndObject();
        }

        /// <summary>
        /// Serializes the properties of <see cref="AdditionalPropertiesClass" />
        /// </summary>
        /// <param name="writer"></param>
        /// <param name="additionalPropertiesClass"></param>
        /// <param name="jsonSerializerOptions"></param>
        /// <exception cref="NotImplementedException"></exception>
        public void WriteProperties(ref Utf8JsonWriter writer, AdditionalPropertiesClass additionalPropertiesClass, JsonSerializerOptions jsonSerializerOptions)
        {
            writer.WritePropertyName("empty_map");
            JsonSerializer.Serialize(writer, additionalPropertiesClass.EmptyMap, jsonSerializerOptions);            writer.WritePropertyName("map_of_map_property");
            JsonSerializer.Serialize(writer, additionalPropertiesClass.MapOfMapProperty, jsonSerializerOptions);            writer.WritePropertyName("map_property");
            JsonSerializer.Serialize(writer, additionalPropertiesClass.MapProperty, jsonSerializerOptions);            writer.WritePropertyName("map_with_undeclared_properties_anytype_1");
            JsonSerializer.Serialize(writer, additionalPropertiesClass.MapWithUndeclaredPropertiesAnytype1, jsonSerializerOptions);            writer.WritePropertyName("map_with_undeclared_properties_anytype_2");
            JsonSerializer.Serialize(writer, additionalPropertiesClass.MapWithUndeclaredPropertiesAnytype2, jsonSerializerOptions);            writer.WritePropertyName("map_with_undeclared_properties_anytype_3");
            JsonSerializer.Serialize(writer, additionalPropertiesClass.MapWithUndeclaredPropertiesAnytype3, jsonSerializerOptions);            writer.WritePropertyName("map_with_undeclared_properties_string");
            JsonSerializer.Serialize(writer, additionalPropertiesClass.MapWithUndeclaredPropertiesString, jsonSerializerOptions);            writer.WritePropertyName("anytype_1");
            JsonSerializer.Serialize(writer, additionalPropertiesClass.Anytype1, jsonSerializerOptions);
        }
    }
}
