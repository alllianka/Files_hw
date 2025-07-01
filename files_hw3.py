file1 = '1.txt'
file2 = '2.txt'
file3 = '3.txt'

input_files = [file1, file2, file3]
output_file = 'output_file.txt'

def files_combiner(input_files, output_file):
    index = 0
    info = {}

    for infile in input_files:
        with open(infile, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            num_lines = len(lines)
            info[infile] = (num_lines, lines)  

    sorted_files = sorted(info.items(), key=lambda x: x[1][0])      
    with open(infile, 'w', encoding='utf-8') as outfile:    
        for infile, (num_lines, content) in sorted_files:
            outfile.write(f"{infile}\n")
            outfile.write(f"{num_lines}\n")
            outfile.writelines(content)
            outfile.write("\n")
         
files_combiner([file1, file2, file3], output_file)


