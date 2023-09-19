class Main:
    """Main class"""

    def __init__(self, APIKEY=""):
        """Constructor"""
        self.api_key = APIKEY

    def test(self):
        """Test function"""
        print(self.api_key)
