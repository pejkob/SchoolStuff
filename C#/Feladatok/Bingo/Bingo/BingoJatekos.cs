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


    }
}
