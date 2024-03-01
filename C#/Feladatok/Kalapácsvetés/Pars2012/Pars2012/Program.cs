using System.IO;
class Program
{
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
        Console.ReadKey();
    }
}