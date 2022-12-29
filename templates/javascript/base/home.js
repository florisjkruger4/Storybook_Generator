// js content linked to home.html

const prevBtns = document.querySelectorAll(".btn-prev");
const nextBtns = document.querySelectorAll(".btn-next");
const progress = document.getElementById("progress");
const formSteps = document.querySelectorAll(".form-step");
const progressSteps = document.querySelectorAll(".progress-step");

let formStepsNum = 0;

focusType1 = document.getElementById("contained")
focusType2 = document.getElementById("location")

function checkValue1() {
    var name = document.getElementById("name");
    if(name.value === "") {
        return false;
    } else {
        return true;
    }
}

function checkValue2() {
    var name = document.getElementById("contained");
    if(name.value === "") {
        return false;
    } else {
        return true;
    }
}

nextBtns.forEach((btn) => {
    btn.addEventListener("keydown", (event) => {
        if (event.key === "Enter") {
            if (!checkValue1()) {
                return
            } 

            if (formStepsNum === 1) {
                if (!checkValue2()) {
                    return
                }
            }

            event.preventDefault();
            formStepsNum++;
            updateFormSteps();
            updateProgressbar();
            updateAnim();
        }
    });
});

prevBtns.forEach((btn) => {
btn.addEventListener("click", () => {
    formStepsNum--;
    updateFormSteps();
    updateProgressbar();
});
});

function updateFormSteps() {
formSteps.forEach((formStep) => {
    formStep.classList.contains("form-step-active") &&
    formStep.classList.remove("form-step-active");
});

formSteps[formStepsNum].classList.add("form-step-active");
focusType1.focus();
focusType2.focus();
}


function updateProgressbar() {
progressSteps.forEach((progressStep, idx) => {
    if (idx < formStepsNum + 1) {
        progressStep.classList.add("progress-step-active");
    } else {
        progressStep.classList.remove("progress-step-active");
    }
});

const progressActive = document.querySelectorAll(".progress-step-active");

progress.style.width =
    ((progressActive.length - 1) / (progressSteps.length - 1)) * 100 + "%";
}

function updateAnim() {
    progressSteps.forEach((progressStep) => {
        progressStep.classList.contains("progress-anim") &&
        progressStep.classList.remove("progress-anim");
    });
    progressSteps[formStepsNum].classList.add("progress-anim");
}

function loadAnim() {
    document.getElementById('loader').style.visibility = "visible";
}

currentURL = location.pathname

if (currentURL === "/"){
              document.getElementById('BG').style.backgroundImage = "url(/static/images/fantasy.gif)"
              document.getElementById('BG').style.backgroundPosition = "bottom"
              document.getElementById('BG').style.backgroundPositionY = "-35vh"
              document.getElementById('title').style.fontFamily = "Eagle Lake, cursive"
              document.getElementById('title').style.fontSize = "31px"
              document.getElementById('fantasyBtn').style.animation = "anim 3s ease-in-out infinite"
            }
if (currentURL === "/sportsPage"){
              document.getElementById('BG').style.backgroundImage = "url(/static/images/sports.gif)"
              document.getElementById('BG').style.backgroundPosition = "bottom"
              document.getElementById('BG').style.backgroundPositionY = "-18vh"
              document.getElementById('title').style.fontFamily = "Bungee, cursive"
              document.getElementById('title').style.fontSize = "28px"
              document.getElementById('sportsBtn').style.animation = "anim 3s ease-in-out infinite"
            }
if (currentURL === "/adventurePage"){
              document.getElementById('BG').style.backgroundImage = "url(/static/images/adventure.gif)"
              document.getElementById('BG').style.backgroundPosition = "bottom"
              document.getElementById('BG').style.backgroundPositionY = "-15vh"
              document.getElementById('title').style.fontFamily = "Bangers, cursive"
              document.getElementById('adventureBtn').style.animation = "anim 3s ease-in-out infinite"
            }
if (currentURL === "/spookyPage"){
              document.getElementById('BG').style.backgroundImage = "url(/static/images/spooky.gif)"
              document.getElementById('BG').style.backgroundPosition = "bottom"
              document.getElementById('BG').style.backgroundPositionY = "-10vh"
              document.getElementById('title').style.fontFamily = "Creepster, cursive"
              document.getElementById('spookyBtn').style.animation = "anim 3s ease-in-out infinite"
            }











