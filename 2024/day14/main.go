package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
)

const border_x = 101
const border_y = 103

type Pos struct {
	x int
	y int
}

type Robot struct {
	pos      Pos
	velocity Pos
}

func (r Robot) newPos() Pos {
	new_x := r.pos.x + r.velocity.x
	if new_x >= border_x {
		new_x = new_x - border_x
	} else if new_x < 0 {
		new_x = border_x + new_x
	}

	new_y := r.pos.y + r.velocity.y
	if new_y >= border_y {
		new_y = new_y - border_y
	} else if new_y < 0 {
		new_y = border_y + new_y
	}
	return Pos{new_x, new_y}
}

func main() {
	file, _ := os.Open("day14/input.txt")
	defer file.Close()
	scanner := bufio.NewScanner(file)
	re := regexp.MustCompile(`-*\d+`)
	robots := make([]*Robot, 0)
	for scanner.Scan() {
		line := scanner.Text()
		digits := re.FindAllString(line, -1)
		x, _ := strconv.Atoi(digits[0])
		y, _ := strconv.Atoi(digits[1])
		vel_x, _ := strconv.Atoi(digits[2])
		vel_y, _ := strconv.Atoi(digits[3])
		robot := Robot{
			pos:      Pos{x, y},
			velocity: Pos{vel_x, vel_y},
		}
		robots = append(robots, &robot)
	}
	//fmt.Printf("%+v", robots)
	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}

	for _, r := range robots {
		fmt.Printf("positions %v, velocities %v\n", r.pos, r.velocity)
	}
	for _, r := range robots {
		for range 100 {
			r.pos = r.newPos()
		}
	}
	fmt.Println("after")
	for _, r := range robots {
		fmt.Printf("%v\n", r.pos)
	}

	quadrants := map[int]int{}
	for _, r := range robots {
		if r.pos.x < border_x/2 && r.pos.y < border_y/2 {
			quadrants[1] += 1
		} else if r.pos.x > border_x/2 && r.pos.y > border_y/2 {
			quadrants[4] += 1
		} else if r.pos.x < border_x/2 && r.pos.y > border_y/2 {
			quadrants[3] += 1
		} else if r.pos.x > border_x/2 && r.pos.y < border_y/2 {
			quadrants[2] += 1
		}
	}
	safetyFactor := 1
	for key, val := range quadrants {
		fmt.Printf("quadrant %d: robots %d\n", key, val)
		safetyFactor *= val
	}
	fmt.Println(safetyFactor)
}
