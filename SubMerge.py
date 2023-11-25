import argparse
import re
import os

def read_subdomains(filename):
    subdomains = set()
    with open(filename, 'r') as file:
        for line in file:
            subdomain = line.strip()
            if is_valid_domain(subdomain):
                subdomains.add(subdomain)
    return subdomains

def is_valid_domain(subdomain):
    pattern = r'^[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    return re.match(pattern, subdomain) is not None

def merge_file(file1, file2, output_file):
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as output:
        content1 = f1.read()
        content2 = f2.read()
        output.write(content1)
        output.write(content2)

def merge_files(directory, output_file):
    subdomains = set()
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            filepath = os.path.join(directory, filename)
            subdomains.update(read_subdomains(filepath))
    print(f"Read {len(subdomains)} subdomains from files in directory {directory}.")
    with open(output_file, 'w') as file:
        for i, subdomain in enumerate(sorted(subdomains)):
            file.write(subdomain + '\n')
    print(f"Total domains: {i + 1}")

def main():
    parser = argparse.ArgumentParser(description='Subdomain Deduplication and File Merge')

    parser.add_argument('-D', '--deduplicate', metavar='FILENAME',
                        help='perform subdomain deduplication on the specified file')
    parser.add_argument('-m', '--merge', nargs=2, metavar=('FILE1', 'FILE2'),
                        help='merge the contents of two files')
    parser.add_argument('-d', '--directory', metavar='DIRECTORY',
                        help='perform subdomain deduplication on the files in the specified directory')
    parser.add_argument('-o', '--output', metavar='OUTPUT_FILE',
                        help='output file for the results')
   
    args = parser.parse_args()

    if args.deduplicate:
        filename = args.deduplicate
        subdomains = read_subdomains(filename)
        if args.output:
            output_file = args.output
            print(f"Read {len(subdomains)} subdomains from {filename}.")
            with open(output_file, 'w') as file:
                for i, subdomain in enumerate(sorted(subdomains)):
                    file.write(subdomain + "\n")
            print(f"Total domains: {i + 1}\n")
        else:
            print(f"Read {len(subdomains)} subdomains from {filename}:")
            for i, subdomain in enumerate(sorted(subdomains)):
                print(subdomain)
            print(f"Total domains: {i + 1}")

    if args.merge:
        file1, file2 = args.merge
        if args.output:
            output_file = args.output
            merge_file(file1, file2, output_file)
            print(f'Merged {file1} and {file2} into {output_file}.')
        else:
            print("Please provide an output file using the -o/--output option.")

    if args.directory:
        directory = args.directory
        if args.output:
            output_file = args.output
            merge_files(directory, output_file)
            print(f"Merged subdomains from files in directory {directory} into {output_file}.")
        else:
            print("Please provide an output file using the -o/--output option.")

if __name__ == '__main__':
    main()