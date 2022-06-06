using Newtonsoft.Json;

namespace ArtGenerator.Utilities
{
	/// <summary>Utility class to convert json to generic T.</summary>
	public static class JsonUtility<T>
	{
		/// <summary>Convert JSON to given generic T.</summary>
		/// <returns>Generic T</returns>
		public static T ConvertFromJson(string json) => JsonConvert.DeserializeObject<T>(json);
	}
}
