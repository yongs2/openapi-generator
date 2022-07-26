# coding: utf-8

"""
    openapi 3.0.3 sample spec

    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""

from unit_test_api.api_client import ApiClient
from unit_test_api.api.content_type_json_api_endpoints.post_additionalproperties_allows_a_schema_which_should_validate_request_body import PostAdditionalpropertiesAllowsASchemaWhichShouldValidateRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_additionalproperties_allows_a_schema_which_should_validate_response_body_for_content_types import PostAdditionalpropertiesAllowsASchemaWhichShouldValidateResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_additionalproperties_are_allowed_by_default_request_body import PostAdditionalpropertiesAreAllowedByDefaultRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_additionalproperties_are_allowed_by_default_response_body_for_content_types import PostAdditionalpropertiesAreAllowedByDefaultResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_additionalproperties_can_exist_by_itself_request_body import PostAdditionalpropertiesCanExistByItselfRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_additionalproperties_can_exist_by_itself_response_body_for_content_types import PostAdditionalpropertiesCanExistByItselfResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_additionalproperties_should_not_look_in_applicators_request_body import PostAdditionalpropertiesShouldNotLookInApplicatorsRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_additionalproperties_should_not_look_in_applicators_response_body_for_content_types import PostAdditionalpropertiesShouldNotLookInApplicatorsResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_allof_combined_with_anyof_oneof_request_body import PostAllofCombinedWithAnyofOneofRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_allof_combined_with_anyof_oneof_response_body_for_content_types import PostAllofCombinedWithAnyofOneofResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_allof_request_body import PostAllofRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_allof_response_body_for_content_types import PostAllofResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_allof_simple_types_request_body import PostAllofSimpleTypesRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_allof_simple_types_response_body_for_content_types import PostAllofSimpleTypesResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_allof_with_base_schema_request_body import PostAllofWithBaseSchemaRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_allof_with_base_schema_response_body_for_content_types import PostAllofWithBaseSchemaResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_allof_with_one_empty_schema_request_body import PostAllofWithOneEmptySchemaRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_allof_with_one_empty_schema_response_body_for_content_types import PostAllofWithOneEmptySchemaResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_allof_with_the_first_empty_schema_request_body import PostAllofWithTheFirstEmptySchemaRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_allof_with_the_first_empty_schema_response_body_for_content_types import PostAllofWithTheFirstEmptySchemaResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_allof_with_the_last_empty_schema_request_body import PostAllofWithTheLastEmptySchemaRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_allof_with_the_last_empty_schema_response_body_for_content_types import PostAllofWithTheLastEmptySchemaResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_allof_with_two_empty_schemas_request_body import PostAllofWithTwoEmptySchemasRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_allof_with_two_empty_schemas_response_body_for_content_types import PostAllofWithTwoEmptySchemasResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_anyof_complex_types_request_body import PostAnyofComplexTypesRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_anyof_complex_types_response_body_for_content_types import PostAnyofComplexTypesResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_anyof_request_body import PostAnyofRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_anyof_response_body_for_content_types import PostAnyofResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_anyof_with_base_schema_request_body import PostAnyofWithBaseSchemaRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_anyof_with_base_schema_response_body_for_content_types import PostAnyofWithBaseSchemaResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_anyof_with_one_empty_schema_request_body import PostAnyofWithOneEmptySchemaRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_anyof_with_one_empty_schema_response_body_for_content_types import PostAnyofWithOneEmptySchemaResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_array_type_matches_arrays_request_body import PostArrayTypeMatchesArraysRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_array_type_matches_arrays_response_body_for_content_types import PostArrayTypeMatchesArraysResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_boolean_type_matches_booleans_request_body import PostBooleanTypeMatchesBooleansRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_boolean_type_matches_booleans_response_body_for_content_types import PostBooleanTypeMatchesBooleansResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_by_int_request_body import PostByIntRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_by_int_response_body_for_content_types import PostByIntResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_by_number_request_body import PostByNumberRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_by_number_response_body_for_content_types import PostByNumberResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_by_small_number_request_body import PostBySmallNumberRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_by_small_number_response_body_for_content_types import PostBySmallNumberResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_date_time_format_request_body import PostDateTimeFormatRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_date_time_format_response_body_for_content_types import PostDateTimeFormatResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_email_format_request_body import PostEmailFormatRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_email_format_response_body_for_content_types import PostEmailFormatResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_enum_with0_does_not_match_false_request_body import PostEnumWith0DoesNotMatchFalseRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_enum_with0_does_not_match_false_response_body_for_content_types import PostEnumWith0DoesNotMatchFalseResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_enum_with1_does_not_match_true_request_body import PostEnumWith1DoesNotMatchTrueRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_enum_with1_does_not_match_true_response_body_for_content_types import PostEnumWith1DoesNotMatchTrueResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_enum_with_escaped_characters_request_body import PostEnumWithEscapedCharactersRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_enum_with_escaped_characters_response_body_for_content_types import PostEnumWithEscapedCharactersResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_enum_with_false_does_not_match0_request_body import PostEnumWithFalseDoesNotMatch0RequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_enum_with_false_does_not_match0_response_body_for_content_types import PostEnumWithFalseDoesNotMatch0ResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_enum_with_true_does_not_match1_request_body import PostEnumWithTrueDoesNotMatch1RequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_enum_with_true_does_not_match1_response_body_for_content_types import PostEnumWithTrueDoesNotMatch1ResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_enums_in_properties_request_body import PostEnumsInPropertiesRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_enums_in_properties_response_body_for_content_types import PostEnumsInPropertiesResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_forbidden_property_request_body import PostForbiddenPropertyRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_forbidden_property_response_body_for_content_types import PostForbiddenPropertyResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_hostname_format_request_body import PostHostnameFormatRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_hostname_format_response_body_for_content_types import PostHostnameFormatResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_integer_type_matches_integers_request_body import PostIntegerTypeMatchesIntegersRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_integer_type_matches_integers_response_body_for_content_types import PostIntegerTypeMatchesIntegersResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_invalid_instance_should_not_raise_error_when_float_division_inf_request_body import PostInvalidInstanceShouldNotRaiseErrorWhenFloatDivisionInfRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_invalid_instance_should_not_raise_error_when_float_division_inf_response_body_for_content_types import PostInvalidInstanceShouldNotRaiseErrorWhenFloatDivisionInfResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_invalid_string_value_for_default_request_body import PostInvalidStringValueForDefaultRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_invalid_string_value_for_default_response_body_for_content_types import PostInvalidStringValueForDefaultResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_ipv4_format_request_body import PostIpv4FormatRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_ipv4_format_response_body_for_content_types import PostIpv4FormatResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_ipv6_format_request_body import PostIpv6FormatRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_ipv6_format_response_body_for_content_types import PostIpv6FormatResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_json_pointer_format_request_body import PostJsonPointerFormatRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_json_pointer_format_response_body_for_content_types import PostJsonPointerFormatResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_maximum_validation_request_body import PostMaximumValidationRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_maximum_validation_response_body_for_content_types import PostMaximumValidationResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_maximum_validation_with_unsigned_integer_request_body import PostMaximumValidationWithUnsignedIntegerRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_maximum_validation_with_unsigned_integer_response_body_for_content_types import PostMaximumValidationWithUnsignedIntegerResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_maxitems_validation_request_body import PostMaxitemsValidationRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_maxitems_validation_response_body_for_content_types import PostMaxitemsValidationResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_maxlength_validation_request_body import PostMaxlengthValidationRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_maxlength_validation_response_body_for_content_types import PostMaxlengthValidationResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_maxproperties0_means_the_object_is_empty_request_body import PostMaxproperties0MeansTheObjectIsEmptyRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_maxproperties0_means_the_object_is_empty_response_body_for_content_types import PostMaxproperties0MeansTheObjectIsEmptyResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_maxproperties_validation_request_body import PostMaxpropertiesValidationRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_maxproperties_validation_response_body_for_content_types import PostMaxpropertiesValidationResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_minimum_validation_request_body import PostMinimumValidationRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_minimum_validation_response_body_for_content_types import PostMinimumValidationResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_minimum_validation_with_signed_integer_request_body import PostMinimumValidationWithSignedIntegerRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_minimum_validation_with_signed_integer_response_body_for_content_types import PostMinimumValidationWithSignedIntegerResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_minitems_validation_request_body import PostMinitemsValidationRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_minitems_validation_response_body_for_content_types import PostMinitemsValidationResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_minlength_validation_request_body import PostMinlengthValidationRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_minlength_validation_response_body_for_content_types import PostMinlengthValidationResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_minproperties_validation_request_body import PostMinpropertiesValidationRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_minproperties_validation_response_body_for_content_types import PostMinpropertiesValidationResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_nested_allof_to_check_validation_semantics_request_body import PostNestedAllofToCheckValidationSemanticsRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_nested_allof_to_check_validation_semantics_response_body_for_content_types import PostNestedAllofToCheckValidationSemanticsResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_nested_anyof_to_check_validation_semantics_request_body import PostNestedAnyofToCheckValidationSemanticsRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_nested_anyof_to_check_validation_semantics_response_body_for_content_types import PostNestedAnyofToCheckValidationSemanticsResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_nested_items_request_body import PostNestedItemsRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_nested_items_response_body_for_content_types import PostNestedItemsResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_nested_oneof_to_check_validation_semantics_request_body import PostNestedOneofToCheckValidationSemanticsRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_nested_oneof_to_check_validation_semantics_response_body_for_content_types import PostNestedOneofToCheckValidationSemanticsResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_not_more_complex_schema_request_body import PostNotMoreComplexSchemaRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_not_more_complex_schema_response_body_for_content_types import PostNotMoreComplexSchemaResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_not_request_body import PostNotRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_not_response_body_for_content_types import PostNotResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_nul_characters_in_strings_request_body import PostNulCharactersInStringsRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_nul_characters_in_strings_response_body_for_content_types import PostNulCharactersInStringsResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_null_type_matches_only_the_null_object_request_body import PostNullTypeMatchesOnlyTheNullObjectRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_null_type_matches_only_the_null_object_response_body_for_content_types import PostNullTypeMatchesOnlyTheNullObjectResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_number_type_matches_numbers_request_body import PostNumberTypeMatchesNumbersRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_number_type_matches_numbers_response_body_for_content_types import PostNumberTypeMatchesNumbersResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_object_properties_validation_request_body import PostObjectPropertiesValidationRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_object_properties_validation_response_body_for_content_types import PostObjectPropertiesValidationResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_object_type_matches_objects_request_body import PostObjectTypeMatchesObjectsRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_object_type_matches_objects_response_body_for_content_types import PostObjectTypeMatchesObjectsResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_oneof_complex_types_request_body import PostOneofComplexTypesRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_oneof_complex_types_response_body_for_content_types import PostOneofComplexTypesResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_oneof_request_body import PostOneofRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_oneof_response_body_for_content_types import PostOneofResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_oneof_with_base_schema_request_body import PostOneofWithBaseSchemaRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_oneof_with_base_schema_response_body_for_content_types import PostOneofWithBaseSchemaResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_oneof_with_empty_schema_request_body import PostOneofWithEmptySchemaRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_oneof_with_empty_schema_response_body_for_content_types import PostOneofWithEmptySchemaResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_pattern_is_not_anchored_request_body import PostPatternIsNotAnchoredRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_pattern_is_not_anchored_response_body_for_content_types import PostPatternIsNotAnchoredResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_pattern_validation_request_body import PostPatternValidationRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_pattern_validation_response_body_for_content_types import PostPatternValidationResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_properties_with_escaped_characters_request_body import PostPropertiesWithEscapedCharactersRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_properties_with_escaped_characters_response_body_for_content_types import PostPropertiesWithEscapedCharactersResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_property_named_ref_that_is_not_a_reference_request_body import PostPropertyNamedRefThatIsNotAReferenceRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_property_named_ref_that_is_not_a_reference_response_body_for_content_types import PostPropertyNamedRefThatIsNotAReferenceResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_ref_in_additionalproperties_request_body import PostRefInAdditionalpropertiesRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_ref_in_additionalproperties_response_body_for_content_types import PostRefInAdditionalpropertiesResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_ref_in_allof_request_body import PostRefInAllofRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_ref_in_allof_response_body_for_content_types import PostRefInAllofResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_ref_in_anyof_request_body import PostRefInAnyofRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_ref_in_anyof_response_body_for_content_types import PostRefInAnyofResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_ref_in_items_request_body import PostRefInItemsRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_ref_in_items_response_body_for_content_types import PostRefInItemsResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_ref_in_oneof_request_body import PostRefInOneofRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_ref_in_oneof_response_body_for_content_types import PostRefInOneofResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_ref_in_property_request_body import PostRefInPropertyRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_ref_in_property_response_body_for_content_types import PostRefInPropertyResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_required_default_validation_request_body import PostRequiredDefaultValidationRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_required_default_validation_response_body_for_content_types import PostRequiredDefaultValidationResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_required_validation_request_body import PostRequiredValidationRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_required_validation_response_body_for_content_types import PostRequiredValidationResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_required_with_empty_array_request_body import PostRequiredWithEmptyArrayRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_required_with_empty_array_response_body_for_content_types import PostRequiredWithEmptyArrayResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_simple_enum_validation_request_body import PostSimpleEnumValidationRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_simple_enum_validation_response_body_for_content_types import PostSimpleEnumValidationResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_string_type_matches_strings_request_body import PostStringTypeMatchesStringsRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_string_type_matches_strings_response_body_for_content_types import PostStringTypeMatchesStringsResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_the_default_keyword_does_not_do_anything_if_the_property_is_missing_request_body import PostTheDefaultKeywordDoesNotDoAnythingIfThePropertyIsMissingRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_the_default_keyword_does_not_do_anything_if_the_property_is_missing_response_body_for_content_types import PostTheDefaultKeywordDoesNotDoAnythingIfThePropertyIsMissingResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_uniqueitems_false_validation_request_body import PostUniqueitemsFalseValidationRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_uniqueitems_false_validation_response_body_for_content_types import PostUniqueitemsFalseValidationResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_uniqueitems_validation_request_body import PostUniqueitemsValidationRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_uniqueitems_validation_response_body_for_content_types import PostUniqueitemsValidationResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_uri_format_request_body import PostUriFormatRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_uri_format_response_body_for_content_types import PostUriFormatResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_uri_reference_format_request_body import PostUriReferenceFormatRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_uri_reference_format_response_body_for_content_types import PostUriReferenceFormatResponseBodyForContentTypes
from unit_test_api.api.content_type_json_api_endpoints.post_uri_template_format_request_body import PostUriTemplateFormatRequestBody
from unit_test_api.api.content_type_json_api_endpoints.post_uri_template_format_response_body_for_content_types import PostUriTemplateFormatResponseBodyForContentTypes


class ContentTypeJsonApi(
    PostAdditionalpropertiesAllowsASchemaWhichShouldValidateRequestBody,
    PostAdditionalpropertiesAllowsASchemaWhichShouldValidateResponseBodyForContentTypes,
    PostAdditionalpropertiesAreAllowedByDefaultRequestBody,
    PostAdditionalpropertiesAreAllowedByDefaultResponseBodyForContentTypes,
    PostAdditionalpropertiesCanExistByItselfRequestBody,
    PostAdditionalpropertiesCanExistByItselfResponseBodyForContentTypes,
    PostAdditionalpropertiesShouldNotLookInApplicatorsRequestBody,
    PostAdditionalpropertiesShouldNotLookInApplicatorsResponseBodyForContentTypes,
    PostAllofCombinedWithAnyofOneofRequestBody,
    PostAllofCombinedWithAnyofOneofResponseBodyForContentTypes,
    PostAllofRequestBody,
    PostAllofResponseBodyForContentTypes,
    PostAllofSimpleTypesRequestBody,
    PostAllofSimpleTypesResponseBodyForContentTypes,
    PostAllofWithBaseSchemaRequestBody,
    PostAllofWithBaseSchemaResponseBodyForContentTypes,
    PostAllofWithOneEmptySchemaRequestBody,
    PostAllofWithOneEmptySchemaResponseBodyForContentTypes,
    PostAllofWithTheFirstEmptySchemaRequestBody,
    PostAllofWithTheFirstEmptySchemaResponseBodyForContentTypes,
    PostAllofWithTheLastEmptySchemaRequestBody,
    PostAllofWithTheLastEmptySchemaResponseBodyForContentTypes,
    PostAllofWithTwoEmptySchemasRequestBody,
    PostAllofWithTwoEmptySchemasResponseBodyForContentTypes,
    PostAnyofComplexTypesRequestBody,
    PostAnyofComplexTypesResponseBodyForContentTypes,
    PostAnyofRequestBody,
    PostAnyofResponseBodyForContentTypes,
    PostAnyofWithBaseSchemaRequestBody,
    PostAnyofWithBaseSchemaResponseBodyForContentTypes,
    PostAnyofWithOneEmptySchemaRequestBody,
    PostAnyofWithOneEmptySchemaResponseBodyForContentTypes,
    PostArrayTypeMatchesArraysRequestBody,
    PostArrayTypeMatchesArraysResponseBodyForContentTypes,
    PostBooleanTypeMatchesBooleansRequestBody,
    PostBooleanTypeMatchesBooleansResponseBodyForContentTypes,
    PostByIntRequestBody,
    PostByIntResponseBodyForContentTypes,
    PostByNumberRequestBody,
    PostByNumberResponseBodyForContentTypes,
    PostBySmallNumberRequestBody,
    PostBySmallNumberResponseBodyForContentTypes,
    PostDateTimeFormatRequestBody,
    PostDateTimeFormatResponseBodyForContentTypes,
    PostEmailFormatRequestBody,
    PostEmailFormatResponseBodyForContentTypes,
    PostEnumWith0DoesNotMatchFalseRequestBody,
    PostEnumWith0DoesNotMatchFalseResponseBodyForContentTypes,
    PostEnumWith1DoesNotMatchTrueRequestBody,
    PostEnumWith1DoesNotMatchTrueResponseBodyForContentTypes,
    PostEnumWithEscapedCharactersRequestBody,
    PostEnumWithEscapedCharactersResponseBodyForContentTypes,
    PostEnumWithFalseDoesNotMatch0RequestBody,
    PostEnumWithFalseDoesNotMatch0ResponseBodyForContentTypes,
    PostEnumWithTrueDoesNotMatch1RequestBody,
    PostEnumWithTrueDoesNotMatch1ResponseBodyForContentTypes,
    PostEnumsInPropertiesRequestBody,
    PostEnumsInPropertiesResponseBodyForContentTypes,
    PostForbiddenPropertyRequestBody,
    PostForbiddenPropertyResponseBodyForContentTypes,
    PostHostnameFormatRequestBody,
    PostHostnameFormatResponseBodyForContentTypes,
    PostIntegerTypeMatchesIntegersRequestBody,
    PostIntegerTypeMatchesIntegersResponseBodyForContentTypes,
    PostInvalidInstanceShouldNotRaiseErrorWhenFloatDivisionInfRequestBody,
    PostInvalidInstanceShouldNotRaiseErrorWhenFloatDivisionInfResponseBodyForContentTypes,
    PostInvalidStringValueForDefaultRequestBody,
    PostInvalidStringValueForDefaultResponseBodyForContentTypes,
    PostIpv4FormatRequestBody,
    PostIpv4FormatResponseBodyForContentTypes,
    PostIpv6FormatRequestBody,
    PostIpv6FormatResponseBodyForContentTypes,
    PostJsonPointerFormatRequestBody,
    PostJsonPointerFormatResponseBodyForContentTypes,
    PostMaximumValidationRequestBody,
    PostMaximumValidationResponseBodyForContentTypes,
    PostMaximumValidationWithUnsignedIntegerRequestBody,
    PostMaximumValidationWithUnsignedIntegerResponseBodyForContentTypes,
    PostMaxitemsValidationRequestBody,
    PostMaxitemsValidationResponseBodyForContentTypes,
    PostMaxlengthValidationRequestBody,
    PostMaxlengthValidationResponseBodyForContentTypes,
    PostMaxproperties0MeansTheObjectIsEmptyRequestBody,
    PostMaxproperties0MeansTheObjectIsEmptyResponseBodyForContentTypes,
    PostMaxpropertiesValidationRequestBody,
    PostMaxpropertiesValidationResponseBodyForContentTypes,
    PostMinimumValidationRequestBody,
    PostMinimumValidationResponseBodyForContentTypes,
    PostMinimumValidationWithSignedIntegerRequestBody,
    PostMinimumValidationWithSignedIntegerResponseBodyForContentTypes,
    PostMinitemsValidationRequestBody,
    PostMinitemsValidationResponseBodyForContentTypes,
    PostMinlengthValidationRequestBody,
    PostMinlengthValidationResponseBodyForContentTypes,
    PostMinpropertiesValidationRequestBody,
    PostMinpropertiesValidationResponseBodyForContentTypes,
    PostNestedAllofToCheckValidationSemanticsRequestBody,
    PostNestedAllofToCheckValidationSemanticsResponseBodyForContentTypes,
    PostNestedAnyofToCheckValidationSemanticsRequestBody,
    PostNestedAnyofToCheckValidationSemanticsResponseBodyForContentTypes,
    PostNestedItemsRequestBody,
    PostNestedItemsResponseBodyForContentTypes,
    PostNestedOneofToCheckValidationSemanticsRequestBody,
    PostNestedOneofToCheckValidationSemanticsResponseBodyForContentTypes,
    PostNotMoreComplexSchemaRequestBody,
    PostNotMoreComplexSchemaResponseBodyForContentTypes,
    PostNotRequestBody,
    PostNotResponseBodyForContentTypes,
    PostNulCharactersInStringsRequestBody,
    PostNulCharactersInStringsResponseBodyForContentTypes,
    PostNullTypeMatchesOnlyTheNullObjectRequestBody,
    PostNullTypeMatchesOnlyTheNullObjectResponseBodyForContentTypes,
    PostNumberTypeMatchesNumbersRequestBody,
    PostNumberTypeMatchesNumbersResponseBodyForContentTypes,
    PostObjectPropertiesValidationRequestBody,
    PostObjectPropertiesValidationResponseBodyForContentTypes,
    PostObjectTypeMatchesObjectsRequestBody,
    PostObjectTypeMatchesObjectsResponseBodyForContentTypes,
    PostOneofComplexTypesRequestBody,
    PostOneofComplexTypesResponseBodyForContentTypes,
    PostOneofRequestBody,
    PostOneofResponseBodyForContentTypes,
    PostOneofWithBaseSchemaRequestBody,
    PostOneofWithBaseSchemaResponseBodyForContentTypes,
    PostOneofWithEmptySchemaRequestBody,
    PostOneofWithEmptySchemaResponseBodyForContentTypes,
    PostPatternIsNotAnchoredRequestBody,
    PostPatternIsNotAnchoredResponseBodyForContentTypes,
    PostPatternValidationRequestBody,
    PostPatternValidationResponseBodyForContentTypes,
    PostPropertiesWithEscapedCharactersRequestBody,
    PostPropertiesWithEscapedCharactersResponseBodyForContentTypes,
    PostPropertyNamedRefThatIsNotAReferenceRequestBody,
    PostPropertyNamedRefThatIsNotAReferenceResponseBodyForContentTypes,
    PostRefInAdditionalpropertiesRequestBody,
    PostRefInAdditionalpropertiesResponseBodyForContentTypes,
    PostRefInAllofRequestBody,
    PostRefInAllofResponseBodyForContentTypes,
    PostRefInAnyofRequestBody,
    PostRefInAnyofResponseBodyForContentTypes,
    PostRefInItemsRequestBody,
    PostRefInItemsResponseBodyForContentTypes,
    PostRefInOneofRequestBody,
    PostRefInOneofResponseBodyForContentTypes,
    PostRefInPropertyRequestBody,
    PostRefInPropertyResponseBodyForContentTypes,
    PostRequiredDefaultValidationRequestBody,
    PostRequiredDefaultValidationResponseBodyForContentTypes,
    PostRequiredValidationRequestBody,
    PostRequiredValidationResponseBodyForContentTypes,
    PostRequiredWithEmptyArrayRequestBody,
    PostRequiredWithEmptyArrayResponseBodyForContentTypes,
    PostSimpleEnumValidationRequestBody,
    PostSimpleEnumValidationResponseBodyForContentTypes,
    PostStringTypeMatchesStringsRequestBody,
    PostStringTypeMatchesStringsResponseBodyForContentTypes,
    PostTheDefaultKeywordDoesNotDoAnythingIfThePropertyIsMissingRequestBody,
    PostTheDefaultKeywordDoesNotDoAnythingIfThePropertyIsMissingResponseBodyForContentTypes,
    PostUniqueitemsFalseValidationRequestBody,
    PostUniqueitemsFalseValidationResponseBodyForContentTypes,
    PostUniqueitemsValidationRequestBody,
    PostUniqueitemsValidationResponseBodyForContentTypes,
    PostUriFormatRequestBody,
    PostUriFormatResponseBodyForContentTypes,
    PostUriReferenceFormatRequestBody,
    PostUriReferenceFormatResponseBodyForContentTypes,
    PostUriTemplateFormatRequestBody,
    PostUriTemplateFormatResponseBodyForContentTypes,
    ApiClient,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
