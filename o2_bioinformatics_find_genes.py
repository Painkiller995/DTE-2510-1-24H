"""
This module represents a bioinformatics implementation.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2510-1-24H

"""

GENE_CHARACTERS = "ACGT"
START_TRIPLET = "ATG"
END_TRIPLETS = ["TAA", "TAG", "TGA"]


def find_genes(dna_sequence: str) -> str:
    """
    Find the genes in the given DNA sequence.

    Args:
        dna_sequence: The DNA sequence.

    Returns:
        The genes found in the DNA sequence. If no genes are found, return "No genes found!".
    """
    gene_list = []

    index = 0
    length = len(dna_sequence)

    while index < length:
        start_index = dna_sequence.find(START_TRIPLET, index)
        if start_index == -1:
            break

        stop_index = None
        for end_triplet in END_TRIPLETS:
            end_index = dna_sequence.find(end_triplet, start_index + 3)
            if end_index != -1 and (stop_index is None or end_index < stop_index):
                stop_index = end_index

        if stop_index:
            gene = dna_sequence[start_index + 3 : stop_index]
            if is_valid_gene(gene):
                gene_list.append(gene)

        index = start_index + 1

    return ",".join(gene_list) if gene_list else "No genes found!"


def is_valid_gene(gene: str) -> bool:
    """
    Check if the extracted gene is valid.

    Args:
        gene: The gene.

    Returns:
        True if the gene is valid, otherwise False.
    """
    return (
        len(gene) % 3 == 0
        and START_TRIPLET not in gene
        and all(end not in gene for end in END_TRIPLETS)
        and gene != ""
    )


def get_user_input() -> str:
    """
    Get the user input and validate it.

    Returns:
        The user input as a string.
    """
    while True:
        user_input: str = input("Please enter a gene sequence: \n")

        if not all(char in GENE_CHARACTERS for char in user_input):
            print(
                "Oops! 😅 It seems you entered an invalid input, please enter a valid gene sequence. "
            )
            continue

        print("-------------------------------------------------")
        return user_input


if __name__ == "__main__":
    sequence = get_user_input()
    genes = find_genes(sequence)
    print(f"The genes found in the DNA sequence are: \n {genes}")
