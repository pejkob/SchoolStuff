class Program
{

    public static bool MaxDobas(Versenyzo versenyzo)
    {
        if (versenyzo.d1 ==-2 || versenyzo.d2 ==-2 || versenyzo.d3 ==-2)
        {
            return true;
        }
        return false;
    }
    static void Main(string[] args)
    {
        List<Versenyzo> versenyzok = new List<Versenyzo>();
        using (StreamReader sr = new StreamReader("Selejtezo2012.txt"))
        {
            string elsoSor = sr.ReadLine();
            while (!sr.EndOfStream)
            {
                versenyzok.Add(new Versenyzo(sr.ReadLine()));
            }
        }

        Console.WriteLine($"5. feladat: Versenyzők száma a selejtezőben: {versenyzok.Count} fő");
        int tovabbjutott = 0;
        foreach (var item in versenyzok)
        {
            if (MaxDobas(item))
            {
                tovabbjutott++;
            }
        }
        Console.WriteLine($"6. feladat: 78,00 feletti eredménnyel továbbjutott: {tovabbjutott} fő" );
        Console.ReadKey();
    }
}