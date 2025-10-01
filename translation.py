from Bio.Seq import Seq

# During translation, the mRNA is "read". Each group of three bases in mRNA constitutes a codon.
# Each codon specifies a particular amino acid sequence in proteins. The mRNA sequence is thus used as a template 
# to assemblate the chain of amino acids that form a protein. The amino acids are specified by each mRNA codons. 
# Note: multiple codons can code for the same amino acid. 

dic = {
  "GCA": "Alanine",
  "TGC": "Cysteine",
  "GGA": "Glycine",
  "AAA": "Lysine",
  "ATG": "Methionine",
  "AAC": "Asparagine",
  "CCA": "Glutamine",
  "CGT": "Arginine",
  "AGC": "Serine",
  "ACA": "Threonine",
  "GTA": "Valine",
  "TGG": "Tryptophan",
  "TAC": "Glutamine",
  "TAA": "stop codon",
  "TAG": "stop codon",
  "TGA": "stop codon"
}

def translate_codon_to_amino_acids(DNASeq):
  protein_seq = []
  for i in range(0, len(DNASeq, 3)):
    codon = DNASeq[i:i+3]
    if codon == "TAG" or codon == "TAA" or codon == "TGA":
      print("stop codon found at position", i)
      break
    else : 
      protein_seq.append(codon)
  
  amino_acids = []
  for codon in protein_seq:
    amino_acid = dic.get(codon)
    if amino_acid: 
      amino_acids.append(amino_acid)

  print(" - ".join(amino_acids))
