const formulario = document.getElementById("formulario");
const botonEnviar = document.getElementById("botonEnviar");
const mensajeContainer = document.getElementById("mensaje-container");

formulario.addEventListener("submit", (event) => {
    event.preventDefault();

    botonEnviar.textContent = "Enviando...";
    botonEnviar.disabled = true;

    setTimeout(() => {
        botonEnviar.textContent = "Enviado";
        botonEnviar.disabled = false;

        const mensajeExito = document.createElement("p");
        mensajeExito.textContent = "¡Tu formulario fue enviado exitosamente!";
        mensajeExito.classList.add("mensaje-exito");
        mensajeContainer.appendChild(mensajeExito); // Agrega el mensaje al contenedor
    }, 2000);
});