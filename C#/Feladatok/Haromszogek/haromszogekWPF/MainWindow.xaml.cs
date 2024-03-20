using haromszogekCLI;
using System;
using System.Collections.Generic;
using System.IO;
using System.Windows;

namespace haromszogekWPF
{
    public partial class MainWindow : Window
    {
        private List<Haromszog> triangles = new List<Haromszog>();

        public MainWindow()
        {
            InitializeComponent();
            LoadData();
        }

        private void LoadData()
        {
            try
            {
                using (StreamReader sr = new StreamReader("haromszogek2.csv"))
                {
                    while (!sr.EndOfStream)
                    {
                        string line = sr.ReadLine();
                        triangles.Add(new Haromszog(line));
                    }
                }

                dtg_adatok.ItemsSource = triangles;
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error loading data: " + ex.Message);
            }
        }

        private void btn_hozzaad_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                int a = Convert.ToInt32(txb_a.Text);
                int b = Convert.ToInt32(txb_b.Text);
                int c = Convert.ToInt32(txb_c.Text);

                if (a > 0 && b > 0 && c > 0 && a < b + c && b < a + c && c < a + b)
                {
                    triangles.Add(new Haromszog($"{a} {b} {c}" ));
                    dtg_adatok.Items.Refresh();
                }
                else
                {
                    MessageBox.Show("Nem megfelelő értékek!");
                }
            }
            catch (FormatException)
            {
                MessageBox.Show("Hibás formátum! Kérem, adjon meg számokat.");
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error: " + ex.Message);
            }
        }

        private void btn_mentes_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                StreamWriter sw = new StreamWriter("haromszogek3.csv");
                foreach (var item in triangles)
                {
                    sw.WriteLine(item.a+" "+item.b+" "+item.c);
                }
                sw.Flush();
                sw.Close();
                MessageBox.Show("Mentés sikeresen megtörtént!");
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }
    }
}
