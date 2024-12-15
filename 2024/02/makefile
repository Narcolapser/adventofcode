build :
	gcc -o program.bin main.c list.c

run :
	./program.bin

test :
	gcc -o test.bin list.c test.c 
	gcc -o test_list.bin list.c line.test.c
	./test.bin
	./test_list.bin