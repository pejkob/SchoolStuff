using System;

	public class Hianyzasok
	{
		public Hianyzasok(string nev, string osztaly, int elso, int utolso, int mulasztott)
		{
			this.nev = nev;
			this.osztaly = osztaly;
			this.elsoNap = elso;
			this.utolsoNap = utolso;
			this.mulasztottOrakSzama = mulasztott;
		}

		public string nev { get; set; }
		public string osztaly { get; set; }
		public int elsoNap { get; set; }
		public int utolsoNap { get; set; }
		public int mulasztottOrakSzama { get; set; }
	}


