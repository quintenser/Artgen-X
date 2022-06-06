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
using ArtGenerator.API.JsonBodies;
using ArtGenerator.API;
using System.Diagnostics;

namespace ArtGenerator
{
    /// <summary>
    /// Interaction logic for ConfigScreen.xaml
    /// </summary>
    public partial class ConfigScreen : UserControl
    {
        public ConfigJsonBody UserValues { get; set; }

        public ConfigScreen()
        {
            UserValues = new ConfigJsonBody();
            InitializeComponent();
            PythonAPI.API.ResetArtGenerator();
            PythonAPI.API.UpdateGeneratorConfig(UserValues);
        }

        private void sli_Conf(object sender, System.Windows.RoutedPropertyChangedEventArgs<double> e)
        {
            if ((sliLine != null) && (sliCircle !=  null) && (sliRectangle != null) && (sliTriangle != null) && (sliAlg!= null) && (sliSmaMu != null) && (sliBigMu != null) && (sliWidth != null) && (sliHeight != null) && (sliParents != null))
            {
                UserValues.lineAmount = (int)sliLine.Value;
                UserValues.circleAmount = (int)sliCircle.Value;
                UserValues.squareAmount = (int)sliRectangle.Value;
                UserValues.triangleAmount = (int)sliTriangle.Value;
                UserValues.generations_until_algorithm_is_used = (int)sliAlg.Value;
                UserValues.small_mutation_chance = (int)sliSmaMu.Value;
                UserValues.big_mutation_chance = (int)sliBigMu.Value;
                UserValues.imageWidth = (int)sliWidth.Value;
                UserValues.imageHeight = (int)sliHeight.Value;
                UserValues.max_parents = (int)sliParents.Value;
                if ((int)sliLine.Value > 2200)
                {
                    label_Line.Foreground = new SolidColorBrush(Color.FromArgb(255, 245, 163, 0));
                }
                if ((int)sliLine.Value < 2200)
                {
                    label_Line.Foreground = new SolidColorBrush(Color.FromArgb(255, 66, 251, 128));
                }
                if ((int)sliCircle.Value > 700)
                {
                    label_Circle.Foreground = new SolidColorBrush(Color.FromArgb(255, 245, 163, 0));
                }
                if ((int)sliCircle.Value < 700)
                {
                    label_Circle.Foreground = new SolidColorBrush(Color.FromArgb(255, 66, 251, 128));
                }
                if ((int)sliRectangle.Value > 700)
                {
                    label_Square.Foreground = new SolidColorBrush(Color.FromArgb(255, 245, 163, 0));
                }
                if ((int)sliRectangle.Value < 700)
                {
                    label_Square.Foreground = new SolidColorBrush(Color.FromArgb(255, 66, 251, 128));
                }
                if ((int)sliTriangle.Value > 500)
                {
                    label_Triangle.Foreground = new SolidColorBrush(Color.FromArgb(255, 245, 163, 0));
                }
                if((int)sliTriangle.Value < 500)
                {
                    label_Triangle.Foreground = new SolidColorBrush(Color.FromArgb(255, 66, 251, 128));
                }
                if ((int)sliHeight.Value > 1921)
                {
                    label_Height.Foreground = new SolidColorBrush(Color.FromArgb(255, 246, 113, 113));
                }
                if ((int)sliHeight.Value < 1921)
                {
                    label_Height.Foreground = new SolidColorBrush(Color.FromArgb(255, 66, 251, 128));
                }
                if ((int)sliWidth.Value > 1080)
                {
                    label_Width.Foreground = new SolidColorBrush(Color.FromArgb(255, 246, 113, 113));
                }
                if ((int)sliWidth.Value < 1080)
                {
                    label_Width.Foreground = new SolidColorBrush(Color.FromArgb(255, 66, 251, 128));
                }
            }
        }

        private void displayStart(object sender, RoutedEventArgs e)
        {
            Window StartWindow = new Window
            {
                Title = "Kunstgenerator",
                WindowState = WindowState.Maximized,
                Content = new StartScreen()

            };
            StartWindow.Show();
            Window.GetWindow(this).Close();
        }

        public void displayGenerator()
        {
            MainWindow NewWindow = new MainWindow()
            {
                WindowState = WindowState.Maximized
            };
            NewWindow.Show();
            Window.GetWindow(this).Close();
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            PythonAPI.API.UpdateGeneratorConfig(UserValues);
            displayGenerator();
        }

    }
}
