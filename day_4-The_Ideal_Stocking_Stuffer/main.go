package main

import (
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"strconv"
	"strings"
)


func main() {
	key := []byte("iwrupvqb")
	var i int64 = 1
	for ; ; i++ {
		m := md5.Sum(strconv.AppendInt(key, i, 10))
		hex := hex.EncodeToString(m[:])

		if strings.HasPrefix(hex, "00000") {
			break
		}
	}

	fmt.Println(i)
}