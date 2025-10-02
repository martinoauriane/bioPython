from Bio.Seq import Seq

# Recoding the GC function  : from Bio.SeqUtils import GC
# GC("ACTGN") 
# // 40.0

# THe human genome comprises four types of nitrogenous bases : Thymine, Guanine, Adenine and Cytosine. The structure of a 
# base + phosphate + sugar is known as 'nucleotide'. 
# In molecular biology and genetics, GC-content (or guanine-cytosine content) is the percentage of nitrogenous bases in a DNA 
# or RNA molecule that are either guanine (G) or cytosine (C). This measure indicates the proportion of G and C bases out of
# an implied four total bases. 

# A DNA with more GC content is highly stable due to the presence of more hydrogen bonds. Indeed, the bases G and C have 
# 3 hydrogen bonds, while A and T only have 2. The more GC there are in a fragment, the more thermally stable the DNA is.

def calculate_GC_content(DNA_seq):
  if len(DNA_seq) == 0:
    return 0
  DNA = DNA_seq.upper()
  GC_count = 0
  GC_count = DNA.count("G") + DNA.count("C")
  GC_content = (GC_count / float(len(DNA))) * 100
  return GC_content


