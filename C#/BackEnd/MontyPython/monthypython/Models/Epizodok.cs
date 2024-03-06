using System;
using System.Collections.Generic;
using System.Text.Json.Serialization;

namespace monthypython.Models;

public partial class Epizodok
{
    public int Id { get; set; }

    public string Nev { get; set; } = null!;

    public string Sorozat { get; set; } = null!;
    [JsonIgnore]
    public virtual ICollection<Forgatokonyv> Forgatokonyvs { get; set; } = new List<Forgatokonyv>();
}
