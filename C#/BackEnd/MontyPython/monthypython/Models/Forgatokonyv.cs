using System;
using System.Collections.Generic;

namespace monthypython.Models;

public partial class Forgatokonyv
{
    public int Id { get; set; }

    public int Epizodid { get; set; }

    public string Resz { get; set; } = null!;

    public int Tipusid { get; set; }

    public string Szinesz { get; set; } = null!;

    public string Karakter { get; set; } = null!;

    public string Reszletek { get; set; } = null!;

    public DateTime FelvetelDatuma { get; set; }

    public DateTime LejatszasDatuma { get; set; }
    
    public virtual Epizodok Epizod { get; set; } = null!;

    public virtual Tipusok Tipus { get; set; } = null!;
}
