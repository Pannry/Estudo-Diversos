using System;

namespace ifood_challenge.Controllers
{
    public class PlayListRecomedation
    {
        // public double Latitude { get; set; }
        private double _temperature;
        public PlayListRecomedation(string city)
        {
            _temperature = requestTemperure(city);
        }

        public PlayListRecomedation(double latitude, double longitude)
        {
            _temperature = requestTemperure(latitude, longitude);
        }

        public string GetRecomedation()
        {
            if (_temperature > 30) return "Party";
            if (_temperature <= 30 && _temperature >= 15) return "PopMusic";
            if (_temperature >= 10 && _temperature <= 14) return "RockMusic";
            return "ClassicMusic";
        }

        public double getTemperature()
        {
            return _temperature;
        }

        private double requestTemperure(double latitude, double longitude)
        {
            OpenWeatherMapsApi weatherApi = new OpenWeatherMapsApi();
            return weatherApi.getTemperure(latitude, longitude);
        }

        private double requestTemperure(string city)
        {
            OpenWeatherMapsApi weatherApi = new OpenWeatherMapsApi();
            return weatherApi.getTemperure(city);
        }
    }
}