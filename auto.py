import os
import PyPDF2
from symspellpy.symspellpy import SymSpell, Verbosity  # import the module
from tika import parser

pdfFileObj = open("Test.pdf", 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
tempPage = pdfReader.getPage(0)
print(tempPage)
words = tempPage.extractText()
print(words)

raw = parser.from_file('Test.pdf')
pdfData = (raw['content'])

initial_capacity = 83000
max_edit_distance_dictionary = 5 # maximum edit distance per dictionary precalculation
prefix_length = 7
sym_spell = SymSpell(initial_capacity, max_edit_distance_dictionary,
                     prefix_length)
# load dictionary
dictionary_path = os.path.join(os.path.dirname("auto.py"),"frequency_dictionary_en_82_765.txt")

term_index = 0  # column of the term in the dictionary text file
count_index = 1  # column of the term frequency in the dictionary text file
sym_spell.load_dictionary(dictionary_path, term_index, count_index)

'''
#lookup suggestions for single-word input strings
input_term = "throghot"  # misspelling of "throughout"
#max edit distance per lookup
#(max_edit_distance_lookup <= max_edit_distance_dictionary)
max_edit_distance_lookup = 2
suggestion_verbosity = Verbosity.CLOSEST  # TOP, CLOSEST, ALL
suggestions = sym_spell.lookup(input_term, suggestion_verbosity,
                              max_edit_distance_lookup)
#display suggestion term, term frequency, and edit distance
for suggestion in suggestions:
   print("{}, {}, {}".format(suggestion.term, suggestion.count,
                             suggestion.distance))

#lookup suggestions for multi-word input strings (supports compound splitting & merging)
input_term = ("whereis th elove hehad dated forImuch of thepast who "
              "couqdn'tread in sixtgrade and ins pired him")
'''
#input_term = ("Sometimes, when I am in your clas, I think about leaving and saying my computer crashe. However, I would like an A, so I do not do it. Also, I think it wuld be better if you gave us less work or were niice like Mr. Field.")
# max edit distance per lookup (per single word, not per whole input string)
input_term = pdfData
max_edit_distance_lookup = 5
suggestions = sym_spell.lookup_compound(input_term,
                                        max_edit_distance_lookup)
# display suggestion term, edit distance, and term frequency
for suggestion in suggestions:
    print(suggestion.term)


from autocorrect import spell
#f = open("test.txt", "r")
#for line in f:
	#words = line.split(" ")
	#for w in words:
		#print(spell(w), end = " ")

words = pdfData.split(" ")
for w in words:
	print(spell(w), end = " ")