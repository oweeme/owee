/* Crear palabras en Owee: comprueba una propuesta con las mismas reglas que 02_Diccionario/datos (generar_ciencias.py,
   verificar_propuestas.py) y la norma de practicidad (lote 20). Funciona en el navegador y en Node (para las pruebas). */
(function (root) {
  var SIL = /(?:sh|ch|[pbtdkgfsmnlr])?[aeou]/g;
  var VALIDA = /^(?:(?:sh|ch|[pbtdkgfsmnlr])?[aeou])+$/;
  var CONS = ["p", "b", "t", "d", "k", "g", "f", "s", "m", "n", "l", "r", "sh", "ch"];

  function silabas(p) { return p.match(SIL) || []; }
  function lev(a, b) {
    var d = [], i, j;
    for (j = 0; j <= b.length; j++) d[j] = j;
    for (i = 1; i <= a.length; i++) {
      var p = d[0]; d[0] = i;
      for (j = 1; j <= b.length; j++) { var t = d[j]; d[j] = Math.min(d[j] + 1, d[j - 1] + 1, p + (a[i - 1] === b[j - 1] ? 0 : 1)); p = t; }
    }
    return d[b.length];
  }
  function sinTildes(s) { return s.normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase(); }
  function glosas(m) {   // «agua / río (curso)» -> ["agua", "río"]
    return m.replace(/\s*\(.*?\)/g, "").split(" / ").map(function (x) { return sinTildes(x.trim().replace(/\/a\b/, "")); }).filter(Boolean);
  }
  function aOwee(w) {    // cómo sonaría una palabra española escrita con letras de Owee (para avisar de parecidos)
    w = sinTildes(w);
    [["qu", "k"], ["gu", "g"], ["ll", "e"], ["ch", "C"], ["c", "k"], ["z", "s"], ["v", "b"], ["j", "k"], ["h", ""], ["y", "e"], ["i", "e"], ["ñ", "n"], ["x", "ks"], ["w", "u"], ["C", "ch"]]
      .forEach(function (r) { w = w.split(r[0]).join(r[1]); });
    return w.replace(/[^a-z]/g, "");
  }
  function raices(LEX) { return Object.keys(LEX).filter(function (w) { return w.indexOf("-") < 0 && VALIDA.test(w); }); }

  function analizar(forma, significado, LEX) {
    var r = { errores: [], avisos: [], bien: [], silabas: 0, partes: [], tipo: "" };
    forma = (forma || "").trim().toLowerCase(); significado = (significado || "").trim();
    if (!forma) { r.errores.push("Escribe la palabra en romano (por ejemplo «nelo-kopa»)."); return r; }
    var partes = forma.split("-"); r.partes = partes;
    r.tipo = partes.length > 1 ? "compuesto" : "raíz";
    partes.forEach(function (p) {
      if (!p) r.errores.push("Hay un guion de más.");
      else if (!VALIDA.test(p)) r.errores.push("«" + p + "» no es Owee válido: solo vocales a e o u y consonantes p b t d k g f s m n l r sh ch, en sílabas V o CV (sin «i» ni consonante al final).");
    });
    if (r.errores.length) return r;
    r.silabas = partes.reduce(function (n, p) { return n + silabas(p).length; }, 0);
    if (LEX[forma]) { r.errores.push("«" + forma + "» ya existe: " + LEX[forma][0] + "."); return r; }
    if (partes.length > 3) r.errores.push("Un compuesto tiene como máximo 3 elementos.");
    if (r.tipo === "compuesto") {
      partes.forEach(function (p) {
        if (!LEX[p]) r.errores.push("La parte «" + p + "» no existe en el diccionario: propónla primero como raíz, o usa una raíz que exista.");
      });
      if (r.silabas > 6) r.errores.push("Tiene " + r.silabas + " sílabas: demasiado larga. Busca una construcción de 2 elementos.");
      else if (r.silabas > 5) r.avisos.push("Tiene " + r.silabas + " sílabas: aceptable para algo técnico o poco frecuente, larga para algo de cada día.");
      else r.bien.push("Compuesto de " + partes.length + " elementos y " + r.silabas + " sílabas: práctico.");
      if (!r.errores.length) r.bien.push("Se lee: " + partes.map(function (p) { return p + " (" + LEX[p][0].split(" (")[0] + ")"; }).join(" + ") + ".");
    } else {
      var n = r.silabas, rs = raices(LEX);
      if (n < 2) r.errores.push("Las raíces de 1 sílaba están reservadas a operadores y números (pa, no, be…).");
      else if (n > 3) r.errores.push("Una raíz tiene 2 o 3 sílabas; para ideas más largas une raíces con guion.");
      else {
        var cerca = rs.filter(function (x) { return silabas(x).length === n && lev(forma, x) < 2; });
        cerca.forEach(function (x) { r.errores.push("Suena casi igual que «" + x + "» (" + LEX[x][0] + "): a una sola letra. Elige otra."); });
        if (n === 2) {
          var s = silabas(forma), inv = s[0].slice(0, -1) + s[1].slice(-1) + s[1].slice(0, -1) + s[0].slice(-1);
          if (inv !== forma && LEX[inv] && rs.indexOf(inv) >= 0) r.errores.push("Con las vocales cambiadas es «" + inv + "» (" + LEX[inv][0] + ").");
          if (!cerca.length) r.avisos.push("Raíz de 2 sílabas: casi no quedan libres; están reservadas para lo más frecuente.");
        }
        var ss = silabas(forma);
        if (ss.filter(function (x) { return x.slice(0, 2) === "sh" || x.slice(0, 2) === "ch"; }).length > 1) r.avisos.push("Tiene más de un sh/ch: difícil de pronunciar rápido.");
        if (!r.errores.length) r.bien.push("Raíz nueva de " + n + " sílabas, sin vecinos que se confundan.");
      }
      if (significado) glosas(significado).forEach(function (g) {
        g.split(/\s+/).forEach(function (w) {
          var o = aOwee(w);
          if (o.length >= 3 && lev(forma, o) <= Math.max(1, Math.floor(o.length / 3))) r.avisos.push("Se parece a la palabra «" + w + "»: Owee prefiere formas propias, que no copien otra lengua (salvo nombres propios).");
        });
      });
    }
    if (significado) {
      var gs = glosas(significado), igual = [];
      Object.keys(LEX).forEach(function (w) {
        if (w === forma) return;
        if (glosas(LEX[w][0]).some(function (x) { return gs.indexOf(x) >= 0; })) igual.push(w);
      });
      igual.forEach(function (w) { r.errores.push("Ya hay una palabra con ese significado: «" + w + "» (" + LEX[w][0] + "). Una forma = un significado."); });
    } else r.avisos.push("Escribe también el significado: así se comprueba que no exista ya.");
    return r;
  }

  function buscar(texto, LEX, max) {   // raíces y compuestos cuyo significado contiene el texto
    var q = sinTildes(texto || "").trim(); if (q.length < 2) return [];
    var out = [];
    Object.keys(LEX).forEach(function (w) {
      var palabras = sinTildes(LEX[w][0]).split(/[^a-zñ]+/);
      if (palabras.some(function (x) { return x.indexOf(q) === 0; })) out.push(w);
    });
    out.sort(function (a, b) { return (a.indexOf("-") >= 0) - (b.indexOf("-") >= 0) || a.length - b.length; });
    return out.slice(0, max || 12);
  }

  function sugerirRaices(LEX, cantidad, azar) {   // raíces libres de 3 sílabas que cumplen la norma
    azar = azar || Math.random;
    var rs = raices(LEX).filter(function (x) { return silabas(x).length === 3; }), out = [], intentos = 0;
    var SY = []; CONS.forEach(function (c) { "aeou".split("").forEach(function (v) { SY.push(c + v); }); });
    while (out.length < (cantidad || 5) && intentos++ < 20000) {
      var s = [0, 1, 2].map(function () { return SY[Math.floor(azar() * SY.length)]; });
      var c = s.map(function (x) { return x.slice(0, -1); });
      if (c[0] === c[1] || c[1] === c[2] || s[0] === s[1] || s[1] === s[2]) continue;
      if (c.filter(function (x) { return x === "sh" || x === "ch"; }).length > 1) continue;
      var w = s.join("");
      if (LEX[w] || out.indexOf(w) >= 0) continue;
      if (rs.concat(out).some(function (x) { return lev(w, x) < 2; })) continue;
      out.push(w);
    }
    return out;
  }

  var api = { analizar: analizar, buscar: buscar, sugerirRaices: sugerirRaices, silabas: silabas, lev: lev };
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.OweeCrear = api;
})(typeof window !== "undefined" ? window : this);
