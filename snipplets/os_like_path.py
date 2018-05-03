# adapt slashes and backslashes for windows or unix
from pathlib import Path
import os

pdfrechungsfile = str(Path(((os.getcwd()) + '/file.pdf')))
print(pdfrechungsfile)

# Path pass die slash oder backslash je nach windos oder nix

# os.getcwd findet der current folder