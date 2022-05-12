/**
 * OpenAPI Petstore
 *
 * This is a sample server Petstore server. For this sample, you can use the api key `special-key` to test the authorization filters.
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * Please note:
 * This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * Do not edit this file manually.
 */

@file:Suppress(
    "ArrayInDataClass",
    "EnumEntryName",
    "RemoveRedundantQualifierName",
    "UnusedImport"
)

package org.openapitools.client.apis

import java.io.IOException

import org.openapitools.client.models.ModelApiResponse
import org.openapitools.client.models.Pet

import com.squareup.moshi.Json

import org.openapitools.client.infrastructure.ApiClient
import org.openapitools.client.infrastructure.ApiResponse
import org.openapitools.client.infrastructure.ClientException
import org.openapitools.client.infrastructure.ClientError
import org.openapitools.client.infrastructure.ServerException
import org.openapitools.client.infrastructure.ServerError
import org.openapitools.client.infrastructure.MultiValueMap
import org.openapitools.client.infrastructure.PartConfig
import org.openapitools.client.infrastructure.RequestConfig
import org.openapitools.client.infrastructure.RequestMethod
import org.openapitools.client.infrastructure.ResponseType
import org.openapitools.client.infrastructure.Success
import org.openapitools.client.infrastructure.toMultiValue

class PetApi(basePath: kotlin.String = defaultBasePath) : ApiClient(basePath) {
    companion object {
        @JvmStatic
        val defaultBasePath: String by lazy {
            System.getProperties().getProperty(ApiClient.baseUrlKey, "http://petstore.swagger.io/v2")
        }
    }

    /**
     * Add a new pet to the store
     * 
     * @param body Pet object that needs to be added to the store
     * @return void
     * @throws IllegalStateException If the request is not correctly configured
     * @throws IOException Rethrows the OkHttp execute method exception
     * @throws UnsupportedOperationException If the API returns an informational or redirection response
     * @throws ClientException If the API returns a client error response
     * @throws ServerException If the API returns a server error response
     */
    @Throws(IllegalStateException::class, IOException::class, UnsupportedOperationException::class, ClientException::class, ServerException::class)
    fun addPet(body: Pet) : Unit {
        val localVarResponse = addPetWithHttpInfo(body = body)

        return when (localVarResponse.responseType) {
            ResponseType.Success -> Unit
            ResponseType.Informational -> throw UnsupportedOperationException("Client does not support Informational responses.")
            ResponseType.Redirection -> throw UnsupportedOperationException("Client does not support Redirection responses.")
            ResponseType.ClientError -> {
                val localVarError = localVarResponse as ClientError<*>
                throw ClientException("Client error : ${localVarError.statusCode} ${localVarError.message.orEmpty()}", localVarError.statusCode, localVarResponse)
            }
            ResponseType.ServerError -> {
                val localVarError = localVarResponse as ServerError<*>
                throw ServerException("Server error : ${localVarError.statusCode} ${localVarError.message.orEmpty()}", localVarError.statusCode, localVarResponse)
            }
        }
    }

    /**
     * Add a new pet to the store
     * 
     * @param body Pet object that needs to be added to the store
     * @return ApiResponse<Unit?>
     * @throws IllegalStateException If the request is not correctly configured
     * @throws IOException Rethrows the OkHttp execute method exception
     */
    @Throws(IllegalStateException::class, IOException::class)
    fun addPetWithHttpInfo(body: Pet) : ApiResponse<Unit?> {
        val localVariableConfig = addPetRequestConfig(body = body)

        return request<Pet, Unit>(
            localVariableConfig
        )
    }

    /**
     * To obtain the request config of the operation addPet
     *
     * @param body Pet object that needs to be added to the store
     * @return RequestConfig
     */
    fun addPetRequestConfig(body: Pet) : RequestConfig<Pet> {
        val localVariableBody = body
        val localVariableQuery: MultiValueMap = mutableMapOf()
        val localVariableHeaders: MutableMap<String, String> = mutableMapOf()
        localVariableHeaders["Content-Type"] = "application/json"
        
        return RequestConfig(
            method = RequestMethod.POST,
            path = "/pet",
            query = localVariableQuery,
            headers = localVariableHeaders,
            body = localVariableBody
        )
    }

    /**
     * Deletes a pet
     * 
     * @param apiKey  (optional)
     * @param petId Pet id to delete
     * @return void
     * @throws IllegalStateException If the request is not correctly configured
     * @throws IOException Rethrows the OkHttp execute method exception
     * @throws UnsupportedOperationException If the API returns an informational or redirection response
     * @throws ClientException If the API returns a client error response
     * @throws ServerException If the API returns a server error response
     */
    @Throws(IllegalStateException::class, IOException::class, UnsupportedOperationException::class, ClientException::class, ServerException::class)
    fun deletePet(apiKey: kotlin.String? = null, petId: kotlin.Long) : Unit {
        val localVarResponse = deletePetWithHttpInfo(apiKey = apiKey, petId = petId)

        return when (localVarResponse.responseType) {
            ResponseType.Success -> Unit
            ResponseType.Informational -> throw UnsupportedOperationException("Client does not support Informational responses.")
            ResponseType.Redirection -> throw UnsupportedOperationException("Client does not support Redirection responses.")
            ResponseType.ClientError -> {
                val localVarError = localVarResponse as ClientError<*>
                throw ClientException("Client error : ${localVarError.statusCode} ${localVarError.message.orEmpty()}", localVarError.statusCode, localVarResponse)
            }
            ResponseType.ServerError -> {
                val localVarError = localVarResponse as ServerError<*>
                throw ServerException("Server error : ${localVarError.statusCode} ${localVarError.message.orEmpty()}", localVarError.statusCode, localVarResponse)
            }
        }
    }

    /**
     * Deletes a pet
     * 
     * @param apiKey  (optional)
     * @param petId Pet id to delete
     * @return ApiResponse<Unit?>
     * @throws IllegalStateException If the request is not correctly configured
     * @throws IOException Rethrows the OkHttp execute method exception
     */
    @Throws(IllegalStateException::class, IOException::class)
    fun deletePetWithHttpInfo(apiKey: kotlin.String?, petId: kotlin.Long) : ApiResponse<Unit?> {
        val localVariableConfig = deletePetRequestConfig(apiKey = apiKey, petId = petId)

        return request<Unit, Unit>(
            localVariableConfig
        )
    }

    /**
     * To obtain the request config of the operation deletePet
     *
     * @param apiKey  (optional)
     * @param petId Pet id to delete
     * @return RequestConfig
     */
    fun deletePetRequestConfig(apiKey: kotlin.String?, petId: kotlin.Long) : RequestConfig<Unit> {
        val localVariableBody = null
        val localVariableQuery: MultiValueMap = mutableMapOf()
        val localVariableHeaders: MutableMap<String, String> = mutableMapOf()
        apiKey?.apply { localVariableHeaders["api_key"] = this.toString() }
        
        return RequestConfig(
            method = RequestMethod.DELETE,
            path = "/pet/{petId}".replace("{"+"petId"+"}", "$petId"),
            query = localVariableQuery,
            headers = localVariableHeaders,
            body = localVariableBody
        )
    }

    /**
     * enum for parameter status
     */
     enum class Status_findPetsByStatus(val value: kotlin.String) {
         @Json(name = "available") available("available"),
         @Json(name = "pending") pending("pending"),
         @Json(name = "sold") sold("sold")
     }

    /**
     * Finds Pets by status
     * Multiple status values can be provided with comma separated strings
     * @param status Status values that need to be considered for filter
     * @return kotlin.collections.List<Pet>
     * @throws IllegalStateException If the request is not correctly configured
     * @throws IOException Rethrows the OkHttp execute method exception
     * @throws UnsupportedOperationException If the API returns an informational or redirection response
     * @throws ClientException If the API returns a client error response
     * @throws ServerException If the API returns a server error response
     */
    @Suppress("UNCHECKED_CAST")
    @Throws(IllegalStateException::class, IOException::class, UnsupportedOperationException::class, ClientException::class, ServerException::class)
    fun findPetsByStatus(status: kotlin.collections.List<Status_findPetsByStatus>) : kotlin.collections.List<Pet> {
        val localVarResponse = findPetsByStatusWithHttpInfo(status = status)

        return when (localVarResponse.responseType) {
            ResponseType.Success -> (localVarResponse as Success<*>).data as kotlin.collections.List<Pet>
            ResponseType.Informational -> throw UnsupportedOperationException("Client does not support Informational responses.")
            ResponseType.Redirection -> throw UnsupportedOperationException("Client does not support Redirection responses.")
            ResponseType.ClientError -> {
                val localVarError = localVarResponse as ClientError<*>
                throw ClientException("Client error : ${localVarError.statusCode} ${localVarError.message.orEmpty()}", localVarError.statusCode, localVarResponse)
            }
            ResponseType.ServerError -> {
                val localVarError = localVarResponse as ServerError<*>
                throw ServerException("Server error : ${localVarError.statusCode} ${localVarError.message.orEmpty()}", localVarError.statusCode, localVarResponse)
            }
        }
    }

    /**
     * Finds Pets by status
     * Multiple status values can be provided with comma separated strings
     * @param status Status values that need to be considered for filter
     * @return ApiResponse<kotlin.collections.List<Pet>?>
     * @throws IllegalStateException If the request is not correctly configured
     * @throws IOException Rethrows the OkHttp execute method exception
     */
    @Suppress("UNCHECKED_CAST")
    @Throws(IllegalStateException::class, IOException::class)
    fun findPetsByStatusWithHttpInfo(status: kotlin.collections.List<Status_findPetsByStatus>) : ApiResponse<kotlin.collections.List<Pet>?> {
        val localVariableConfig = findPetsByStatusRequestConfig(status = status)

        return request<Unit, kotlin.collections.List<Pet>>(
            localVariableConfig
        )
    }

    /**
     * To obtain the request config of the operation findPetsByStatus
     *
     * @param status Status values that need to be considered for filter
     * @return RequestConfig
     */
    fun findPetsByStatusRequestConfig(status: kotlin.collections.List<Status_findPetsByStatus>) : RequestConfig<Unit> {
        val localVariableBody = null
        val localVariableQuery: MultiValueMap = mutableMapOf<kotlin.String, kotlin.collections.List<kotlin.String>>()
            .apply {
                put("status", toMultiValue(status.toList(), "csv"))
            }
        val localVariableHeaders: MutableMap<String, String> = mutableMapOf()
        localVariableHeaders["Accept"] = "application/json"

        return RequestConfig(
            method = RequestMethod.GET,
            path = "/pet/findByStatus",
            query = localVariableQuery,
            headers = localVariableHeaders,
            body = localVariableBody
        )
    }

    /**
     * Finds Pets by tags
     * Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing.
     * @param tags Tags to filter by
     * @return kotlin.collections.List<Pet>
     * @throws IllegalStateException If the request is not correctly configured
     * @throws IOException Rethrows the OkHttp execute method exception
     * @throws UnsupportedOperationException If the API returns an informational or redirection response
     * @throws ClientException If the API returns a client error response
     * @throws ServerException If the API returns a server error response
     */
    @Suppress("UNCHECKED_CAST")
    @Throws(IllegalStateException::class, IOException::class, UnsupportedOperationException::class, ClientException::class, ServerException::class)
    @Deprecated(message = "This operation is deprecated.")
    fun findPetsByTags(tags: kotlin.collections.List<kotlin.String>) : kotlin.collections.List<Pet> {
        @Suppress("DEPRECATION")
        val localVarResponse = findPetsByTagsWithHttpInfo(tags = tags)

        return when (localVarResponse.responseType) {
            ResponseType.Success -> (localVarResponse as Success<*>).data as kotlin.collections.List<Pet>
            ResponseType.Informational -> throw UnsupportedOperationException("Client does not support Informational responses.")
            ResponseType.Redirection -> throw UnsupportedOperationException("Client does not support Redirection responses.")
            ResponseType.ClientError -> {
                val localVarError = localVarResponse as ClientError<*>
                throw ClientException("Client error : ${localVarError.statusCode} ${localVarError.message.orEmpty()}", localVarError.statusCode, localVarResponse)
            }
            ResponseType.ServerError -> {
                val localVarError = localVarResponse as ServerError<*>
                throw ServerException("Server error : ${localVarError.statusCode} ${localVarError.message.orEmpty()}", localVarError.statusCode, localVarResponse)
            }
        }
    }

    /**
     * Finds Pets by tags
     * Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing.
     * @param tags Tags to filter by
     * @return ApiResponse<kotlin.collections.List<Pet>?>
     * @throws IllegalStateException If the request is not correctly configured
     * @throws IOException Rethrows the OkHttp execute method exception
     */
    @Suppress("UNCHECKED_CAST")
    @Throws(IllegalStateException::class, IOException::class)
    @Deprecated(message = "This operation is deprecated.")
    fun findPetsByTagsWithHttpInfo(tags: kotlin.collections.List<kotlin.String>) : ApiResponse<kotlin.collections.List<Pet>?> {
        @Suppress("DEPRECATION")
        val localVariableConfig = findPetsByTagsRequestConfig(tags = tags)

        return request<Unit, kotlin.collections.List<Pet>>(
            localVariableConfig
        )
    }

    /**
     * To obtain the request config of the operation findPetsByTags
     *
     * @param tags Tags to filter by
     * @return RequestConfig
     */
    @Deprecated(message = "This operation is deprecated.")
    fun findPetsByTagsRequestConfig(tags: kotlin.collections.List<kotlin.String>) : RequestConfig<Unit> {
        val localVariableBody = null
        val localVariableQuery: MultiValueMap = mutableMapOf<kotlin.String, kotlin.collections.List<kotlin.String>>()
            .apply {
                put("tags", toMultiValue(tags.toList(), "csv"))
            }
        val localVariableHeaders: MutableMap<String, String> = mutableMapOf()
        localVariableHeaders["Accept"] = "application/json"

        return RequestConfig(
            method = RequestMethod.GET,
            path = "/pet/findByTags",
            query = localVariableQuery,
            headers = localVariableHeaders,
            body = localVariableBody
        )
    }

    /**
     * Find pet by ID
     * Returns a single pet
     * @param petId ID of pet to return
     * @return Pet
     * @throws IllegalStateException If the request is not correctly configured
     * @throws IOException Rethrows the OkHttp execute method exception
     * @throws UnsupportedOperationException If the API returns an informational or redirection response
     * @throws ClientException If the API returns a client error response
     * @throws ServerException If the API returns a server error response
     */
    @Suppress("UNCHECKED_CAST")
    @Throws(IllegalStateException::class, IOException::class, UnsupportedOperationException::class, ClientException::class, ServerException::class)
    fun getPetById(petId: kotlin.Long) : Pet {
        val localVarResponse = getPetByIdWithHttpInfo(petId = petId)

        return when (localVarResponse.responseType) {
            ResponseType.Success -> (localVarResponse as Success<*>).data as Pet
            ResponseType.Informational -> throw UnsupportedOperationException("Client does not support Informational responses.")
            ResponseType.Redirection -> throw UnsupportedOperationException("Client does not support Redirection responses.")
            ResponseType.ClientError -> {
                val localVarError = localVarResponse as ClientError<*>
                throw ClientException("Client error : ${localVarError.statusCode} ${localVarError.message.orEmpty()}", localVarError.statusCode, localVarResponse)
            }
            ResponseType.ServerError -> {
                val localVarError = localVarResponse as ServerError<*>
                throw ServerException("Server error : ${localVarError.statusCode} ${localVarError.message.orEmpty()}", localVarError.statusCode, localVarResponse)
            }
        }
    }

    /**
     * Find pet by ID
     * Returns a single pet
     * @param petId ID of pet to return
     * @return ApiResponse<Pet?>
     * @throws IllegalStateException If the request is not correctly configured
     * @throws IOException Rethrows the OkHttp execute method exception
     */
    @Suppress("UNCHECKED_CAST")
    @Throws(IllegalStateException::class, IOException::class)
    fun getPetByIdWithHttpInfo(petId: kotlin.Long) : ApiResponse<Pet?> {
        val localVariableConfig = getPetByIdRequestConfig(petId = petId)

        return request<Unit, Pet>(
            localVariableConfig
        )
    }

    /**
     * To obtain the request config of the operation getPetById
     *
     * @param petId ID of pet to return
     * @return RequestConfig
     */
    fun getPetByIdRequestConfig(petId: kotlin.Long) : RequestConfig<Unit> {
        val localVariableBody = null
        val localVariableQuery: MultiValueMap = mutableMapOf()
        val localVariableHeaders: MutableMap<String, String> = mutableMapOf()
        localVariableHeaders["Accept"] = "application/json"

        return RequestConfig(
            method = RequestMethod.GET,
            path = "/pet/{petId}".replace("{"+"petId"+"}", "$petId"),
            query = localVariableQuery,
            headers = localVariableHeaders,
            body = localVariableBody
        )
    }

    /**
     * Update an existing pet
     * 
     * @param body Pet object that needs to be added to the store
     * @return void
     * @throws IllegalStateException If the request is not correctly configured
     * @throws IOException Rethrows the OkHttp execute method exception
     * @throws UnsupportedOperationException If the API returns an informational or redirection response
     * @throws ClientException If the API returns a client error response
     * @throws ServerException If the API returns a server error response
     */
    @Throws(IllegalStateException::class, IOException::class, UnsupportedOperationException::class, ClientException::class, ServerException::class)
    fun updatePet(body: Pet) : Unit {
        val localVarResponse = updatePetWithHttpInfo(body = body)

        return when (localVarResponse.responseType) {
            ResponseType.Success -> Unit
            ResponseType.Informational -> throw UnsupportedOperationException("Client does not support Informational responses.")
            ResponseType.Redirection -> throw UnsupportedOperationException("Client does not support Redirection responses.")
            ResponseType.ClientError -> {
                val localVarError = localVarResponse as ClientError<*>
                throw ClientException("Client error : ${localVarError.statusCode} ${localVarError.message.orEmpty()}", localVarError.statusCode, localVarResponse)
            }
            ResponseType.ServerError -> {
                val localVarError = localVarResponse as ServerError<*>
                throw ServerException("Server error : ${localVarError.statusCode} ${localVarError.message.orEmpty()}", localVarError.statusCode, localVarResponse)
            }
        }
    }

    /**
     * Update an existing pet
     * 
     * @param body Pet object that needs to be added to the store
     * @return ApiResponse<Unit?>
     * @throws IllegalStateException If the request is not correctly configured
     * @throws IOException Rethrows the OkHttp execute method exception
     */
    @Throws(IllegalStateException::class, IOException::class)
    fun updatePetWithHttpInfo(body: Pet) : ApiResponse<Unit?> {
        val localVariableConfig = updatePetRequestConfig(body = body)

        return request<Pet, Unit>(
            localVariableConfig
        )
    }

    /**
     * To obtain the request config of the operation updatePet
     *
     * @param body Pet object that needs to be added to the store
     * @return RequestConfig
     */
    fun updatePetRequestConfig(body: Pet) : RequestConfig<Pet> {
        val localVariableBody = body
        val localVariableQuery: MultiValueMap = mutableMapOf()
        val localVariableHeaders: MutableMap<String, String> = mutableMapOf()
        localVariableHeaders["Content-Type"] = "application/json"
        
        return RequestConfig(
            method = RequestMethod.PUT,
            path = "/pet",
            query = localVariableQuery,
            headers = localVariableHeaders,
            body = localVariableBody
        )
    }

    /**
     * Updates a pet in the store with form data
     * 
     * @param petId ID of pet that needs to be updated
     * @param name Updated name of the pet (optional)
     * @param status Updated status of the pet (optional)
     * @return void
     * @throws IllegalStateException If the request is not correctly configured
     * @throws IOException Rethrows the OkHttp execute method exception
     * @throws UnsupportedOperationException If the API returns an informational or redirection response
     * @throws ClientException If the API returns a client error response
     * @throws ServerException If the API returns a server error response
     */
    @Throws(IllegalStateException::class, IOException::class, UnsupportedOperationException::class, ClientException::class, ServerException::class)
    fun updatePetWithForm(petId: kotlin.Long, name: kotlin.String? = null, status: kotlin.String? = null) : Unit {
        val localVarResponse = updatePetWithFormWithHttpInfo(petId = petId, name = name, status = status)

        return when (localVarResponse.responseType) {
            ResponseType.Success -> Unit
            ResponseType.Informational -> throw UnsupportedOperationException("Client does not support Informational responses.")
            ResponseType.Redirection -> throw UnsupportedOperationException("Client does not support Redirection responses.")
            ResponseType.ClientError -> {
                val localVarError = localVarResponse as ClientError<*>
                throw ClientException("Client error : ${localVarError.statusCode} ${localVarError.message.orEmpty()}", localVarError.statusCode, localVarResponse)
            }
            ResponseType.ServerError -> {
                val localVarError = localVarResponse as ServerError<*>
                throw ServerException("Server error : ${localVarError.statusCode} ${localVarError.message.orEmpty()}", localVarError.statusCode, localVarResponse)
            }
        }
    }

    /**
     * Updates a pet in the store with form data
     * 
     * @param petId ID of pet that needs to be updated
     * @param name Updated name of the pet (optional)
     * @param status Updated status of the pet (optional)
     * @return ApiResponse<Unit?>
     * @throws IllegalStateException If the request is not correctly configured
     * @throws IOException Rethrows the OkHttp execute method exception
     */
    @Throws(IllegalStateException::class, IOException::class)
    fun updatePetWithFormWithHttpInfo(petId: kotlin.Long, name: kotlin.String?, status: kotlin.String?) : ApiResponse<Unit?> {
        val localVariableConfig = updatePetWithFormRequestConfig(petId = petId, name = name, status = status)

        return request<Map<String, PartConfig<*>>, Unit>(
            localVariableConfig
        )
    }

    /**
     * To obtain the request config of the operation updatePetWithForm
     *
     * @param petId ID of pet that needs to be updated
     * @param name Updated name of the pet (optional)
     * @param status Updated status of the pet (optional)
     * @return RequestConfig
     */
    fun updatePetWithFormRequestConfig(petId: kotlin.Long, name: kotlin.String?, status: kotlin.String?) : RequestConfig<Map<String, PartConfig<*>>> {
        val localVariableBody = mapOf(
            "name" to PartConfig(body = name, headers = mutableMapOf()),
            "status" to PartConfig(body = status, headers = mutableMapOf()),)
        val localVariableQuery: MultiValueMap = mutableMapOf()
        val localVariableHeaders: MutableMap<String, String> = mutableMapOf("Content-Type" to "application/x-www-form-urlencoded")
        
        return RequestConfig(
            method = RequestMethod.POST,
            path = "/pet/{petId}".replace("{"+"petId"+"}", "$petId"),
            query = localVariableQuery,
            headers = localVariableHeaders,
            body = localVariableBody
        )
    }

    /**
     * uploads an image
     * 
     * @param petId ID of pet to update
     * @param additionalMetadata Additional data to pass to server (optional)
     * @param file file to upload (optional)
     * @return ModelApiResponse
     * @throws IllegalStateException If the request is not correctly configured
     * @throws IOException Rethrows the OkHttp execute method exception
     * @throws UnsupportedOperationException If the API returns an informational or redirection response
     * @throws ClientException If the API returns a client error response
     * @throws ServerException If the API returns a server error response
     */
    @Suppress("UNCHECKED_CAST")
    @Throws(IllegalStateException::class, IOException::class, UnsupportedOperationException::class, ClientException::class, ServerException::class)
    fun uploadFile(petId: kotlin.Long, additionalMetadata: kotlin.String? = null, file: java.io.File? = null) : ModelApiResponse {
        val localVarResponse = uploadFileWithHttpInfo(petId = petId, additionalMetadata = additionalMetadata, file = file)

        return when (localVarResponse.responseType) {
            ResponseType.Success -> (localVarResponse as Success<*>).data as ModelApiResponse
            ResponseType.Informational -> throw UnsupportedOperationException("Client does not support Informational responses.")
            ResponseType.Redirection -> throw UnsupportedOperationException("Client does not support Redirection responses.")
            ResponseType.ClientError -> {
                val localVarError = localVarResponse as ClientError<*>
                throw ClientException("Client error : ${localVarError.statusCode} ${localVarError.message.orEmpty()}", localVarError.statusCode, localVarResponse)
            }
            ResponseType.ServerError -> {
                val localVarError = localVarResponse as ServerError<*>
                throw ServerException("Server error : ${localVarError.statusCode} ${localVarError.message.orEmpty()}", localVarError.statusCode, localVarResponse)
            }
        }
    }

    /**
     * uploads an image
     * 
     * @param petId ID of pet to update
     * @param additionalMetadata Additional data to pass to server (optional)
     * @param file file to upload (optional)
     * @return ApiResponse<ModelApiResponse?>
     * @throws IllegalStateException If the request is not correctly configured
     * @throws IOException Rethrows the OkHttp execute method exception
     */
    @Suppress("UNCHECKED_CAST")
    @Throws(IllegalStateException::class, IOException::class)
    fun uploadFileWithHttpInfo(petId: kotlin.Long, additionalMetadata: kotlin.String?, file: java.io.File?) : ApiResponse<ModelApiResponse?> {
        val localVariableConfig = uploadFileRequestConfig(petId = petId, additionalMetadata = additionalMetadata, file = file)

        return request<Map<String, PartConfig<*>>, ModelApiResponse>(
            localVariableConfig
        )
    }

    /**
     * To obtain the request config of the operation uploadFile
     *
     * @param petId ID of pet to update
     * @param additionalMetadata Additional data to pass to server (optional)
     * @param file file to upload (optional)
     * @return RequestConfig
     */
    fun uploadFileRequestConfig(petId: kotlin.Long, additionalMetadata: kotlin.String?, file: java.io.File?) : RequestConfig<Map<String, PartConfig<*>>> {
        val localVariableBody = mapOf(
            "additionalMetadata" to PartConfig(body = additionalMetadata, headers = mutableMapOf()),
            "file" to PartConfig(body = file, headers = mutableMapOf()),)
        val localVariableQuery: MultiValueMap = mutableMapOf()
        val localVariableHeaders: MutableMap<String, String> = mutableMapOf("Content-Type" to "multipart/form-data")
        localVariableHeaders["Accept"] = "application/json"

        return RequestConfig(
            method = RequestMethod.POST,
            path = "/pet/{petId}/uploadImage".replace("{"+"petId"+"}", "$petId"),
            query = localVariableQuery,
            headers = localVariableHeaders,
            body = localVariableBody
        )
    }

}
