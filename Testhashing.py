import screed
import os
import sourmash
from sourmash import MinHash

directory = '/home/josh/Documents/Reference_sequences/testyboii'
ksize = 21

def build_kmers(sequence, ksize):
    kmers = []
    n_kmers = len(sequence) - ksize + 1

    for i in range(n_kmers):
        kmer = sequence[i:i + ksize]
        kmers.append(kmer)

    return kmers

def read_genes_from_file(file, ksize):
    genes_dict = {}
    for record in screed.open(file):
        description = record.name  
        sequence = record.sequence
        kmers = build_kmers(sequence, ksize)
        # Create a MinHash object
        minhash = MinHash(n=0, ksize=ksize, scaled=1)
        # Add the k-mers to the MinHash object
        for kmer in kmers:
            minhash.add_kmer(kmer)
        # Store the MinHash object in the genes_dict dictionary
        genes_dict[description] = minhash
    return genes_dict

def process_directory(directory, ksize):
    all_files_dict = {}
    for dirpath, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".fna"):
                file_path = os.path.join(dirpath, file)
                genes_dict = read_genes_from_file(file_path, ksize)
                all_files_dict[file] = genes_dict
    return all_files_dict

# Get the dictionary containing all MinHash objects for all genes from all files
all_files_dict = process_directory(directory, ksize)

# access the MinHash object for a specific gene:
file_name = 'Uberis_ref.fna'
genes_dict = all_files_dict.get(file_name, {})
