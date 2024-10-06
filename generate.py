import unidecode

def load_mob_names(filename : str):
    mob_names = {}
    try:
        with open(filename, 'r', encoding = 'ansi') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) >= 2:
                    # Creating dict where key = mob id, value = mob name
                    # and replacing chars for better look.
                    mob_names[parts[0]] = unidecode.unidecode(' '.join(parts[1:]).replace(' ', '_').replace('.',''))
    except FileNotFoundError:
        print(f'File {filename} not found.')

    return mob_names

def replace_group_names(input_filename : str, mob_names : dict):
    try:
        with open(input_filename, 'r', encoding='ansi') as input_file, open("result/mob_drop_item_generated.txt", 'w', encoding='ansi') as output_file:
            bad_id_count = 0
            group_section_lines = []

            for line in input_file:
                if line.startswith("Group") or line.startswith("group"):
                    output_file.writelines(group_section_lines) # Write entire group section to the file.
                    group_section_lines.clear() # Clear list to begin with new group section
                else:
                    group_section_lines.append(line) # Creating group section without group name

                if line.startswith("\tMob") or line.startswith("\tmob"):
                    mob_id = line.strip().split()[1] 
                    mob_name = mob_names.get(mob_id, None) # Get name from dictionary, return None, where id does not exist
                    
                    if mob_name:
                        new_group_name = f"Group\t{mob_name}\n"
                    else:
                        bad_id_count += 1
                        new_group_name = f"Group\tTHERE IS NO SUCH MOB ID: {mob_id} IN {input_filename}\n"

                    group_section_lines.insert(0, new_group_name) # Insert new group name at beggining

        print("File 'mob_drop_item_generated.cpp' generated succesfully.")

    except FileNotFoundError:
        print(f'File {input_filename} not found.')

def main(mob_names_file, input_file):
    mob_names_dict = load_mob_names(mob_names_file)
    replace_group_names(input_file, mob_names_dict)

if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser(description='Process some mob data.')
    parser.add_argument('--mob_names_file', type=str, default='example/mob_names.txt', help='The path to the mob names file (default: example/mob_names.txt)')
    parser.add_argument('--input_file', type=str, default='example/mob_drop_item.txt', help='The path to the input file (default: example/mob_drop_item.txt)')
    parser.add_argument('--test_time', type=int, default=0, help='How many times to measure the execution time (default: 0, dont measure time)')
    args = parser.parse_args()

    if args.test_time != 0:
        import timeit
        elapsed_time = timeit.timeit(lambda: main(args.mob_names_file, args.input_file), number=args.test_time)
        print(f"Total time taken(for {args.test_time} times): {elapsed_time} seconds")
        print(f"Time taken for Script: {elapsed_time / args.test_time} seconds")
    else:
        main(args.mob_names_file, args.input_file)