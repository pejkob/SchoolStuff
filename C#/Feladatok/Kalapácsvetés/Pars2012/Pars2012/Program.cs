﻿
class Program
{
    public static bool MaxDobas(Versenyzo versenyzo)
    {
        if (versenyzo.d1 == -2 || versenyzo.d2 == -2 || versenyzo.d3 == -2)
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
        Console.WriteLine($"6. feladat: 78,00 feletti eredménnyel továbbjutott: {tovabbjutott} fő");
        int maxindex = 0;
        for (int i = 0; i < versenyzok.Count; i++)
        {
            if (versenyzok[i].Eredmeny() > versenyzok[maxindex].Eredmeny())
            {
                maxindex = i;
            }
        }

        Console.WriteLine($"9. feladat: A selejtező nyertese\n\tNév: {versenyzok[maxindex].nev}\n\tCsoport: {versenyzok[maxindex].csoport}\n\tNemzet: {Versenyzo.Nemzet(versenyzok[maxindex])}\n\tNemzet kód: {Versenyzo.Kod(versenyzok[maxindex])}\n\tSorozat: {versenyzok[maxindex].d1};{versenyzok[maxindex].d2};{versenyzok[maxindex].d3}\n\tEredmény: {versenyzok[maxindex].Eredmeny()} ");


        int helyezes = 0;
        using (StreamWriter sw = new StreamWriter("Dontos2012.txt"))
        {
            sw.WriteLine("Helyezés;Név;Csoport;Nemzet;NemzetKód;Sorozat;Eredmény");

            while (helyezes < 13 && versenyzok.Count > 0)
            {
                helyezes++;
                int max = 0;
                for (int i = 0; i < versenyzok.Count; i++)
                {
                    if (versenyzok[i].Eredmeny() > versenyzok[max].Eredmeny())
                    {
                        max = i;
                    }
                }
                sw.WriteLine($"{helyezes};{versenyzok[max].nev};{versenyzok[max].csoport};{Versenyzo.Nemzet(versenyzok[max])};{Versenyzo.Kod(versenyzok[max])};{versenyzok[max].d1};{versenyzok[max].d2};{versenyzok[max].d3};{versenyzok[max].Eredmeny()}");
                versenyzok.RemoveAt(max);
            }
        }

        Console.ReadKey();
    }
}

