package main

import (
    "fmt"
    "sync"
    "time"
)

type ReadWriteLock struct {
    mu         sync.Mutex
    readersCounter    int
    isWriteLock bool
	cond       *sync.Cond
}

func NewReadWriteLock() *ReadWriteLock {
    return &ReadWriteLock{
        cond: sync.NewCond(&sync.Mutex{}),
    }
}

func (rw *ReadWriteLock) ReadLock() {
    rw.mu.Lock()
    for rw.isWriteLock {
		rw.cond.Wait()
    }
    rw.readersCounter++
	fmt.Println("====read locked====")
    rw.mu.Unlock()
}

func (rw *ReadWriteLock) ReadUnlock() {
    rw.mu.Lock()
    rw.readersCounter--
    if rw.readersCounter == 0 {
		rw.cond.Signal()
		fmt.Println("====read unlocked====")
    } 
	rw.mu.Unlock()
}

func (rw *ReadWriteLock) WriteLock() {
    rw.mu.Lock()
    for rw.readersCounter > 0 || rw.isWriteLock {
		rw.cond.Wait()
    }
    rw.isWriteLock = true
	fmt.Println("====write locked waiting====")
	time.Sleep(1)
    rw.mu.Unlock()
}

func (rw *ReadWriteLock) WriteUnlock() {
    rw.mu.Lock()
    rw.isWriteLock = false
	rw.cond.Broadcast()
	fmt.Println("====write unlocked====")
    rw.mu.Unlock()
}

var (
    data map[string]string
    rwLock   *ReadWriteLock
)

func init() {
    data = make(map[string]string)
	rwLock = NewReadWriteLock()
}

func readData(key string) string {
    rwLock.ReadLock()
    defer rwLock.ReadUnlock()

    return data[key]
}

func writeData(key, value string) {
    rwLock.WriteLock()
    defer rwLock.WriteUnlock()

    data[key] = value
}

func main() {
    writeData("a", "123")
	fmt.Println("Write: a -> 123")

    for i := 0; i < 10; i++ {
        go func() {
            fmt.Println("Read a:", readData("a"))
        }()
    }

    go func() {
        writeData("a", "9999")
        fmt.Println("Write: a -> 9999")
    }()

	go func() {
        writeData("a", "7777")
        fmt.Println("Write: a -> 7777")
    }()

	go func() {
        writeData("a", "6666")
        fmt.Println("Write: a -> 6666")
    }()

	for i := 0; i < 3; i++ {
        go func() {
            fmt.Println("Read a:", readData("a"))
        }()
    }

	go func() {
        writeData("b", "555")
        fmt.Println("Write: b -> 555")
    }()

	for i := 0; i < 3; i++ {
        go func() {
            fmt.Println("Read b:", readData("b"))
        }()
    }

    time.Sleep(10 * time.Second)
}
