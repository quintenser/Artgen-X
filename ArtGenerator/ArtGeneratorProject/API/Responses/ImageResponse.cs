namespace ArtGenerator.API.Responses
{
	/// <summary>HTTP response containing image properties.</summary>
	public class ImageResponse
	{
		public int imageId { get; set; }
		public string base64String { get; set; }
	}
}
