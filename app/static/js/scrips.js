// Función para búsqueda de cursos
document.addEventListener('DOMContentLoaded', function() {
    const busquedaInput = document.getElementById('busquedaInput');
    if (busquedaInput) {
        busquedaInput.addEventListener('keyup', function() {
            const termino = busquedaInput.value.toLowerCase();
            const cursoCards = document.querySelectorAll('.curso-card');
            let encontrado = false;

            cursoCards.forEach(function(card) {
                const titulo = card.querySelector('.curso-titulo').textContent.toLowerCase();
                const descripcion = card.querySelector('.curso-descripcion').textContent.toLowerCase();

                if (titulo.includes(termino) || descripcion.includes(termino)) {
                    card.style.display = 'block';
                    encontrado = true;
                } else {
                    card.style.display = 'none';
                }
            });

            const noResultados = document.getElementById('sinResultados');
            if (noResultados) {
                noResultados.style.display = encontrado ? 'none' : 'block';
            }
        });
    }
});