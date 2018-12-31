#Code for Paiwise associatin mining


import collections
from itertools import combinations
def normalize_strings(s):
    newstring=''
    for a in s:
        if(a.isalpha())==True:
            if(a.islower())==True:
                newstring =newstring + a
            else:
                newstring = newstring + (a.lower())
        else:
            if(a.isspace())==True:
                newstring = newstring + a
    return newstring

def get_normalized_words(s):
    return normalize_strings(s).split()

def make_item_sets(words):
    get_words=[]
    for w in words:
        get_words.append(set(w))
    return get_words

def update_pair_counts(pair_counts,itemset):
    for a,b in combinations(itemset,2):
        pair_counts[(a,b)] +=1
        pair_counts[(b,a)] +=1
        
def update_item_counts(item_counts,itemset):
    for a in itemset:
        item_counts[a] +=1
        
def filter_rules_by_conf(pair_counts,item_counts,threshold):
    rules_pair={}
    for a,b in pair_counts:
        rules=((pair_counts[(a,b)])/item_counts[a])
        if(rules>=threshold):
            rules_pair[(a,b)]=rules
    return rules_pair

def assoc_rules(receipts,threshold):
    pair_counts = collections.defaultdict(int)
    item_counts = collections.defaultdict(int)
    for words in receipts:
        update_pair_counts(pair_counts,words)
        update_item_counts(item_counts,words)
    rule=filter_rules_by_conf(pair_counts,item_counts,threshold)
    return rule

latin_text = """
Sed ut perspiciatis, unde omnis iste natus error sit
voluptatem accusantium doloremque laudantium, totam
rem aperiam eaque ipsa, quae ab illo inventore
veritatis et quasi architecto beatae vitae dicta
sunt, explicabo. Nemo enim ipsam voluptatem, quia
voluptas sit, aspernatur aut odit aut fugit, sed
quia consequuntur magni dolores eos, qui ratione
voluptatem sequi nesciunt, neque porro quisquam est,
qui dolorem ipsum, quia dolor sit amet consectetur
adipisci[ng] velit, sed quia non numquam [do] eius
modi tempora inci[di]dunt, ut labore et dolore
magnam aliquam quaerat voluptatem. Ut enim ad minima
veniam, quis nostrum exercitationem ullam corporis
suscipit laboriosam, nisi ut aliquid ex ea commodi
consequatur? Quis autem vel eum iure reprehenderit,
qui in ea voluptate velit esse, quam nihil molestiae
consequatur, vel illum, qui dolorem eum fugiat, quo
voluptas nulla pariatur?

At vero eos et accusamus et iusto odio dignissimos
ducimus, qui blanditiis praesentium voluptatum
deleniti atque corrupti, quos dolores et quas
molestias excepturi sint, obcaecati cupiditate non
provident, similique sunt in culpa, qui officia
deserunt mollitia animi, id est laborum et dolorum
fuga. Et harum quidem rerum facilis est et expedita
distinctio. Nam libero tempore, cum soluta nobis est
eligendi optio, cumque nihil impedit, quo minus id,
quod maxime placeat, facere possimus, omnis voluptas
assumenda est, omnis dolor repellendus. Temporibus
autem quibusdam et aut officiis debitis aut rerum
necessitatibus saepe eveniet, ut et voluptates
repudiandae sint et molestiae non recusandae. Itaque
earum rerum hic tenetur a sapiente delectus, ut aut
reiciendis voluptatibus maiores alias consequatur
aut perferendis doloribus asperiores repellat.
"""

english_text = """
But I must explain to you how all this mistaken idea
of denouncing of a pleasure and praising pain was
born and I will give you a complete account of the
system, and expound the actual teachings of the great
explorer of the truth, the master-builder of human
happiness. No one rejects, dislikes, or avoids
pleasure itself, because it is pleasure, but because
those who do not know how to pursue pleasure
rationally encounter consequences that are extremely
painful. Nor again is there anyone who loves or
pursues or desires to obtain pain of itself, because
it is pain, but occasionally circumstances occur in
which toil and pain can procure him some great
pleasure. To take a trivial example, which of us
ever undertakes laborious physical exercise, except
to obtain some advantage from it? But who has any
right to find fault with a man who chooses to enjoy
a pleasure that has no annoying consequences, or
one who avoids a pain that produces no resultant
pleasure?

On the other hand, we denounce with righteous
indignation and dislike men who are so beguiled and
demoralized by the charms of pleasure of the moment,
so blinded by desire, that they cannot foresee the
pain and trouble that are bound to ensue; and equal
blame belongs to those who fail in their duty
through weakness of will, which is the same as
saying through shrinking from toil and pain. These
cases are perfectly simple and easy to distinguish.
In a free hour, when our power of choice is
untrammeled and when nothing prevents our being
able to do what we like best, every pleasure is to
be welcomed and every pain avoided. But in certain
circumstances and owing to the claims of duty or
the obligations of business it will frequently
occur that pleasures have to be repudiated and
annoyances accepted. The wise man therefore always
holds in these matters to this principle of
selection: he rejects pleasures to secure other
greater pleasures, or else he endures pains to
avoid worse pains.
"""

latin_words = get_normalized_words(latin_text)
latin_set = make_item_sets(latin_words)
latin_rules =  assoc_rules(latin_set,0.75)           
print (latin_rules)

print()
print()

english_words = get_normalized_words(english_text)
english_set = make_item_sets(english_words)
english_rules =  assoc_rules(english_set,0.75)           
print (english_rules)

set1 = set(latin_rules.keys())
set2 = set(english_rules.keys())
print(set1.intersection(set2))