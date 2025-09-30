// core/static/core/js/faq.js
document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('.faq-question').forEach(function(q){
    var answer = document.getElementById(q.getAttribute('aria-controls'));
    if (!answer) return;
    // estado inicial
    answer.style.maxHeight = '0px';
    q.setAttribute('aria-expanded','false');
    answer.setAttribute('aria-hidden','true');

    function toggle(){
      var open = q.getAttribute('aria-expanded') === 'true';
      if(open){
        // cerrar
        answer.style.maxHeight = answer.scrollHeight + 'px';
        requestAnimationFrame(function(){ answer.style.maxHeight = '0px'; });
        q.setAttribute('aria-expanded','false');
        answer.setAttribute('aria-hidden','true');
        answer.classList.remove('open');
      } else {
        // abrir
        answer.classList.add('open');
        answer.style.maxHeight = answer.scrollHeight + '5px';
        q.setAttribute('aria-expanded','true');
        answer.setAttribute('aria-hidden','false');
      }
    }

    q.addEventListener('click', toggle);
    q.addEventListener('keydown', function(e){
      if(e.key === 'Enter' || e.key === ' '){ e.preventDefault(); toggle(); }
    });
  });
});

