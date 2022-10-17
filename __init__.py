import sys


def main():
    try:
        with open(sys.argv[0], "r+") as source:
            for a in source.readlines():
                with open(sys.argv[1], "+w") as t:
                    t.write(a)
    except IndexError as e:
        print("""
        no arguments for src or dest
        for example do red.txt /Docuements
    
        """)
