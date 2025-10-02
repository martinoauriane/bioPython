# GOAL : recode the molecular_weight function 
# form Bio.SeqUtils import molecular_weight
# seq_example = Seq("ATGCTACGAT")
# mw = molecular_weight(seq_example, seq_type='DNA')

from Bio.Seq import Seq

def molecular_weight(dna_seq):
  nucleotide_weights = {
    'A': 313.21,
    'T': 304.2,
    'G': 329.21,
    'C': 289.18,
  }

  DNA_seq = dna_seq.upper()
  molecular_weight = 0
  for nucleotide in DNA_seq:
    if nucleotide in nucleotide_weights:
      molecular_weight += nucleotide_weights[nucleotide]
    else : 
      raise ValueError(f"Unknown nucleotide: {nucleotide}")
  
  #then we substract the H20 weight for each phosphodier link
  if len(DNA_seq) > 1:
    molecular_weight = molecular_weight - ((len(DNA_seq)-1) * 18.015)
  
  return molecular_weight

# Now let's try to use the molecular_weight function: 
example_DNA = Seq("ATCGATCAGTAGCGCTA")
mw = molecular_weight(example_DNA)
print(f"Molecular weight equals: {mw}g/mol")




