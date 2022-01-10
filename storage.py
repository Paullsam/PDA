import argparse
import os
import tempfile
import json

parser = argparse.ArgumentParser(description='Saving/reading data KEY: VALUE to the file')
parser.add_argument('--key', dest='key', required=True,
                    help='The key by which the values are saved/imported')
parser.add_argument('--val', dest='value',
                    help='The value assigned to the key (if there is no value, then the data is imported from the file)')

args = parser.parse_args()

data_file = (os.path.join(tempfile.gettempdir(), 'storage.data'))

data = {}
data = {args.key: args.value}


def in_file():
    results = []
    if os.path.exists(data_file):
        with open(data_file, 'r') as infile:
            lines = infile.readlines()
            for line in lines:
                new_data = json.loads(line)
                if new_data.get(args.key):
                    results.append(new_data.get(args.key))
        infile.close()
    else:
        pass
    return print(*results, sep=', ')


def out_file():
    if os.path.exists(data_file):
        with open(data_file, 'a') as outfile:
            json.dump(data, outfile)
            outfile.write('\n')
            outfile.close()
    else:
        with open(data_file, 'w') as outfile:
            json.dump(data, outfile)
            outfile.write('\n')
            outfile.close()
    return


if args.value is None:
    in_file()
else:
    out_file()
