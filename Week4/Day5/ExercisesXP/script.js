// // Exercise 1 
// let div0 = document.querySelector("#container")
// console.log(div0)
// let pete = document.getElementById("pete")
// pete.lastElementChild.textContent = "Richard"
// console.log(pete.lastElementChild.textContent)
// let uls = document.getElementsByClassName('list')[0]
// console.log(uls)
// let firstEl = document.getElementById('firstEl')
// uls.firstElementChild.textContent = "Gleb"
// firstEl.textContent = "Gleb"
// let sarah = document.getElementById("sarah");
// sarah.remove()
// let ulClass = document.getElementsByClassName('list')[0]
// console.log(pete)
// ulClass.classList.add("student_list")
// pete.classList.add("university", "attendance")

// // Exercise 2 
// let div1 = document.getElementById("users")
// div1.setAttribute("style", "background-color: Aqua;");  
// let john = document.getElementById('john')
// john.style.display='none';
// let pete1 = document.getElementById('pete1')
// pete1.setAttribute("style", "border: 4px black solid")
// document.body.style.fontSize = "20px"

// Exercise 3
// let nav = document.getElementById("navBar")
// nav.setAttribute("id", "socialNetworkNavigation")
// console.log(nav)
// let li0 = document.createElement("li")
// let log = document.createTextNode("LogOut")
// li0.appendChild(log)
// console.log(li0)
// let ulNav = document.getElementById("navLi")
// console.log(ulNav)
// ulNav.appendChild(li0)

// Exercise 4
 let books = []

 let bk0 = {
    tittle: "Lord of the rings",
    author: "J.R.R. Tolkien",
    image: "https://picsum.photos/200/300",
    alreadyRead: true
 }
 let bk1 = {
    tittle: "Harry Potter",
    author: "J.K. Rowling",
    image: "https://picsum.photos/200/300",
    alreadyRead: false
 }
 books.push(bk0, bk1)

 console.log(books)
 let table = document.createElement("table")
 table.innerHTML= `
 <thead>
    <tr>
        <th colspan = "3">Book list</th>
    </tr>
 </thead>
 <tbody>
    <tr class = "${bk0.alreadyRead ? 'red' : ''}">
        <td>${bk0.tittle} written by ${bk0.author}</td>
        <td>
        <img src= "${bk0.image}" />
       </td>
        <td>Aleready read: ${bk0.alreadyRead}</td>
    </tr>
    <tr class = "${bk1.alreadyRead ? 'red' : ''}">
        <td>${bk1.tittle} written by ${bk1.author}</td>
        <td>
        <img src= "${bk1.image}" />
       </td>
        <td>Aleready read: ${bk1.alreadyRead}</td>
    </tr>
 </tbody>
 `
 let bkList = document.querySelector(".list-books")
 bkList.appendChild(table)