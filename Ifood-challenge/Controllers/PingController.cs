using System;
using Microsoft.AspNetCore.Mvc;

namespace ifood_challenge.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class PingController : ControllerBase
    {
        [HttpGet]
        public string Get()
        {
            return "Pong";
        }
    }
}