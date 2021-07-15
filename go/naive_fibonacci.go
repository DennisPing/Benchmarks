package main

import (
	"fmt"
	"time"
)

func fibonacci(n int64) int64 {
	if n < 2 {
		return n
	}
	return fibonacci(n-1) + fibonacci(n-2)
}

func runNaiveFib() {
	const n = 47
	for i:=0 ; i<5 ; i++ {
		t1 := time.Now()
		fmt.Println(fibonacci(n))
		duration := time.Since(t1)
		fmt.Printf("Time taken: %.3f\n", duration.Seconds())
	}
}