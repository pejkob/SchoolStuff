using System;
using System.Collections.Generic;

namespace AutoBerles.Models;

public partial class Autok
{
    public int Id { get; set; }

    public string Rendszam { get; set; } = null!;

    public string Tipus { get; set; } = null!;

    public int Evjarat { get; set; }

    public string Szin { get; set; } = null!;
}
