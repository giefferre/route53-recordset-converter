import csv
import json
import sys


def main(input_filename: str, output_filename: str):
    output = []
    with open(input_filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader, None)  # skip headers

        for row in csv_reader:
            record_type = row[1]

            record_name = row[0]
            if '\\052' in record_name:
                record_name = record_name.replace('\\052', '*')

            value = row[2]
            if record_type in ['CNAME', 'MX']:
                value = "%s." % value

            output.append({
                'name': record_name,
                'type': record_type,
                'value': [
                    value
                ],
                'ttl': int(row[3]),
            })

    with open(output_filename, mode='w+') as output_file:
        output_file.write(json.dumps(output))


if __name__ == "__main__":
    # @ TODO check args and print usage
    main(sys.argv[1], sys.argv[2])
