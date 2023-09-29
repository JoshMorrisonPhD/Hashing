import screed
import os
import csv
from sourmash import MinHash

directory = '/home/josh/Documents/Reference_sequences'
ksize = 21
output_csv_file = 'comparison.csv'


def process_file(file, ksize):
    with screed.open(file) as seqfile:
        gene_data = {}
        for record in seqfile:
            description = record.name
            sequence = record.sequence
            minhash = MinHash(n=0, ksize=ksize, scaled=1)
            for i in range(len(sequence) - ksize + 1):
                kmer = sequence[i:i + ksize]
                minhash.add_kmer(kmer)
            gene_data[description] = minhash
        return gene_data


def compare_minhashes(gene_data_dict):
    comparison_data = []
    # Compare each gene with every other gene from every file
    for desc1, file1 in gene_data_dict.items():
        for desc2, file2 in gene_data_dict.items():
            if desc1 != desc2:  # Avoid comparing the same file
                for gene_desc1, mh1 in file1.items():
                    for gene_desc2, mh2 in file2.items():
                        jaccard_similarity = mh1.jaccard(mh2)
                        comparison_data.append(
                            (desc1, gene_desc1, desc2, gene_desc2, jaccard_similarity))
    return comparison_data


def process_directory(directory, ksize, output_csv_file):
    gene_data_dict = {}
    for dirpath, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".fna"):
                file_path = os.path.join(dirpath, file)
                gene_data = process_file(file_path, ksize)
                gene_data_dict[file] = gene_data  # Store gene data with filename as key

    all_comparisons = compare_minhashes(gene_data_dict)

    # Write comparisons to CSV
    with open(output_csv_file, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(
            ['File1', 'Gene1', 'File2', 'Gene2', 'Jaccard Similarity'])
        csvwriter.writerows(all_comparisons)


process_directory(directory, ksize, output_csv_file)