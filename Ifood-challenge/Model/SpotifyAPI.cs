using System;
using System.Collections.Generic;
using System.Text;
using System.Net.Http;
using System.Threading.Tasks;
using Microsoft.Extensions.Configuration;
using Microsoft.AspNetCore.WebUtilities;

using System.Net.Http.Headers;

namespace ifood_challenge.Controllers
{
    public class SpotifyAPI
    {
        private const string baseUrl = "https://accounts.spotify.com/api/token";
        private readonly IConfiguration _configuration;
        public SpotifyAPI(IConfiguration configuration)
        {
            _configuration = configuration;
        }

        public string getPlayList()
        {
            return "";
        }

        public string GetPermissions()
        {
            return GetAccessToken();
        }

        public string GetAccessToken()
        {
            string clientId = _configuration["Spotfy:ServiceApiId"];
            string clientSecret = _configuration["Spotfy:ServiceApiSecret"];

            Console.WriteLine(clientId);
            Console.WriteLine(clientSecret);


            string json = "";
            byte[] authorizationBytes = Encoding.UTF8.GetBytes(clientId + ":" + clientSecret);
            string authorization = WebEncoders.Base64UrlEncode(authorizationBytes);
            HttpClient httpClient = new HttpClient();
            try
            {
                httpClient.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Basic", authorization);
                Dictionary<string, string> requestData = new Dictionary<string, string>();
                requestData.Add("grant_type", "client_credentials");
                // FormUrlEncodedContent possui internamente o {Content-Type: application/x-www-form-urlencoded} 
                FormUrlEncodedContent requestBody = new FormUrlEncodedContent(requestData);

                json = Task<string>.Run(async () =>
                {
                    HttpResponseMessage response = await httpClient.PostAsync(baseUrl, requestBody);
                    string json = await response.Content.ReadAsStringAsync();
                    return await Task<string>.FromResult(json);
                }).Result;
            }
            catch (System.Exception)
            {

                throw;
            }

            return json;
        }
    }
}