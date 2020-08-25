using System;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Threading;
using System.Threading.Tasks;

using System.Text.Json;

namespace ifood_challenge.Controllers
{

    public class OpenWeatherMapsApi
    {
        private const string apiKey = "b77e07f479efe92156376a8b07640ced";
        private HttpClient _client;
        public OpenWeatherMapsApi()
        {
            _client = new HttpClient();
        }

        public double getTemperure(double latitude, double longitude)
        {
            string url = $"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={latitude}&appid={apiKey}&units=metric";
            return requestWeatherTemperature(url);
        }
        public double getTemperure(string city)
        {
            string url = $"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&units=metric";
            return requestWeatherTemperature(url);
        }

        private double requestWeatherTemperature(string url)
        {
            try
            {
                string json = Task<string>.Run(async () =>
                {
                    HttpResponseMessage response = await _client.GetAsync(url);
                    string json = await response.Content.ReadAsStringAsync();
                    return await Task<string>.FromResult(json);
                }).Result;

                Console.WriteLine(json);

                return GetTemperatureInJson(json);
            }
            catch (Exception e)
            {
                Console.WriteLine(e);
            }

            return 0;
        }

        private double GetTemperatureInJson(string json)
        {
            var options = new JsonDocumentOptions
            {
                AllowTrailingCommas = true
            };
            JsonDocument document = JsonDocument.Parse(json, options);

            foreach (JsonProperty element in document.RootElement.EnumerateObject())
                if (element.NameEquals("main"))
                    foreach (JsonProperty elementMain in element.Value.EnumerateObject())
                        if (elementMain.NameEquals("temp"))
                            return elementMain.Value.GetDouble();
            return 0;
        }
    }

}