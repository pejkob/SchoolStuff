using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using monthypython.Models;

namespace monthypython.Controllers
{
    [Route("[controller]")]
    [ApiController]
    public class MonthyPythonController : ControllerBase
    {

        [HttpGet("/ForgatoKonyv")]
        public IActionResult GetForgatoKonyv()
        {
            using (var context=new MonthypythonContext())
            {
                try
                {
                    return StatusCode(200, context.Forgatokonyvs.Include(f=>f.Epizod).Include(f=>f.Tipus).ToList());
                    
                }
                catch (Exception ex)
                {
                    return StatusCode(400, ex.Message);
                }
            }
        }

        [HttpGet]
        public IActionResult GetEpizod()
        {
            using (var context = new MonthypythonContext())
            {
                try
                {
                    return StatusCode(200, context.Epizodoks.ToList());
                }
                catch (Exception ex)
                {
                    return StatusCode(400, ex.Message);
                }
            }
        }

        [HttpPost]
        public IActionResult postEpizod(Epizodok epizod)
        {
            using (var context = new MonthypythonContext())
            {
                try
                {
                    context.Epizodoks.Add(epizod);
                    context.SaveChanges();
                    return StatusCode(200, "Sikeres hozzáadás");
                }
                catch (Exception ex)
                {
                    return StatusCode(400, ex.Message);
                }
            }
        }

        [HttpPut]
        public IActionResult putEpizod(Epizodok putEpizod)
        {
            using (var context=new MonthypythonContext())
            {
                try
                {
                    context.Epizodoks.Update(putEpizod);
                    context.SaveChanges();
                    return StatusCode(200, "Sikeres adatmódosítás");
                }
                catch (Exception ex)
                {
                    return StatusCode(400, ex.Message);
                }
            }
        }
        [HttpDelete]
        public IActionResult deleteEpizod(int id)
        {
            using (var context=new MonthypythonContext())
            {
                try
                {
                    var delete= context.Epizodoks.Find(id);
                    context.Epizodoks.Remove(delete);
                    context.SaveChanges();
                    return StatusCode(200, "Sikeres adattörlés");
                }
                catch (Exception ex)
                {
                    return StatusCode(400, ex.Message);
                }
            }
        }

    }
}
