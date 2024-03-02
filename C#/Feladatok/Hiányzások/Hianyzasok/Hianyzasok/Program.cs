class Program
{
    private static void Main(string[] args)
    {
        Console.WriteLine("Hello, World!");

        List<Hianyzasok> hianyzasokLista = new List<Hianyzasok>();
        StreamReader sr = new StreamReader("szeptember.csv");
        string elsoSor = sr.ReadLine();
        while (!sr.EndOfStream)
        {
            string sor = sr.ReadLine();
            string[] sorSplit = sor.Split(";");
            hianyzasokLista.Add(new Hianyzasok(sorSplit[0], sorSplit[1], Convert.ToInt32(sorSplit[2]), Convert.ToInt32(sorSplit[3]), Convert.ToInt32(sorSplit[4])));
        }
        int osszesMulasztott = 0;
        foreach (var item in hianyzasokLista)
        {
            osszesMulasztott += item.mulasztottOrakSzama;
        }
        Console.WriteLine($"2. feladat\n\tÖsszes mulasztott órák száma: {osszesMulasztott} óra.");
        int bekertSzam;
        do
        {
            Console.Write("3. fealdat\n\tKérem adjon meg egy napot: ");
        } while (!int.TryParse(Console.ReadLine(), out bekertSzam) || bekertSzam < 1 || bekertSzam > 30);

        Console.Write("\tTanuló neve: ");
        string bekertNev = Console.ReadLine();

        bool hianyzott = false;

        foreach (var item in hianyzasokLista)
        {
            if (item.nev==bekertNev)
            {
                hianyzott = true;
                break;
            }
        }
        Console.WriteLine("4. feladat");
        Console.Write(hianyzott?"\tA tanuló hiányzott szeptemberben":"\tA tanuló nem hiányzott szeptemberben" );

        List<Hianyzasok> hianyzasokAdottNapon = new List<Hianyzasok>();
        foreach (var item in hianyzasokLista)
        {
            if (item.elsoNap==bekertSzam||item.utolsoNap==bekertSzam)
            {
                hianyzasokAdottNapon.Add(item);
            }
        }

        Console.WriteLine($"5. feladat: Hiányzók 2017.09.{bekertSzam}-n:");
        if (hianyzasokAdottNapon.Count==0)
        {
            Console.WriteLine("\tNem volt hiányzó");
        }
        else
        {
            foreach (var item in hianyzasokAdottNapon)
            {
                Console.WriteLine($"\t{item.nev} {item.osztaly}");
            }
        }

        Dictionary<string, int> osszesites = new Dictionary<string, int>();

        foreach (var item in hianyzasokLista)
        {
            if (!osszesites.ContainsKey(item.osztaly))
            {
                osszesites[item.osztaly] = item.mulasztottOrakSzama;
            }
            else
            {
                osszesites[item.osztaly] += item.mulasztottOrakSzama;
            }
        }

        using (StreamWriter sw = new StreamWriter("osszesites.csv"))
        {
            foreach (var item in osszesites)
            {
                sw.WriteLine($"{item.Key};{item.Value}");
            }
        }



        Console.ReadKey();
    }
}