package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func isValid(report []int) bool {
	dir := 0
	if report[0] > report[len(report)-1] {
		dir = -1
	} else if report[0] < report[len(report)-1] {
		dir = 1
	} else {
		return false
	}
	for i := range len(report) - 1 {
		diff := report[i+1] - report[i]
		if diff*dir <= 0 || diff*dir > 3 {
			return false
		}
	}
	return true
}

func main() {
	file, _ := os.Open("day2/input.txt")
	defer file.Close()
	scanner := bufio.NewScanner(file)
	reports := make([][]int, 0)
	for scanner.Scan() {
		line := scanner.Text()
		nums := strings.Split(line, " ")
		report := make([]int, 0)
		for _, num := range nums {
			numI, err := strconv.Atoi(num)
			if err != nil {
				panic(err)
			}
			report = append(report, numI)
		}
		reports = append(reports, report)
	}

	//fmt.Printf("%v", reports)

	validReports := 0
	for _, report := range reports {
		if isValid(report) {
			validReports += 1
		} else {
			// part 2
			for i := range len(report) {
				repCopy := append([]int{}, report...)
				subreport := append(repCopy[:i], repCopy[i+1:]...)
				if isValid(subreport) {
					validReports += 1
					break
				}
			}
		}
	}
	fmt.Println(validReports)

}
