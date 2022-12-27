// References to DOM Elements
const prevBtn = document.querySelector("#prev-btn");
const nextBtn = document.querySelector("#next-btn");
const book = document.querySelector("#book");

const paper0 = document.querySelector("#p0");
const paper1 = document.querySelector("#p1");
const paper2 = document.querySelector("#p2");
const paper3 = document.querySelector("#p3");

// Event Listener
prevBtn.addEventListener("click", goPrevPage);
nextBtn.addEventListener("click", goNextPage);

// Business Logic
let currentLocation = 1;
let numOfPapers = 5;
let maxLocation = numOfPapers + 1;

function openBook() {
    book.style.transform = "translateX(50%)";
    prevBtn.style.transform = "translateX(-80px)";
    nextBtn.style.transform = "translateX(80px)";
}

function closeBook(isAtBeginning) {
    if(isAtBeginning) {
        book.style.transform = "translateX(0%)";
    } else {
        book.style.transform = "translateX(100%)";
    }
    
    prevBtn.style.transform = "translateX(0px)";
    nextBtn.style.transform = "translateX(0px)";
}

function goNextPage() {
    if(currentLocation < maxLocation) {
        switch(currentLocation) {
            case 1:
                openBook();
                paper0.classList.add("flipped");
                paper0.style.zIndex = 1;
                break;
            case 2:
                paper1.classList.add("flipped");
                paper1.style.zIndex = 2;
                break;
            case 3:
                paper2.classList.add("flipped");
                paper2.style.zIndex = 3;
                paper3.style.zIndex = 3;
                break;
            case 4:
                paper3.classList.add("flipped");
                paper3.style.zIndex = 4;
                paper3.style.backgroundColor = '#624a2e'
                closeBook(false);
                break;
            default:
                throw new Error("unkown state");
        }
        currentLocation++;
    }
}

function goPrevPage() {
    if(currentLocation > 1) {
        switch(currentLocation) {
            case 2:
                closeBook(true);
                paper0.classList.remove("flipped");
                paper0.style.zIndex = 4;
                break;
            case 3:
                paper1.classList.remove("flipped");
                paper1.style.zIndex = 3;
                break;
            case 4:
                paper2.classList.remove("flipped");
                paper2.style.zIndex = 2;
                paper3.style.zIndex = 1;
                break;
            case 5:
                openBook();
                paper3.classList.remove("flipped");
                paper3.style.zIndex = 3;
                break;
            default:
                throw new Error("unkown state");
        }

        currentLocation--;
    }
}


//existing text must be rendered in the first container so we know how high it is compared to the div
//get references to avoid overhead in jQuery
var cont1 = $('#f1');
var cont1Height = cont1.height();

var p1 = $('#f1 p');
var p1Height = p1.height();

var cont2 = $('#b1');
var p2 = $('#b1 p');

var cont3 = $('#f2');
var p3 = $('#f2 p');

var cont4 = $('#b2');
var p4 = $('#b2 p')

var cont5 = $('#f3');
var p5 = $('#f3 p')

//get text and explode it as an array
var p1text = p1.text();
p1text = p1text.split('');

//prepare p2 text
p2text = [];

//if greater height
while (p1Height > cont1Height) {

    //remove last character
    lastChar = p1text.pop();

    //prepend to p2 text
    p2text.unshift(lastChar);

    //reassemble p1 text
    p1temp = p1text.join('');

    //place back to p1
    p1.text(p1temp);

    //re-evaluate height
    p1Height = p1.height();

    //loop
}

//if less than, assemble p2 text and render to p2 container
p2.text(p2text.join(''));

var cont2Height = cont1.height();

var p2Height = p2.height();

//get text and explode it as an array
var p2text = p2.text();
p2text = p2text.split('');

//prepare p3 text
p3text = [];

//if greater height
while (p2Height > cont2Height) {

    //remove last character
    lastChar = p2text.pop();

    //prepend to p2 text
    p3text.unshift(lastChar);

    //reassemble p1 text
    p2temp = p2text.join('');

    //place back to p1
    p2.text(p2temp);

    //re-evaluate height
    p2Height = p2.height();

    //loop
}

//if less than, assemble p2 text and render to p2 container
p3.text(p3text.join(''));

var cont3Height = cont1.height();

var p3Height = p3.height();

//get text and explode it as an array
var p3text = p3.text();
p3text = p3text.split('');

//prepare p4 text
p4text = [];

//if greater height
while (p3Height > cont3Height) {

    //remove last character
    lastChar = p3text.pop();

    //prepend to p2 text
    p4text.unshift(lastChar);

    //reassemble p1 text
    p3temp = p3text.join('');

    //place back to p1
    p3.text(p3temp);

    //re-evaluate height
    p3Height = p3.height();

    //loop
}

//if less than, assemble p2 text and render to p2 container
p4.text(p4text.join(''));

var cont4Height = cont1.height();

var p4Height = p4.height();

//get text and explode it as an array
var p4text = p4.text();
p4text = p4text.split('');

//prepare p5 text
p5text = [];

//if greater height
while (p4Height > cont4Height) {

    //remove last character
    lastChar = p4text.pop();

    //prepend to p2 text
    p5text.unshift(lastChar);

    //reassemble p1 text
    p4temp = p4text.join('');

    //place back to p1
    p4.text(p4temp);

    //re-evaluate height
    p4Height = p4.height();

    //loop
}

//if less than, assemble p2 text and render to p2 container
p5.text(p5text.join(''));