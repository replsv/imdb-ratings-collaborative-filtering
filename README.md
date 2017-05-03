# iMDB Ratings - Collaborative Filtering applied over ratings

Scrape movies' data using BeautifulSoup. Aggregated data and either determine similar user classes or suggest titles rated under a determined value.

Sample output:
```
[+] Extracting data
{u'Aged 18-29': {'American Gangster (2007)': 8.0,
                 'Captain America: Civil War (2016)': 8.0,
                 'Captain Phillips (2013)': 8.0,
                 'Guardians of the Galaxy (2014)': 8.1,
                 'Lock, Stock and Two Smoking Barrels (1998)': 8.3,
                 'Logan (2017)': 8.5,
                 "One Flew Over the Cuckoo's Nest (1975)": 8.8,
                 'RocknRolla (2008)': 7.5,
                 'The Invisible Guest (2016)': 8.2,
                 'The Pianist (2002)': 8.7,
                 'The Transporter (2002)': 6.9,
                 'Titanic (1997)': 8.0},
 u'Aged 30-44': {'American Gangster (2007)': 7.7,
                 'Captain America: Civil War (2016)': 7.7,
                 'Captain Phillips (2013)': 7.7,
                 'Guardians of the Galaxy (2014)': 7.9,
                 'Lock, Stock and Two Smoking Barrels (1998)': 8.2,
                 'Logan (2017)': 8.2,
                 "One Flew Over the Cuckoo's Nest (1975)": 8.7,
                 'RocknRolla (2008)': 7.2,
                 'The Invisible Guest (2016)': 7.8,
                 'The Pianist (2002)': 8.4,
                 'The Transporter (2002)': 6.7,
                 'Titanic (1997)': 7.4},
 u'Aged 45+': {'American Gangster (2007)': 7.5,
               'Captain America: Civil War (2016)': 7.7,
               'Captain Phillips (2013)': 7.7,
               'Guardians of the Galaxy (2014)': 7.9,
               'Lock, Stock and Two Smoking Barrels (1998)': 7.8,
               'Logan (2017)': 8.0,
               "One Flew Over the Cuckoo's Nest (1975)": 8.7,
               'RocknRolla (2008)': 7.0,
               'The Invisible Guest (2016)': 7.5,
               'The Pianist (2002)': 8.2,
               'The Transporter (2002)': 6.8,
               'Titanic (1997)': 7.5},
 u'Aged under 18': {'American Gangster (2007)': 8.1,
                    'Captain America: Civil War (2016)': 8.4,
                    'Captain Phillips (2013)': 8.1,
                    'Guardians of the Galaxy (2014)': 8.5,
                    'Lock, Stock and Two Smoking Barrels (1998)': 8.3,
                    'Logan (2017)': 9.1,
                    "One Flew Over the Cuckoo's Nest (1975)": 9.0,
                    'RocknRolla (2008)': 7.3,
                    'The Invisible Guest (2016)': 8.8,
                    'The Pianist (2002)': 8.7,
                    'The Transporter (2002)': 7.1,
                    'Titanic (1997)': 8.2},
 u'Females': {'American Gangster (2007)': 7.6,
              'Captain America: Civil War (2016)': 8.0,
              'Captain Phillips (2013)': 7.9,
              'Guardians of the Galaxy (2014)': 8.1,
              'Lock, Stock and Two Smoking Barrels (1998)': 8.1,
              'Logan (2017)': 8.3,
              "One Flew Over the Cuckoo's Nest (1975)": 8.6,
              'RocknRolla (2008)': 7.5,
              'The Invisible Guest (2016)': 8.3,
              'The Pianist (2002)': 8.6,
              'The Transporter (2002)': 6.9,
              'Titanic (1997)': 8.1},
 u'Females Aged 18-29': {'American Gangster (2007)': 7.7,
                         'Captain America: Civil War (2016)': 8.0,
                         'Captain Phillips (2013)': 7.9,
                         'Guardians of the Galaxy (2014)': 8.1,
                         'Lock, Stock and Two Smoking Barrels (1998)': 8.2,
                         'Logan (2017)': 8.3,
                         "One Flew Over the Cuckoo's Nest (1975)": 8.7,
                         'RocknRolla (2008)': 7.6,
                         'The Invisible Guest (2016)': 8.3,
                         'The Pianist (2002)': 8.8,
                         'The Transporter (2002)': 6.9,
                         'Titanic (1997)': 8.3},
 u'Females Aged 30-44': {'American Gangster (2007)': 7.6,
                         'Captain America: Civil War (2016)': 7.8,
                         'Captain Phillips (2013)': 7.8,
                         'Guardians of the Galaxy (2014)': 8.0,
                         'Lock, Stock and Two Smoking Barrels (1998)': 8.0,
                         'Logan (2017)': 8.1,
                         "One Flew Over the Cuckoo's Nest (1975)": 8.6,
                         'RocknRolla (2008)': 7.3,
                         'The Invisible Guest (2016)': 8.1,
                         'The Pianist (2002)': 8.5,
                         'The Transporter (2002)': 6.8,
                         'Titanic (1997)': 7.8},
 u'Females Aged 45+': {'American Gangster (2007)': 7.3,
                       'Captain America: Civil War (2016)': 7.9,
                       'Captain Phillips (2013)': 8.0,
                       'Guardians of the Galaxy (2014)': 8.0,
                       'Lock, Stock and Two Smoking Barrels (1998)': 7.1,
                       'Logan (2017)': 8.1,
                       "One Flew Over the Cuckoo's Nest (1975)": 8.7,
                       'RocknRolla (2008)': 7.2,
                       'The Invisible Guest (2016)': 8.6,
                       'The Pianist (2002)': 8.3,
                       'The Transporter (2002)': 7.1,
                       'Titanic (1997)': 7.7},
 u'Females under 18': {'American Gangster (2007)': 8.1,
                       'Captain America: Civil War (2016)': 8.8,
                       'Captain Phillips (2013)': 8.1,
                       'Guardians of the Galaxy (2014)': 8.5,
                       'Lock, Stock and Two Smoking Barrels (1998)': 8.5,
                       'Logan (2017)': 9.0,
                       "One Flew Over the Cuckoo's Nest (1975)": 8.8,
                       'RocknRolla (2008)': 7.9,
                       'The Invisible Guest (2016)': 8.6,
                       'The Pianist (2002)': 8.9,
                       'The Transporter (2002)': 7.0,
                       'Titanic (1997)': 8.5},
 u'IMDb staff': {'American Gangster (2007)': 7.4,
                 'Captain America: Civil War (2016)': 7.6,
                 'Captain Phillips (2013)': 8.0,
                 'Guardians of the Galaxy (2014)': 8.2,
                 'Lock, Stock and Two Smoking Barrels (1998)': 7.6,
                 'Logan (2017)': 7.7,
                 "One Flew Over the Cuckoo's Nest (1975)": 8.5,
                 'RocknRolla (2008)': 6.6,
                 'The Pianist (2002)': 8.2,
                 'The Transporter (2002)': 6.9,
                 'Titanic (1997)': 7.6},
 u'Males': {'American Gangster (2007)': 7.8,
            'Captain America: Civil War (2016)': 7.8,
            'Captain Phillips (2013)': 7.8,
            'Guardians of the Galaxy (2014)': 8.0,
            'Lock, Stock and Two Smoking Barrels (1998)': 8.2,
            'Logan (2017)': 8.4,
            "One Flew Over the Cuckoo's Nest (1975)": 8.7,
            'RocknRolla (2008)': 7.3,
            'The Invisible Guest (2016)': 7.8,
            'The Pianist (2002)': 8.5,
            'The Transporter (2002)': 6.8,
            'Titanic (1997)': 7.6},
 u'Males Aged 18-29': {'American Gangster (2007)': 8.0,
                       'Captain America: Civil War (2016)': 8.0,
                       'Captain Phillips (2013)': 8.0,
                       'Guardians of the Galaxy (2014)': 8.1,
                       'Lock, Stock and Two Smoking Barrels (1998)': 8.3,
                       'Logan (2017)': 8.5,
                       "One Flew Over the Cuckoo's Nest (1975)": 8.8,
                       'RocknRolla (2008)': 7.5,
                       'The Invisible Guest (2016)': 8.2,
                       'The Pianist (2002)': 8.7,
                       'The Transporter (2002)': 6.9,
                       'Titanic (1997)': 7.9},
 u'Males Aged 30-44': {'American Gangster (2007)': 7.7,
                       'Captain America: Civil War (2016)': 7.7,
                       'Captain Phillips (2013)': 7.7,
                       'Guardians of the Galaxy (2014)': 7.9,
                       'Lock, Stock and Two Smoking Barrels (1998)': 8.2,
                       'Logan (2017)': 8.2,
                       "One Flew Over the Cuckoo's Nest (1975)": 8.7,
                       'RocknRolla (2008)': 7.2,
                       'The Invisible Guest (2016)': 7.7,
                       'The Pianist (2002)': 8.4,
                       'The Transporter (2002)': 6.7,
                       'Titanic (1997)': 7.3},
 u'Males Aged 45+': {'American Gangster (2007)': 7.5,
                     'Captain America: Civil War (2016)': 7.6,
                     'Captain Phillips (2013)': 7.7,
                     'Guardians of the Galaxy (2014)': 7.9,
                     'Lock, Stock and Two Smoking Barrels (1998)': 7.8,
                     'Logan (2017)': 8.0,
                     "One Flew Over the Cuckoo's Nest (1975)": 8.7,
                     'RocknRolla (2008)': 7.0,
                     'The Invisible Guest (2016)': 7.4,
                     'The Pianist (2002)': 8.2,
                     'The Transporter (2002)': 6.7,
                     'Titanic (1997)': 7.4},
 u'Males under 18': {'American Gangster (2007)': 8.1,
                     'Captain America: Civil War (2016)': 8.3,
                     'Captain Phillips (2013)': 8.2,
                     'Guardians of the Galaxy (2014)': 8.4,
                     'Lock, Stock and Two Smoking Barrels (1998)': 8.3,
                     'Logan (2017)': 9.1,
                     "One Flew Over the Cuckoo's Nest (1975)": 9.0,
                     'RocknRolla (2008)': 7.2,
                     'The Invisible Guest (2016)': 8.9,
                     'The Pianist (2002)': 8.7,
                     'The Transporter (2002)': 7.1,
                     'Titanic (1997)': 8.0},
 u'Non-US users': {'American Gangster (2007)': 7.8,
                   'Captain America: Civil War (2016)': 7.7,
                   'Captain Phillips (2013)': 7.8,
                   'Guardians of the Galaxy (2014)': 7.9,
                   'Lock, Stock and Two Smoking Barrels (1998)': 8.2,
                   'Logan (2017)': 8.2,
                   "One Flew Over the Cuckoo's Nest (1975)": 8.7,
                   'RocknRolla (2008)': 7.3,
                   'The Invisible Guest (2016)': 7.9,
                   'The Pianist (2002)': 8.5,
                   'The Transporter (2002)': 6.8,
                   'Titanic (1997)': 7.7},
 u'Top 1000 voters': {'American Gangster (2007)': 7.3,
                      'Captain America: Civil War (2016)': 7.5,
                      'Captain Phillips (2013)': 7.4,
                      'Guardians of the Galaxy (2014)': 7.5,
                      'Lock, Stock and Two Smoking Barrels (1998)': 7.1,
                      'Logan (2017)': 7.8,
                      "One Flew Over the Cuckoo's Nest (1975)": 8.7,
                      'RocknRolla (2008)': 6.1,
                      'The Invisible Guest (2016)': 7.1,
                      'The Pianist (2002)': 8.1,
                      'The Transporter (2002)': 6.4,
                      'Titanic (1997)': 7.2},
 u'US users': {'American Gangster (2007)': 7.8,
               'Captain America: Civil War (2016)': 8.1,
               'Captain Phillips (2013)': 7.8,
               'Guardians of the Galaxy (2014)': 8.3,
               'Lock, Stock and Two Smoking Barrels (1998)': 8.0,
               'Logan (2017)': 8.6,
               "One Flew Over the Cuckoo's Nest (1975)": 8.7,
               'RocknRolla (2008)': 7.3,
               'The Invisible Guest (2016)': 7.9,
               'The Pianist (2002)': 8.4,
               'The Transporter (2002)': 6.8,
               'Titanic (1997)': 7.6}}
---
[+] Collaborative filtering based on user classes
--- Top 3 similar user classes for each user class - Similarity function used: Cosine Distance
[-] IMDb staff
[(1.983, u'Females under 18'),
 (1.866, u'Aged under 18'),
 (1.827, u'Males under 18')]
[-] Aged 30-44
[(1.922, u'Females under 18'),
 (1.817, u'Aged under 18'),
 (1.786, u'Males under 18')]
[-] Females
[(2.0, u'Top 1000 voters'),
 (1.675, u'Females under 18'),
 (1.626, u'Males Aged 45+')]
[-] Females under 18
[(2.321, u'Top 1000 voters'), (2.065, u'Males Aged 45+'), (2.033, u'Aged 45+')]
[-] Females Aged 45+
[(1.904, u'Females under 18'),
 (1.797, u'Top 1000 voters'),
 (1.776, u'Aged under 18')]
[-] Males
[(1.866, u'Top 1000 voters'),
 (1.817, u'Females under 18'),
 (1.698, u'Aged under 18')]
[-] Males Aged 18-29
[(2.057, u'Top 1000 voters'),
 (1.71, u'Males Aged 45+'),
 (1.663, u'IMDb staff')]
[-] Aged under 18
[(2.251, u'Top 1000 voters'), (1.975, u'Males Aged 45+'), (1.94, u'Aged 45+')]
[-] Aged 18-29
[(2.065, u'Top 1000 voters'),
 (1.721, u'Males Aged 45+'),
 (1.675, u'IMDb staff')]
[-] Females Aged 30-44
[(1.857, u'Top 1000 voters'),
 (1.847, u'Females under 18'),
 (1.732, u'Aged under 18')]
[-] Males Aged 30-44
[(1.94, u'Females under 18'),
 (1.837, u'Aged under 18'),
 (1.807, u'Males under 18')]
[-] Top 1000 voters
[(2.321, u'Females under 18'),
 (2.251, u'Aged under 18'),
 (2.231, u'Males under 18')]
[-] Aged 45+
[(2.033, u'Females under 18'),
 (1.94, u'Aged under 18'),
 (1.913, u'Males under 18')]
[-] US users
[(1.922, u'Top 1000 voters'),
 (1.754, u'Females under 18'),
 (1.626, u'Aged under 18')]
[-] Females Aged 18-29
[(2.049, u'Top 1000 voters'),
 (1.698, u'Males Aged 45+'),
 (1.663, u'IMDb staff')]
[-] Males under 18
[(2.231, u'Top 1000 voters'), (1.949, u'Males Aged 45+'), (1.913, u'Aged 45+')]
[-] Non-US users
[(1.847, u'Top 1000 voters'),
 (1.837, u'Females under 18'),
 (1.721, u'Aged under 18')]
[-] Males Aged 45+
[(2.065, u'Females under 18'),
 (1.975, u'Aged under 18'),
 (1.949, u'Males under 18')]
---
--- Recommend movie for each user class
[-] IMDb staff
[(8.181375358166186, 'The Invisible Guest (2016)'),
 (7.813037249283665, 'American Gangster (2007)'),
 (7.317765042979939, 'RocknRolla (2008)'),
 (6.878366762177649, 'The Transporter (2002)')]
[-] Aged 30-44
[(7.90538033395176, 'Titanic (1997)'),
 (7.230241187384042, 'RocknRolla (2008)'),
 (6.899443413729128, 'The Transporter (2002)')]
[-] Females
[(6.816240875912411, 'The Transporter (2002)')]
[-] Females under 18
[(6.7878001921229565, 'The Transporter (2002)')]
[-] Females Aged 45+
[(8.078340365682136, 'Lock, Stock and Two Smoking Barrels (1998)'),
 (7.777215189873417, 'American Gangster (2007)'),
 (7.23389592123769, 'RocknRolla (2008)'),
 (6.842194092827004, 'The Transporter (2002)')]
[-] Males
[(7.153333333333334, 'RocknRolla (2008)'),
 (6.868484848484847, 'The Transporter (2002)')]
[-] Males Aged 18-29
[(6.798576512455517, 'The Transporter (2002)')]
[-] Aged under 18
[(7.0699196326062, 'RocknRolla (2008)'),
 (6.775200918484501, 'The Transporter (2002)')]
[-] Aged 18-29
[(6.796302816901406, 'The Transporter (2002)')]
[-] Females Aged 30-44
[(7.1703921568627464, 'RocknRolla (2008)'),
 (6.862549019607845, 'The Transporter (2002)')]
[-] Males Aged 30-44
[(7.909608540925264, 'Titanic (1997)'),
 (7.240747330960853, 'RocknRolla (2008)'),
 (6.902313167259786, 'The Transporter (2002)')]
[-] Top 1000 voters
[(8.24799331103679, 'The Invisible Guest (2016)'),
 (8.13897893030794, 'Lock, Stock and Two Smoking Barrels (1998)'),
 (7.936547811993517, 'Captain Phillips (2013)'),
 (7.902917341977308, 'Titanic (1997)'),
 (7.819773095623986, 'American Gangster (2007)'),
 (7.360210696920586, 'RocknRolla (2008)'),
 (6.908184764991897, 'The Transporter (2002)')]
[-] Aged 45+
[(7.317711598746081, 'RocknRolla (2008)'),
 (6.909404388714732, 'The Transporter (2002)')]
[-] US users
[(7.140257352941177, 'RocknRolla (2008)'),
 (6.847426470588234, 'The Transporter (2002)')]
[-] Females Aged 18-29
[(6.81, 'The Transporter (2002)')]
[-] Males under 18
[(7.082552693208431, 'RocknRolla (2008)'),
 (6.77751756440281, 'The Transporter (2002)')]
[-] Non-US users
[(7.166599190283399, 'RocknRolla (2008)'),
 (6.874089068825911, 'The Transporter (2002)')]
[-] Males Aged 45+
[(8.3018154311649, 'The Invisible Guest (2016)'),
 (7.943191800878477, 'Titanic (1997)'),
 (7.330161054172767, 'RocknRolla (2008)'),
 (6.914055636896046, 'The Transporter (2002)')]
```