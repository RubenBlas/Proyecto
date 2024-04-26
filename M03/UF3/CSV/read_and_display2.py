#A slightly more advanced use of the reader — catching and reporting errors:

import csv, sys

filename = 'some.csv'

try:

   with open(filename, newline='') as f:

       reader = csv.reader(f)



       for row in reader:

           print(row)

except csv.Error as e:

   sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))

except FileNotFoundError:

   print(f"Fitxer/Directory no trobat: {filename}")