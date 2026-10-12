/* owee.js — Roman Owee <-> Owee Script (PUA) · Owee Glyph Master 3.3
 *
 * Mismas reglas que el IME Fcitx5:
 *  - minúsculas; sh/ch se leen antes que las consonantes simples;
 *  - sólo V o CV; la i no existe;
 *  - una palabra imposible se deja en roman (no se pierde texto);
 *  - espacios, guiones y puntuación se conservan;
 *  - opcional: cifras 0-9 -> dígitos Owee U+E040..U+E049.
 *
 * Uso:  Owee.toScript("me suna nume 2026", {digits: true})
 *       Owee.toRoman(" ...")
 *       Owee.syllables("meka")  -> ["me","ka"]
 */
(function (root) {
  "use strict";
  var VOWELS = ["a", "e", "o", "u"];
  var CONS = ["p", "b", "t", "d", "k", "g", "f", "s", "m", "n", "l", "r", "sh", "ch"];
  var DIGIT_READING = ["cho", "be", "du", "ga", "fo", "sa", "ku", "mu", "na", "she"];

  var units = [];            // {roman, id, cp, kind}
  var byRoman = {};
  var byChar = {};
  var cp = 0xE000;
  VOWELS.forEach(function (v) { add(v, "vowel"); });
  CONS.forEach(function (c) { VOWELS.forEach(function (v) { add(c + v, "syllable"); }); });
  for (var d = 0; d < 10; d++) {
    var u = { roman: String(d), id: "OWEE_DIGIT_" + d, cp: 0xE040 + d, kind: "digit", reading: DIGIT_READING[d] };
    u.char = String.fromCharCode(u.cp);
    units.push(u); byChar[u.char] = u;
  }

  var JOIN = String.fromCharCode(0xE03C), NAME = String.fromCharCode(0xE03D);   // nexo de compuesto, marca de nombre propio
  byChar[JOIN] = { roman: "-", id: "OWEE_MARK_JOIN", cp: 0xE03C, kind: "mark", char: JOIN };
  byChar[NAME] = { roman: "^", id: "OWEE_MARK_NAME", cp: 0xE03D, kind: "mark", char: NAME };

  function add(roman, kind) {
    var u = { roman: roman, id: "OWEE_SYL_" + roman.toUpperCase(), cp: cp, kind: kind };
    u.char = String.fromCharCode(cp);
    units.push(u); byRoman[roman] = u; byChar[u.char] = u;
    cp++;
  }

  function isVowel(c) { return c === "a" || c === "e" || c === "o" || c === "u"; }

  /** Divide una palabra roman en sílabas Owee; null si no es válida. */
  function syllables(word) {
    var w = word.toLowerCase(), out = [], i = 0;
    while (i < w.length) {
      var c = w[i];
      if (isVowel(c)) { out.push(c); i++; continue; }
      var cons = null;
      if ((c === "s" || c === "c") && w[i + 1] === "h") cons = c + "h";
      else if (CONS.indexOf(c) >= 0) cons = c;
      if (!cons) return null;
      var v = w[i + cons.length];
      if (!v || !isVowel(v)) return null;
      out.push(cons + v); i += cons.length + 1;
    }
    return out.length ? out : null;
  }

  function wordToScript(word) {
    var s = syllables(word);
    if (!s) return null;
    return s.map(function (x) { return byRoman[x].char; }).join("");
  }

  /** Convierte texto roman a Owee Script conservando todo lo demás.
   *  - guion entre dos palabras Owee válidas -> nexo de compuesto U+E03C (sade-kelo);
   *  - palabra con inicial mayúscula (nombre propio) -> marca U+E03D + la palabra (Ana). */
  function toScript(text, opts) {
    var digits = opts && opts.digits;
    return text.replace(/[A-Za-z]+(?:-[A-Za-z]+)*|[0-9]/g, function (tok) {
      if (/[0-9]/.test(tok)) return digits ? String.fromCharCode(0xE040 + Number(tok)) : tok;
      var name = /^[A-Z][a-z]*$/.test(tok.split("-")[0]) && tok.split("-")[0].length > 0;
      var parts = tok.split("-"), conv = parts.map(function (p) { return wordToScript(p); });
      var out = conv.every(function (c) { return c !== null; })
        ? conv.join(JOIN)
        : parts.map(function (p, i) { return conv[i] === null ? p : conv[i]; }).join("-");
      return (name && conv[0] !== null ? NAME : "") + out;
    });
  }

  /** Convierte Owee Script (PUA) de vuelta a roman. Los dígitos vuelven a 0-9. */
  function toRoman(text) {
    var out = "", cap = false;
    for (var i = 0; i < text.length; i++) {
      var u = byChar[text[i]];
      if (u && u.kind === "mark" && u.roman === "^") { cap = true; continue; }
      var r = u ? u.roman : text[i];
      if (cap && u) { r = r.charAt(0).toUpperCase() + r.slice(1); cap = false; }
      out += r;
    }
    return out;
  }

  /** Palabras roman que no se pudieron convertir (para avisar al usuario). */
  function invalidWords(text) {
    var bad = [];
    (text.match(/[A-Za-z]+/g) || []).forEach(function (w) {
      if (!syllables(w) && bad.indexOf(w) < 0) bad.push(w);
    });
    return bad;
  }

  root.Owee = {
    version: "3.3",
    units: units,
    syllables: syllables,
    toScript: toScript,
    toRoman: toRoman,
    invalidWords: invalidWords,
    unit: function (x) { return byRoman[x] || byChar[x] || null; }
  };
})(typeof window !== "undefined" ? window : globalThis);
