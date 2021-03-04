from textwrap import wrap

CODON_TRANSLATION_LIST = {
    "AUG" : "Methionine",
    "UUU" : "Phenylalanine",
    "UUC" : "Phenylalanine",
    "UUA" : "Leucine",
    "UUG" : "Leucine",
    "UCU" : "Serine",
    "UCC" : "Serine",
    "UCA" : "Serine",
    "UCG" : "Serine",
    "UAU" : "Tyrosine",
    "UAC" : "Tyrosine",
    "UGU" : "Cysteine",
    "UGC" : "Cysteine",
    "UGG" :"Tryptophan",
    "UAA" : "STOP",
    "UAG" : "STOP",
    "UGA" : "STOP"
}

def translate_codon(codon):
    return CODON_TRANSLATION_LIST[codon]

def get_next_codon(list_of_codons):
    for codon in list_of_codons:
        amino_acid = translate_codon(codon)
        yield amino_acid


def translate_list_of_codons(list_of_codons):
    list_of_amino_acids = []
    amino_acid_translator = get_next_codon(list_of_codons)
    breakpoint = 0
    for amino_acid in amino_acid_translator:
        print(amino_acid)
        if amino_acid == "STOP":
            return list_of_amino_acids
        list_of_amino_acids.append(amino_acid)
    return list_of_amino_acids


def translate_2(list_of_codons):
    return list(map(translate_codon, list_of_codons))


def proteins(strand):
    list_of_codons = wrap(strand, 3)
    print("Given string = {} as list = {}".format(strand, list_of_codons))
    result = translate_list_of_codons(list_of_codons)
    return result
