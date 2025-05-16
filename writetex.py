input_file = "matrices.txt"
output_file = "defqsingle.tex"
output = []

with open(input_file, "r") as file:
    matrices = [line.strip() for line in file if line.strip()]

for matrix in matrices:
    matrix1 = matrix.replace("_", "\\_")
    filename = f"{matrix1}\\_commload\\_multi\\_rome16q"
    figure_snippet = f"""\\begin{{figure}}[H]
    \\centering
    \\incfig{{{filename}}}
    \\caption{{}}
    \\label{{fig:{filename.replace("\\_","_")}}}
\\end{{figure}}"""

    output.append(figure_snippet)

# Write snippets to output file
with open(output_file, "a") as file:
    file.write("\n\n".join(output))
