const getUSDValue = () => fetch(`https://api.coingecko.com/api/v3/simple/price?ids=Pagan-Gods-FUR-Token&vs_currencies=usd`)
  .then(res => res.json())
const getBRLValue = () => fetch(`https://api.coingecko.com/api/v3/simple/price?ids=Pagan-Gods-FUR-Token&vs_currencies=brl`)
  .then(res => res.json())


function start(){
    getAsync();
}

const getAsync = async () => {
    let usdValue = await getUSDValue()
    usd = document.getElementById('usdValue')
    usd.innerHTML = 'US$ ' + (usdValue['pagan-gods-fur-token']['usd']).toLocaleString(
        undefined, // leave undefined to use the visitor's browser 
                   // locale or a string like 'en-US' to override it.
        { minimumFractionDigits: 6 }
      );

    let brlValue = await getBRLValue()
    brl = document.getElementById('brlValue')
    brl.innerHTML = 'R$ ' + (brlValue['pagan-gods-fur-token']['brl']).toLocaleString(
        undefined, // leave undefined to use the visitor's browser 
                   // locale or a string like 'en-US' to override it.
        { minimumFractionDigits: 5 }
      );
}

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

function checkCalculateBtn() {
    let selector01 = document.getElementById("warrior")
    let selector02 = document.getElementById("ilevel")
    let selector03 = document.getElementById("flevel")
    let btn = document.getElementById("calculateBtn")

    if (selector01.value != "Choose warrior" && 
        selector02.value != "Choose initial level") {
        btn.disabled = false
    }
    else {
        btn.disabled = true       
    }
}