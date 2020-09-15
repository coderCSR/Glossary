import textconversion
import dictionaryconversion
import json
textfile=textconversion.pdf_to_text('se.pdf')
dictionary=dictionaryconversion.dictionary_convertor(textfile.get_text())

"""for each,value in dictionary.items():
	print(each,"---->",value)
	count+=1
print(count)"""
s=json.dumps(dictionary)
#print(s)
with open("final_output.txt","w") as f:
	f.write(s)