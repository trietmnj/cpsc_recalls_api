import argparse


class UserInterface:
    """CLI interface"""
    parser = None

    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description="Download recall data to a csv file")
        self.__add_args()

    def __add_args(self):
        # https://gist.github.com/fralau/061a4f6c13251367ef1d9a9a99fb3e8d
        self.parser.add_argument("-kv", "--key-value", metavar="KEY=VALUE",
                                 nargs="+", help="Specify key-value pairs "
                                 "(do not put spaces before or after the = sign). "
                                 "If a value contains spaces, you should define "
                                 "it with double quotes: "
                                 'foo="this is a sentence". Note that '
                                 "values are always treated as strings.")

    def get_args(self):
        return self.parser.parse_args()

    def get_args_dict(self) -> dict:
        """Returns a dict with key / value pairs specified using -kv"""
        return self.__parse_vars(self.parser.parse_args().key_value)

    @staticmethod
    def __parse_var(s):
        """
        Parse a key, value pair, separated by '='
        That's the reverse of ShellArgs.

        On the command line (argparse) a declaration will typically look like:
            foo=hello
        or
            foo="hello world"
        """
        items = s.split('=')
        key = items[0].strip() # we remove blanks around keys, as is logical
        if len(items) > 1:
            # rejoin the rest:
            value = '='.join(items[1:])
        return (key, value)

    def __parse_vars(self, items):
        """
        Parse a series of key-value pairs and return a dictionary
        """
        d = {}

        if items:
            for item in items:
                key, value = self.__parse_var(item)
                d[key] = value
        return d

