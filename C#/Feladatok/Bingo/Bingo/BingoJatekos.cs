using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Bingo
{

    public class BingoJatekos
    {
       
        public BingoJatekos(string jatekosNeve, string elsoSor, string masodikSor, string harmadikSor, string negyedikSor, string otodikSor)
        {
            this.jatekosNeve = jatekosNeve;
            this.elsoSor = elsoSor;
            this.masodikSor = masodikSor;
            this.harmadikSor = harmadikSor;
            this.negyedikSor = negyedikSor;
            this.otodikSor = otodikSor;
        }

        
        public string jatekosNeve { get; set; }
        public string elsoSor {  get; set; }
        public string masodikSor { get; set; }  
        public string harmadikSor { get; set; }
        public string negyedikSor { get; set; }
        public string otodikSor { get; set; }

        public static bool BingoEll(BingoJatekos jatekos)
        {
            if (HasBingo(jatekos.elsoSor) || HasBingo(jatekos.masodikSor) || HasBingo(jatekos.harmadikSor) ||
                HasBingo(jatekos.negyedikSor) || HasBingo(jatekos.otodikSor))
                return true;

            for (int i = 0; i < 5; i++)
            {
                string column = jatekos.elsoSor[i].ToString() + jatekos.masodikSor[i] + jatekos.harmadikSor[i] +
                                jatekos.negyedikSor[i] + jatekos.otodikSor[i];
                if (HasBingo(column))
                    return true;
            }

            string diagonal1 = jatekos.elsoSor[0].ToString() + jatekos.masodikSor[1] + jatekos.harmadikSor[2] +
                                jatekos.negyedikSor[3] + jatekos.otodikSor[4];
            string diagonal2 = jatekos.elsoSor[4].ToString() + jatekos.masodikSor[3] + jatekos.harmadikSor[2] +
                                jatekos.negyedikSor[1] + jatekos.otodikSor[0];

            if (HasBingo(diagonal1) || HasBingo(diagonal2))
                return true;

            return false;
        }

        private static bool HasBingo(string line)
        {
            return line.Replace("X", "").Length == 0;
        }


        public static void SorsoltSzamotJelol(int szam, BingoJatekos jatekos)
        {
            char[] elsoSorArray = jatekos.elsoSor.ToCharArray();
            for (int i = 0; i < elsoSorArray.Length; i++)
            {
                if (Convert.ToInt32(elsoSorArray[i]) == szam)
                {
                    elsoSorArray[i] = 'X';
                }
            }
            jatekos.elsoSor = new string(elsoSorArray);

            char[] masodikSorArray = jatekos.masodikSor.ToCharArray();
            for (int i = 0; i < masodikSorArray.Length; i++)
            {
                if (Convert.ToInt32(masodikSorArray[i]) == szam)
                {
                    masodikSorArray[i] = 'X';
                }
            }
            jatekos.masodikSor = new string(masodikSorArray);

            char[] harmadikSorArray = jatekos.harmadikSor.ToCharArray();
            for (int i = 0; i < harmadikSorArray.Length; i++)
            {
                if (Convert.ToInt32(harmadikSorArray[i]) == szam)
                {
                    harmadikSorArray[i] = 'X';
                }
            }
            jatekos.harmadikSor = new string(harmadikSorArray);

            char[] negyedikSorArray = jatekos.negyedikSor.ToCharArray();
            for (int i = 0; i < negyedikSorArray.Length; i++)
            {
                if (Convert.ToInt32(negyedikSorArray[i]) == szam)
                {
                    negyedikSorArray[i] = 'X';
                }
            }
            jatekos.negyedikSor = new string(negyedikSorArray);

            char[] otodikSorArray = jatekos.otodikSor.ToCharArray();
            for (int i = 0; i < otodikSorArray.Length; i++)
            {
                if (Convert.ToInt32(otodikSorArray[i]) == szam)
                {
                    otodikSorArray[i] = 'X';
                }
            }
            jatekos.otodikSor = new string(otodikSorArray);
        }

    }
}
