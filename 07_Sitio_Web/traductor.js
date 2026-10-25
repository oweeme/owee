/* Traductor asistido Owee <-> espanol (prototipo). Funciona en el navegador y en Node.
 * Owee -> espanol: analiza palabra por palabra (separa compuestos, marcas de tiempo, negacion y pregunta) y propone
 *                  una lectura aproximada. ES -> Owee: busca cada palabra en el diccionario y propone la forma.
 * Es un traductor GLOSADO (traduccion asistida), no un traductor automatico perfecto: el contexto lo pone la persona. */
(function (root) {
  "use strict";
  var LEX = root.OWEE_LEX || {};            // forma -> [significado, pronunciacion]
  var norm = function (s) { return s.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "").trim(); };
  var PRON = { me: "yo", tu: "tú", ra: "él/ella", mene: "nosotros", tune: "ustedes", rane: "ellos/ellas", ne: "(plural humano)" };
  var TIEMPO = { pe: "pasado", te: "presente", pu: "futuro" };
  var PREP = { bo: "en", ba: "fuera de", to: "hacia", de: "desde", go: "arriba", gu: "abajo", le: "cerca", lu: "lejos", ko: "con", so: "sin", re: "y", lo: "o", ke: "si", balo: "pero", kasu: "porque" };

  function primero(m) { return m.replace(/\s*\(.*?\)/g, "").split(" / ")[0].trim(); }
  var VERBALES = ["nume","moke","pode","pelo","pume","sule","pema","gura","delo","fena","bure","kose","kade","dare","galo","daro","tase","fela","duma","lore","lare","rena","karo","reka","kera","fedo","rude","telo","mede","beka","lodu","dune"];
  function esVerbo(t) {
    if (VERBALES.indexOf(t) >= 0) return true;
    if (typeof VERB_EN_OVR !== "undefined" && VERB_EN_OVR[t]) return true;
    var ps = t.split("-"); var u = ps[ps.length - 1];
    var cl = LEX[t] && LEX[t][2] ? LEX[t][2] : "";
    return /acci[oó]n|modalidad/.test(cl) || (ps.length > 1 && VERBALES.indexOf(u) >= 0 && ["duma","kera","fedo","telo","pume"].indexOf(u) >= 0);
  }
  function glosa(w) {
    w = w.toLowerCase();
    if (PRON[w]) return PRON[w];
    if (w === "mora") return "estar / existir";
    if (LEX[w]) return primero(LEX[w][0]);
    if (w.indexOf("-") > 0) { var ps = w.split("-"), g = ps.map(function (p) { return LEX[p] ? primero(LEX[p][0]) : "?"; }); return g.join(" + ") + "  (compuesto)"; }
    return null;
  }

  function owee2es(texto) {
    var frases = texto.split(/[.!?¿¡\n]+/).map(function (s) { return s.trim(); }).filter(Boolean);
    return frases.map(function (fr) {
      var toks = fr.toLowerCase().match(/[a-z]+(?:-[a-z]+)*/g) || [];
      var preg = toks[toks.length - 1] === "ka"; if (preg) toks.pop();
      var tiempo = null, neg = false, partes = [];
      toks.forEach(function (t) {
        if (TIEMPO[t]) { tiempo = TIEMPO[t]; return; }
        if (t === "no") { neg = true; partes.push({ t: t, g: "no" }); return; }
        partes.push({ t: t, g: PREP[t] || glosa(t), prep: !!PREP[t] });
      });
      var pal = partes.map(function (p) { return { owee: p.t, es: p.g || "(no está en el diccionario)", ok: !!p.g }; });
      var lit = partes.map(function (p) { return p.g || "?"; });
      // orden SOV -> SVO: si el ultimo elemento es un verbo, pasa justo despues del sujeto
      var ult = partes.length ? partes[partes.length - 1] : null, svo = lit.slice();
      if (ult && !ult.prep && esVerbo(ult.t) && partes.length > 1) {
        var v = svo.pop(), sujN = (PRON[partes[0].t] || partes[0].t === "no") ? 1 : 1;
        var ins = []; if (neg) { svo = svo.filter(function (x, i) { return partes[i].t !== "no"; }); ins.push("no"); }
        if (tiempo && tiempo !== "presente") ins.push("[" + tiempo + "]");
        ins.push(v);
        svo.splice(sujN, 0, ins.join(" "));
      } else if (tiempo && tiempo !== "presente") svo.splice(Math.max(0, svo.length - 1), 0, "[" + tiempo + "]");
      var PREPS = ["en", "fuera de", "hacia", "desde", "arriba", "abajo", "cerca", "lejos", "con", "sin"];
      for (var u = 0; u < svo.length - 1; u++) if (PREPS.indexOf(svo[u + 1]) >= 0 && svo[u + 1].indexOf(" ") < 0 && ["yo", "tú"].indexOf(svo[u]) < 0) { var t2 = svo[u]; svo[u] = svo[u + 1]; svo[u + 1] = t2; u++; }
      var aprox = (preg ? "¿" : "") + svo.join(" ") + (preg ? "?" : "");
      return { frase: fr, palabras: pal, aproximada: aprox, pregunta: preg, tiempo: tiempo, negacion: neg };
    });
  }

  // espanol -> owee
  var INDICE = null;
  function indice() {
    if (INDICE) return INDICE; INDICE = {};
    Object.keys(LEX).forEach(function (f) {
      var m = LEX[f][0].replace(/\s*\(.*?\)/g, "");
      m.split(/\s*\/\s*| o /).forEach(function (v) {
        v = norm(v); if (!v) return;
        (INDICE[v] = INDICE[v] || []).push(f);
        v.split(/\s+/).forEach(function () {});
      });
    });
    return INDICE;
  }
  var FUNC = { a: "to", y: "re", o: "lo", si: "ke", con: "ko", sin: "so", en: "bo", hacia: "to", desde: "de", cerca: "le", lejos: "lu", pero: "balo", porque: "kasu",
               no: "no", yo: "me", tu: "tu", el: "ra", ella: "ra", nosotros: "mene", ustedes: "tune", ellos: "rane", ellas: "rane", que: "ka-kema", quien: "ka-nara",
               donde: "ka-kore", cuando: "ka-tera", como: "ka-mode", cuanto: "ka-bema", si_: "tare", hoy: "te-fusu", ayer: "pe-fusu", manana: "pu-fusu" };
  var VERBOS = { querer: "nume", necesitar: "moke", poder: "pode", deber: "pelo", comer: "pume", beber: "nobe pume", dormir: "sule", ver: "luma-salo", oir: "luma-sone",
    hablar: "reka", decir: "reka", saber: "lare", pensar: "rena", entender: "karo", dar: "pema", recibir: "gura", tomar: "delo", poner: "fena", abrir: "bure", cerrar: "kose",
    usar: "kade", hacer: "dare", ayudar: "galo", trabajar: "daro", aprender: "tase", ensenar: "fela", caminar: "kalu-duma", ir: "duma", venir: "duma", mover: "duma", vivir: "suma",
    amar: "lore", comprar: "kera-fedo", vender: "pema-fedo", pagar: "fedo", buscar: "kera-nume", encontrar: "kera", obtener: "kera", jugar: "lena-duma", cantar: "sabe-sone",
    llorar: "loke-suna", reir: "sabe-lena", esperar: "pu-dure", cocinar: "pore-dare", morir: "suma-gune", romper: "bosa", reparar: "rude", cambiar: "telo", medir: "mede",
    escribir: "beka", leer: "lodu", sentir: "dune", estar: "mora", existir: "mora", haber: "mora", tener: "pase", ser: "gade" };
  var FORMAS_IRREG = { quiero: "querer", quieres: "querer", quiere: "querer", quieren: "querer", puedo: "poder", puedes: "poder", puede: "poder", voy: "ir", vas: "ir", va: "ir",
    vamos: "ir", van: "ir", fui: "ir", soy: "ser", eres: "ser", es: "ser", somos: "ser", son: "ser", estoy: "estar", estas: "estar", esta: "estar", hay: "haber", tengo: "tener",
    tienes: "tener", tiene: "tener", hago: "hacer", hizo: "hacer", doy: "dar", das: "dar", veo: "ver", ves: "ver", vio: "ver", se: "saber", sabe: "saber", digo: "decir",
    dice: "decir", duermo: "dormir", duermes: "dormir", duerme: "dormir", vengo: "venir", viene: "venir", pienso: "pensar", piensa: "pensar", entiendo: "entender", pido: "pedir" };
  var SINON = { nino: "naku", nina: "naku", hijo: "naku", hija: "naku", padre: "pade", madre: "pade", amigo: "reme", amiga: "reme", persona: "nara", gente: "naro", hombre: "nara", mujer: "nara",
    casa: "kuma", hogar: "kuma", ciudad: "kuma-seta", comida: "fame", bebida: "nobe", fruta: "nelo-fame", libro: "beka kema", dinero: "bado-feke", tiempo: "tera", dia: "fusu",
    noche: "kuna-bore", sol: "sade", luna: "mune", estrella: "sade-lu", cielo: "kuna", tierra: "taro", fuego: "pore", aire: "sura", rio: "suna-duma", mar: "suna-gore-pa", arbol: "nelo-gore-pa",
    grande: "gore-pa", pequeno: "gore-po", caliente: "fure-pa", frio: "fure-po", rapido: "sape-pa", lento: "sape-po", bueno: "lafe", nuevo: "tame", viejo: "gule", si: "tare" };
  function lema(w) {
    if (FORMAS_IRREG[w]) return FORMAS_IRREG[w];
    if (VERBOS[w]) return w;
    var base = w.replace(/(aron|ieron|aste|iste|amos|emos|imos|ando|iendo|aba|ia|o|as|es|an|en|a|e|i|io)$/, "");
    var cands = Object.keys(VERBOS).filter(function (v) { return v.indexOf(base) === 0 && base.length >= 3; });
    return cands.length ? cands[0] : null;
  }
  function tiempoDe(w) {
    if (/(aron|ieron|aste|iste|aba|ia|fui|hizo|vio)$/.test(w) || (/(i|io)$/.test(w) && lema(w))) return "pe";
    if (/(are|ere|ire|aras|eras|iras|ara|era|ira|aremos|eremos|iremos|aran|eran|iran)$/.test(w) && w.length > 5) return "pu";
    return null;
  }
  function es2owee(texto) {
    var frases = texto.split(/[.!?¿¡\n]+/).map(function (s) { return s.trim(); }).filter(Boolean), I = indice();
    return frases.map(function (fr) {
      var pal = (norm(fr).match(/[a-zñ]+/g) || []), out = [], det = [], tiempo = null;
      pal.forEach(function (w) {
        if (["la", "los", "las", "un", "una", "unos", "unas", "del", "al", "lo"].indexOf(w) >= 0) { det.push({ es: w, owee: "(sin equivalente: Owee no usa artículos)", ok: true }); return; }
        if (FUNC[w]) { out.push(FUNC[w]); det.push({ es: w, owee: FUNC[w], ok: true }); return; }
        var l = lema(w);
        if (l) { var t = tiempoDe(w); if (t) tiempo = t; out.push(VERBOS[l]); det.push({ es: w, owee: VERBOS[l] + (t ? " (" + (t === "pe" ? "pasado" : "futuro") + ")" : ""), ok: true }); return; }
        var s = w.replace(/(es|s)$/, "");
        if (SINON[w]) { out.push(SINON[w]); det.push({ es: w, owee: SINON[w], ok: true }); return; }
        var c = I[w] || I[s] || I[w.replace(/(a|o)$/, "")] || null;
        if (c) { out.push(c[0]); det.push({ es: w, owee: c.slice(0, 3).join(" · "), ok: true }); return; }
        det.push({ es: w, owee: "(no encontrada)", ok: false });
      });
      // orden SOV: sujeto/objetos primero y el verbo (ultimo concepto verbal) al final
      var POSP = ["bo", "ba", "to", "de", "go", "gu", "le", "lu", "ko", "so"], sug = out.slice();
      for (var q = 0; q < sug.length - 1; q++) if (POSP.indexOf(sug[q]) >= 0) { var tmp = sug[q]; sug[q] = sug[q + 1]; sug[q + 1] = tmp; q++; }
      var iv = -1; pal.forEach(function (w, i) { if (lema(w)) iv = i; });
      var ADV = ["pe-fusu", "pu-fusu", "te-fusu"];
      if (tiempo && !sug.some(function (x) { return ADV.indexOf(x) >= 0; })) { var k = sug.length - 1; var pos = out.indexOf(VERBOS[lema(pal[iv] || "")]); if (pos >= 0) sug.splice(pos, 0, tiempo); }
      var verbo = iv >= 0 ? VERBOS[lema(pal[iv])] : null;
      if (verbo) { var j = sug.indexOf(verbo); if (j >= 0 && j !== sug.length - 1) { sug.splice(j, 1); sug.push(verbo); } }
      return { frase: fr, palabras: det, sugerencia: sug.join(" ") };
    });
  }
  root.OweeTraductor = { owee2es: owee2es, es2owee: es2owee };
  // ------------------------------------------------------------------ ingles (por pivote: el ingles de cada forma sale de su significado en espanol)
  var PRON_EN = { me: "I", tu: "you", ra: "he/she", mene: "we", tune: "you (all)", rane: "they", ne: "(plural)" };
  var PREP_EN = { bo: "in", ba: "outside", to: "to", de: "from", go: "up", gu: "down", le: "near", lu: "far", ko: "with", so: "without", re: "and", lo: "or", ke: "if", balo: "but", kasu: "because" };
  var IRREG_PAST = { eat: "ate", drink: "drank", give: "gave", take: "took", see: "saw", hear: "heard", know: "knew", go: "went", make: "made", put: "put", get: "got", say: "said", sleep: "slept",
    think: "thought", sing: "sang", buy: "bought", sell: "sold", break: "broke", feel: "felt", hold: "held", leave: "left", teach: "taught", understand: "understood", speak: "spoke", find: "found",
    pay: "paid", write: "wrote", read: "read", come: "came", be: "was", have: "had", do: "did", run: "ran", sit: "sat", stand: "stood", lie: "lay", bite: "bit", cry: "cried", learn: "learned" };
  var VERB_EN_OVR = { duma: "move", nume: "want", moke: "need", lodu: "read", beka: "write", reka: "say", lare: "know", rena: "think", karo: "understand", daro: "work", galo: "help", dare: "make",
    telo: "change", suma: "live", lore: "love", fedo: "pay", kera: "get", mede: "measure", dune: "feel", pema: "give", gura: "receive", delo: "take", fena: "put", bure: "open", kose: "close",
    kade: "use", tase: "learn", fela: "teach", sule: "sleep", pume: "eat", pode: "can", pelo: "must", "kalu-duma": "walk", "pore-dare": "cook", "kera-fedo": "buy", "pema-fedo": "sell" };
  function enGlosa(w) { w = w.toLowerCase(); if (PRON_EN[w]) return PRON_EN[w]; if (PREP_EN[w]) return PREP_EN[w]; if (w === "mora") return "be"; if (LEX[w] && LEX[w][3]) return LEX[w][3].split(" / ")[0];
    if (w.indexOf("-") > 0) { var g = w.split("-").map(function (p) { return LEX[p] && LEX[p][3] ? LEX[p][3].split(" / ")[0] : "?"; }); return g.join(" ") + "  (compound)"; } return null; }
  function pastOf(v) { if (IRREG_PAST[v]) return IRREG_PAST[v]; if (/e$/.test(v)) return v + "d"; if (/[^aeiou]y$/.test(v)) return v.slice(0, -1) + "ied"; return v + "ed"; }
  function thirdOf(v) { if (/(s|x|z|ch|sh|o)$/.test(v)) return v + "es"; if (/[^aeiou]y$/.test(v)) return v.slice(0, -1) + "ies"; return v + "s"; }
  function owee2en(texto) {
    var frases = texto.split(/[.!?¿¡\n]+/).map(function (x) { return x.trim(); }).filter(Boolean);
    return frases.map(function (fr) {
      var toks = fr.toLowerCase().match(/[a-z]+(?:-[a-z]+)*/g) || [], preg = toks[toks.length - 1] === "ka"; if (preg) toks.pop();
      var tiempo = "presente", neg = false, partes = [];
      toks.forEach(function (t) { if (TIEMPO[t]) { tiempo = TIEMPO[t]; return; } if (t === "no") { neg = true; return; } if (t === "mora" && toks.length > 1) return; partes.push({ t: t, g: enGlosa(t), prep: !!PREP_EN[t] }); });
      var pal = partes.map(function (p) { return { owee: p.t, es: p.g || "(not in the dictionary)", ok: !!p.g }; });
      var iv = -1; for (var i = partes.length - 1; i >= 0; i--) { if (!partes[i].prep && esVerbo(partes[i].t)) { iv = i; break; } }
      var sujeto = partes.length ? partes[0] : null, resto = [], i2;
      var subj = sujeto && (PRON_EN[sujeto.t] || iv !== 0) ? (sujeto.g || "?") : "";
      for (i2 = (subj ? 1 : 0); i2 < partes.length; i2++) if (i2 !== iv) resto.push(partes[i2].g || "?");
      for (var q = 0; q < resto.length - 1; q++) if (Object.keys(PREP_EN).some(function (k) { return PREP_EN[k] === resto[q + 1]; }) && ["I", "you"].indexOf(resto[q]) < 0) { var tm = resto[q]; resto[q] = resto[q + 1]; resto[q + 1] = tm; q++; }
      var plural = ["I", "you", "we", "they", "you (all)"].indexOf(subj) >= 0, out;
      if (iv >= 0) {
        var v = (VERB_EN_OVR[partes[iv].t] || partes[iv].g || "?").replace(/^to /, ""), aux = "", main = v;
        if (tiempo === "futuro") { aux = neg ? "will not" : "will"; }
        else if (tiempo === "pasado") { if (neg) { aux = "did not"; } else main = pastOf(v); }
        else { if (neg) aux = plural ? "do not" : "does not"; else main = plural || subj === "" ? v : thirdOf(v); }
        if (preg) { var d = tiempo === "futuro" ? "will" : tiempo === "pasado" ? "did" : (plural ? "do" : "does"); out = [d, subj, neg ? "not" : "", v].filter(Boolean).concat(resto); }
        else out = [subj, aux, main].filter(Boolean).concat(resto);
      } else {
        var be = tiempo === "pasado" ? (subj === "I" || !plural ? "was" : "were") : tiempo === "futuro" ? "will be" : (subj === "I" ? "am" : plural ? "are" : "is");
        out = preg ? [be.split(" ")[0] === "will" ? "will" : be, subj].concat(resto) : [subj, be + (neg ? " not" : "")].filter(Boolean).concat(resto);
        if (subj === "" && resto.length) out = resto;
      }
      return { frase: fr, palabras: pal, aproximada: (preg ? "" : "") + out.join(" ") + (preg ? "?" : ""), pregunta: preg, tiempo: tiempo, negacion: neg };
    });
  }
  var IND_EN = null, VERB_EN = null;
  var VERB_EXTRA = { want: 'nume', need: 'moke', go: 'duma', come: 'duma', move: 'duma', live: 'suma', love: 'lore', like: 'lore', drink: 'nobe pume', walk: 'kalu-duma', cook: 'pore-dare', buy: 'kera-fedo', sell: 'pema-fedo', can: 'pode', must: 'pelo', work: 'daro', help: 'galo', make: 'dare', read: 'lodu', write: 'beka', say: 'reka', speak: 'reka', think: 'rena', know: 'lare' };
  function indEn() {
    if (IND_EN) return IND_EN; IND_EN = {}; VERB_EN = {};
    Object.keys(LEX).forEach(function (f) { var e = LEX[f][3] || ""; e.split(" / ").forEach(function (v) { v = v.toLowerCase().trim(); if (!v) return;
      if (/^to /.test(v)) { VERB_EN[v.slice(3)] = f; } else (IND_EN[v] = IND_EN[v] || []).push(f); }); });
    Object.keys(VERB_EXTRA).forEach(function (k) { VERB_EN[k] = VERB_EXTRA[k]; });
    return IND_EN;
  }
  var FUNC_EN = { and: "re", or: "lo", if: "ke", with: "ko", without: "so", in: "bo", at: "bo", on: "bo", to: "to", from: "de", near: "le", far: "lu", but: "balo", because: "kasu", up: "go", down: "gu", outside: "ba",
    i: "me", you: "tu", he: "ra", she: "ra", it: "ra", we: "mene", they: "rane", what: "ka-kema", who: "ka-nara", where: "ka-kore", when: "ka-tera", how: "ka-mode", why: "ka-kasu", yes: "tare",
    today: "te-fusu", yesterday: "pe-fusu", tomorrow: "pu-fusu", never: "tera-no", always: "tera-fese", nothing: "kema-no", nobody: "nara-no", everything: "kema-fese", also: "re-se" };
  var BACK_PAST = {}; Object.keys(IRREG_PAST).forEach(function (k) { BACK_PAST[IRREG_PAST[k]] = k; });
  function enLema(w) {
    indEn();
    if (VERB_EN[w]) return { v: w, t: null };
    if (BACK_PAST[w] && VERB_EN[BACK_PAST[w]]) return { v: BACK_PAST[w], t: "pe" };
    var m;
    if ((m = w.match(/^(.*)ed$/)) && (VERB_EN[m[1]] || VERB_EN[m[1] + "e"])) return { v: VERB_EN[m[1]] ? m[1] : m[1] + "e", t: "pe" };
    if ((m = w.match(/^(.*)ies$/)) && VERB_EN[m[1] + "y"]) return { v: m[1] + "y", t: null };
    if ((m = w.match(/^(.*)(es|s)$/)) && (VERB_EN[m[1]] || VERB_EN[w.slice(0, -1)])) return { v: VERB_EN[m[1]] ? m[1] : w.slice(0, -1), t: null };
    if ((m = w.match(/^(.*)ing$/)) && (VERB_EN[m[1]] || VERB_EN[m[1] + "e"])) return { v: VERB_EN[m[1]] ? m[1] : m[1] + "e", t: null };
    return null;
  }
  function en2owee(texto) {
    var frases = texto.split(/[.!?¿¡\n]+/).map(function (x) { return x.trim(); }).filter(Boolean), I = indEn();
    return frases.map(function (fr) {
      var pal = (fr.toLowerCase().replace(/n't/g, " not").match(/[a-z]+/g) || []), out = [], det = [], tiempo = null, neg = false, preg = /\?\s*$/.test(fr) || /^(do|does|did)\b/i.test(fr), verbo = null;
      pal.forEach(function (w, i) {
        if (["a", "an", "the", "do", "does", "is", "are", "am", "be", "been"].indexOf(w) >= 0) { det.push({ es: w, owee: "(no equivalent: Owee has no articles or auxiliaries)", ok: true }); return; }
        if (w === "did") { tiempo = "pe"; det.push({ es: w, owee: "pe (past)", ok: true }); return; }
        if (w === "will") { tiempo = "pu"; det.push({ es: w, owee: "pu (future)", ok: true }); return; }
        if (w === "not") { neg = true; det.push({ es: w, owee: "no", ok: true }); return; }
        if (FUNC_EN[w]) { out.push(FUNC_EN[w]); det.push({ es: w, owee: FUNC_EN[w], ok: true }); return; }
        var l = enLema(w);
        if (l) { if (l.t) tiempo = l.t; verbo = VERB_EN[l.v]; out.push(verbo); det.push({ es: w, owee: verbo + (l.t ? " (past)" : ""), ok: true }); return; }
        var c = I[w] || I[w.replace(/s$/, "")] || null;
        if (c) { out.push(c[0]); det.push({ es: w, owee: c.slice(0, 3).join(" · "), ok: true }); return; }
        det.push({ es: w, owee: "(not found)", ok: false });
      });
      var POSP = ["bo", "ba", "to", "de", "go", "gu", "le", "lu", "ko", "so"], sug = out.slice();
      for (var q = 0; q < sug.length - 1; q++) if (POSP.indexOf(sug[q]) >= 0) { var tmp = sug[q]; sug[q] = sug[q + 1]; sug[q + 1] = tmp; q++; }
      if (verbo) { var j = sug.indexOf(verbo); if (j >= 0) { sug.splice(j, 1); if (neg) sug.push("no"); if (tiempo && sug.every(function (x) { return ["pe-fusu", "pu-fusu", "te-fusu"].indexOf(x) < 0; })) sug.push(tiempo); sug.push(verbo); } }
      else if (neg) { var k = sug.length ? sug.length - 1 : 0; sug.splice(k, 0, "no"); }
      if (preg) sug.push("ka");
      return { frase: fr, palabras: det, sugerencia: sug.join(" ") };
    });
  }
  root.OweeTraductor.owee2en = owee2en; root.OweeTraductor.en2owee = en2owee;

})(typeof window !== "undefined" ? window : globalThis);
