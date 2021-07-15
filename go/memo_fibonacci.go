package main

import (
	"fmt"
	"time"
)

func fibonacciMemo(n int64, memo []int64) int64 {
	if n < 2 {
		return n
	}
	if memo[n] == 0 {
		memo[n] = fibonacciMemo(n-1, memo) + fibonacciMemo(n-2, memo)
	}
	return memo[n]
}

func runMemoFib() {
	const n = 47
	var memo [n+1]int64
	for i:=0 ; i<5 ; i++ {
		start := time.Now()
		fmt.Println(fibonacciMemo(n, memo[:]))
		duration := time.Since(start)
		fmt.Printf("Time taken: %.3f\n", duration.Seconds())
	}
}
