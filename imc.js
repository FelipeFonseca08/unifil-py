function Imc(peso, altura) {
    return peso/(altura*altura);
}

function ClassificarImc(imc) {
    if (imc < 18.5) {
        return "Subpeso";
    } else if (imc < 24.9) {
        return "Peso Normal";
    } else if (imc < 29.9) {
        return "Sobrepeso";
    } else if (imc < 34.9) {
        return "Obesidade Classe I";
    } else if (imc < 39.9) {
        return "Obesidade Classe II";
    } else {
        return "Obesidade Classe III";
    }
}

let peso = 70;
let altura = 1.70;


let imc = Imc(peso, altura);
let classificacaoImc = ClassificarImc(imc);

console.log("\nIMC:",  imc.toFixed(2));
console.log("Classificação do meu IMC:", classificacaoImc, "\n");