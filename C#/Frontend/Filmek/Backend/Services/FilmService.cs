using Filmek.Models;

namespace Filmek.Services;

public static class FilmService
{
    static List<Film> Filmek { get; }
    static int nextId = 5;
    static FilmService()
    {
        Filmek = new List<Film>
        {
            new Film { Id = 1, Nev = "StarWars", KiadasEve=2022, Ertekeles=5, Kepneve="starwars.jpg" },
            new Film { Id = 2, Nev = "Tenet", KiadasEve=2021, Ertekeles=4, Kepneve="tenet.jpg" },
            new Film { Id = 3, Nev = "X-akták", KiadasEve=2018, Ertekeles=3, Kepneve="thexfiles.jpg" },
            new Film { Id = 4, Nev = "Wednesday", KiadasEve=2022, Ertekeles=5, Kepneve="wednesday.jpg" }
        };
    }

    public static List<Film> GetAll() => Filmek;

    public static Film? Get(int id) => Filmek.FirstOrDefault(p => p.Id == id);

    public static void Add(Film film)
    {
        film.Id = nextId++;
        Filmek.Add(film);
    }

    public static void Delete(int id)
    {
        var film = Get(id);
        if(film is null)
            return;

        Filmek.Remove(film);
    }

    public static void Update(Film film)
    {
        var index = Filmek.FindIndex(p => p.Id == film.Id);
        if(index == -1)
            return;

        Filmek[index] = film;
    }
}