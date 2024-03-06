using System;
using System.Collections.Generic;

namespace AutoBerles.Models;

public partial class Kolcsonze
{
    public int Id { get; set; }

    public int Berloid { get; set; }

    public int Autoid { get; set; }

    public DateTime Berletkezdete { get; set; }

    public int Napokszama { get; set; }

    public double Napidij { get; set; }

    public virtual Berlok Berlo { get; set; } = null!;
}
