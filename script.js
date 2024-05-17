function convert() {
    var conversionType = document.getElementById("conversionType").value;
    var inputNumber = document.getElementById("inputNumber").value;
    var resultElement = document.getElementById("result");
    
    if (conversionType === "hexToDec") {
        var decimalNumber = parseInt(inputNumber, 16);
        resultElement.innerText = "Decimal: " + decimalNumber;
    } else {
        var hexNumber = (+inputNumber).toString(16).toUpperCase();
        resultElement.innerText = "Hexadecimal: 0x" + hexNumber;
    }
}

