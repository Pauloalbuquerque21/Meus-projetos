
var a = window.document.getElementById('sobremim')
        a.addEventListener('mouseout',sair)
        a.addEventListener('mouseenter',entrar)
        a.addEventListener('click',clicar)

        var b = window.document.getElementById('projetos')
        b.addEventListener('mouseout',sair1)
        b.addEventListener('mouseenter',entrar1)
        b.addEventListener('click',clicar1)
        var c = window.document.getElementById('habilidades')
        c.addEventListener('mouseout',sair2)
        c.addEventListener('mouseenter',entrar2)
        c.addEventListener('click',clicar2)
        function entrar(){ 
            a.style.color = 'purple'
        }
        function sair(){
            a.style.color='blue'
        }
        function clicar(){
            a.style.color='red'
        }
        function entrar1(){ 
            b.style.color = 'purple'
        }
        function sair1(){
            b.style.color='blue'
        }
        function clicar1(){
            b.style.color='red'
        }
        function entrar2(){ 
            c.style.color = 'purple'
        }
        function sair2(){
            c.style.color='blue'
        }
        function clicar2(){
            c.style.color='red'
        }