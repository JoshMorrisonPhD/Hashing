# Hashing
A repository for multiple code snippets relating to the hashing of gene sequences.

For a quick overview of how I arrived at this: https://sourmash.readthedocs.io/en/latest/kmers-and-minhash.html#Running-this-notebook
A note on minimum message length: https://vrs.ga4gh.org/en/1.0/appendices/truncated_digest_collision_analysis.html#truncated-digest-collision-analysis


Hashing.py is my initial attempt at understanding the screed library. My understanding is that screed snips out each sequence/header combo and creates a dictionary object with every sequence and its associated header data which is then callable/consultable at will. This was required to be able to move from full genome fasta files to fasta files of individual genes seperated with unique headers for each gene.

Minhashing.py is how I was trying to visualise the MinHash objects. It turns out doing a pairwise comparison of 3700 to 3700 genes takes a long time and generates a CSV which is about 1.8 million lines long, it also turns out that the MinHash object is not really printable to CSV because it's a sum of properties, not a singular value as I was hoping. I realise appending every single iteration is incredibly bad for performance but i'm not really sure how else to do that.

Testhashing.py is the current code I'm working with. It's simply an attempt at accessing the MinHash objects.
