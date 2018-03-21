
import argparse
import re
from operator import itemgetter
import json

elements = []
errors = []

def main():
    args = validate_inputs()
    first_names = load_names('firstnames.txt')
    input_data = load(args.input)

    line_num=0
    for line in input_data:

        output_record = {'color':'','firstname':'','lastname':'','phonenumber':'','zipcode':''}

        # parse names
        # many ways to skin a cat, but here's one based on sample dataset
        # if more time, i'd make more generic
        if len(line) == 5:
            name_end=2
            if is_firstname(line[0].split(' ')[0],first_names):
                output_record.update(dict(firstname=line[0].strip()))
                output_record.update(dict(lastname=line[1].strip()))
            else:
                output_record.update(dict(lastname=line[0].strip()))
                output_record.update(dict(firstname=line[1].strip()))
        elif len(line) == 4:
            name_end=1
            output_record.update(dict(firstname=line[0].strip().split(' ')[0]))
            output_record.update(dict(lastname=line[0].strip().split(' ')[1]))
        else:
            errors.append(line_num)
            break

        for i in range(name_end,len(line)):
            if is_zip(line[i]):
                output_record.update(dict(zipcode=normalize_zip_code(line[i].strip())))
            elif is_phonenum(line[i]):
                output_record.update(dict(phonenumber=normalize_phone_num(line[i].strip())))
            elif is_color(line[i]):
                output_record.update(dict(color=line[i].strip()))

        print output_record
        elements.append(output_record)
        line_num+=1


    lname_fname_sorted = sorted(elements, key=itemgetter('lastname','firstname'))

    data = {}
    data['entries'] = lname_fname_sorted
    data['errors'] = errors


    write_json(args.output,data)


def normalize_phone_num(phone_num):
    clean_phone_num = re.sub('[^0-9]+', '', phone_num)
    normalized_phone_num = "%c%c%c-%c%c%c-%c%c%c%c" % tuple(map(ord, clean_phone_num))
    return normalized_phone_num

def normalize_zip_code(zip_code):
    clean_zip_code = re.sub('[^0-9]+', '', zip_code)
    if len(clean_zip_code) == 9:
        normalized_zip_code = "%c%c%c%c%c-%c%c%c%c" % tuple(map(ord, clean_zip_code))
    else:
        normalized_zip_code = clean_zip_code

    return normalized_zip_code

def normalize_phonenum(self):
    # strip non-numeric characters
    phone = re.sub(r'\D', '', self.phone)
    # remove leading 1 (area codes never start with 1)
    phone = phone.lstrip('1')
    return '{}.{}.{}'.format(phone[0:3], phone[3:6], phone[6:])

def is_phonenum(phone_num):
    result = re.sub('[^0-9]+','', phone_num)
    if len(result) != 10:
        return False
    return True

def is_zip(zip):
    result = re.sub('[^0-9]+','', zip)
    if len(result) in [5,9]:
        return True
    return False

def is_color(color):
    # TODO:noramlly i'd read this from a file/url/db, but time boxing project
    colors = ['yellow','red','purple','etc','etc']
    if color.strip() not in colors:
        return False
    return True

def is_firstname(name, first_names):
    if name.lower() in first_names:
        return True
    return False

def write_json(fout,data):
    print 'outputting pretty json to file..',fout
    with open(fout, 'w') as outfile:
        json.dump(data, outfile, sort_keys = True, indent = 2,
               ensure_ascii = False)

def load(fname):
    # TODO: needs error checking
    f = open(fname,'r')
    input_data = []
    for line in f.readlines():
        input_data.append(line.strip().split(','))

    f.close()

    return input_data

def load_names(fname):
    # TODO: needs error checking
    f = open(fname,'r')
    input_data = []
    for line in f.readlines():
        line = line.strip().split(' ')
        input_data.append(line[0])

    f.close()

    return input_data

def validate_inputs():
    parser = argparse.ArgumentParser(description='Take home test to port flat file to json')
    parser.add_argument('-in', dest='input',
        default='At-Home Coding Test -inputfile.txt',
        help="A file with each line contains ""PII"", information, which consists of a first name, last name, phone number, favorite color and zip code.")
    parser.add_argument('-out', dest='output',
        default='At-Home Coding Test - outputfile2.txt',
        help="The program outputs a valid, formatted JSON object to this text file.")

    args = parser.parse_args()

    # TODO:needs validation here

    return args

if __name__ == "__main__":
    main()
