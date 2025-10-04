from Bio.Seq import Seq 

# The goal of this count is to count the number of bases in a 
# DNA sequence.

def count_bases(sequence):
  return {
    'A': sequence.count('A'),
    'T': sequence.count('T'),
    'G': sequence.count('G'),
    'C': sequence.count('C')
  }

DNA = Seq("TCGATCGAAGTCTCA")
print(count_bases(DNA))