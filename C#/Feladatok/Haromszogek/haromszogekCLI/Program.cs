namespace haromszogekCLI
{
    public class Program
    {
        public static List<Haromszog> triangles = new List<Haromszog>();

        public static void LoadData()
        {

            StreamReader sr = new StreamReader("haromszogek2.csv");

            while (!sr.EndOfStream)
            {
                triangles.Add(new Haromszog(sr.ReadLine()));
            }
            sr.Close();
        }
        static void Main(string[] args)
        {

            LoadData();

            foreach (var item in triangles)
            {
                if (item.derekszogu(item.a, item.b, item.c))
                {
                    Console.WriteLine($"a:{item.a} b:{item.b} c:{item.c}");
                }

            }
                double maxTerulet = 0;
                int maxIndex = 0;
                for (int i = 0; i < triangles.Count; i++)
                {
                    double aktTerulet = triangles[i].a * triangles[i].b / 2;
                    if (maxTerulet < aktTerulet && triangles[i].derekszogu(triangles[i].a, triangles[i].b, triangles[i].c))
                    {
                        maxTerulet = aktTerulet;
                        maxIndex = i;
                    }
                }
                Console.WriteLine("A legnagyobb területű derékszögű háromszög adatai:");
                Console.WriteLine($"a: {triangles[maxIndex].a} b: {triangles[maxIndex].b} c: {triangles[maxIndex].c}");
        }
    }
}
