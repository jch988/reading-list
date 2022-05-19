import csv
from operator import itemgetter

filename = 'book_list.csv'

# Create a list of books, each as a dictionary
with open(filename) as f:
	reader = csv.DictReader(f)
	books = []
	for row in reader:
		books.append(dict(row))

# Add cosmere books to their own list and sort by publication date
cosmere_books = [b for b in books if b['Cosmere'] == 'Yes']
cosmere_books_sorted = sorted(cosmere_books, key=itemgetter('Publication year'), reverse=True)

# Add Expanse books to their own list and sort by order in series
expanse_books = [b for b in books if b['Series'] == 'The Expanse']
expanse_books_sorted = sorted(expanse_books, key = itemgetter('Number in series'), reverse=True)

# Add non-cosmere books to their own list and sort by publication order
non_cosmere_books = [b for b in books if b['Cosmere'] == 'No' and b['Series'] != 'The Expanse']
non_cosmere_books_sorted = sorted(non_cosmere_books, key=itemgetter('Publication year'), reverse=True)


def add_cosmere():
	"""Add the next cosmere book"""
	cosmere_addition = cosmere_books_sorted.pop()
	final_reading_order.append(cosmere_addition)

def add_expanse():
	"""Add the next expanse book"""
	expanse_addition = expanse_books_sorted.pop()
	final_reading_order.append(expanse_addition)

def add_next():
	"""Add next non-cosmere non-expanse book"""
	non_cosmere_addition = non_cosmere_books_sorted.pop()
	final_reading_order.append(non_cosmere_addition)



def add_book(title, author, pub_year, series='None', num_in_series='n/a', Cosmere='No'):
	"""Add a new book to the reading list"""

	headers = ['Title', 'Publication year', 'Author', 'Cosmere', 'Series', 'Number in series']
	addition = {
			'Title': title,
			'Author': author,
			'Publication year': pub_year,
			'Cosmere': Cosmere,
			'Series': series, 
			'Number in series': num_in_series,
	}

	with open(filename, 'a+', newline='\n') as f:
		writer = csv.DictWriter(f, fieldnames=headers)
		writer.writerow(addition)


def remove_book(title):
	"""Remove the given book from the to-read list"""
	pass

def change_book_info():
	"""Change information about a book on the list"""
	pass


def publish():
	"""Publish the list"""
	output = 'computed_reading_list.txt'
	with open(output, 'w') as f:
		for book in final_reading_order:
			if book['Cosmere'] == 'Yes':
				f.write(f"{book['Title']} ({book['Publication year']}) — Cosmere\n")
			elif book['Series'] == 'The Expanse':
				f.write(f"{book['Title']} ({book['Publication year']}) — The Expanse\n")
			else:
				f.write(f"{book['Title']} ({book['Publication year']})\n")


final_reading_order = []


# Create the reading list
while cosmere_books_sorted:
	add_cosmere()
	if non_cosmere_books_sorted:
		add_next()
	if expanse_books_sorted:
		add_expanse()
		if non_cosmere_books_sorted:
			add_next()


publish()