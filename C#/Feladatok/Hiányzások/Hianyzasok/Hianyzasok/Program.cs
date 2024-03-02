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
        Console.ReadKey();
    }
}