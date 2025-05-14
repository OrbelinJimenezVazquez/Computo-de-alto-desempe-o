document.addEventListener("DOMContentLoaded", function () {
  const chartCtx = document.getElementById("chart").getContext("2d");

  // Cargar datos desde el archivo CSV
  fetch("data/GOOG.csv")
    .then((response) => {
      if (!response.ok) {
        throw new Error(`Error HTTP! Estado: ${response.status}`);
      }
      return response.text();
    })
    .then((text) => {
      // Convertir el CSV a un arreglo de objetos
      const data = csvToArray(text);

      // Procesar los datos para la visualización
      return processData(data);
    })
    .then((chartData) => {
      createChart(chartData, chartCtx);
    })
    .catch((error) => {
      console.error("Error cargando datos:", error);
      document.querySelector(
        ".chart-container"
      ).innerHTML = `<div class="error-message">
          <h3>Error al cargar los datos</h3>
          <p>${error.message}</p>
          <p>Ruta intentada: data/GOOG.csv</p>
        </div>`;
    });
});

function csvToArray(csv) {
  const lines = csv.trim().split("\n");
  const headers = lines[0].split(",");
  return lines.slice(1).map((line) => {
    const values = line.split(",");
    let obj = {};
    headers.forEach((header, i) => {
      obj[header] = values[i];
    });
    return obj;
  });
}

function processData(data) {
  // Extraer las fechas y precios de cierre (Close) y apertura (Open)
  const dates = data.map((item) => item.Date);
  const opens = data.map((item) => parseFloat(item.Open));
  const closes = data.map((item) => parseFloat(item.Close));

  return {
    dates: dates,
    opens: opens,
    closes: closes,
  };
}

function createChart(data, ctx) {
  const openColor = "rgba(165, 0, 68, 0.8)"; // Color para precio de apertura
  const closeColor = "rgba(0, 77, 152, 0.8)"; // Color para precio de cierre

  new Chart(ctx, {
    type: "line",
    data: {
      labels: data.dates,
      datasets: [
        {
          label: "Apertura",
          data: data.opens,
          backgroundColor: openColor,
          borderColor: openColor.replace("0.8", "1"),
          borderWidth: 1,
        },
        {
          label: "Cierre",
          data: data.closes,
          backgroundColor: closeColor,
          borderColor: closeColor.replace("0.8", "1"),
          borderWidth: 1,
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        title: {
          display: true,
          text: "Precio de las acciones de Google (GOOG)",
          font: {
            size: 18,
            weight: "bold",
          },
          padding: {
            top: 10,
            bottom: 20,
          },
        },
        legend: {
          position: "top",
        },
        tooltip: {
          callbacks: {
            afterLabel: function (context) {
              const index = context.dataIndex;
              const datasetLabel = context.dataset.label;

              if (datasetLabel === "Apertura") {
                return `Apertura: $${data.opens[index].toFixed(2)}`;
              } else {
                return `Cierre: $${data.closes[index].toFixed(2)}`;
              }
            },
          },
        },
      },
      scales: {
        y: {
          beginAtZero: false,
          title: {
            display: true,
            text: "Precio (USD)",
          },
          grid: {
            display: true,
            color: "rgba(0, 0, 0, 0.05)",
          },
        },
        x: {
          title: {
            display: true,
            text: "Fecha",
          },
          grid: {
            display: false,
          },
        },
      },
    },
  });
}
