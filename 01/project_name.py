import os

#!/usr/bin/env python3

def main():
    nazvy = ["README.md", "readme.md", "README", "readme"]
    pom = False
    nazev = None
    try:
        for i in range(len(nazvy)):
            if os.path.isfile(nazvy[i]):
                nazev = nazvy[i]
                pom = True
                break
        if pom:
            with open(nazev, mode="r", encoding="utf-8") as f:
                line = f.readline()
                while(line != ""): # čte po řádcích, dokud neskončí soubor
                    
                    if line[0] == "\n":
                        line = f.readline()
                        continue
                    elif line[0] == "":
                        line = f.readline()
                        continue
                    elif line.strip().lstrip('# ') == '':
                        line = f.readline()
                        continue
                    else:
                        s = line.replace("#", " ")  
                        s = s.strip()
                        print(s)
                        break
                

        else:
            print(os.path.basename(os.getcwd()))
    except:
        print(os.path.basename(os.getcwd()))

if __name__ == '__main__':
    main()
