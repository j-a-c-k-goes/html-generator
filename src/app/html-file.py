""" 
    Because index.html and style.css files 
    have been generated in frequent volume,
    copy and pasting becomes less effective; 
    + exposure to command-line parsing.  
"""

from optparse import OptionParser

class Parameters:
    def __init__(self, **kwargs):
        self.fileName = kwargs.get("fileName")
        self.h1 = kwargs.get("h1")
        self.destination = kwargs.get("destination")
    
    def view(inputs): 
        print(options)

    def make_file(inputs):
        filename = f"{options.destination}{options.fileName}"
        with open(filename, "w+") as file:
            file.write(
                f"""
<!HTML doctype>
    <head>
        <meta charset="utf-8"/>
    <title>{options.h1} | {options.fileName} </title>
    <link rel="stylesheet" type="text/css" src="./style.css">
</head>
    <body>
        <h1>{options.h1}</h1>
    </body>
</html>
                """)
        print(f"new file: {filename}")

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option(
        "--file", 
        dest="fileName", 
        help="something.html, something.css"
        )
    parser.add_option(
        "--h1", 
        dest="h1", 
        help="names h1 tag"
        )
    parser.add_option(
        "--destination", 
        dest="destination", 
        help="absolute directory, ./output/"
        )
    (options, args) = parser.parse_args()
    parameters = Parameters(
        fileName=options.fileName, 
        headline=options.h1, 
        destination=options.destination
        )
    parameters.make_file()
