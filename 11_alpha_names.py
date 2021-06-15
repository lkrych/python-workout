from operator import itemgetter

PEOPLE=[{'first':'Reuven', 'last':'Lerner', 'email':'reuven@lerner.co.il'},
        {'first': 'Revven', 'last': 'Lerner', 'email': 'thisshouldbesecond@blah.com'},
         {'first':'Donald', 'last':'Trump', 'email':'president@whitehouse.gov'},
          {'first':'Vladimir', 'last':'Putin','email':'president@kremvax.ru'}]

def alphabetize_names():
    #assumes the presence of a PEOPLE
    return sorted(PEOPLE, key=itemgetter('last', 'first'))

print(alphabetize_names())
