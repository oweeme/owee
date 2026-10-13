/* Calculadora de numeros Owee: lectura, glifos, numeros romanos y operaciones.
   Mismas reglas que Matematicas 2.0: coeficiente + escala (tanu 10, gabu 100, soku 1000, benu 1 000 000),
   las posiciones con 0 no se leen, be (1) si se lee, "doto" es la coma decimal, "po" el signo negativo. */
(function (root) {
  var NOMBRES = ["cho", "be", "du", "ga", "fo", "sa", "ku", "mu", "na", "she"];
  var OPS = { "+": "dapa", "-": "dopo", "−": "dopo", "×": "kebu", "*": "kebu", "÷": "faku", "/": "faku", "=": "se" };

  function leer3(n) {
    var h = Math.floor(n / 100), t = Math.floor(n / 10) % 10, u = n % 10, w = [];
    if (h) w.push(NOMBRES[h] + " gabu");
    if (t) w.push(NOMBRES[t] + " tanu");
    if (u) w.push(NOMBRES[u]);
    return w.join(" ");
  }
  /** Texto numerico ("247", "25.50") -> lectura Owee. Hasta 999 999 999. */
  function leerNum(txt) {
    var p = String(txt).split("."), n = parseInt(p[0], 10), dec = p[1] || "", w = [];
    if (isNaN(n) || n >= 1e9) return null;
    if (n === 0) w.push("cho");
    else {
      var m = Math.floor(n / 1e6), k = Math.floor(n / 1000) % 1000, r = n % 1000;
      if (m) w.push(leer3(m) + " benu");
      if (k) w.push(leer3(k) + " soku");
      if (r) w.push(leer3(r));
    }
    if (dec) w.push("doto " + dec.split("").map(function (d) { return NOMBRES[+d]; }).join(" "));
    return w.join(" ");
  }
  /** Lectura Owee ("du gabu fo tanu mu") -> numero (o null si no es valida). */
  function leerOwee(txt) {
    var t = String(txt).toLowerCase().trim().split(/\s+/).filter(Boolean), neg = false, total = 0, grp = 0, pend = null, dec = null;
    if (!t.length) return null;
    if (t[0] === "po") { neg = true; t.shift(); }
    for (var i = 0; i < t.length; i++) {
      var w = t[i], d = NOMBRES.indexOf(w);
      if (dec !== null) { if (d < 0) return null; dec += d; continue; }
      if (w === "doto") { total += grp + (pend || 0); grp = 0; pend = null; dec = ""; continue; }
      if (d >= 0) { if (pend !== null) return null; pend = d; }
      else if (w === "tanu") { grp += (pend === null ? 1 : pend) * 10; pend = null; }
      else if (w === "gabu") { grp += (pend === null ? 1 : pend) * 100; pend = null; }
      else if (w === "soku") { total += (grp + (pend || 0)) * 1000; grp = 0; pend = null; }
      else if (w === "benu") { total += (grp + (pend || 0)) * 1e6; grp = 0; pend = null; }
      else return null;
    }
    if (dec === null) total += grp + (pend || 0);
    var v = dec !== null && dec !== "" ? parseFloat(total + "." + dec) : total;
    return neg ? -v : v;
  }
  /** Numero -> lectura Owee, con signo (po) y decimales. */
  function leerValor(v) {
    if (!isFinite(v)) return null;
    var neg = v < 0, s = String(Math.abs(+v.toFixed(8)));
    var r = leerNum(s);
    return r === null ? null : (neg ? "po " : "") + r;
  }
  /** Glifos numericos Owee (U+E040..E049) para un texto con cifras. */
  function glifos(txt) { return String(txt).replace(/[0-9]/g, function (d) { return String.fromCharCode(0xE040 + +d); }); }

  var ROM = [[1000, "M"], [900, "CM"], [500, "D"], [400, "CD"], [100, "C"], [90, "XC"], [50, "L"], [40, "XL"], [10, "X"], [9, "IX"], [5, "V"], [4, "IV"], [1, "I"]];
  function aRomano(n) {
    if (!(n >= 1 && n <= 3999) || n !== Math.floor(n)) return null;
    var s = "";
    ROM.forEach(function (p) { while (n >= p[0]) { s += p[1]; n -= p[0]; } });
    return s;
  }
  function deRomano(txt) {
    var s = String(txt).toUpperCase().trim();
    if (!/^[MDCLXVI]+$/.test(s)) return null;
    var v = 0, i = 0;
    ROM.forEach(function (p) { while (s.substr(i, p[1].length) === p[1]) { v += p[0]; i += p[1].length; } });
    return i === s.length && aRomano(v) === s ? v : null;   // solo formas canonicas (IIII no vale)
  }

  /** Evaluador seguro (sin eval): + - x / con prioridad, parentesis, negativo unario, decimales. */
  function evaluar(expr) {
    var toks = String(expr).replace(/\s+/g, "").replace(/−/g, "-").replace(/×/g, "*").replace(/÷/g, "/").match(/\d+\.?\d*|\.\d+|[-+*\/()]/g);
    if (!toks || toks.join("") !== String(expr).replace(/\s+/g, "").replace(/−/g, "-").replace(/×/g, "*").replace(/÷/g, "/")) return NaN;
    var i = 0;
    function prim() {
      var t = toks[i++];
      if (t === "-") return -prim();
      if (t === "+") return prim();
      if (t === "(") { var v = suma(); if (toks[i++] !== ")") throw 0; return v; }
      if (t === undefined || !/^[\d.]/.test(t)) throw 0;
      return parseFloat(t);
    }
    function prod() { var v = prim(); while (toks[i] === "*" || toks[i] === "/") { var o = toks[i++], b = prim(); v = o === "*" ? v * b : v / b; } return v; }
    function suma() { var v = prod(); while (toks[i] === "+" || toks[i] === "-") { var o = toks[i++], b = prod(); v = o === "+" ? v + b : v - b; } return v; }
    try { var r = suma(); return i === toks.length ? r : NaN; } catch (e) { return NaN; }
  }
  /** Expresion -> lectura Owee ("2 + 3" -> "du dapa ga"). */
  function leerExpr(expr) {
    var toks = String(expr).replace(/\s+/g, "").match(/\d+\.?\d*|[-+*\/−×÷=()]/g) || [], out = [], prev = null;
    toks.forEach(function (t) {
      if (/^\d/.test(t)) out.push(leerNum(t));
      else if ((t === "-" || t === "−") && (prev === null || !/^\d|\)/.test(prev))) out.push("po");
      else if (t === "+" && (prev === null || !/^\d|\)/.test(prev))) out.push("pa");
      else if (t === "(" || t === ")") { /* sin lectura */ }
      else out.push(OPS[t]);
      prev = t;
    });
    return out.join(" ");
  }

  var API = { leerNum: leerNum, leerOwee: leerOwee, leerValor: leerValor, glifos: glifos, aRomano: aRomano, deRomano: deRomano, evaluar: evaluar, leerExpr: leerExpr };
  if (typeof module !== "undefined") module.exports = API; else root.OweeCalc = API;
})(typeof window !== "undefined" ? window : this);
