function carregar() {
    var msg = window.document.getElementById('msg')
    var img = window.document.getElementById('imagem')
    var data = new Date();
    var hora = data.getDate();
    msg.innerHTML = `Agora são ${hora} horas.`
    if (hora >= 6 && hora < 12) {
        msg.innerHTML += ' Bom dia!'
        img.src = '/ex014/images/manha.png'
        document.body.style.background = '#bed0df'
    } else if (hora  >= 12 && hora < 19){
        msg.innerHTML += ' Boa tarde!'
        img.src = '/ex014/images/tarde.png'
        document.body.style.background = '#fec66a'
    } else {
        msg.innerHTML += ' Boa noite!'
        img.src = '/ex014/images/noite.png'
        document.body.style.background = '#21346a'
    }
}