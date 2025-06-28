file1 = '1.txt'
file2 = '2.txt'
file3 = '3.txt'

input_files = [file1, file2, file3]
output_file = 'output_file.txt'

def files_combiner(input_files, output_file):
    index = 0
    info = {}

    for infile in input_files:
        strings = len(open(infile, 'r', encoding='utf-8').readlines())
        info.setdefault(strings, infile)
        sorted_info = dict(sorted(info.items()))
        with open(infile, 'r+', encoding='utf-8') as infile:    
            content = infile.read()
            infile.seek(0,0)
            infile.write(infile.name+'\n'+str(strings)+'\n')
            infile.write(content)
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for key, infile in sorted_info.items():
            with open(infile, 'r', encoding='utf-8') as infile:
                outfile.write(infile.read())
                outfile.write('\n')
         
files_combiner([file1, file2, file3], output_file)


