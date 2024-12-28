#taken from the charm++ directory

CHARMDIR= #path to charm++ directory 
CHARMC = #path to charmc 

#CHARMDIR= /Users/stevenqie/software/charm
#CHARMC = /Users/stevenqie/software/charm/netlrts-darwin-arm8/bin/charmc 

all: server

server: server.o
	$(CHARMC) -o $@ server.o -language converse++

server.o: server.C
	$(CHARMC) -c server.C -language converse++

clean:
	rm -f client server *.o conv-host charmrun