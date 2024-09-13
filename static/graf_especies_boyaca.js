// Crear el gráfico inicial en el canvas con Chart.js
var ctx = document.getElementById('grafico1').getContext('2d');
var grafico1 = new Chart(ctx, {
    type: 'pie', // Tipo de gráfico: 'pie' (torta)
    data: {
        labels: [], // Etiquetas vacías inicialmente
        datasets: [{
            label: 'Distribución por Categoría',
            data: [], // Datos vacíos inicialmente
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(4, 6, 253, 0.5)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(4, 6, 253, 0.5)'
            ],
            borderWidth: 1
        }]
    }
});

// Función para obtener datos del servidor y actualizar el gráfico
function actualizarGrafico() {
    fetch('/data')  // Solicita los datos al servidor
        .then(response => response.json())
        .then(data => {
            // Actualizar los datos del gráfico
            grafico1.data.labels = data.labels;  // Actualizar las etiquetas
            grafico1.data.datasets[0].data = data.values;  // Actualizar los valores
            grafico1.update();  // Refrescar el gráfico
        });
}

// Llamar a la función actualizarGrafico cada 5 segundos para obtener nuevos datos
setInterval(actualizarGrafico, 5000);