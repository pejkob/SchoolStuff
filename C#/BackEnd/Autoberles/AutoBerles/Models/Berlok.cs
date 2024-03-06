using System;
using System.Collections.Generic;

namespace AutoBerles.Models;

public partial class Berlok
{
    public int Id { get; set; }

    public string Nev { get; set; } = null!;

    public string Jogositvanyszama { get; set; } = null!;

    public string Telefonszam { get; set; } = null!;

    public DateTime Szuletesiido { get; set; }

    public string Lakcim { get; set; } = null!;

    public virtual ICollection<Kolcsonze> Kolcsonzes { get; set; } = new List<Kolcsonze>();
}
