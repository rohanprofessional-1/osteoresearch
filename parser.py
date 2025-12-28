import pathlib
import os
import pandas as pd

directory_path = '/Users/rohannair/Desktop/Shenanigans/Independent Research/test_folder'
data_file = "data.csv"

def build_headers_from_file(file_name):
    genes = []
    with open(file_name, "r") as f:
        for line in f:
            if not line.strip():
                continue
            gene = line.strip().split()[0]
            genes.append(gene)
    cols = ["sample"]
    for g in genes:
        cols.extend([f"{g}_val1", f"{g}_val2"])
    return genes, cols

def read_patient_values(file_path, genes):
    file_name = file_path.stem
    values_map = {g: [None, None] for g in genes}

    with open(file_path, "r") as f:
        for line in f:
            if not line.strip():
                continue
            parts = line.strip().split()
            if len(parts) != 3:
                continue
            gene, val1, val2 = parts
            if gene in values_map:
                values_map[gene] = [val1, val2]

    row = {"sample": file_name}
    for g in genes:
        v1, v2 = values_map[g]
        row[f"{g}_val1"] = v1
        row[f"{g}_val2"] = v2
    return row

if __name__ == "__main__":
    txt_files = list(pathlib.Path(directory_path).glob("*.txt"))
    if not txt_files:
        raise SystemExit("No .txt files found")

    # use first file to define header and gene order
    genes, columns = build_headers_from_file(txt_files[0])

    all_rows = []
    for file_path in txt_files:
        row = read_patient_values(file_path, genes)
        all_rows.append(row)

    df = pd.DataFrame(all_rows, columns=columns)
    df.to_csv(data_file, index=False)
