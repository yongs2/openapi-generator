/*
 * OpenAPI Petstore
 *
 * This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\
 *
 * The version of the OpenAPI document: 1.0.0
 * Generated by: https://github.com/openapitools/openapi-generator.git
 */

using System;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.DependencyInjection;
using System.Collections.Generic;
using System.Security.Cryptography;
using UseSourceGeneration.Client;
using UseSourceGeneration.Api;
using UseSourceGeneration.Extensions;
using Xunit;

namespace UseSourceGeneration.Test.Api
{
    /// <summary>
    ///  Tests the dependency injection.
    /// </summary>
    public class DependencyInjectionTest
    {
        private readonly IHost _hostUsingConfigureWithoutAClient = 
            Host.CreateDefaultBuilder(Array.Empty<string>()).ConfigureApi((context, services, options) =>
            {
                ApiKeyToken apiKeyToken = new ApiKeyToken($"<token>", timeout: TimeSpan.FromSeconds(1));
                options.AddTokens(apiKeyToken);
                
                BearerToken bearerToken = new BearerToken($"<token>", timeout: TimeSpan.FromSeconds(1));
                options.AddTokens(bearerToken);
                
                BasicToken basicToken = new BasicToken("<username>", "<password>", timeout: TimeSpan.FromSeconds(1));
                options.AddTokens(basicToken);
                
                HttpSigningConfiguration config = new HttpSigningConfiguration("<keyId>", "<keyFilePath>", null, new List<string>(), HashAlgorithmName.SHA256, "<signingAlgorithm>", 0);
                HttpSignatureToken httpSignatureToken = new HttpSignatureToken(config, timeout: TimeSpan.FromSeconds(1));
                options.AddTokens(httpSignatureToken);
                
                OAuthToken oauthToken = new OAuthToken("token", timeout: TimeSpan.FromSeconds(1));
                options.AddTokens(oauthToken);
            })
            .Build();

        private readonly IHost _hostUsingConfigureWithAClient =
            Host.CreateDefaultBuilder(Array.Empty<string>()).ConfigureApi((context, services, options) =>
            {
                ApiKeyToken apiKeyToken = new ApiKeyToken($"<token>", timeout: TimeSpan.FromSeconds(1));
                options.AddTokens(apiKeyToken);
                
                BearerToken bearerToken = new BearerToken($"<token>", timeout: TimeSpan.FromSeconds(1));
                options.AddTokens(bearerToken);
                
                BasicToken basicToken = new BasicToken("<username>", "<password>", timeout: TimeSpan.FromSeconds(1));
                options.AddTokens(basicToken);
                
                HttpSigningConfiguration config = new HttpSigningConfiguration("<keyId>", "<keyFilePath>", null, new List<string>(), HashAlgorithmName.SHA256, "<signingAlgorithm>", 0);
                HttpSignatureToken httpSignatureToken = new HttpSignatureToken(config, timeout: TimeSpan.FromSeconds(1));
                options.AddTokens(httpSignatureToken);
                
                OAuthToken oauthToken = new OAuthToken("token", timeout: TimeSpan.FromSeconds(1));
                options.AddTokens(oauthToken);
                options.AddApiHttpClients(client => client.BaseAddress = new Uri(ClientUtils.BASE_ADDRESS));
            })
            .Build();

        private readonly IHost _hostUsingAddWithoutAClient =
            Host.CreateDefaultBuilder(Array.Empty<string>()).ConfigureServices((host, services) =>
            {
                services.AddApi(options =>
                {
                    ApiKeyToken apiKeyToken = new ApiKeyToken($"<token>", timeout: TimeSpan.FromSeconds(1));
                    options.AddTokens(apiKeyToken);
                    
                    BearerToken bearerToken = new BearerToken($"<token>", timeout: TimeSpan.FromSeconds(1));
                    options.AddTokens(bearerToken);
                    
                    BasicToken basicToken = new BasicToken("<username>", "<password>", timeout: TimeSpan.FromSeconds(1));
                    options.AddTokens(basicToken);
                    
                    HttpSigningConfiguration config = new HttpSigningConfiguration("<keyId>", "<keyFilePath>", null, new List<string>(), HashAlgorithmName.SHA256, "<signingAlgorithm>", 0);
                    HttpSignatureToken httpSignatureToken = new HttpSignatureToken(config, timeout: TimeSpan.FromSeconds(1));
                    options.AddTokens(httpSignatureToken);
                    
                    OAuthToken oauthToken = new OAuthToken("token", timeout: TimeSpan.FromSeconds(1));
                    options.AddTokens(oauthToken);
                });
            })
            .Build();

        private readonly IHost _hostUsingAddWithAClient =
            Host.CreateDefaultBuilder(Array.Empty<string>()).ConfigureServices((host, services) =>
            {
                services.AddApi(options =>
                {
                    ApiKeyToken apiKeyToken = new ApiKeyToken($"<token>", timeout: TimeSpan.FromSeconds(1));
                    options.AddTokens(apiKeyToken);
                    
                    BearerToken bearerToken = new BearerToken($"<token>", timeout: TimeSpan.FromSeconds(1));
                    options.AddTokens(bearerToken);
                    
                    BasicToken basicToken = new BasicToken("<username>", "<password>", timeout: TimeSpan.FromSeconds(1));
                    options.AddTokens(basicToken);
                    
                    HttpSigningConfiguration config = new HttpSigningConfiguration("<keyId>", "<keyFilePath>", null, new List<string>(), HashAlgorithmName.SHA256, "<signingAlgorithm>", 0);
                    HttpSignatureToken httpSignatureToken = new HttpSignatureToken(config, timeout: TimeSpan.FromSeconds(1));
                    options.AddTokens(httpSignatureToken);
                    
                    OAuthToken oauthToken = new OAuthToken("token", timeout: TimeSpan.FromSeconds(1));
                    options.AddTokens(oauthToken);
                    options.AddApiHttpClients(client => client.BaseAddress = new Uri(ClientUtils.BASE_ADDRESS));
                });
            })
            .Build();

        /// <summary>
        /// Test dependency injection when using the configure method
        /// </summary>
        [Fact]
        public void ConfigureApiWithAClientTest()
        {
            var anotherFakeApi = _hostUsingConfigureWithAClient.Services.GetRequiredService<IAnotherFakeApi>();
            Assert.True(anotherFakeApi.HttpClient.BaseAddress != null);
            
            var defaultApi = _hostUsingConfigureWithAClient.Services.GetRequiredService<IDefaultApi>();
            Assert.True(defaultApi.HttpClient.BaseAddress != null);
            
            var fakeApi = _hostUsingConfigureWithAClient.Services.GetRequiredService<IFakeApi>();
            Assert.True(fakeApi.HttpClient.BaseAddress != null);
            
            var fakeClassnameTags123Api = _hostUsingConfigureWithAClient.Services.GetRequiredService<IFakeClassnameTags123Api>();
            Assert.True(fakeClassnameTags123Api.HttpClient.BaseAddress != null);
            
            var petApi = _hostUsingConfigureWithAClient.Services.GetRequiredService<IPetApi>();
            Assert.True(petApi.HttpClient.BaseAddress != null);
            
            var storeApi = _hostUsingConfigureWithAClient.Services.GetRequiredService<IStoreApi>();
            Assert.True(storeApi.HttpClient.BaseAddress != null);
            
            var userApi = _hostUsingConfigureWithAClient.Services.GetRequiredService<IUserApi>();
            Assert.True(userApi.HttpClient.BaseAddress != null);
        }

        /// <summary>
        /// Test dependency injection when using the configure method
        /// </summary>
        [Fact]
        public void ConfigureApiWithoutAClientTest()
        {
            var anotherFakeApi = _hostUsingConfigureWithoutAClient.Services.GetRequiredService<IAnotherFakeApi>();
            Assert.True(anotherFakeApi.HttpClient.BaseAddress != null);
            
            var defaultApi = _hostUsingConfigureWithoutAClient.Services.GetRequiredService<IDefaultApi>();
            Assert.True(defaultApi.HttpClient.BaseAddress != null);
            
            var fakeApi = _hostUsingConfigureWithoutAClient.Services.GetRequiredService<IFakeApi>();
            Assert.True(fakeApi.HttpClient.BaseAddress != null);
            
            var fakeClassnameTags123Api = _hostUsingConfigureWithoutAClient.Services.GetRequiredService<IFakeClassnameTags123Api>();
            Assert.True(fakeClassnameTags123Api.HttpClient.BaseAddress != null);
            
            var petApi = _hostUsingConfigureWithoutAClient.Services.GetRequiredService<IPetApi>();
            Assert.True(petApi.HttpClient.BaseAddress != null);
            
            var storeApi = _hostUsingConfigureWithoutAClient.Services.GetRequiredService<IStoreApi>();
            Assert.True(storeApi.HttpClient.BaseAddress != null);
            
            var userApi = _hostUsingConfigureWithoutAClient.Services.GetRequiredService<IUserApi>();
            Assert.True(userApi.HttpClient.BaseAddress != null);
        }

        /// <summary>
        /// Test dependency injection when using the add method
        /// </summary>
        [Fact]
        public void AddApiWithAClientTest()
        {
            var anotherFakeApi = _hostUsingAddWithAClient.Services.GetRequiredService<IAnotherFakeApi>();
            Assert.True(anotherFakeApi.HttpClient.BaseAddress != null);
            
            var defaultApi = _hostUsingAddWithAClient.Services.GetRequiredService<IDefaultApi>();
            Assert.True(defaultApi.HttpClient.BaseAddress != null);
            
            var fakeApi = _hostUsingAddWithAClient.Services.GetRequiredService<IFakeApi>();
            Assert.True(fakeApi.HttpClient.BaseAddress != null);
            
            var fakeClassnameTags123Api = _hostUsingAddWithAClient.Services.GetRequiredService<IFakeClassnameTags123Api>();
            Assert.True(fakeClassnameTags123Api.HttpClient.BaseAddress != null);
            
            var petApi = _hostUsingAddWithAClient.Services.GetRequiredService<IPetApi>();
            Assert.True(petApi.HttpClient.BaseAddress != null);
            
            var storeApi = _hostUsingAddWithAClient.Services.GetRequiredService<IStoreApi>();
            Assert.True(storeApi.HttpClient.BaseAddress != null);
            
            var userApi = _hostUsingAddWithAClient.Services.GetRequiredService<IUserApi>();
            Assert.True(userApi.HttpClient.BaseAddress != null);
        }

        /// <summary>
        /// Test dependency injection when using the add method
        /// </summary>
        [Fact]
        public void AddApiWithoutAClientTest()
        {
            var anotherFakeApi = _hostUsingAddWithoutAClient.Services.GetRequiredService<IAnotherFakeApi>();
            Assert.True(anotherFakeApi.HttpClient.BaseAddress != null);
            
            var defaultApi = _hostUsingAddWithoutAClient.Services.GetRequiredService<IDefaultApi>();
            Assert.True(defaultApi.HttpClient.BaseAddress != null);
            
            var fakeApi = _hostUsingAddWithoutAClient.Services.GetRequiredService<IFakeApi>();
            Assert.True(fakeApi.HttpClient.BaseAddress != null);
            
            var fakeClassnameTags123Api = _hostUsingAddWithoutAClient.Services.GetRequiredService<IFakeClassnameTags123Api>();
            Assert.True(fakeClassnameTags123Api.HttpClient.BaseAddress != null);
            
            var petApi = _hostUsingAddWithoutAClient.Services.GetRequiredService<IPetApi>();
            Assert.True(petApi.HttpClient.BaseAddress != null);
            
            var storeApi = _hostUsingAddWithoutAClient.Services.GetRequiredService<IStoreApi>();
            Assert.True(storeApi.HttpClient.BaseAddress != null);
            
            var userApi = _hostUsingAddWithoutAClient.Services.GetRequiredService<IUserApi>();
            Assert.True(userApi.HttpClient.BaseAddress != null);
        }
    }
}
