using AutoBerles.Models;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace AutoBerles.Controllers
{
    [Route("[controller]")]
    [ApiController]
    public class AutoBerlesController : ControllerBase
    {
        [HttpGet]
        public IActionResult GetAutoByRendszam(string rendszam)
        {
            
            using (var context=new AutoberlesContext())
            {
                try
                {
                    return StatusCode(200, context.Autoks.FirstOrDefault(a => a.Rendszam == rendszam));

                }
                catch (Exception ex)
                {
                    return StatusCode(400,ex.Message);
                }
            }
        }

        [HttpGet("/Kolcsonzes")]
        public IActionResult GetAllKolcsoncszes()
        {
            using (var context=new AutoberlesContext())
            {
                try
                {
                    var response = context.Kolcsonzes.ToList();
                   return StatusCode(200, response);
                }
                catch (Exception ex)
                {
                    return StatusCode(400, ex.Message);
                }
            }
        }

        [HttpPost]
        public IActionResult PostAuto(Autok ujauto)
        {
            using (var context = new AutoberlesContext())
            {
                try
                {
                    context.Autoks.Add(ujauto);
                    context.SaveChanges();
                    return StatusCode(200,"Új autó létrehozása sikeres!");

                }
                catch (Exception ex)
                {
                    return StatusCode(400, ex.Message);
                }
            }
        }
        [HttpPut]
        public IActionResult PutAuto(Autok ujauto)
        {
            using (var context = new AutoberlesContext())
            {
                try
                {
                    var existingAuto = context.Autoks.Find(ujauto.Id);

                    if (existingAuto == null)
                    {
                        return NotFound("Auto not found");
                    }

                    context.Entry(existingAuto).CurrentValues.SetValues(ujauto);
                    context.SaveChanges();

                    return Ok("Adat módosítása sikeres");
                }
                catch (Exception ex)
                {
                    return BadRequest(ex.Message);
                }
            }
        }


        [HttpDelete]
        public IActionResult DeleteAuto(int id)
        {
            using (var context = new AutoberlesContext())
            {
                try
                {
                    var deleteAuto= context.Autoks.Find(id);
                    context.Autoks.Remove(deleteAuto);
                    context.SaveChanges();
                    return StatusCode(200, "Adat törlése sikeres");

                }
                catch (Exception ex)
                {
                    return StatusCode(400, ex.Message);
                }
            }
        }
    }
}
