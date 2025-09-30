// core/static/core/js/script.js

// Validación cliente y envío POST
function validateAndSubmit(e){
    e.preventDefault();
    const nombre = document.getElementById('nombre').value.trim();
    const correo = document.getElementById('correo').value.trim();
    const mensaje = document.getElementById('mensaje').value.trim();

    if(!nombre || !correo || !mensaje){
      alert('Completa nombre, correo y mensaje.');
      return false;
    }

    // simple email regex
    const emailRe = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if(!emailRe.test(correo)){
      alert('Ingresa un correo válido.');
      return false;
    }

    // push event for GTM
    if(window.dataLayer){
      dataLayer.push({event: 'contact_form_submit', form_name: 'contactame'});
    }

    document.getElementById('contactForm').submit();
}
