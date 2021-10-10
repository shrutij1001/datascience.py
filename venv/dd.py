def flatten_list(_2d_list):
    flat_list = []
    # Iterate through the outer list
    for element in _2d_list:
        if type(element) is list:
            # If the element is of type list, iterate through the sublist
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list


a = """राममुनि
अंजना
द्रव्य
हस्तानापुर
व्रशभसेन
शंभुकुमार
आदिनाथ
उमास्वामी
चामुंडराय
गजकुमार मुनि
तोडरमल जी
दीवान अमर चंद
रावण
मांगी तुंगी
कमठ
भावहिंसा
विदेह क्षेत्र
विषणु कुमार
रुकमणि
आचार्य उमास्वामी
बनारसीदासजी
दौलत रामजी
दुर्योधन
सोमा सति
धवल सेठ
आचार्य
धर्म नाथ
श्रेयांश
काल
कुंद कुंद
दौलत राम
चंद्र प्रभ
नकुल
जम्बूद्वीप
अगुरुलाघुत्व
माया
चंदन
शीतलनाथ
जीव
मैना
तीन
विभाव"""

import random


allnew = []
for i in range(0, 150):
    gl = []
    sep = a.split("\n")
    for j in range(0, 5):
        new = random.choice(sep)
        gl.append(new)
        sep.remove(new)
    sep.extend(gl)

    allnew.append(gl)
print(len(sep))
for k in allnew:
    print(k)
dic={}
lists=flatten_list(allnew)
print(lists)
for i in range(len(sep)):
    a=lists.count(sep[i])
    dic[sep[i]]=a
print(dic)
print(len(dic.keys()))









