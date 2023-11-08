import Levenshtein as lev

def calc_jaro_similarity(seq1, seq2):
    # Calculate the Levenshtein (edit) distance
    distance = lev.distance(seq1, seq2)

    # Convert the distance to a similarity score
    max_len = max(len(seq1), len(seq2))
    if max_len == 0:
        return 0.0
    jaro_similarity = 1 - (distance / max_len)

    return jaro_similarity

def gen_similarity_matrix(series1, series2):
    matrix = []
    for gene1 in series1:
        row = []
        for gene2 in series2:
            similarity = calc_jaro_similarity(gene1, gene2)
            row.append(similarity)
        matrix.append(row)
    return matrix

seq1 = input("Enter the first genetic series-->").split(',')
seq2 = input("Enter the second genetic series-->").split(',')
similarity_matrix = gen_similarity_matrix(seq1, seq2)

for row in similarity_matrix:
    print(row)
