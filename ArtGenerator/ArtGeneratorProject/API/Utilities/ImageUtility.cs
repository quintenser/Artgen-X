using System;
using System.IO;
using System.Windows.Media.Imaging;

namespace ArtGenerator.Utilities
{
	/// <summary>Utility class to clean and convert base64 string to a <c>BitmapImage</c>.</summary>
	public static class ImageUtility
	{
		/// <summary>Cleans given string from any wrapping and converts it to a <c>BitmapImage</c>.</summary>
		/// <returns><c>BitmapImage</c></returns>
		public static BitmapImage ConvertFromBase64ToBitmapImage(string str)
		{
			BitmapImage image = new BitmapImage();
			image.BeginInit();
			image.StreamSource = new MemoryStream(Convert.FromBase64String(CleanBase64String(str)));
			image.EndInit();
			return image;
		}

		/// <summary>Cleans given string from any wrapping.</summary>
		/// <returns>Clean base64 string</returns>
		private static string CleanBase64String(string str) => str.Split("'")[1];
	}
}
