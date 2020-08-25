using Microsoft.AspNetCore.Mvc;
using System;

namespace ifood_challenge.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class PlaylistController : ControllerBase
    {
        [HttpGet("city/{nameId}")]
        // http://localhost:5000/playlist/city/fortaleza
        public string GetLocationByName(string nameId)
        {
            PlayListRecomedation playlist = new PlayListRecomedation(nameId);
            string line = playlist.getTemperature().ToString();

            SpotifyAPI spotifyAPI = new SpotifyAPI();
            string line2 = spotifyAPI.GetPermissions();

            return line2;
        }

        [HttpGet("coordinates/{latitude}/{longitude}")]
        // http://localhost:5000/playlist/coordinates/10.5/10.5
        public string GetLocationByCoordinates(double latitude, double longitude)
        {
            PlayListRecomedation playlist = new PlayListRecomedation(latitude, longitude);
            string line = playlist.getTemperature().ToString();
            return $"Temperatura do local {latitude} , {longitude}: {line}";
        }
    }
}


// ?cidade = <nome>
// ?latitute = <numero> longitude = <numero>



// ~~~~~~~~~~~~         Formas        ~~~~~~~~~~~~~~

// latitude ? chave1=parametro1 & chave2=parametro2 & ...
//                        ou
// [Route("customers/{customerId}/orders")]
// public IEnumerable<Order> GetOrdersByCustomer(int customerId) { ... }
