using ArtGenerator.API.Containers;
using ArtGenerator.API.Responses;
using ArtGenerator.Utilities;
using ArtGenerator.API.JsonBodies;
using System.Windows.Forms;
using System.IO;

namespace ArtGenerator.API
{
	/// <summary>API to make requests to the Python Art Generator REST API.</summary>
	public class PythonAPI
	{
		private static PythonAPI api;
		private PythonRequester PythonRequester { get; set; }
		public bool ReceiveImageData { get; set; }
		private string SavePath { get; set; }

		/// <summary>API to make requests to the Python Art Generator REST API.</summary>
		/// <returns><c>PythonAPI</c></returns>
		public static PythonAPI API => api ??= new PythonAPI();

		/// <summary>Check if local server is active.</summary>
		/// <returns>bool status of server</returns>
		public bool IsServerActive => PythonRequester.IsServerActive;

		private PythonAPI()
		{
			PythonRequester = new PythonRequester();
		}

		/// <summary>Requests a <c>Image</c> from the Python Art Generator REST API.</summary>
		/// <returns><c>ImageContainer</c></returns>
		public ImageContainer GetImage()
		{
			ImageResponse response = PythonRequester.SendImageRequest();
			return new ImageContainer(response.imageId, ImageUtility.ConvertFromBase64ToBitmapImage(response.base64String));
		}

		public void SelectImage(int id)
		{
			DataResponse response = PythonRequester.SendSelectImageRequest(id);

			if (ReceiveImageData)
			{	
				File.WriteAllText($"{SavePath}/liked_image_generation{response.id}.json", response.canvasData);
			}
		}

		public void UpdateGeneratorConfig(ConfigJsonBody userValues)
		{
			ConfigResponse response = PythonRequester.SendUpdateConfigRequest(userValues);
		}

		public bool SaveSelectedPath(bool willSave)
        {
			if (willSave)
			{
				FolderBrowserDialog folderDlg = new FolderBrowserDialog();
				DialogResult result = folderDlg.ShowDialog();

				if (result == DialogResult.OK)
				{
					SavePath = folderDlg.SelectedPath;
					return true;
				}
			}
			return false;
		}

		public void ResetArtGenerator()
		{
			PythonRequester.ResetArtGeneratorRequest();
		}
    }
}
