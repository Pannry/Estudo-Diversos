using System.Linq.Expressions;
using System.Reflection;
using Microsoft.Extensions.Configuration;
using Microsoft.AspNetCore.Mvc;
using System.Net.Http;
using System;
using Newtonsoft.Json.Linq;

using ifood_challenge.Models;

namespace ifood_challenge.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class PlaylistController : ControllerBase
    {
        private readonly IConfiguration _configuration;
        public PlaylistController(IConfiguration configuration)
        {
            // IConfiguration: Carregado automaticamente ao inicar a aplicação
            _configuration = configuration;
        }

        [HttpGet("city/{nameId}")]
        // http://localhost:5000/playlist/city/fortaleza
        public ContentResult GetLocationByName(string nameId)
        {
            PlayListRecomedation playlist = new PlayListRecomedation(nameId);
            Category musicType = playlist.getRecomedation();


            SpotifyAPI spotifyAPI = new SpotifyAPI(_configuration);
            string json = spotifyAPI.getListOfTracks(musicType);
            Console.WriteLine(json);
            return Content(json, "application/json");
        }

        [HttpGet("coordinates/{latitude}/{longitude}")]
        // http://localhost:5000/playlist/coordinates/10.5/10.5
        public ContentResult GetLocationByCoordinates(double latitude, double longitude)
        {
            PlayListRecomedation playlist = new PlayListRecomedation(latitude, longitude);
            Category musicType = playlist.getRecomedation();

            SpotifyAPI spotifyAPI = new SpotifyAPI(_configuration);
            string json = spotifyAPI.getListOfTracks(musicType);
            Console.WriteLine(json);
            return Content(json, "application/json");
        }
    }
}

