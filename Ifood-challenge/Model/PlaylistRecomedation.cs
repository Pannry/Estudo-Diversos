using System;

namespace ifood_challenge.Models
{
    public class PlayListRecomedation
    {
        private double _temperature;
        public PlayListRecomedation(string city)
        {
            _temperature = requestTemperure(city);
        }

        public PlayListRecomedation(double latitude, double longitude)
        {
            _temperature = requestTemperure(latitude, longitude);
        }

        public Category getRecomedation()
        {
            if (_temperature > 30) return Category.PartyMusic;
            if (_temperature <= 30 && _temperature >= 15) return Category.PopMusic;
            if (_temperature >= 10 && _temperature <= 14) return Category.RockMusic;
            return Category.ClassicalMusic;
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