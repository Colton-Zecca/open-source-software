all: programStatic programShared

programStatic: program.c static_block.a Makefile
			gcc program.c static_block.a -o programStatic

programShared: program.c shared_block.so Makefile
			gcc program.c shared_block.so -o programShared -Wl, -rpath .

static_block.a: block.o Makefile 
			ar qc static_block.a block.o

shared_block.so: block.o Makefile 
			gcc -shared -o shared_block.so block.o

block.o: source/block.c Makefile
		gcc -fPIC -c source/block.c -o block.o

.PHONY: clean
clean:	
	rm -rf *.o *.a *.so programShared programStatic