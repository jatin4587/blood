import itertools

def possible_children(parent1, parent2):
    """Return all possible child genotypes given two parents' alleles."""
    # Each parent contributes one allele
    children = set()
    for allele1 in parent1:
        for allele2 in parent2:
            children.add("".join(sorted(allele1 + allele2)))  # sort so AO=OA
    return children

def genotype_to_bloodtype(geno):
    """Convert genotype to blood type phenotype."""
    if geno == "OO":
        return "O"
    elif geno in ("AA", "AO"):
        return "A"
    elif geno in ("BB", "BO"):
        return "B"
    elif geno == "AB":
        return "AB"
    else:
        return "Unknown"

# Example 1
p1 = "AO"
p2 = "BB"
children = possible_children(p1, p2)
print(f"Parent1={p1}, Parent2={p2}")
print("Possible child genotypes:", children)
print("Possible child blood types:", {genotype_to_bloodtype(c) for c in children})

# Example 2
p1 = "AO"
p2 = "OB"
children = possible_children(p1, p2)
print(f"\nParent1={p1}, Parent2={p2}")
print("Possible child genotypes:", children)
print("Possible child blood types:", {genotype_to_bloodtype(c) for c in children})
