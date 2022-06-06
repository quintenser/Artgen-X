using System.Diagnostics;
using System.IO;
using RestSharp;
using ArtGenerator.API.Responses;
using ArtGenerator.API.JsonBodies;
using System.Reflection;

namespace ArtGenerator.API
{
	/// <summary>Python requests generator.</summary>
	public class PythonRequester
	{
		private const string BaseUrl = "http://127.0.0.1:5000/api";

		private RestClient Client { get; set; }
		private Process Process { get; set; }

		/// <summary>Check if local server is active.</summary>
		/// <returns>bool status of server</returns>
		public bool IsServerActive => Client.Execute(new RestRequest("/status"), Method.GET).StatusCode == System.Net.HttpStatusCode.OK ? true : false;

		public PythonRequester()
		{
			Client = new RestClient(BaseUrl);

			if (!IsServerActive)
			{
				StartLocalServer();
			}
		}

		/// <summary>Send request to reset the art generator.</summary>
		/// <returns><c>ImageResponse</c></returns>
		public ImageResponse SendImageRequest()
		{
			Request<ImageResponse> request = new Request<ImageResponse>(Client, $"/image", Method.GET);
			return request.Send();
		}

		public DataResponse SendSelectImageRequest(int id)
		{
			Request<DataResponse> request = new Request<DataResponse>(Client, $"/{id}/image", Method.POST);
			return request.Send();
		}

		/// <summary>Send request to get a image.</summary>
		public void ResetArtGeneratorRequest()
		{
			Client.Execute(new RestRequest("/reset"), Method.GET);
		}

		/// <summary>Send request to update the config the generator uses.</summary>
		/// <returns><c>ConfigResponse</c></returns>
		public ConfigResponse SendUpdateConfigRequest(ConfigJsonBody userValues)
		{
			Request<ConfigResponse> request = new Request<ConfigResponse>(Client, "/config", Method.POST);
			return request.Send(userValues);
		}

		/// <summary>Start local server</summary>
		private void StartLocalServer()
		{
			string pathToCurrentDirectory = Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location);
			string pathToServerStartFile = Path.Combine(pathToCurrentDirectory, @"Python\start_server.bat");

			Process = new Process();
			Process.StartInfo = new ProcessStartInfo()
			{
				FileName = pathToServerStartFile,
				UseShellExecute = false,
				WorkingDirectory = Path.Combine(pathToCurrentDirectory, @"Python")
			};
			Process.Start();
		}
	}
}
