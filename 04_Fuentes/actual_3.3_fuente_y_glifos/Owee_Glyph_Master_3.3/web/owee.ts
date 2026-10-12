/**
 * owee.ts — Roman Owee <-> Owee Script (PUA) · Owee Glyph Master 3.3
 *
 * Mismas reglas que el IME Fcitx5 y que owee.js:
 *  - minúsculas; sh/ch se leen antes que las consonantes simples;
 *  - sólo V o CV; la i no existe;
 *  - una palabra imposible se deja en roman (no se pierde texto);
 *  - espacios, guiones y puntuación se conservan;
 *  - opcional: cifras 0-9 -> dígitos Owee U+E040..U+E049.
 *
 *   import { toScript, toRoman } from './owee'
 *   toScript('me suna nume 2026', { digits: true })
 */

export type OweeKind = 'vowel' | 'syllable' | 'digit' | 'mark';

export interface OweeUnit {
  roman: string;
  id: string;
  cp: number;
  char: string;
  kind: OweeKind;
  reading?: string;
}

const VOWELS = ['a', 'e', 'o', 'u'] as const;
const CONS = ['p', 'b', 't', 'd', 'k', 'g', 'f', 's', 'm', 'n', 'l', 'r', 'sh', 'ch'] as const;
const DIGIT_READING = ['cho', 'be', 'du', 'ga', 'fo', 'sa', 'ku', 'mu', 'na', 'she'] as const;

export const units: OweeUnit[] = [];
const byRoman = new Map<string, OweeUnit>();
const byChar = new Map<string, OweeUnit>();

function add(u: Omit<OweeUnit, 'char'>): void {
  const unit: OweeUnit = { ...u, char: String.fromCharCode(u.cp) };
  units.push(unit);
  byChar.set(unit.char, unit);
  if (unit.kind !== 'digit') byRoman.set(unit.roman, unit);
}

let cp = 0xe000;
for (const v of VOWELS)
  add({ roman: v, id: `OWEE_SYL_${v.toUpperCase()}`, cp: cp++, kind: 'vowel' });
for (const c of CONS)
  for (const v of VOWELS)
    add({ roman: c + v, id: `OWEE_SYL_${(c + v).toUpperCase()}`, cp: cp++, kind: 'syllable' });
DIGIT_READING.forEach((reading, d) =>
  add({ roman: String(d), id: `OWEE_DIGIT_${d}`, cp: 0xe040 + d, kind: 'digit', reading }),
);

const JOIN = String.fromCharCode(0xe03c); // nexo de compuesto (sade-kelo)
const NAME = String.fromCharCode(0xe03d); // marca de nombre propio (Ana)
byChar.set(JOIN, { roman: '-', id: 'OWEE_MARK_JOIN', cp: 0xe03c, kind: 'mark', char: JOIN } as OweeUnit);
byChar.set(NAME, { roman: '^', id: 'OWEE_MARK_NAME', cp: 0xe03d, kind: 'mark', char: NAME } as OweeUnit);

const isVowel = (c: string | undefined): boolean =>
  c === 'a' || c === 'e' || c === 'o' || c === 'u';

/** Divide una palabra roman en sílabas Owee; null si no es válida. */
export function syllables(word: string): string[] | null {
  const w = word.toLowerCase();
  const out: string[] = [];
  let i = 0;
  while (i < w.length) {
    const c = w.charAt(i);
    if (isVowel(c)) {
      out.push(c);
      i++;
      continue;
    }
    let cons: string | null = null;
    if ((c === 's' || c === 'c') && w.charAt(i + 1) === 'h') cons = c + 'h';
    else if ((CONS as readonly string[]).includes(c)) cons = c;
    if (!cons) return null;
    const v = w.charAt(i + cons.length);
    if (!isVowel(v)) return null;
    out.push(cons + v);
    i += cons.length + 1;
  }
  return out.length ? out : null;
}

/** Convierte texto roman a Owee Script conservando todo lo demás.
 *  Guion entre palabras Owee válidas -> nexo U+E03C; inicial mayúscula -> marca de nombre U+E03D. */
export function toScript(text: string, opts: { digits?: boolean } = {}): string {
  return text.replace(/[A-Za-z]+(?:-[A-Za-z]+)*|[0-9]/g, (tok) => {
    if (/[0-9]/.test(tok)) return opts.digits ? String.fromCharCode(0xe040 + Number(tok)) : tok;
    const parts = tok.split('-');
    const conv = parts.map((p) => {
      const s = syllables(p);
      return s ? s.map((x) => byRoman.get(x)?.char ?? x).join('') : null;
    });
    const name = /^[A-Z][a-z]*$/.test(parts[0] ?? '');
    const out = conv.every((c) => c !== null)
      ? conv.join(JOIN)
      : parts.map((p, i) => conv[i] ?? p).join('-');
    return (name && conv[0] !== null ? NAME : '') + out;
  });
}

/** Convierte Owee Script (PUA) de vuelta a roman. Los dígitos vuelven a 0-9. */
export function toRoman(text: string): string {
  let out = '';
  let cap = false;
  for (const ch of text) {
    const u = byChar.get(ch);
    if (u && u.kind === 'mark' && u.roman === '^') {
      cap = true;
      continue;
    }
    let r = u ? u.roman : ch;
    if (cap && u) {
      r = r.charAt(0).toUpperCase() + r.slice(1);
      cap = false;
    }
    out += r;
  }
  return out;
}

/** Palabras roman que no se pudieron convertir. */
export function invalidWords(text: string): string[] {
  const bad: string[] = [];
  for (const w of text.match(/[A-Za-z]+/g) ?? [])
    if (!syllables(w) && !bad.includes(w)) bad.push(w);
  return bad;
}

/** Busca una unidad por roman ('na') o por carácter PUA. */
export function unit(x: string): OweeUnit | null {
  return byRoman.get(x) ?? byChar.get(x) ?? null;
}

export const version = '3.3';
