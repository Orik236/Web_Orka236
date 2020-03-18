let input = document.getElementById("inputVal")
input.addEventListener("keyup", function(event) {
    if (event.keyCode === 13) {
      document.getElementById("addButton").click()
    }else if(event.keyCode === 46){
        document.querySelector("LI").remove()
    }
})

let myList = document.getElementsByTagName("LI")
for (let i = 0; i < myList.length; i++) {
    var span = document.createElement("SPAN")
    span.className = "close"
    image = document.createElement('img')
    image.setAttribute("src", "https://cdn2.iconfinder.com/data/icons/ui-essentials-2/1250/trash-delete-can-garbage-app-android-phone-512.png")
    image.setAttribute("width", "20")
    image.setAttribute("height", "25")
    span.append((image))
    myList[i].append(span)
}

let close = document.getElementsByClassName("close")
for (let i = 0; i < close.length; i++) {
    close[i].onclick = function () {
        let element = this.parentElement
        element.style.display = "none"
    }
}

let list = document.querySelector('UL')
list.addEventListener('click', function (event) {
    if (event.target.tagName === 'LI') {
        event.target.classList.toggle('checked')
    }
}, false)
list.addEventListener('dblclick', function (event) {
    if (event.target.tagName === 'LI') {
        let input = document.getElementById("inputVal")
        input.value = event.target.children[0].innerHTML
    }
}, false)

function newElement() {
    let li = document.createElement("LI")
    let inputValue = document.getElementById("inputVal").value
    let listVal = document.createElement("p")
    listVal.className = "listText"
    listVal.append(inputValue)
    li.append(listVal)
    if (inputValue === '') {
        alert("You must write something!")
    } else {
        document.getElementById("list").append(li)
    }
    document.getElementById("inputVal").value = ""

    let span = document.createElement("SPAN")
    span.className = "close"
    image = document.createElement('img')
    image.setAttribute("src", "https://cdn2.iconfinder.com/data/icons/ui-essentials-2/1250/trash-delete-can-garbage-app-android-phone-512.png")
    image.setAttribute("width", "20")
    image.setAttribute("height", "25")
    span.append((image))
    li.append(span)

    for (let i = 0; i < close.length; i++) {
        close[i].onclick = function () {
            var element = this.parentElement
            element.style.display = "none"
        }
    }
}