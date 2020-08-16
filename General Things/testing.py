a= [('Gbanzili',), ('Dagaga',), ('Dagada',), ("Dagoda'",), ('Yatê',), ('find out',), ('switchboard',), ('caucus',), ('board,',), ('Comission',), ('inlay',), ('panelling',), ('casing',), ('facing',), ('lining',), ('assumption of Mary',), ('auscultation',)]
words_list = []
final_list = []
for field in a:
    words_list.append(str(field))
for i in words_list:
    print(i[2:-3])
    final_list.append(i[2:-3])
print (final_list)
