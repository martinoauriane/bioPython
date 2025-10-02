from Bio.Seq import Seq

# A codon is  sequence of three nucleotides which together form a unit of genetic code in a DNA or RNA molecule. 61 codons
# specifiy amino acids. 3 codons are used as stop signals. Each codon instructs the cell to start the creation of a protein 
# chain, to add a specific amino acid to the growing protein chain, or to stop creation of the protein chain.  


def count_codons(specific_codon, DNA):
  codon = specific_codon.upper()
  count = 0
  DNA_seq = Seq(DNA.upper())
  for i in range (0, len(DNA_seq), 3):
    codon = DNA_seq[i: i+3]
    if codon == specific_codon:
      count += 1
  return count
