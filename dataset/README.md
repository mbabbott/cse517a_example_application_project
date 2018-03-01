Dataset
=======

.gitignore
----------

It is good practice to not upload datasets to your repositories both because they are often large but also because datasets have certain intellectual property associated with them and you should give proper credit to the source where you got the dataset (unless you have made your own dataset).

Source
------

The dataset is a compilation of MIDI sequences of songs in the key of G major or the key of D major. Most of the sequences are pieces composed by J.S. Bach, downloaded from http://jsbach.net/midi/. We chose G and D major because a large portion of Bach's work is in one of those keys. We selected pieces of the appropriate key using the listing on https://en.wikipedia.org/wiki/List_of_compositions_by_Johann_Sebastian_Bach

We treated the data as bag-of-words collections of musical notes. Each note in a given MIDI sequence is a single 'word' and the number of times the note appears is its frequency. We stored the data in .csv files, with each column representing a piece. The first 12 rows correspond to a musical note, starting at the note C and stepping up a semitone row by row. The number in a given cell represents the percentage of a piece that a given note takes up. The 13th row corresponds to the actual key of the piece, with 1 representing the key of G major and 0 representing the key of D major. We read calculated the note ratios using midi2bagofratio. We manually separated the pieces by key into different folders.

Statistics
----------

35 pieces are in the key of D Major

	in our dataset:
	C represents 2.72% of notes in D major pieces
	C# represents 9.1% of notes in D major pieces
	D represents 16.5% of notes in D major pieces
	D# represents 1.04% of notes in D major pieces
	E represents 15.1% of notes in D major pieces
	F represents 2.26% of notes in D major pieces
	F# represents 13.1% of notes in D major pieces
	G represents 9.56% of notes in D major pieces
	G# represents 3.08% of notes in D major pieces
	A represents 15.8% of notes in D major pieces
	A# represents 1.02% of notes in D major pieces
	B represents 10.7% of notes in D major pieces

74 pieces are in the key of G Major

	in our dataset:
	C represents 9.01% of notes in G major pieces
	C# represents 3.77% of notes in G major pieces
	D represents 14.7% of notes in G major pieces
	D# represents 2.1% of notes in G major pieces
	E represents 12.1% of notes in G major pieces
	F represents 1.59% of notes in G major pieces
	F# represents 11.3% of notes in G major pieces
	G represents 15.5% of notes in G major pieces
	G# represents 1.12% of notes in G major pieces
	A represents 14.1% of notes in G major pieces
	A# represents 1.44% of notes in G major pieces
	B represents 13.3% of notes in G major pieces
	