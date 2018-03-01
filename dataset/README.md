Dataset
=======

.gitignore
----------

It is good practice to not upload datasets to your repositories both because they are often large but also because datasets have certain intellectual property associated with them and you should give proper credit to the source where you got the dataset (unless you have made your own dataset).

Source
------

The dataset is a compilation of MIDI sequences of songs composed by J.S. Bach. They were downloaded from http://jsbach.net/midi/. We manually looked up the key of each piece using https://en.wikipedia.org/wiki/List_of_compositions_by_Johann_Sebastian_Bach, and wrote those keys into a file ordered by BWV number (https://en.wikipedia.org/wiki/Bach-Werke-Verzeichnis). The files are all in the Dataset folder ordered by filename. Because of the way the files are named, this also orders them by BWV number. 

The data contains at least one song of every musical key. We read the MIDI files as collections of musical notes, bag-of-words style and store the information in a .csv file. The 'words' are musical notes, and their frequency is the number of times they appear in the piece. Technically, because of the way these MIDI files are written, each note appears twice, but since we're using the ratio of each note relative to the total, it doesn't matter. We're also thinking about implementing the bag-of-notes based on the total duration of each note, rather than the number of occurences.
