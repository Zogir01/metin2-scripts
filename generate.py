import unidecode

def load_mob_names(filename):
    mob_names = {}
    with open(filename, 'r', encoding = 'ansi') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) >= 2:
                mob_names[parts[0]] = ' '.join(parts[1:])
    return mob_names

def replace_group_names(input_filename, output_filename, mob_names):
    new_group_names = []
    with open(input_filename, 'r', encoding='ansi') as input_file:
        bad_id_count = 0
        for line in input_file:
            if line.startswith("\tMob") or line.startswith("\tmob"):
                mob_id = line.strip().split()[1] 
                mob_name = mob_names.get(mob_id, None)
                if mob_name:
                    new_group_names.append(f"Group\t{mob_name}\n")
                else:
                    bad_id_count += 1
                    new_group_names.append(f"Group\tNIE_MA_TAKIEGO_ID_{bad_id_count}\n")

    with open(input_filename, 'r', encoding='ansi') as input_file, open(output_filename, 'w', encoding='ansi') as output_file:
        i = 0
        for line in input_file:
            if line.startswith("Group") or line.startswith("group"):
                new_string = new_group_names[i].replace(' ', '_').replace('.','')
                new_string_normalized = unidecode.unidecode(new_string)
                output_file.write(new_string_normalized)
                i = i + 1
            else:
                output_file.write(line)

def main():
    mob_names = load_mob_names("mob_names.txt")
    replace_group_names("mob_drop_item.cpp", "mob_drop_item_generated.cpp", mob_names)
    print("Names replaced.")

if __name__ == "__main__":
    main()