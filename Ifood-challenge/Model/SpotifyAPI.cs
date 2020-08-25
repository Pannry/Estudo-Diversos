using System;
using System.Collections.Generic;
using System.Text;
using System.Net.Http;
using System.Threading.Tasks;
using Microsoft.AspNetCore.WebUtilities;

using System.Net.Http.Headers;

namespace ifood_challenge.Controllers
{
    public class SpotifyAPI
    {

        private const string baseUrl = "https://accounts.spotify.com/api/token";

        // https://docs.microsoft.com/en-us/aspnet/core/security/app-secrets?view=aspnetcore-3.1&tabs=windows
        // https://blog.elmah.io/asp-net-core-not-that-secret-user-secrets-explained/
        // https://imasters.com.br/dotnet/app-secrets-no-desenvolvimento-asp-net-core-2-0

        private const string clientId = "";
        private const string clientSecret = "";

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