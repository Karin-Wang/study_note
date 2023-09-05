import mmap
import ctypes
import threading

memory_blocks = []  
lock = threading.Lock()  

class Block:
    def __init__(self, size):
        self.size = size
        self.data = None
        self.used = 0
        self.freed = False
        self.prev = None  
        self.next = None  

def start_malloc(size):
    if len(memory_blocks) == 0 or memory_blocks[-1].used + size > memory_blocks[-1].size:
        print("allocate memory, create new block")
        new_heap = mmap.mmap(-1, 4096, mmap.MAP_PRIVATE | mmap.MAP_ANONYMOUS)
        block1 = Block(size=4096)
        block1.data = new_heap
        block1.used = 0
        if len(memory_blocks) > 1:
            block1.prev = memory_blocks[-2] 
        memory_blocks.append(block1)
        if memory_blocks[-1].prev:
            memory_blocks[-1].prev.next = memory_blocks[-1]

    c = 0
    for block in memory_blocks:
        print("find available slot in NO." + str(c) + " block")
        if block.used + size <= block.size:
            print("current used size is " + str(block.used))
            ptr = ctypes.addressof(ctypes.c_void_p.from_buffer(block.data)) + block.used
            block.used += size
            print("now the used size is " + str(block.used))
            return ptr

    return None  

def malloc(size):
    with lock:
        if size == 0:
            return None
        size = (size + 15) & ~15  
        return start_malloc(size)

def merge_blocks():
    for block in memory_blocks:
        if block.freed and block.prev and block.prev.freed:
            print("merging freed")
            block.prev.size += block.size
            memory_blocks.remove(block)
            if block.next:
                block.next.prev = block.prev
            continue

def start_free(ptr):
    for block in memory_blocks:
        if ctypes.addressof(ctypes.c_void_p.from_buffer(block.data)) <= ptr < ctypes.addressof(ctypes.c_void_p.from_buffer(block.data)) + block.used:
            block.freed = True
            print("freed " + str(ptr))
            merge_blocks()
            return

def free(ptr):
    with lock:
        start_free(ptr)

def realloc(ptr, size):
    if size == 0:
        return ptr

    new_ptr = malloc(size)
    if new_ptr:
        old_size = 0
        for block in memory_blocks:
            if ctypes.addressof(ctypes.c_void_p.from_buffer(block.data)) <= ptr < ctypes.addressof(ctypes.c_void_p.from_buffer(block.data)) + block.used:
                old_size = block.used
                break
        ctypes.memmove(new_ptr, ptr, min(old_size, size))
        free(ptr)
        return new_ptr
    else:
        return None

if __name__ == "__main__":

    ptr1 = malloc(4080)
    if ptr1 is not None:
        print("meow meow allocate 128 bytes for ptr1")
    
    ptr1 = realloc(ptr1, 256)
    if ptr1 is not None:
        print("realloc 256 bytes for ptr1")

    ptr2 = malloc(4080)
    if ptr2 is not None:
        print("meow meow malloc 256 bytes for ptr2")

    ptr3 = malloc(4080)
    if ptr3 is not None:
        print("meow meow malloc 4096 bytes ptr3")


    ptr4 = malloc(4080)
    if ptr3 is not None:
        print("meow meow malloc 4096 bytes ptr4")

    print("meow release")
    free(ptr1)
    free(ptr2)
    free(ptr3)
    free(ptr4)


    ptr = malloc(128)
    if ptr is not None:
        try:
            ctypes.memmove(ptr, b"beat kabi bear", 30)
            data = ctypes.string_at(ptr)
            print("read:", data.decode('utf-8'))  
        except Exception as e:
            print("error", e)
        finally:
            free(ptr)
    else:
        print("prt is None")

