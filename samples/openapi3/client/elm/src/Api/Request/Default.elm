{-
   Elm generator test
   No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

   The version of the OpenAPI document: 1.0.0

   NOTE: This file is auto generated by the openapi-generator.
   https://github.com/openapitools/openapi-generator.git

   DO NOT EDIT THIS FILE MANUALLY.

   For more info on generating Elm code, see https://eriktim.github.io/openapi-elm/
-}


module Api.Request.Default exposing
    ( headerPost, HeaderType(..), headerTypeVariants
    , maybeGet
    , pathStringIntegerEnumerationGet, Enumeration(..), enumerationVariants
    , queryGet, Enum(..), enumVariants
    , securedPost
    , uuidGet
    )

import Api
import Api.Data
import Dict
import Http
import Json.Decode
import Json.Encode
import Uuid exposing (Uuid)


type HeaderType
    = HeaderTypeLeft
    | HeaderTypeRight


headerTypeVariants : List HeaderType
headerTypeVariants =
    [ HeaderTypeLeft
    , HeaderTypeRight
    ]


stringFromHeaderType : HeaderType -> String
stringFromHeaderType model =
    case model of
        HeaderTypeLeft ->
            "left"

        HeaderTypeRight ->
            "right"




type Enumeration
    = EnumerationA
    | EnumerationB
    | EnumerationC


enumerationVariants : List Enumeration
enumerationVariants =
    [ EnumerationA
    , EnumerationB
    , EnumerationC
    ]


stringFromEnumeration : Enumeration -> String
stringFromEnumeration model =
    case model of
        EnumerationA ->
            "a"

        EnumerationB ->
            "b"

        EnumerationC ->
            "c"




type Enum
    = EnumA
    | EnumB
    | EnumC


enumVariants : List Enum
enumVariants =
    [ EnumA
    , EnumB
    , EnumC
    ]


stringFromEnum : Enum -> String
stringFromEnum model =
    case model of
        EnumA ->
            "a"

        EnumB ->
            "b"

        EnumC ->
            "c"





headerPost : String -> Maybe Int -> Maybe HeaderType -> Api.Request String
headerPost string_header integer_header headerType_header =
    Api.request
        "POST"
        "/header"
        []
        []
        [ ( "string", Just <| identity string_header ), ( "integer", Maybe.map String.fromInt integer_header ), ( "headerType", Maybe.map stringFromHeaderType headerType_header ) ]
        Nothing
        Json.Decode.string



maybeGet : Api.Request Api.Data.Maybe_
maybeGet =
    Api.request
        "GET"
        "/maybe"
        []
        []
        []
        Nothing
        Api.Data.maybeDecoder



pathStringIntegerEnumerationGet : String -> Int -> Enumeration -> Api.Request ()
pathStringIntegerEnumerationGet string_path integer_path enumeration_path =
    Api.request
        "GET"
        "/path/{string}/{integer}/{enumeration}"
        [ ( "string", identity string_path ), ( "integer", String.fromInt integer_path ), ( "enumeration", stringFromEnumeration enumeration_path ) ]
        []
        []
        Nothing
        (Json.Decode.succeed ())



queryGet : Maybe String -> Maybe Int -> Maybe Enum -> Api.Request ()
queryGet string_query int_query enum_query =
    Api.request
        "GET"
        "/query"
        []
        [ ( "string", Maybe.map identity string_query ), ( "int", Maybe.map String.fromInt int_query ), ( "enum", Maybe.map stringFromEnum enum_query ) ]
        []
        Nothing
        (Json.Decode.succeed ())



securedPost : String -> Api.Request ()
securedPost auth_token =
    Api.request
        "POST"
        "/secured"
        []
        []
        []
        Nothing
        (Json.Decode.succeed ())
        |> Api.withBearerToken auth_token



uuidGet : Maybe Uuid -> Api.Request Uuid
uuidGet value_query =
    Api.request
        "GET"
        "/uuid"
        []
        [ ( "value", Maybe.map identityUuid.toString value_query ) ]
        []
        Nothing
        Uuid.decoder
