// platform: {platform}
// id: {id}
// title: {title}
// url: {url}
// tags: {tags}
// date: {date}
// language: Go
// time: {time}
// space: {space}
// status: {status}

package main

import (
    "fmt"
    "io"
    "os"
)

func main() {
    b, _ := io.ReadAll(os.Stdin)
    // TODO: implement solution
    if len(b) > 0 {
        fmt.Print(string(b))
    }
}
