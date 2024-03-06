using System;
using System.Collections.Generic;
using System.Text.Json.Serialization;

namespace monthypython.Models;

public partial class Tipusok
{
    public int Id { get; set; }

    public string Tipus { get; set; } = null!;
    [JsonIgnore]
    public virtual ICollection<Forgatokonyv> Forgatokonyvs { get; set; } = new List<Forgatokonyv>();
}
