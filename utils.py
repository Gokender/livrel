import yaml

def load_conf(filepath, debug=False):
    with open(filepath, 'r') as infile:
        data = yaml.load(infile, Loader=yaml.FullLoader)
    if debug:
        print('Loading config file {}'.format(filepath))
        print(data)
        print('############')
    return data
