import pandas

def enlarge(n):
    return 100*n

 # it's important to not have global junk when using your function


def df_nulls(df):
    return df.loc[:, df.isna().any()]


def split_addresses(place):
    '''
    Split addresses into multiple columns city, state, zip
    -> df['city'] df['state'] df['zip']
place.split(',')[0]

    '''
    array = []
    x = place.split(',')
    city = x[0]
    array.append(city)
    y = x[1].strip()
    z = y.split(' ')
    state = z[0]
    zip_code = z[1]
    array.extend([state,zip_code])
    return array

def state_abbreviation(x):
    '''
    State abbreviation -> Full Name and visa versa. FL -> Florida, etc.
    (Handle Washington DC and territories like Puerto Rico etc.)
    '''
    states = '''Alabama
    Alaska
    Arizona
    Arkansas
    California
    Colorado
    Connecticut
    Delaware
    Florida
    Georgia
    Hawaii
    Idaho
    Illinois
    Indiana
    Iowa
    Kansas
    Kentucky
    Louisiana
    Maine
    Maryland
    Massachusetts
    Michigan
    Minnesota
    Mississippi
    Missouri
    Montana
    Nebraska
    Nevada
    New Hampshire
    New Jersey
    New Mexico
    New York
    North Carolina
    North Dakota
    Ohio
    Oklahoma
    Oregon
    Pennsylvania
    Rhode Island
    South Carolina
    South Dakota
    Tennessee
    Texas
    Utah
    Vermont
    Virginia
    Washington
    West Virginia
    Wisconsin
    Wyoming'''
    states = states.split()
    states1 = '''Alabama - AL
    Alaska - AK
    Arizona - AZ
    Arkansas - AR
    California - CA
    Colorado - CO
    Connecticut - CT
    Delaware - DE
    Florida - FL
    Georgia - GA
    Hawaii - HI
    Idaho - ID
    Illinois - IL
    Indiana - IN
    Iowa - IA
    Kansas - KS
    Kentucky - KY
    Louisiana - LA
    Maine - ME
    Maryland - MD
    Massachusetts - MA
    Michigan - MI
    Minnesota - MN
    Mississippi - MS
    Missouri - MO
    Montana - MT
    Nebraska - NE
    Nevada - NV
    New Hampshire - NH
    New Jersey - NJ
    New Mexico - NM
    New York - NY
    North Carolina - NC
    North Dakota - ND
    Ohio - OH
    Oklahoma - OK
    Oregon - OR
    Pennsylvania - PA
    Rhode Island - RI
    South Carolina - SC
    South Dakota - SD
    Tennessee - TN
    Texas - TX
    Utah - UT
    Vermont - VT
    Virginia - VA
    Washington - WA
    West Virginia - WV
    Wisconsin - WI
    Wyoming - WY'''
    states1 = states1.split('\n')
    abbreviations = []
    x = x.title()
    for state in states1:
      abbreviations.append(state[-2:])
    if x in states:
        index = states.index(x)
        return abbreviations[index]
    print(x in states)
    index = abbreviations.index(x)
    return states[index]