from Bio.Seq import Seq
ADN = Seq("AGTACACTGGTA")
print(ADN.reverse_complement())

""" convert DNA to proteins """
print(ADN.translate())

""" Interrogation de la base de données PubMed 
Utilisons PubMed pour chercher des articles scientifiques relatifs à la transferrine 
"""

from Bio import Entrez
Entrez.email="auriane.martino@hotmail.com"
req_esearch=Entrez.esearch(db="pubmed", term="transferrin")
res_esearch=Entrez.read(req_esearch)

print(res_esearch.keys())
""" 
dict_keys(['Count', 'RetMax', 'RetStart', 'IdList', 'TranslationSet',
'TranslationStack', 'QueryTranslation'])

"""
print(res_esearch["IdList"])
""" 
['30411489', '30409795', '30405884', '30405827', '30402883', '30401570',
'30399508', '30397276', '30395963', '30394734', '30394728', '30394123',
'30393423', '30392910', '30392664', '30391706', '30391651', '30391537',
'30391296', '30390672']
"""

""" En réalité, le nombre exact de publications (en janvier 2024) est connu : """
print(res_esearch["Count"])


