/* owee-i18n.js — selector de idioma Espanol / Owee (romano) / Owee Script para oweeme.com, mibolivia.online y apps web.
 *
 * Requiere (en este orden): qow.js (window.OWEE_DICT), owee.js (window.Owee) y owee.css (fuentes Owee).
 *
 *   <h1 data-i18n="Settings">Configuración</h1>              <!-- clave = texto en ingles de ui_glosario.tsv -->
 *   <button data-i18n="Save">Guardar</button>
 *   <button data-owee-set="es">Español</button> <button data-owee-set="owee">Owee</button> <button data-owee-set="script">Owee Script</button>
 *   <script>OweeI18n.init({ default: "es" })</script>
 *
 * Modos: es (el texto original de la pagina), owee (romano) y script (glifos Owee).
 * El texto SIEMPRE se guarda en romano; los glifos solo se pintan al mostrar.
 */
(function (w) {
  "use strict";
  var KEY = "owee-ui-mode", dict = w.OWEE_DICT || {};
  var original = new WeakMap();

  function setMode(mode) {
    try { localStorage.setItem(KEY, mode); } catch (e) {}
    document.documentElement.lang = mode === "es" ? "es" : "qow";   // qow = codigo de uso privado para Owee
    document.documentElement.dataset.oweeMode = mode;
    document.querySelectorAll("[data-i18n]").forEach(function (el) {
      if (!original.has(el)) original.set(el, el.textContent);
      var e = dict[el.dataset.i18n];
      if (mode === "es" || !e) { el.textContent = original.get(el); el.classList.remove("owee"); el.removeAttribute("title"); return; }
      if (mode === "owee") { el.textContent = e.owee; el.classList.remove("owee"); el.title = e.es; }
      else { el.textContent = w.Owee ? w.Owee.toScript(e.owee, { digits: true }) : e.owee; el.classList.add("owee"); el.title = e.owee + " — " + e.es; }
    });
    document.querySelectorAll("[data-owee-set]").forEach(function (b) {
      b.setAttribute("aria-pressed", b.dataset.oweeSet === mode);
    });
  }

  w.OweeI18n = {
    init: function (opt) {
      var m = (opt && opt.default) || "es";
      try { m = localStorage.getItem(KEY) || m; } catch (e) {}
      document.querySelectorAll("[data-owee-set]").forEach(function (b) { b.addEventListener("click", function () { setMode(b.dataset.oweeSet); }); });
      setMode(m);
    },
    set: setMode,
    /* traducir una clave desde codigo: OweeI18n.t("Save", "script") */
    t: function (key, mode) { var e = dict[key]; if (!e) return key; return mode === "es" ? e.es : mode === "owee" ? e.owee : (w.Owee ? w.Owee.toScript(e.owee) : e.owee); }
  };
})(window);
