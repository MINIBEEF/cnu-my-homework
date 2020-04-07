OBJECTS = main.o read.o write.o

CC = gcc
CFLAGS = -g

TARGET = test

$(TARGET) : $(OBJECTS)
	$(CC) -o $(TARGET) $(OBJECTS)

main.o : main.c
	$(CC) -c main.c
read.o : io.h read.c
	$(CC) -c read.c
write.o : io.h write.c
	$(CC) -c write.c

clean :
	rm -rf $(OBJECTS) $(TARGET) test.txt
