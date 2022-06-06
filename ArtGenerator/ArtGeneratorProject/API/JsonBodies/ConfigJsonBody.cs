namespace ArtGenerator.API.JsonBodies
{
	public class ConfigJsonBody : JsonBodyBase
	{
		public int imageWidth { get; set; } = 1080;
		public int imageHeight { get; set; } = 1920;
		public int lineAmount { get; set; } = 7;
		public int squareAmount { get; set; } = 10;
		public int circleAmount { get; set; } = 8;
        public int triangleAmount { get; set; } = 20;
		public int generations_until_algorithm_is_used { get; set; } = 6;
		public int small_mutation_chance { get; set; } = 3;
		public int big_mutation_chance { get; set; } = 80;
		public int max_parents { get; set; } = 30;
	}
}
