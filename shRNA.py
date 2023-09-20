def shRNA():
    ASinput = input('What is your AS strand? ')
    ASinputlow = ASinput.lower()
    ASlist = list(ASinputlow)
    ASdna = ""
    SSdnapre = ""
    SSdnalast = ""
    SSdna = ""
    for letter in ASlist:
        if letter == "u":
            ASdna += "t"
        else:
            ASdna += letter
    SSdnapre = ASdna[::-1]
    SSdnalast = list(SSdnapre)
    for letter2 in SSdnalast:
      if letter2 == "a":
        SSdna += "t"
      elif letter2 == "t":
        SSdna += "a"
      elif letter2 == "g":
        SSdna += "c"
      else:
        SSdna += "g"
    print("First oligo is (5' to 3'): " + "ctagcagt" + SSdna.upper() + "tagttatattcaagcata" + ASdna.upper() + "gcg")
    print("Second oligo is (5' to 3'): " + "aattcgc" + SSdna.upper() + "tatgcttgaatataacta" + ASdna.upper() + "actg")

    input("Press Enter to exit...")
shRNA()