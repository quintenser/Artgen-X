using System.Windows.Media.Imaging;

namespace ArtGenerator.API.Containers
{
	/// <summary>Contains image properties.</summary>
	public class ImageContainer
	{
		public int Id { get; private set; }
		public BitmapImage Image { get; private set; }

		public ImageContainer(int id, BitmapImage image)
		{
			Id = id;
			Image = image;
		}
	}
}
