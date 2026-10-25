# Lote 19 — raíces propias para alimentos y animales (aprobado el 2026-10-25)

> **Lote 20 (2026-10-25):** los compuestos de 6 sílabas de este lote (tomate, lechuga, manzana, sandía, palta, camote, pimienta, repollo, cerveza, salteña, charque, conejo, abeja, haba, lenteja) pasaron a raíces cortas por practicidad. Ver [`lotes_20.md`](lotes_20.md).

**40 términos** (18 raíces nuevas de 2 sílabas y 22 compuestos) que sustituyen a 37 nombres adaptados del español (`tomate`, `sanaorea`, `lechuga`, `uba`…) y a la raíz `meto` (mito). Lo pidió el autor: una palabra Owee no debe parecer una palabra española, sino nacer de las raíces del idioma.

**Criterio:**

1. **Compuesto** cuando una descripción con raíces existentes identifica el alimento sin ambigüedad (≤ 3 elementos): `rale-nede-fame` (verdura roja) = tomate, `suna-nelo-fame` (fruta de agua) = sandía, `bore-nobe` (bebida negra) = café, `tabu-nelo` (planta del pan) = trigo.
2. **Raíz nueva** cuando no hay rasgo único (cebolla, limón, uva, pera…). Cada raíz: sílabas CV sin `i`, distancia ≥ 2 con toda raíz de 2 sílabas del léxico y entre ellas, sin metátesis, sin parecido (≥ 0,75) con ninguna palabra del diccionario español y sin coincidir con palabras comunes del español o del inglés.
3. **Legumbres**: una raíz de clase, `dobu` (grano que crece en vaina), y el resto por color o tamaño: `rale-dobu` frijol, `nede-dobu` arveja, `kale-dobu` garbanzo, `dobu-gore-pa` haba, `dobu-gore-po` lenteja.
4. Los compuestos que dependían de formas sustituidas cambian con ellas: `uba-nobe` → `nugu-nobe` (vino), `terego-nobe` → `tabu-nelo-nobe` (cerveza).

Comprobado con `generar_ciencias.py` (0 por revisar), `verificar_propuestas.py` (sin vecinos a distancia 1, sin sinónimos) y `revision_semantica.py`.

| Antes | Ahora | Significado | Inglés |
|---|---|---|---|
| `kunape` | `dusho` | **cuñapé (pan de queso y almidón)** | cuñapé (cheese bread) |
| `papaea` | `chamu` | **papaya** | papaya |
| `perea` | `chede` | **pera** | pear |
| `kakao` | `choru` | **cacao** | cocoa |
| `durasano` | `gesho` | **durazno** | peach |
| `naranaka` | `lufo` | **naranja** | orange |
| `uba` | `nugu` | **uva** | grape |
| `ananasa` | `shebo` | **piña** | pineapple |
| `lemono` | `shefa` | **limón** | lemon |
| `—` | `dobu` | **legumbre (grano que crece en vaina)** | legume |
| `kenua` | `kupu` | **quinua** | quinoa |
| `meto` | `fonu` | **mito (relato sagrado del origen)** | myth |
| `kalabasa` | `kushu` | **calabaza** | pumpkin |
| `esepenaka` | `lepu` | **espinaca** | spinach |
| `seboea` | `nolu` | **cebolla** | onion |
| `pepeno` | `rofu` | **pepino** | cucumber |
| `sanaorea` | `shuko` | **zanahoria** | carrot |
| `ako` | `tushe` | **ajo** | garlic |
| `abeka` | `ruma-nelo-lena` | **abeja (animal de la flor)** | bee |
| `koneko` | `ruma-sone-loke` | **conejo (animal de orejas)** | rabbit |
| `kafea` | `bore-nobe` | **café (bebida negra)** | coffee |
| `uba-nobe` | `nugu-nobe` | **vino (bebida de uva)** | wine |
| `terego-nobe` | `tabu-nelo-nobe` | **cerveza (bebida de trigo)** | beer |
| `charake` | `bora-gume-sade` | **charque (carne de sol)** | charque (dried meat) |
| `salotena` | `tabu-bora-gume` | **salteña (pan de carne)** | salteña (Bolivian pastry) |
| `palata` | `mase-nelo-fame` | **palta (fruta de grasa)** | avocado |
| `manasana` | `rale-nelo-fame` | **manzana (fruta roja)** | apple |
| `sanadea` | `suna-nelo-fame` | **sandía (fruta de agua)** | watermelon |
| `abana` | `dobu-gore-pa` | **haba (legumbre grande)** | broad bean |
| `leneteka` | `dobu-gore-po` | **lenteja (legumbre pequeña)** | lentil |
| `garabanaso` | `kale-dobu` | **garbanzo (legumbre amarilla)** | chickpea |
| `arabeka` | `nede-dobu` | **arveja (legumbre verde)** | pea |
| `ferekolo` | `rale-dobu` | **frijol (legumbre roja)** | bean |
| `terego` | `tabu-nelo` | **trigo (planta del pan)** | wheat |
| `kamoto` | `fuko-lena-gume` | **camote (papa de azúcar)** | sweet potato |
| `chokolo` | `mugo-tame` | **choclo (maíz nuevo)** | sweetcorn |
| `lechuga` | `nelo-maku-fame` | **lechuga (comida de hoja)** | lettuce |
| `repoeo` | `nelo-maku-selo` | **repollo (hojas en círculo)** | cabbage |
| `pemeeneta` | `pore-pado-nelo` | **pimienta (semilla de fuego)** | pepper |
| `tomate` | `rale-nede-fame` | **tomate (verdura roja)** | tomato |
