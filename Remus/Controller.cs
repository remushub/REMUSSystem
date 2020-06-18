using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Diagnostics.Contracts;
using System.Linq;
using System.Threading.Tasks;

namespace Remus
{
    [ApiController]
    [Route("api")]
    public class Controller : ControllerBase
    {
        Service service = new Service();

        [HttpGet("getValue")]
        public IActionResult GetValue()
        {
            return new ObjectResult(service.getValue());
        }

        [HttpPost("setValue")]
        public IActionResult SetValue([FromBody] int value)
        {
            service.setValue(value);
            return new ObjectResult("Value Changed");
        }
    }
}
