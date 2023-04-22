function puloSim() {
    document.querySelector('input#pulo').style.display = 'none';
}

function puloNao() {
    var numberInput = document.querySelector('input#pulo');
    numberInput.style.display = 'inline';
}

function contar() {
    document.querySelector('div#contagem').innerHTML = '';
    var inicio = parseInt(document.querySelector('input#inicio').value);
    var fim = parseInt(document.querySelector('input#fim').value) + 1;

    if (inicio < fim) {
        if (document.querySelector('input#sim').checked) {
            for (inicio; inicio < fim; inicio++) {
                document.querySelector('div#contagem').innerHTML += inicio;
                document.querySelector('div#contagem').innerHTML += '&#x1F449';    
            }
            document.querySelector('div#contagem').innerHTML += '&#x1F3C1';
        } else {
            var inicio = parseInt(document.querySelector('input#inicio').value);
            var fim = parseInt(document.querySelector('input#fim').value) + 1;
            var pulo = parseInt(document.querySelector('input#pulo').value);
    
            if (pulo == 0 || pulo == 1 || pulo === nil) {
                document.querySelector('div#contagem').innerHTML += 'Algo deu errado, tente novamente.';
            } else {
                for (inicio; inicio < fim; inicio += pulo) {
                    document.querySelector('div#contagem').innerHTML += inicio;
                    document.querySelector('div#contagem').innerHTML += '&#x1F449';
                }
                document.querySelector('div#contagem').innerHTML += '&#x1F3C1';
            }
        }
    }

    else {
        if (document.querySelector('input#sim').checked) {
            for (inicio; inicio < fim; inicio = inicio - 1) {
                document.querySelector('div#contagem').innerHTML += inicio;
                document.querySelector('div#contagem').innerHTML += '&#x1F449';    
            }
            document.querySelector('div#contagem').innerHTML += '&#x1F3C1';
        } else {
            var inicio = parseInt(document.querySelector('input#inicio').value);
            var fim = parseInt(document.querySelector('input#fim').value) + 1;
            var pulo = parseInt(document.querySelector('input#pulo').value);
    
            if (pulo == 0 || pulo == 1 || pulo === nil) {
                document.querySelector('div#contagem').innerHTML += 'Algo deu errado, tente novamente.';
            } else {
                for (inicio; inicio < fim; inicio =- pulo) {
                    document.querySelector('div#contagem').innerHTML += inicio;
                    document.querySelector('div#contagem').innerHTML += '&#x1F449';
                }
                document.querySelector('div#contagem').innerHTML += '&#x1F3C1';
            }
        }
    }
}

window.onload = puloSim();