namespace ifood_challenge.Models
{
    public class Category
    {
        private Category(string value)
        {
            Value = value;
        }

        public string Value { get; }

        public static Category PopMusic
        {
            get
            {
                return new Category("pop");
            }
        }

        public static Category RockMusic
        {
            get
            {
                return new Category("rock");
            }
        }

        public static Category ClassicalMusic
        {
            get
            {
                return new Category("classical");
            }
        }

        public static Category PartyMusic
        {
            get
            {
                return new Category("party");
            }
        }
    }
}
