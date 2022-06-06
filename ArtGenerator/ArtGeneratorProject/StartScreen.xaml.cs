using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace ArtGenerator
{
    /// <summary>
    /// Interaction logic for StartScreen.xaml
    /// </summary>
    public partial class StartScreen : UserControl
    {
        public StartScreen()
        {
            InitializeComponent();
        }

        private void displayGenerator(object sender, RoutedEventArgs e)
        {
            MainWindow NewWindow = new MainWindow()
            {
                WindowState = WindowState.Maximized
            };
            NewWindow.Show();
            Window.GetWindow(this).Close();
        }

        private void displayConfig(object sender, RoutedEventArgs e)
        {
            Window ConfigWindow = new Window
            {
                Title = "Configuratie",
                Content = new ConfigScreen(),
                WindowState = WindowState.Maximized
        };
            ConfigWindow.Show();
            Window.GetWindow(this).Close();
        }

    }

}
