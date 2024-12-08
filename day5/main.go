package main

import (
	"fmt"
	"io"
)

func main() {
	content, err := io.ReadAll("example.txt")
	if err != nil {
		panic(err)
	}
	fmt.Println(string(content))
}
