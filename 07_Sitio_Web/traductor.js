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
               donde: "ka-kore", cuando: "ka-tera", como: "ka-mode", cuanto: "ka-bema", si_: "tare", hoy: "te-loda-kelo", ayer: "pe-loda-kelo", manana: "pu-loda-kelo" };
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
    casa: "kuma", hogar: "kuma", ciudad: "kuma-seta", comida: "fame", bebida: "nobe", fruta: "nelo-fame", libro: "beka kema", dinero: "bado-feke", tiempo: "tera", dia: "loda-kelo",
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
      var ADV = ["pe-loda-kelo", "pu-loda-kelo", "te-loda-kelo"];
      if (tiempo && !sug.some(function (x) { return ADV.indexOf(x) >= 0; })) { var k = sug.length - 1; var pos = out.indexOf(VERBOS[lema(pal[iv] || "")]); if (pos >= 0) sug.splice(pos, 0, tiempo); }
      var verbo = iv >= 0 ? VERBOS[lema(pal[iv])] : null;
      if (verbo) { var j = sug.indexOf(verbo); if (j >= 0 && j !== sug.length - 1) { sug.splice(j, 1); sug.push(verbo); } }
      return { frase: fr, palabras: det, sugerencia: sug.join(" ") };
    });
  }
  root.OweeTraductor = { owee2es: owee2es, es2owee: es2owee };
})(typeof window !== "undefined" ? window : globalThis);
