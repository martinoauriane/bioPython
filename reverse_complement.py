from Bio.Seq import Seq

# Two pythons functions are important when analyzing DNA replication: 

# The complement() function and the reverse_complement() function.

# 1. The complement() function goes through the original DNA sequence and replaces each nucleotide with its complement.
# 
# 2. The reverse_complement() takes step1 further: It reverses the sequence. The new strand is reversed to match the
#    5' 3' orientation relative to the original strand. But because DNA strands are antiparallel, if one strand runs
#    5' 3', then the complementary strand at that point runs 3'5'. At this stage, complementating alone gives the paired
#    bases correctly, but the orientation is 3'5'. So, if we want to present the new strand in standard 5' 3' direction,
#    we must reverse it. We always write sequences 5' 3', even for the complementary strand. Reverse_complement() 
#    reflects this concept. 


# Here's an example of how the function reverse_complement() works
DNA = Seq("AGCTCTAG")
reverse_complement = DNA.reverse_complement()
print(reverse_complement)

# recoding the reverse_complement() function

def recoded_reverse_complement_function(DNAbrin): 
  dict = {
    "A": "T",
    "C": "G",
    "G": "C",
    "T": "A"
  }

  complement=""
  for nucleotide in DNAbrin: 
    complement += dict[nucleotide]
  
  reverse_complement = complement[::-1]

  return reverse_complement

DNA=Seq("TCGACGTACG")
print(recoded_reverse_complement_function(DNA))

