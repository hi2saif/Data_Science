
#Getting original data
#--------------------------------------------------------------------------------#
def on_vocareum():
    import os
    return os.path.exists('.voc')

def download(file, local_dir="", url_base=None, checksum=None):
    import os, requests, hashlib, io
    local_file = "{}{}".format(local_dir, file)
    if not os.path.exists(local_file):
        if url_base is None:
            url_base = "https://cse6040.gatech.edu/datasets/"
        url = "{}{}".format(url_base, file)
        print("Downloading: {} ...".format(url))
        r = requests.get(url)
        with open(local_file, 'wb') as f:
            f.write(r.content)            
    if checksum is not None:
        with io.open(local_file, 'rb') as f:
            body = f.read()
            body_checksum = hashlib.md5(body).hexdigest()
            assert body_checksum == checksum, \
                "Downloaded file '{}' has incorrect checksum: '{}' instead of '{}'".format(local_file,
                                                                                           body_checksum,
                                                                                           checksum)
    print("'{}' is ready!".format(file))
    
if on_vocareum():
    DATA_PATH = "../resource/asnlib/publicdata/"
else:
    DATA_PATH = ""
datasets = {'groceries.csv': '0a3d21c692be5c8ce55c93e59543dcbe'}

for filename, checksum in datasets.items():
    download(filename, local_dir=DATA_PATH, checksum=checksum)

with open('{}{}'.format(DATA_PATH, 'groceries.csv')) as fp:
    groceries_file = fp.read()
print (groceries_file[0:250] + "...\n... (etc.) ...") # Prints the first 250 characters only
print("\n(All data appears to be ready.)")
#---------------------------------------------------------------------------------------------------------------#


MIN_COUNT = 10
THRESHOLD = 0.5
baskets = []
item_counts = defaultdict(int)
for basket_raw in groceries_file.split('\n'):
    itemset = set(basket_raw.split(','))
    baskets.append(itemset)
    update_item_counts(item_counts, itemset)
print("Found {} baskets.".format(len(baskets)))

# Search for an initial set of association rules
initial_basket_rules = find_assoc_rules(baskets, THRESHOLD)

# Filter those rules to exclude infrequent items
basket_rules = {}
for (a, b), v in initial_basket_rules.items():
    if item_counts[a] >= MIN_COUNT:
        basket_rules[(a, b)] = v

print(basket_rules)		
