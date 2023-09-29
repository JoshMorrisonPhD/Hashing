import sourmash
import screed 
import os
import pandas as pd

directory = '/home/josh/Documents/Reference_sequences'
ksize=3
kmer_Set={}

def build_kmers(sequence, ksize):
    kmers = []
    n_kmers = len(sequence) - ksize + 1

    for i in range(n_kmers):
        kmer = sequence[i:i + ksize]
        kmers.append(kmer)

    return kmers


def read_kmers_from_file(file, ksize):
    all_kmers = []
    for record in screed.open(file):
        sequence = record.sequence

        kmers = build_kmers(sequence, ksize)
        all_kmers += kmers

    return all_kmers


for dirpath, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".fna"):
            filename = file
            file=(os.path.join(dirpath, file))
            kmer_Set[filename.split('.fna')[0]]=read_kmers_from_file(file, ksize)      

test=screed.open('/home/josh/Documents/Reference_sequences/Uberis_ref.fna')
print(test)

