using RestSharp;
using ArtGenerator.Utilities;
using ArtGenerator.API.JsonBodies;

namespace ArtGenerator.API
{
	/// <summary>Generic request class.</summary>
	public class Request<T>
	{
		public RestClient Client { get; set; }
		private string Resource { get; set; }
		private Method HttpMethod { get; set; }

		public Request(RestClient client, string resource, Method httpMethod)
		{
			Client = client;
			Resource = resource;
			HttpMethod = httpMethod;
		}

		/// <summary>Send the request.</summary>
		/// <returns><c>Generic T</c></returns>
		public T Send()
		{
			IRestResponse response = Client.Execute(new RestRequest(Resource), HttpMethod);
			return JsonUtility<T>.ConvertFromJson(response.Content);
		}

		/// <summary>Send the request with a json body.</summary>
		/// <returns><c>Generic T</c></returns>
		public T Send(JsonBodyBase body)
		{
			RestRequest request = new RestRequest(Resource);
			request.AddJsonBody(body);
			IRestResponse response = Client.Execute(request, HttpMethod);
			return JsonUtility<T>.ConvertFromJson(response.Content);
		}
	}
}
