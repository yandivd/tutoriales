const app = new Vue({
    el: '#app',
    data: {
        titulo: 'Hello World Vue',
        frutas: [
            {nombre: 'Pera', cantidad: 10},
            {nombre: 'Manzana', cantidad: 0},
            {nombre: 'Uva', cantidad: 11}
        ],
        nuevaFruta: '',
        nuevaCant: 0,
        total: 0
    },
    methods:{
        agregrarFruta(){
            this.frutas.push({
                nombre: this.nuevaFruta, cantidad: this.nuevaCant
            });
            this.nuevaFruta = '';
            this.nuevaCant = 0;
        }
    },
    computed:{
        sumarFrutas(){
            this.total = 0;
            for (fruta of this.frutas){
                this.total += fruta.cantidad
            }
            return this.total;
        }
    }
})
