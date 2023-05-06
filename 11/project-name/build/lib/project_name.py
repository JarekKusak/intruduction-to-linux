#!/usr/bin/env python3

import os
from git import Repo

def get_git_root():
    try:
        repo = Repo('.', search_parent_directories=True)
        return repo.working_tree_dir.split('/')[-1]
    except:
        return None

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
                    if os.stat(nazev).st_size == 0: 
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
            git_root = get_git_root()
            if git_root is not None:
                print(git_root)
                return
            print(os.path.basename(os.getcwd()))
    except:
        print(os.path.basename(os.getcwd()))

if __name__ == '__main__':
    main()
