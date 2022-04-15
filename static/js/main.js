function checkCompareBtn() {
    let selector01 = document.getElementById("warrior01")
    let selector02 = document.getElementById("warrior02")
    let btn = document.getElementById("compareBtn")

    if (selector01.value != "Choose warrior" &&
    selector02.value != "Choose warrior") {
        btn.disabled = false
    }
    else {
        btn.disabled = true       
    }
}

function checkAddBtn() {
    let selector = document.getElementById("warrior")
    let btn = document.getElementById("addBtn")

    if (selector.value != "Choose warrior") {
        btn.disabled = false
    }
    else {
        btn.disabled = true       
    }
}