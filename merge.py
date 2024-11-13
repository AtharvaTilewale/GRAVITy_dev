def read_gro(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    # Get the header and number of atoms
    header = lines[0].strip()
    num_atoms = int(lines[1].strip())
    atom_lines = lines[2:2 + num_atoms]
    footer = lines[2 + num_atoms:]

    return header, atom_lines, footer

def write_gro(filename, header, atom_lines, footer):
    with open(filename, 'w') as file:
        file.write(header + '\n')
        file.write(f"{len(atom_lines)}\n")  # Number of atoms
        file.writelines(atom_lines)
        file.writelines(footer)

def merge_gro(protein_file, ligand_file, output_file):
    protein_header, protein_atoms, protein_footer = read_gro(protein_file)
    ligand_header, ligand_atoms, ligand_footer = read_gro(ligand_file)

    # Combine the atom lines
    combined_atoms = protein_atoms + ligand_atoms

    # Create the new header (you can customize this)
    combined_header = f"Complex: {protein_header} + {ligand_header}"

    # Write to the output .gro file
    write_gro(output_file, combined_header, combined_atoms, protein_footer)

if __name__ == "__main__":
    protein_file = 'protein.gro'
    ligand_file = 'lig.gro'
    output_file = 'complex.gro'

    merge_gro(protein_file, ligand_file, output_file)
    print(f"Generated {output_file} from {protein_file} and {ligand_file}.")
