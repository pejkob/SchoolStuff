using Filmek.Models;
using Filmek.Services;
using Microsoft.AspNetCore.Mvc;

namespace Filmek.Controllers;

[ApiController]
[Route("[controller]")]
public class FilmController : ControllerBase
{
    public FilmController()
    {
    }

    // GET all action
    [HttpGet]
public ActionResult<List<Film>> GetAll() =>
    FilmService.GetAll();

    // GET by Id action
[HttpGet("{id}")]
public ActionResult<Film> Get(int id)
{
    var film = FilmService.Get(id);

    if(film == null)
        return NotFound();

    return film;
}
    // POST action
[HttpPost]
public IActionResult Create(Film film)
{            
    FilmService.Add(film);
    return CreatedAtAction(nameof(Get), new { id = film.Id }, film);
}
    // PUT action
[HttpPut("{id}")]
public IActionResult Update(int id, Film film)
{
    if (id != film.Id)
        return BadRequest();
           
    var existingFilm = FilmService.Get(id);
    if(existingFilm is null)
        return NotFound();
   
    FilmService.Update(film);           
   
    return NoContent();
}
    // DELETE action
    [HttpDelete("{id}")]
public IActionResult Delete(int id)
{
    var film = FilmService.Get(id);
   
    if (film is null)
        return NotFound();
       
    FilmService.Delete(id);
   
    return NoContent();
}
}