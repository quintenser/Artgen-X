using System;
using System.Windows;
using System.Windows.Media;
using System.Windows.Media.Imaging; 
using ArtGenerator.API;
using ArtGenerator.API.Containers;
using System.IO;
using System.Reflection;

namespace ArtGenerator
{
	/// <summary>
	/// Interaction logic for MainWindow.xaml
	/// </summary>
	public partial class MainWindow : Window
	{
		public ImageContainer LeftImageContainer { get; set; }
		public ImageContainer RightImageContainer { get; set; }

		public bool isPinnedL = false;
		public bool isPinnedR = false;

		public bool IsChecked
		{
			get { return PythonAPI.API.ReceiveImageData; }
			set
			{
				PythonAPI.API.ReceiveImageData = PythonAPI.API.SaveSelectedPath(value);
			}
		}

		public MainWindow()
		{

			InitializeComponent();
			PythonAPI.API.ResetArtGenerator();
			RefreshArt();
			cb1.DataContext = this;
		}

		private void sli_ValueChanged(object sender, RoutedPropertyChangedEventArgs<double> e)
		{
			SolidColorBrush magicBrush = (SolidColorBrush)Resources["magicBrush"];

			if ((sliR != null) && (sliG != null) && (sliB != null))
			{
				magicBrush.Color = System.Windows.Media.Color.FromRgb((byte)sliR.Value, (byte)sliG.Value, (byte)sliB.Value);
			}
		}

		private void PinLeft(object sender, RoutedEventArgs e)
        {
			string pathToProject = Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location);
			if (!isPinnedL)
			{ 
				string pinnedPin = Path.Combine(pathToProject, @"Images\Icons\pinned.png");
				pinLeft.Background = new ImageBrush(new BitmapImage(new Uri(pinnedPin, UriKind.Relative)));
			}
			else
            {
				string pin = Path.Combine(pathToProject, @"Images\Icons\pushpin.png");
				pinLeft.Background = new ImageBrush(new BitmapImage(new Uri(@pin, UriKind.Relative)));
			}
			isPinnedL = !isPinnedL;
		}

		private void PinRight(object sender, RoutedEventArgs e)
		{
			string pathToProject = Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location);
			if (!isPinnedR)
			{
				string pinnedPin = Path.Combine(pathToProject, @"Images\Icons\pinned.png");
				pinRight.Background = new ImageBrush(new BitmapImage(new Uri(pinnedPin, UriKind.Relative)));
			}
			else
			{
				string pin = Path.Combine(pathToProject, @"Images\Icons\pushpin.png");
				pinRight.Background = new ImageBrush(new BitmapImage(new Uri(@pin, UriKind.Relative)));
			}
			isPinnedR = !isPinnedR;
		}

		private void LeftImageClick(object sender, RoutedEventArgs e)
		{
			PythonAPI.API.SelectImage(LeftImageContainer.Id);
			RefreshArt();
		}

		private void RightImageClick(object sender, RoutedEventArgs e)
		{
			PythonAPI.API.SelectImage(RightImageContainer.Id);
			RefreshArt();
		}

		private void SaveRightImage_Click(object sender, EventArgs e)
		{
			// Create a SaveFileDialog Window, with the option to save the canvas as PNG format
			Microsoft.Win32.SaveFileDialog dlg = new Microsoft.Win32.SaveFileDialog();
			dlg.FileName = "Canvas";
			dlg.Filter = "PNG Image|*.png";
			if (dlg.ShowDialog() == true)
			{
				// Converts the BitmapImage of the right canvas to a PNG image with the help of the PngBitmapEncoder, then saves it on the set location of the SaveFileDialog
				var encoder = new PngBitmapEncoder(); 
				encoder.Frames.Add(BitmapFrame.Create(RightImageContainer.Image));
				using (var stream = dlg.OpenFile())
				{
					encoder.Save(stream);
				}
			}
		}

		private void SaveLeftImage_Click(object sender, EventArgs e)
		{
			// Create a SaveFileDialog Window, with the option to save the canvas as PNG format
			Microsoft.Win32.SaveFileDialog dlg = new Microsoft.Win32.SaveFileDialog();
			dlg.FileName = "Canvas";
			dlg.Filter = "PNG Image|*.png";
			if (dlg.ShowDialog() == true)
			{
				// Converts the BitmapImage of the left canvas to a PNG image with the help of the PngBitmapEncoder, then saves it on the set location of the SaveFileDialog
				var encoder = new PngBitmapEncoder(); 
				encoder.Frames.Add(BitmapFrame.Create(LeftImageContainer.Image));
				encoder.Frames.Add(BitmapFrame.Create(LeftImageContainer.Image));
				using (var stream = dlg.OpenFile())
				{
					encoder.Save(stream);
				}
			}
		}

		private void RefreshArt()
		{
			if (!isPinnedL)
			{
				LeftImageContainer = PythonAPI.API.GetImage();
				ImageLeft.Source = LeftImageContainer.Image;
			}

			if (!isPinnedR)
			{ 
				RightImageContainer = PythonAPI.API.GetImage();
				ImageRight.Source = RightImageContainer.Image;
			}
		}

		private void displayStart(object sender, RoutedEventArgs e)
		{
			Window StartWindow = new Window
			{
				Title = "Configuratie",
				WindowState = WindowState.Maximized,
				Content = new StartScreen()
			};
			StartWindow.Show();
			Window.GetWindow(this).Close();
		}

    }
}