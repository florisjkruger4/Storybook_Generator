// js content linked to home.html

const prevBtns = document.querySelectorAll(".btn-prev");
const nextBtns = document.querySelectorAll(".btn-next");
const progress = document.getElementById("progress");
const formSteps = document.querySelectorAll(".form-step");
const progressSteps = document.querySelectorAll(".progress-step");

let formStepsNum = 0;

focusType1 = document.getElementById("superpower")
focusType2 = document.getElementById("location")

function checkValue1() {
    var name = document.getElementById("bestfriendsname");
    if(name.value === "") {
        return false;
    } else {
        return true;
    }
}

function checkValue2() {
    var name = document.getElementById("superpower");
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

function loadAnim() {
    document.getElementById('dotcontainer').style.visibility = "visible";
}











