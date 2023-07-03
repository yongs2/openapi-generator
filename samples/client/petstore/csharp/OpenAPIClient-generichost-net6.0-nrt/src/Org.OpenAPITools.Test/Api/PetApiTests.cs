/*
 * OpenAPI Petstore
 *
 * This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\
 *
 * The version of the OpenAPI document: 1.0.0
 * Generated by: https://github.com/openapitools/openapi-generator.git
 */

using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Xunit;
using Microsoft.Extensions.DependencyInjection;
using Org.OpenAPITools.IApi;
using Org.OpenAPITools.Model;


/* *********************************************************************************
*              Follow these manual steps to construct tests.
*              This file will not be overwritten.
*  *********************************************************************************
* 1. Navigate to ApiTests.Base.cs and ensure any tokens are being created correctly.
*    Take care not to commit credentials to any repository.
*
* 2. Mocking is coordinated by ApiTestsBase#AddApiHttpClients.
*    To mock the client, use the generic AddApiHttpClients.
*    To mock the server, change the client's BaseAddress.
*
* 3. Locate the test you want below
*      - remove the skip property from the Fact attribute
*      - set the value of any variables if necessary
*
* 4. Run the tests and ensure they work.
*
*/


namespace Org.OpenAPITools.Test.Api
{
    /// <summary>
    ///  Class for testing PetApi
    /// </summary>
    public sealed class PetApiTests : ApiTestsBase
    {
        private readonly IApi.IPetApi _instance;

        public PetApiTests(): base(Array.Empty<string>())
        {
            _instance = _host.Services.GetRequiredService<IApi.IPetApi>();
        }

        /// <summary>
        /// Test AddPet
        /// </summary>
        [Fact (Skip = "not implemented")]
        public async Task AddPetAsyncTest()
        {
            Pet pet = default!;
            await _instance.AddPetAsync(pet);
        }

        /// <summary>
        /// Test DeletePet
        /// </summary>
        [Fact (Skip = "not implemented")]
        public async Task DeletePetAsyncTest()
        {
            long petId = default!;
            string apiKey = default!;
            await _instance.DeletePetAsync(petId, apiKey);
        }

        /// <summary>
        /// Test FindPetsByStatus
        /// </summary>
        [Fact (Skip = "not implemented")]
        public async Task FindPetsByStatusAsyncTest()
        {
            List<string> status = default!;
            var response = await _instance.FindPetsByStatusAsync(status);
            var model = response.AsModel();
            Assert.IsType<List<Pet>>(model);
        }

        /// <summary>
        /// Test FindPetsByTags
        /// </summary>
        [Fact (Skip = "not implemented")]
        public async Task FindPetsByTagsAsyncTest()
        {
            List<string> tags = default!;
            var response = await _instance.FindPetsByTagsAsync(tags);
            var model = response.AsModel();
            Assert.IsType<List<Pet>>(model);
        }

        /// <summary>
        /// Test GetPetById
        /// </summary>
        [Fact (Skip = "not implemented")]
        public async Task GetPetByIdAsyncTest()
        {
            long petId = default!;
            var response = await _instance.GetPetByIdAsync(petId);
            var model = response.AsModel();
            Assert.IsType<Pet>(model);
        }

        /// <summary>
        /// Test UpdatePet
        /// </summary>
        [Fact (Skip = "not implemented")]
        public async Task UpdatePetAsyncTest()
        {
            Pet pet = default!;
            await _instance.UpdatePetAsync(pet);
        }

        /// <summary>
        /// Test UpdatePetWithForm
        /// </summary>
        [Fact (Skip = "not implemented")]
        public async Task UpdatePetWithFormAsyncTest()
        {
            long petId = default!;
            string name = default!;
            string status = default!;
            await _instance.UpdatePetWithFormAsync(petId, name, status);
        }

        /// <summary>
        /// Test UploadFile
        /// </summary>
        [Fact (Skip = "not implemented")]
        public async Task UploadFileAsyncTest()
        {
            long petId = default!;
            System.IO.Stream file = default!;
            string additionalMetadata = default!;
            var response = await _instance.UploadFileAsync(petId, file, additionalMetadata);
            var model = response.AsModel();
            Assert.IsType<ApiResponse>(model);
        }

        /// <summary>
        /// Test UploadFileWithRequiredFile
        /// </summary>
        [Fact (Skip = "not implemented")]
        public async Task UploadFileWithRequiredFileAsyncTest()
        {
            System.IO.Stream requiredFile = default!;
            long petId = default!;
            string additionalMetadata = default!;
            var response = await _instance.UploadFileWithRequiredFileAsync(requiredFile, petId, additionalMetadata);
            var model = response.AsModel();
            Assert.IsType<ApiResponse>(model);
        }
    }
}
