#!/usr/bin/env python3

import os

def main():
    nazvy = ["README.md", "readme.md", "README", "readme"]
    pom = False
    nazev = None
    semaf = True
    try:
        for i in range(len(nazvy)):
            if semaf == False:
                break
            if os.path.isfile(nazvy[i]):
                nazev = nazvy[i]
                pom = True
            if pom:
                with open(nazev, mode="r", encoding="utf-8") as f:
                    if f.readline(1) == "":
                        continue
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
                            semaf = False
                            break
        if semaf:
            print(os.path.basename(os.getcwd()))
    except:
        print(os.path.basename(os.getcwd()))

if __name__ == '__main__':
    main()
