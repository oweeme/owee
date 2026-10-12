# Owee Química — guía completa (borrador 0.2)

**Estado: VERIFICADA (pendiente de aprobación).** Esta guía **no existía** en el proyecto: se crea aquí con el mismo método de Matemáticas y Física. Nada de lo que contiene está aprobado hasta que lo confirmes. Los números se muestran con el **glifo numérico de Owee** y su lectura; los cálculos se verifican automáticamente al generar el sitio.

> **Principio:** Owee nombra los conceptos; la **notación química internacional se conserva** (símbolos H, O, Na, Cl…, fórmulas H₂O, NaCl, CO₂, flechas, mol, pH, unidades SI). **Todo se construye componiendo raíces ya existentes: esta guía no añade ninguna raíz nueva** (la versión 0.1 proponía 7 y se sustituyeron todas por compuestos). Sin `i`: todas las formas cumplen la fonología V/CV.

## 0. Los números en química

Se calcula con el glifo numérico y se lee con las palabras (ver Matemáticas §0–2).
<!--digitos-->

## 1. Cómo se construyó

1. Se reutilizó todo lo posible: `gume` (materia), `ganu` (átomo), `elenu` (electrón), `poru` (protón), `netu` (neutrón), `chaga` (carga), `rela` (unión), `telo` (cambio), `shome` (calor), `goda`/`luda`/`boga` (estados), `suna` (agua), `suma` (vida).
2. Cada concepto nuevo es una **construcción** *raíz principal + modificador* (máximo 3 elementos).
3. **Ácido y base** usan la definición de Brønsted-Lowry: el ácido *da* protones (`pema`), la base los *recibe* (`gura`), igual que oxidación y reducción dan o reciben electrones.

## 2. Materia, átomo y elemento

Ya existen (Física 2.0): `ganu` átomo · `ganu-choma` núcleo · `elenu` electrón · `poru` protón · `netu` neutrón · `gume` materia · `gama` masa.

| Concepto | Owee | Construcción |
|---|---|---|
| elemento químico | `ganu-dore` | átomo + forma (tipo de átomo) |
| conjunto de elementos | `ganu-dore-seta` | elemento + conjunto |
| tabla periódica | `ganu-dore-seta kelo` | conjunto de elementos + cíclico (`kelo`) |
| número atómico | `ganu-banu` | átomo + número |
| masa atómica | `ganu-gama` | átomo + masa |
| ion | `ganu-chaga` | átomo + carga |
| catión / anión | `ganu-chaga-pa` / `ganu-chaga-po` | ion + positiva / negativa |
| molécula | `ganu-kema` | átomo + objeto (objeto de átomos unidos) |
| masa molecular | `ganu-kema-gama` | molécula + masa |
| compuesto químico | `gume-rela` | materia + unión |
| mezcla | `gume-ko` | materia + con |

Los **nombres de los elementos** (hidrógeno, oxígeno, sodio…) no se traducen por ahora: se conserva su **símbolo** internacional. Ver «Decisiones pendientes».

### 2.1 Contar partículas

El número atómico (`ganu-banu`) es el número de protones; en un átomo neutro hay tantos electrones como protones.

| Caso | Cálculo | Resultado |
|---|---|---|
| Carbono (6 protones, 6 neutrones): número másico | [[6 + 6 = 12]] | 12 |
| Sodio, Na (11 protones): electrones del ion Na⁺ | [[11 − 1 = 10]] | 10 electrones |
| Cloro, Cl (17 protones): electrones del ion Cl⁻ | [[17 + 1 = 18]] | 18 electrones |

## 3. Enlace y estados

| Concepto | Owee | Construcción |
|---|---|---|
| enlace químico | `ganu-rela` | átomo + unión |
| sólido / líquido / gas | `goda` / `luda` / `boga` | Física 2.0 |
| fusión (sólido → líquido) | `goda-to-luda telo` | origen-destino + cambio |
| ebullición (líquido → gas) | `luda-to-boga telo` | origen-destino + cambio |

## 4. La mol y las masas

Se conservan `mol` y g/mol. La **masa molecular** (`ganu-kema-gama`) es la suma de las masas atómicas (H = 1, O = 16, Na = 23, Cl = 35,5, C = 12).

| Sustancia | Cálculo | Masa molar |
|---|---|---|
| H₂O | [[2 × 1 + 16 = 18]] | 18 g/mol |
| CO₂ | [[12 + 2 × 16 = 44]] | 44 g/mol |
| NaCl | [[23 + 35.5 = 58.5]] | 58,5 g/mol |

**Cantidad de sustancia:** `#n = m ÷ M`. 36 g de agua: [[36 ÷ 18 = 2]] mol. 88 g de CO₂: [[88 ÷ 44 = 2]] mol. El número de Avogadro (6,022 × 10²³) se conserva como constante.

## 5. Disoluciones

| Concepto | Owee | Construcción |
|---|---|---|
| disolución | `luda-ko` | líquido + con (líquido que contiene algo) |
| disolución acuosa | `suna-ko` | agua + con |
| concentración | `luda-ko-bema` | disolución + cantidad |

**Concentración:** `#M = n ÷ V`. 2 mol en 4 L: [[2 ÷ 4 = 0.5]] mol/L.

**Dilución:** `#C₁ × V₁ = C₂ × V₂`. Con 2 mol/L y 0,5 L hay [[2 × 0.5 = 1]] mol de soluto.

## 6. Reacción química

| Concepto | Owee | Construcción |
|---|---|---|
| reacción química | `gume-telo` | materia + cambio |
| catalizador | `gume-telo-galo` | reacción + ayuda |
| equilibrio químico | `gume-telo-se` | reacción + igualdad |
| velocidad de reacción | `gume-telo-sape` | reacción + velocidad |
| combustión | `pore-gume-telo` | fuego + reacción |
| reacción exotérmica | `gume-telo shome-pema` | reacción + dar calor |
| reacción endotérmica | `gume-telo shome-gura` | reacción + recibir calor |

**Balance de 2 H₂ + O₂ → 2 H₂O.** Hidrógeno a la izquierda: [[2 × 2 = 4]]; a la derecha: [[2 × 2 = 4]]. Oxígeno a la izquierda: [[1 × 2 = 2]]; a la derecha: [[2 × 1 = 2]]. Está balanceada y es una combustión exotérmica (`pore-gume-telo`, `shome-pema`).

**Balance de CH₄ + 2 O₂ → CO₂ + 2 H₂O.** Oxígeno a la izquierda: [[2 × 2 = 4]]; a la derecha: [[2 + 2 × 1 = 4]]. Hidrógeno: [[1 × 4 = 4]] y [[2 × 2 = 4]].

**Rendimiento.** Si la reacción produce 36 g de agua y la masa esperada es 40 g: [[36 ÷ 40 = 0.9]], es decir, 90 %.

## 7. Ácidos, bases y sales

| Concepto | Owee | Construcción |
|---|---|---|
| ácido | `poru-pema` | protón + dar |
| base (álcali) | `poru-gura` | protón + recibir |
| reacción ácido-base | `poru-telo` | protón + cambio (transferencia de protones) |
| sal | `chaga-rela` | carga + unión |
| escala de pH | `poru-mede` | protón + medir |

**pH.** Se conserva el símbolo pH (`#pH = −log[H⁺]`). Si `#[H⁺] = 10⁻³` mol/L, el pH es 3 y la disolución es ácida (`poru-pema`). Neutro: pH 7. Relación: `#pH + pOH = 14`; con pH 3, pOH = [[14 − 3 = 11]].

**Neutralización:** HCl + NaOH → NaCl + H₂O. El ácido (`poru-pema`) cede su protón a la base (`poru-gura`) y se forma una sal (`chaga-rela`, NaCl) y agua.

## 8. Oxidación y reducción

La transferencia de electrones se nombra con las acciones que ya tiene Owee, `pema` (dar) y `gura` (recibir):

| Concepto | Owee | Construcción |
|---|---|---|
| oxidación | `elenu-pema` | electrón + dar (pierde electrones) |
| reducción | `elenu-gura` | electrón + recibir (gana electrones) |

**Ejemplo.** Zn → Zn²⁺ + 2 e⁻ es una oxidación (`elenu-pema`: se ceden [[2]] electrones). Cu²⁺ + 2 e⁻ → Cu es una reducción (`elenu-gura`). En el conjunto los electrones cedidos y ganados son iguales: [[2 = 2]].

## 9. Química orgánica

`suma-gume` = química orgánica (**materia de la vida**). Inorgánica: `suma-gume no`. **Ejemplo:** el metano CH₄ tiene 1 átomo de carbono y 4 de hidrógeno: [[1 + 4 = 5]] átomos en total.

## 10. Todas las construcciones propuestas
<!--construcciones Química-->

## 11. Ejercicios

1) Construye: reacción química, enlace químico, ion. 2) ¿Qué es `elenu-pema`? 3) Comprueba que 2 H₂ + O₂ → 2 H₂O está balanceada. 4) Masa molar del H₂O (H = 1, O = 16) y moles en 36 g. 5) [H⁺] = 10⁻³ mol/L: pH y si es `poru-pema` o `poru-gura`. 6) NaCl se disuelve en `suna-ko`: ¿qué iones aparecen? 7) Construye elemento químico, molécula y mezcla. 8) Masa molar del CO₂ y moles en 88 g. 9) Concentración de 3 mol en 6 L. 10) ¿Por qué un ácido se llama `poru-pema`?

### Respuestas

1) `gume-telo`; `ganu-rela`; `ganu-chaga`. 2) Oxidación: ceder (dar) electrones. 3) [[2 × 2 = 4]] H y [[1 × 2 = 2]] O a cada lado. 4) [[2 × 1 + 16 = 18]] g/mol; [[36 ÷ 18 = 2]] mol. 5) pH 3: ácido. 6) Na⁺ (`ganu-chaga-pa`) y Cl⁻ (`ganu-chaga-po`). 7) `ganu-dore`; `ganu-kema`; `gume-ko`. 8) [[12 + 2 × 16 = 44]] g/mol; [[88 ÷ 44 = 2]] mol. 9) [[3 ÷ 6 = 0.5]] mol/L. 10) Porque *da* (`pema`) protones (`poru`).

## 12. Decisiones pendientes para Química

- **Nombres de elementos:** conservar solo símbolos (decisión actual) o crear una convención sistemática. Con la fonología Owee, los nombres internacionales (sin `i`, sin consonantes finales) necesitarían una norma de adaptación.
- **Aprobar las construcciones** de esta guía (todas están marcadas PROPUESTA).
- **Valencia, orbital, isótopo, enlace iónico/covalente:** aún sin construcción; conviene decidirlas al escribir textos reales.
- **Nomenclatura de compuestos** (cómo se lee NaCl, H₂SO₄ en Owee).
