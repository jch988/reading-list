import statistics as st


filenames = ['Sunreach.txt', 'ReDawn.txt', 'Evershore.txt']
word_counts_dict = {}

def count_words(book):
	with open(book) as b:
		contents = b.read()
	words = contents.split()
	word_counts_dict[book] = len(words)
	print(f"{book} is about {len(words)} long")

for book in filenames:
	count_words(book)

print(word_counts_dict)
word_counts = [x for x in word_counts_dict.values()]
print(word_counts)
print(f"The average word count it {sum(word_counts) / len(word_counts)}")
print(st.median(word_counts))
