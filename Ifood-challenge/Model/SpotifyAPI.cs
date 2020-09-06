using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;
using System.Linq;
using Microsoft.AspNetCore.WebUtilities;
using Microsoft.Extensions.Configuration;
using System.Net.Http.Headers;

using Newtonsoft.Json;
using Newtonsoft.Json.Linq;

namespace ifood_challenge.Controllers
{
    public class SpotifyAPI
    {
        private const string baseUrl = "https://accounts.spotify.com/api/token";
        private const string baseUrlSearch = "https://api.spotify.com/v1/search";
        private readonly IConfiguration _configuration;
        private HttpClient _client;
        public SpotifyAPI(IConfiguration configuration)
        {
            _configuration = configuration;
            _client = new HttpClient();
        }

        public string getListOfTracks(string query)
        {
            string urlTracks = getUrlPlaylists(query);
            string json = getRequest(urlTracks + "?limit=10");

            JObject rss = JObject.Parse(json);
            var items =
            (
                from item in rss["items"]
                select item["track"]["name"]
            ).ToArray();

            string listJson = "";

            List<string> jsonText = new List<string>();
            foreach (string item in items)
                jsonText.Add(item);

            Dictionary<string, List<string>> JsonDictionary = new Dictionary<string, List<string>>();
            JsonDictionary.Add("tracks", jsonText);
            //return JsonConvert.SerializeObject(JsonDictionary, Formatting.Indented);
            return JsonConvert.SerializeObject(JsonDictionary);
        }

        private string getUrlPlaylists(string query)
        {
            string json = "";
            Dictionary<string, string> headers = new Dictionary<string, string>();
            headers.Add("q", query);
            headers.Add("type", "playlist");
            headers.Add("limit", "1");
            headers.Add("include_external", "audio");
            json = getRequest(headers);

            // return json;

            JObject rss = JObject.Parse(json);
            return (string)rss["playlists"]["items"][0]["tracks"]["href"];
        }

        private string getRequest(Dictionary<string, string> headers)
        {
            int i = 0;
            string parameters = "";
            foreach (KeyValuePair<string, string> header in headers)
            {
                if (i == 0)
                    parameters = $"{header.Key}={header.Value}";
                else
                    parameters = parameters + $"&{header.Key}={header.Value}";
                i++;
            }

            string getUrl = $"{baseUrlSearch}?{parameters}";
            return getRequest(getUrl);
        }
        private string getRequest(string url)
        {
            string token = GetAccessToken();
            var request = new HttpRequestMessage(HttpMethod.Get, url);
            request.Headers.Add("Accept", "application/json");
            request.Headers.Add("Authorization", "Bearer " + token);
            try
            {
                return Task<string>.Run(async () =>
                {
                    var response = await _client.SendAsync(request);
                    string json = await response.Content.ReadAsStringAsync();
                    return await Task<string>.FromResult(json);
                }).Result;
            }
            catch (System.Exception)
            {
                throw;
            }
        }

        private string GetAccessToken()
        {
            string json = authenticate();
            var options = new JsonDocumentOptions { AllowTrailingCommas = true };

            JsonDocument document = JsonDocument.Parse(json, options);
            foreach (JsonProperty element in document.RootElement.EnumerateObject())
                if (element.NameEquals("access_token"))
                    return element.Value.GetString();

            return "";
        }

        private string authenticate()
        {
            string clientId = _configuration["Spotfy:ServiceApiId"];
            string clientSecret = _configuration["Spotfy:ServiceApiSecret"];

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