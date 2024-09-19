"""
This module represents a bioinformatics implementation.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2510-1-24H

"""

START_TRIPLET = "ATG"
END_TRIPLETS = ["TAA", "TAG", "TGA"]


def find_genes(dna_sequence: str) -> str:
    """
    Find the genes in the given DNA sequence.

    Args:
        dna_sequence: The DNA sequence.

    Returns:
        The genes found in the DNA sequence.
    """
    genes = []

    start_triplet_indexes = []
    stop_triplet_indexes = []

    index = 0
    while index < len(dna_sequence):
        start_triplet_index = dna_sequence.find(START_TRIPLET, index)

        if start_triplet_index > 0 and start_triplet_index not in start_triplet_indexes:
            start_triplet_indexes.append(start_triplet_index)

        for end_triplet in END_TRIPLETS:
            end_triplet_index = dna_sequence.find(end_triplet, index)
            if end_triplet_index > 0 and end_triplet_index not in stop_triplet_indexes:
                stop_triplet_indexes.append(end_triplet_index)
        index += 1

    for start_triplet_index in start_triplet_indexes:
        for stop_triplet_index in stop_triplet_indexes:
            if start_triplet_index < stop_triplet_index:
                sub_gene = dna_sequence[start_triplet_index : stop_triplet_index + 3]
                gene = sub_gene[3 : len(sub_gene) - 3]
                if (
                    len(gene) % 3 == 0
                    and START_TRIPLET not in gene
                    and all(end_triplet not in gene for end_triplet in END_TRIPLETS)
                    and gene != ""
                ):
                    genes.append(gene)

    return ",".join(genes)


example = "TTATGATGTTTTAAGGATGGGGCGTTAGTT"
genes = find_genes(example)
print(genes)
