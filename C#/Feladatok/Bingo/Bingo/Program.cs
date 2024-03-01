using System;
using System.Collections.Generic;
using System.IO;

namespace Bingo
{
    public class Program
    {
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

            Console.WriteLine(jatekosok.Count);
            Console.ReadKey();
        }
    }
}