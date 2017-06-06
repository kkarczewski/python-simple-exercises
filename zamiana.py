import re

class replace:
    '''
    '''

    def __init__(self):
        pass

    def read_dictionary(self, fileName=None):
        rlist = []
        with open(fileName, 'r') as f:
            rlist = f.readlines()

        rdict = {}

        for elem in rlist:
            rdict[elem.split('\t')[0]]=elem.split('\t')[1].rstrip('\n')

        return rdict

    def read_input_file(self, fileName=None):
        with open(fileName, 'r') as f:
            inputtext = f.read().replace('\n', '')

        return inputtext

    def search_and_replace(self, input_text=None, dictionary=None):
        t=input_text

        for item in dictionary.keys():
            src_str = re.compile(r'\b%s\b' % item)
            t = src_str.sub(dictionary[item], t)

        return t

    def write_to_file(self, fileName=None, text=None):
        with open(fileName, 'w') as f:
            f.write(text)
        f.close()

def main():

    print("Enter dictionary file path:")
    fd = raw_input()

    print("Enter input file path:")
    ef = raw_input()

    print("Enter output file path:")
    of = raw_input()

    r = replace()
    d=r.read_dictionary(fd)
    i=r.read_input_file(ef)
    t=r.search_and_replace(i, d)
    w=r.write_to_file(of, t)

if __name__== "__main__":
    main()