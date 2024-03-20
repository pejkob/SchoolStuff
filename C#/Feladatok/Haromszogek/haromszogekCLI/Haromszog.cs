using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace haromszogekCLI
{
    public class Haromszog
    {
        public int a { get; set; }
        public int b { get; set; }
        public int c { get; set; }

        public Haromszog(string line)
        {
            string[] bytes = line.Split(" ");
            this.a =Convert.ToInt32( bytes[0]);
            this.b = Convert.ToInt32(bytes[1]);
            this.c = Convert.ToInt32(bytes[2]);
        }

       public  bool derekszogu(int a, int b,int c)
        {
            if (Math.Pow(a,2)+Math.Pow(b,2)==Math.Pow(c,2)) return true;
            return false;
        }
    }
}
