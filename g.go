package main

import "fmt"

type Books struct {
    title string
    author string
    subject string
    book_id int
}

func max(num1, num2 int) int {
    /* 声明局部变量 */
    var result int
    if (num1 > num2) {
        result = num1
    } else {
        result = num2
    }
    return result
}

func main() {
    fmt.Println("Hello, World!" + "xie")
    var stockcode=123
    var enddate="2020-12-31"
    var url="Code=%d endDate=%s"
    var target_url=fmt.Sprintf(url,stockcode,enddate)
    fmt.Println(target_url)
    // 声明一个变量并初始化
    var aw = "RUNOOB"
    fmt.Println(aw)
    // 没有初始化就为零值
    var bw int
    fmt.Println(bw)
    // bool 零值为 false
    var cw bool
    fmt.Println(cw)
    // 直接声明
    ex := "43"
    fmt.Println("wsfsf:", ex)
    println("the max is:" + max(8, 9))

    const LENGTH int = 10
    const WIDTH int = 5  
    var area int
    const a, b, c = 1, false, "str" //多重赋值
    area = LENGTH * WIDTH
    fmt.Printf("面积为 : %d", area)
    println()
    println(a, b, c)
    println(len(aw))

    var seq = [4]int{4, 1, 5, 3}
    s2 := [...]int{3, 5, 0, 3, 2}
    tt := seq[1]
    fmt.Println(tt, s2[3])

    var aa int= 20
    /* 声明实际变量 */
    var ip *int
    /* 声明指针变量 */
    ip = &aa
    /* 指针变量的存储地址 */
    fmt.Printf("a 变量的地址是: %x\n", &aa)
    /* 指针变量的存储地址 */
    fmt.Printf("ip 变量储存的指针地址: %x\n", ip)
    /* 使用指针访问值 */
    fmt.Printf("*ip 变量的值: %d\n", *ip)

    fmt.Println(Books{"Go 语言", "www.runoob.com", "Go 语言教程", 649507})
    // 也可以使用 key => value 格式
    fmt.Println(Books{title: "Go 语言", author: "www.runoob.com", subject: "Go 语言教程", book_id: 6407})
    // 忽略的字段为 0或空
    fmt.Println(Books{title: "Go 语言", author: "www.runoob.com"})
    var Book1 Books
    Book1.title = "Go 语言a"
    Book1.author = "www.runoob.comy"
    Book1.subject = "Go 语言教程x"
    Book1.book_id = 472
    fmt.Printf("Book 1 title : %s\n", Book1.title)
    fmt.Printf("Book 1 author : %s\n", Book1.author)
    fmt.Printf("Book 1 subject : %s\n", Book1.subject)
    fmt.Printf("Book 1 book_id : %d\n", Book1.book_id)

    sl := make([]int, 5)
}