# Filter Fasta program by Umberto Fasci

user_input = input("Enter mixed FASTA file: ")

fna_content = (">ORF", "ttt", "ttc", "tta", "ttg", "tct", "tcc",
 "tca", "tcg", "tat", "tac", "taa", "tag", "tgt", "tgc", "tga",
  "tgg", "ctt", "ctc", "cta", "ctg", "cct", "ccc", "cca", "ccg",
   "cat", "cac", "caa", "cag", "cgt", "cgc", "cga", "cgg", "att",
    "atc", "ata", "atg", "act", "acc", "aca", "acg", "aat", "aac",
     "aaa", "aag", "agt", "agc", "aga", "agg", "gtc", "gta", "gtg",
      "gct", "gcc", "gca", "gcg", "gat", "gac", "gaa", "gag", "ggt",
       "ggc", "gga", "ggg")
final_fna = []
faa_content = (">Translation", "M") # Amino acid Methionine (M) will always begin amino acid sequence.
final_faa = []

try:
    with open(user_input) as in_file:
        try:
            for line in in_file:
                if any(char in line for char in fna_content):
                    final_fna.append(line)
        except:
            pass
except FileNotFoundError:
    print(user_input + ' ' + 'not found.')

fna_file = open(user_input.replace(".fasta", '') + 'dna.fna', 'w')
for line in final_fna:
    fna_file.write(line)
fna_file.close()

try:
    with open(user_input) as in_file:
        try:
            for line in in_file:
                if any(char in line for char in faa_content):
                    final_faa.append(line)
        except:
            pass       
except FileNotFoundError:
    print(user_input + ' ' + 'not found.')

faa_file = open(user_input.replace(".fasta", '') + 'prot.faa', 'w')
for line in final_faa:
    faa_file.write(line)
faa_file.close()

