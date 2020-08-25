using Microsoft.AspNetCore.Mvc;

namespace ifood_challenge.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class SpotfyOauth20Controller : ControllerBase
    {
        [HttpGet]
        public string GetLocationByName(string code)
        {
            return code;
        }
    }
}