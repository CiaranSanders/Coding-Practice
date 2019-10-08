CC=gcc
CFLAGS=-g -Wall

all: r

r: regex_matching.o
	$(CC) -o r $(CFLAGS) regex_matching.o

clean:
	rm -f *.o r
