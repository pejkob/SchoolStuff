using System;
using System.Collections.Generic;
using System.IO;

namespace Bingo
{
    public class Program
    {
        public static Random rnd;
        static void Main(string[] args)
        {
            List<BingoJatekos> jatekosok = new List<BingoJatekos>();

            using (StreamReader sr = new StreamReader("Nevek/nevek.text"))
            {
                while (!sr.EndOfStream)
                {
                    string nevFile = sr.ReadLine();
                    using (StreamReader sr2 = new StreamReader("Nevek/" + nevFile))
                    {
                        string jatekosNeve = Path.GetFileNameWithoutExtension(nevFile);
                        string elsoSor = sr2.ReadLine();
                        string masodikSor = sr2.ReadLine();
                        string harmadikSor = sr2.ReadLine();
                        string negyedikSor = sr2.ReadLine();
                        string otodikSor = sr2.ReadLine();

                        jatekosok.Add(new BingoJatekos(jatekosNeve, elsoSor, masodikSor, harmadikSor, negyedikSor, otodikSor));
                    }
                }
            }

            Console.WriteLine("4. feladat: Játékosok száma: "+jatekosok.Count);


            Console.WriteLine("7. feladat: Kihúzott számok");
            int huzasSzam = 0;

            List<int> sorsoltSzamok = new();
            foreach (var item in jatekosok)
            {
                while (!BingoJatekos.BingoEll(item))
                {
                    rnd = new Random();
                    int sorsoltszam = rnd.Next(1, 75);
                    if (!sorsoltSzamok.Contains(sorsoltszam))
                    {
                        huzasSzam++;
                        sorsoltSzamok.Add(sorsoltszam);
                        BingoJatekos.SorsoltSzamotJelol(sorsoltszam,item);
                        Console.Write($"{huzasSzam}.-> {sorsoltszam} ");
                    }
                    else
                    {
                        sorsoltszam = rnd.Next(1, 75);
                    }
                }
            }
            Console.ReadKey();
        }
    }
}