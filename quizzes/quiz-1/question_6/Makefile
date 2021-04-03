main: main.c helper.c libshared.so libstatic.a
	gcc -c main.c helper.c libstatic.a libshared.so -o main -Wl, -rpath .

# helper.o: helper.c 
# 			gcc helper.c libstatic.a libshared.so -o main -Wl, -rpath .

libshared.so: shared.o 
			gcc -shared -o libshared.so shared.o

libstatic.a: static.o 
			ar qc libstatic.a static.o

shared.o: shared/shared.c 
			gcc -fPIC -c shared/shared.c -o shared.o

static.o: static/static.c
			gcc -fPIC -c static/static.c -o static.o

.PHONY: clean
clean:	
	rm -rf *.o *.a *.so main