public class Versenyzo
{
    public string nev { get; set; }
    public string csoport { get; set; }
    public string nemzetEsKod { get; set; }
    public double d1 { get; set; }
    public double d2 { get; set; }
    public double d3 { get; set; }

    public Versenyzo(string sor)
    {
        
        string[] sorSplit = sor.Split(';');
        if (sorSplit.Length != 6)
        {
            throw new ArgumentException("Invalid input string format. Expected format: 'name;group;nationality_code;d1;d2;d3'");
        }
        this.nev = sorSplit[0];
        this.csoport = sorSplit[1];
        this.nemzetEsKod = sorSplit[2];
        this.d1 = DobasErtek(sorSplit[3]);
        this.d2 = DobasErtek(sorSplit[4]);
        this.d3 = DobasErtek(sorSplit[5]);
    }

    public static double DobasErtek(string dobas)
    {
        switch (dobas)
        {
            case "X":
                return -1;
            case "-":
                return -2;
            default:
                if (double.TryParse(dobas, out double result))
                {
                    return result;
                }
                else
                {
                    throw new FormatException("Invalid input: unable to parse double value.");
                }
        }
    }
}
