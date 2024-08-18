CC = gcc

CFLAGS = -Ic/include
LDFLAGS = -lm
SHARED_FLAGS = -fPIC

SRCS = c/src/main.c c/src/simulation.c
SRC = c/src/simulation.c
OBJS = $(SRCS:.c=.o)
TARGET = simulation

# Link the final executable
$(TARGET): $(OBJS)
	$(CC) -o $@ $^ $(LDFLAGS)

# Rule to compile .c files to .o files
%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

# Create shared library
$(TARGET)-shared:
	$(CC) $(CFLAGS) -shared -o $@.so $(SRC) $(SHARED_FLAGS)

# Compile the Cython code into a Python extension module
$(TARGET)-cython:
	python setup.py build_ext --inplace

clean:
	rm -f $(OBJS) $(TARGET)*