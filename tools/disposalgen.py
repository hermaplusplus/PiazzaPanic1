# Rudimentarily generates disposals code from a list of variable declarations (not all variables are actually disposable).
# Example usage:
#   python .\disposalgen.py """OrthographicCamera camera;
#   >>     SpriteBatch batch;
#   >>     BitmapFont font;"""

import sys
print("\n".join([k.replace(";", ".dispose();") for k in [j.split(" ")[1] for j in [i.strip("\t ") for i in sys.argv[1:][0].split("\n")]]]))
