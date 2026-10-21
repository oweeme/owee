# Lotes 9 a 14 — vocabulario nuevo para aprobar

Propuesta de **268 términos** para hogar, informática y sistema operativo, comprar y vender, cuerpo humano, cocina y alimentos, y agricultura. Todos pasan la verificación automática (fonología V/CV sin `i`, sin colisiones, partes que existen, máximo 3 elementos y 6 sílabas, un significado = una forma, inglés por pivote) y quedan como **VERIFICADA**: no son oficiales hasta que se aprueben. Para aprobar un término, añádelo a `02_Diccionario/datos/aprobadas.txt` y ejecuta `generar_ciencias.py`; para cambiarlo, edítalo en `ciencias_fuente.py`.

**Método:** compuestos de raíces ya existentes (`kuma` hogar, `bora` cuerpo, `fame` comida, `nelo` planta, `ruma` animal, `feke` herramienta, `meka` máquina, `kopa` contenedor, `kore` lugar…), igual que los lotes anteriores. Tras una primera redacción se buscaron los **pares mínimos** (palabras a una sola letra de otra del mismo tema) y se cambiaron unas 45 formas para evitarlos; en `04_Fuentes/.../OweeSans3_3_Source/auditar_palabras_v4.py` se comprueba además que todo el léxico se escribe con los glifos nuevos.

**Decisiones tuyas:**

1. **Nombres de alimentos concretos** (palta, tomate, cebolla…): se adaptaron con la norma de nombres (`adaptar_nombre.py`), como ya se hizo con `kenua` (quinua). Son raíces nuevas. Dos llevan una sílaba más que la adaptación pura porque quedaban a una letra de otra palabra: `abana` (haba, en vez de `aba`, vecina de `uba`) y `kafea` (café, en vez de `kafe`, vecina de `kade`, `lafe`, `kare`, `kale`, `kefe`); y `kamoto` (camote) en vez de `kamote`, casi igual que `ka-mode` («cómo»).
2. **Animales concretos** (`ruma-bume` oveja, `ruma-naku-nobe` vaca, `ruma-mase` cerdo…): se componen por su función. Si prefieres raíces propias, dímelo.
3. **Sentidos** (vista, oído, olfato, gusto, tacto): no se añadieron; ya existen `luma-salo`, `luma-sone`, `luma-sura`, `luma-fame`, `luma-tada`.
4. **Siguen faltando** (ver `cobertura_dominios.md`): materiales de casa (madera, ladrillo, vidrio), tareas y aplicaciones, oferta/factura/crédito, más frutas y verduras, más animales de granja, herramientas de poda e injerto.

## Lote 9 — Hogar y casa (46 términos)

| Forma | Significado | Partes | Inglés |
|---|---|---|---|
| `sede-kema` | **silla** — objeto de asiento | `sede` (asiento) + `kema` (objeto) | chair |
| `kuma-kopa-gore` | **armario** — contenedor grande de la casa | `kuma` (hogar) + `kopa` (contenedor) + `gore` (tamaño) | wardrobe |
| `go-tabe` | **estante** — superficie alta | `go` (arriba) + `tabe` (superficie de apoyo) | shelf |
| `falo-tabe` | **espejo** — superficie de reflexión | `falo` (reflexión) + `tabe` (superficie de apoyo) | mirror |
| `loke-nado-lobe` | **cortina** — cubierta de la ventana | `loke` (ojo) + `nado` (acceso) + `lobe` (cubierta) | curtain |
| `kuma-tabe-lobe` | **alfombra** — cubierta del suelo | `kuma` (hogar) + `tabe` (superficie de apoyo) + `lobe` (cubierta) | rug |
| `tume-sede` | **almohada** — asiento de la cabeza | `tume` (cabeza) + `sede` (asiento) | pillow |
| `sule-lobe` | **manta** — cubierta de dormir | `sule` (dormir) + `lobe` (cubierta) | blanket |
| `sule-tabe-lobe` | **sábana** — cubierta de la cama | `sule` (dormir) + `tabe` (superficie de apoyo) + `lobe` (cubierta) | bed sheet |
| `sura-duma-meka` | **ventilador** — máquina del viento | `sura` (aire) + `duma` (movimiento) + `meka` (máquina) | fan |
| `fure-pa-meka` | **calefacción** — máquina de calor | `fure` (temperatura) + `pa` (más) + `meka` (máquina) | heating |
| `fure-po-kopa` | **refrigerador** — contenedor de frío | `fure` (temperatura) + `po` (menos) + `kopa` (contenedor) | refrigerator |
| `pore-meka` | **estufa** — máquina de fuego | `pore` (fuego) + `meka` (máquina) | stove |
| `gase-meka` | **lavadora** — máquina de limpieza | `gase` (limpieza) + `meka` (máquina) | washing machine |
| `dabo-delo-feke` | **escoba** — herramienta para tomar la suciedad | `dabo` (suciedad) + `delo` (tomar) + `feke` (herramienta) | broom |
| `dabo-gume` | **basura** — materia de suciedad | `dabo` (suciedad) + `gume` (materia) | rubbish |
| `suna-nado` | **grifo** — acceso del agua | `suna` (agua) + `nado` (acceso) | tap |
| `suna-duma-kore` | **tubería** — camino del agua | `suna` (agua) + `duma` (movimiento) + `kore` (lugar) | pipe |
| `suna-gu-duma` | **ducha** — agua que baja | `suna` (agua) + `gu` (abajo) + `duma` (movimiento) | shower |
| `eleka-nado` | **enchufe** — acceso de la electricidad | `eleka` (electricidad) + `nado` (acceso) | socket |
| `bure-kose-feke` | **interruptor** — herramienta de abrir y cerrar | `bure` (abrir) + `kose` (cerrar) + `feke` (herramienta) | switch |
| `kura-rela` | **cable** — unión de la corriente eléctrica | `kura` (corriente eléctrica) + `rela` (unión) | cable |
| `eleka-salo` | **foco** — luz eléctrica | `eleka` (electricidad) + `salo` (luz) | light bulb |
| `sone-salo-sena` | **televisión** — imagen y sonido | `sone` (sonido) + `salo` (luz) + `sena` (signo) | television |
| `sone-meka` | **radio** — máquina de sonido | `sone` (sonido) + `meka` (máquina) | radio |
| `lu-sone-meka` | **teléfono** — máquina de sonido lejano | `lu` (lejos) + `sone` (sonido) + `meka` (máquina) | telephone |
| `kuma-ba-kore` | **patio** — lugar exterior de la casa | `kuma` (hogar) + `ba` (exterior) + `kore` (lugar) | yard |
| `taro-meka-kuma` | **garaje** — casa del coche | `taro` (tierra) + `meka` (máquina) + `kuma` (hogar) | garage |
| `kore-kose` | **valla** — cierre de un lugar | `kore` (lugar) + `kose` (cerrar) | fence |
| `nado-kose-feke` | **cerradura** — herramienta de cerrar el acceso | `nado` (acceso) + `kose` (cerrar) + `feke` (herramienta) | door lock |
| `kuma-gu-kore` | **sótano** — lugar bajo la casa | `kuma` (hogar) + `gu` (abajo) + `kore` (lugar) | basement |
| `kuma-go-kore` | **azotea** — lugar alto de la casa | `kuma` (hogar) + `go` (arriba) + `kore` (lugar) | roof terrace |
| `kuma-fedo-kelo` | **alquiler** — pago periódico de la casa | `kuma` (hogar) + `fedo` (pago) + `kelo` (ciclo) | rent |
| `pase-nara` | **dueño** — persona de posesión | `pase` (posesión) + `nara` (persona) | owner |
| `kuma-telo` | **mudarse** — cambio de casa | `kuma` (hogar) + `telo` (cambiar) | to move house |
| `gase-dare` | **limpiar** — hacer limpieza | `gase` (limpieza) + `dare` (hacer) | to clean |
| `dabo-delo` | **barrer** — tomar la suciedad | `dabo` (suciedad) + `delo` (tomar) | to sweep |
| `sone-tada` | **timbre** — sonido de contacto | `sone` (sonido) + `tada` (contacto) | doorbell |
| `reka-sena-kopa` | **buzón** — contenedor de mensajes | `reka` (comunicación) + `sena` (signo) + `kopa` (contenedor) | mailbox |
| `beka-tabe` | **papel** — superficie de escritura | `beka` (escritura) + `tabe` (superficie de apoyo) | paper |
| `suna-fadu` | **agua potable** — agua segura | `suna` (agua) + `fadu` (seguridad) | drinking water |
| `pore-nelo-gume` | **leña** — materia de planta para el fuego | `pore` (fuego) + `nelo` (planta) + `gume` (materia) | firewood |
| `gase-feke` | **cepillo** — herramienta de limpieza | `gase` (limpieza) + `feke` (herramienta) | brush |
| `tume-nelo-feke` | **peine** — herramienta del cabello | `tume` (cabeza) + `nelo` (planta) + `feke` (herramienta) | comb |
| `delo-nuse-feke` | **tijeras** — herramienta de cortar | `delo` (tomar) + `nuse` (vacío) + `feke` (herramienta) | scissors |
| `bume-rela-feke` | **aguja** — herramienta para unir la ropa | `bume` (ropa) + `rela` (unión) + `feke` (herramienta) | needle |

## Lote 10 — Informática y sistema (55 términos)

| Forma | Significado | Partes | Inglés |
|---|---|---|---|
| `doke-kopa-seta` | **carpeta** — conjunto de archivos | `doke` (información) + `kopa` (contenedor) + `seta` (conjunto) | folder |
| `doke-kopa-foma` | **sistema de archivos** — reglas de los archivos | `doke` (información) + `kopa` (contenedor) + `foma` (regla) | file system |
| `mado-tera` | **proceso de programa** — cálculo en el tiempo | `mado` (cálculo) + `tera` (tiempo) | running process |
| `mado-raga` | **hilo de ejecución** — cálculo en fila | `mado` (cálculo) + `raga` (fila) | thread |
| `mena-sape` | **memoria rápida** — memoria veloz | `mena` (memoria) + `sape` (velocidad) | fast memory |
| `mado-kore` | **procesador** — lugar del cálculo | `mado` (cálculo) + `kore` (lugar) | processor |
| `mena-goda` | **disco** — memoria sólida | `mena` (memoria) + `goda` (estado sólido) | disk |
| `mena-ba` | **memoria externa** — memoria exterior | `mena` (memoria) + `ba` (exterior) | external storage |
| `meka-gora-doma` | **núcleo del sistema** — centro del sistema operativo | `meka` (máquina) + `gora` (mundo) + `doma` (corazón) | kernel |
| `rela-le` | **red local** — unión cercana | `rela` (unión) + `le` (cerca) | local network |
| `mado-foma-fena` | **instalar** — poner programa | `mado` (cálculo) + `foma` (regla) + `fena` (poner) | to install |
| `mado-foma-nuse` | **desinstalar** — programa vacío | `mado` (cálculo) + `foma` (regla) + `nuse` (vacío) | to uninstall |
| `mado-foma-kuma` | **repositorio de programas** — casa de programas | `mado` (cálculo) + `foma` (regla) + `kuma` (hogar) | software repository |
| `lu-doke-gura` | **descargar** — recibir datos de lejos | `lu` (lejos) + `doke` (información) + `gura` (recibir) | to download |
| `lu-doke-pema` | **subir** — dar datos lejos | `lu` (lejos) + `doke` (información) + `pema` (dar) | to upload |
| `dare-se-fadu` | **copia de seguridad** — copia con seguridad | `dare` (hacer) + `se` (igualdad) + `fadu` (seguridad) | backup |
| `doke-rude` | **restaurar** — reparar los datos | `doke` (información) + `rude` (reparación) | to restore |
| `meka-gora-bade` | **administrador** — autoridad del sistema operativo | `meka` (máquina) + `gora` (mundo) + `bade` (autoridad) | administrator |
| `nado-pode` | **permiso** — posibilidad de acceso | `nado` (acceso) + `pode` (posibilidad) | permission |
| `nara-kade-gade` | **cuenta de usuario** — identidad del usuario | `nara` (persona) + `kade` (usar) + `gade` (identidad) | user account |
| `kade-tera` | **sesión** — tiempo de uso | `kade` (usar) + `tera` (tiempo) | session |
| `dese-kera` | **seleccionar** — obtener la decisión | `dese` (decisión) + `kera` (obtener) | to select |
| `dare-se-fena` | **pegar** — poner la copia | `dare` (hacer) + `se` (igualdad) + `fena` (poner) | to paste |
| `dare-se-kopa` | **portapapeles** — contenedor de la copia | `dare` (hacer) + `se` (igualdad) + `kopa` (contenedor) | clipboard |
| `to-pema` | **enviar un mensaje** — dar hacia | `to` (hacia) + `pema` (dar) | to send a message |
| `de-gura` | **recibir un mensaje** — recibir desde | `de` (desde) + `gura` (recibir) | to receive a message |
| `reka-sena` | **mensaje** — signo de comunicación | `reka` (comunicación) + `sena` (signo) | message |
| `reka-paku` | **notificación** — comunicación que llama la atención | `reka` (comunicación) + `paku` (atención) | notification |
| `sone-saku` | **alarma** — sonido de alerta | `sone` (sonido) + `saku` (alerta) | alarm |
| `salo-sena-meka` | **cámara** — máquina de imagen | `salo` (luz) + `sena` (signo) + `meka` (máquina) | camera |
| `sone-gura-meka` | **micrófono** — máquina que recibe sonido | `sone` (sonido) + `gura` (recibir) + `meka` (máquina) | microphone |
| `sone-pema-meka` | **altavoz** — máquina que da sonido | `sone` (sonido) + `pema` (dar) + `meka` (máquina) | loudspeaker |
| `sone-loke-feke` | **auriculares** — herramienta del oído | `sone` (sonido) + `loke` (ojo) + `feke` (herramienta) | headphones |
| `sone-mena` | **audio** — memoria de sonido | `sone` (sonido) + `mena` (memoria) | audio |
| `doke-gore-po` | **comprimir** — datos pequeños | `doke` (información) + `gore` (tamaño) + `po` (menos) | to compress |
| `doke-gore-pa` | **descomprimir** — datos grandes | `doke` (información) + `gore` (tamaño) + `pa` (más) | to decompress |
| `mado-foma-bosa` | **virus informático** — programa de rotura | `mado` (cálculo) + `foma` (regla) + `bosa` (rotura) | computer virus |
| `mado-foma-fadu` | **antivirus** — programa de seguridad | `mado` (cálculo) + `foma` (regla) + `fadu` (seguridad) | antivirus |
| `rela-fadu` | **cortafuegos** — seguridad de la red | `rela` (unión) + `fadu` (seguridad) | firewall |
| `meka-foma` | **controlador de dispositivo** — reglas de la máquina | `meka` (máquina) + `foma` (regla) | device driver |
| `dare-reka-kore` | **terminal de comandos** — lugar de comandos | `dare` (hacer) + `reka` (comunicación) + `kore` (lugar) | command console |
| `dare-reka-beka` | **script** — comandos escritos | `dare` (hacer) + `reka` (comunicación) + `beka` (escritura) | script |
| `kelo-dare` | **bucle** — hacer ciclo | `kelo` (ciclo) + `dare` (hacer) | loop |
| `kore-rela` | **enlace** — unión a un lugar | `kore` (lugar) + `rela` (unión) | link |
| `se-tera-dare` | **sincronizar** — hacer igual en el tiempo | `se` (igualdad) + `tera` (tiempo) + `dare` (hacer) | to synchronize |
| `foma-beka-dare` | **programar** — hacer código | `foma` (regla) + `beka` (escritura) + `dare` (hacer) | to code |
| `foma-beka-bure` | **código abierto** — código abierto | `foma` (regla) + `beka` (escritura) + `bure` (abrir) | open source |
| `telo-tera-mena` | **registro de eventos** — memoria de los eventos | `telo` (cambiar) + `tera` (tiempo) + `mena` (memoria) | event log |
| `loke-kopa-palo` | **pestaña de ventana** — parte de la ventana | `loke` (ojo) + `kopa` (contenedor) + `palo` (parte) | tab |
| `kade-mena` | **historial** — memoria de uso | `kade` (usar) + `mena` (memoria) | history log |
| `enu-pema-feke` | **cargador** — herramienta que da energía | `enu` (energía) + `pema` (dar) + `feke` (herramienta) | charger |
| `enu-fena` | **cargar la batería** — poner energía | `enu` (energía) + `fena` (poner) | to charge the battery |
| `nara-seta` | **contactos** — conjunto de personas | `nara` (persona) + `seta` (conjunto) | contacts |
| `luma-meka` | **sensor** — máquina de percepción | `luma` (percepción) + `meka` (máquina) | sensor |
| `meka-daro` | **robot** — máquina de trabajo | `meka` (máquina) + `daro` (trabajo) | robot |

## Lote 11 — Comprar y vender (32 términos)

| Forma | Significado | Partes | Inglés |
|---|---|---|---|
| `fedo-gura` | **cobrar** — recibir pago | `fedo` (pago) + `gura` (recibir) | to charge |
| `fedo-telo` | **vuelto** — pago de cambio | `fedo` (pago) + `telo` (cambiar) | money back |
| `bado-goda` | **moneda** — valor sólido | `bado` (valor) + `goda` (estado sólido) | coin |
| `bado-tabe` | **billete** — superficie de valor | `bado` (valor) + `tabe` (superficie de apoyo) | banknote |
| `fedo-kema` | **tarjeta de pago** — objeto de pago | `fedo` (pago) + `kema` (objeto) | payment card |
| `fedo-beka` | **recibo** — escritura del pago | `fedo` (pago) + `beka` (escritura) | receipt |
| `kera-fedo-nara` | **comprador** — persona que compra | `kera` (obtener) + `fedo` (pago) + `nara` (persona) | buyer |
| `pema-fedo-nara` | **vendedor** — persona que vende | `pema` (dar) + `fedo` (pago) + `nara` (persona) | seller |
| `kume-daro-nara` | **comerciante** — persona del trabajo de intercambio | `kume` (intercambio) + `daro` (trabajo) + `nara` (persona) | merchant |
| `bado-po-dare` | **descuento** — hacer menos valor | `bado` (valor) + `po` (menos) + `dare` (hacer) | discount |
| `bado-reka` | **regatear** — comunicar el valor | `bado` (valor) + `reka` (comunicación) | to haggle |
| `bado-pema-pu` | **préstamo** — valor dado y devuelto en el futuro | `bado` (valor) + `pema` (dar) + `pu` (posterior) | loan |
| `bado-fena-pu` | **ahorrar** — poner valor para el futuro | `bado` (valor) + `fena` (poner) + `pu` (posterior) | to save money |
| `bado-gade` | **cuenta bancaria** — identidad de valor | `bado` (valor) + `gade` (identidad) | bank account |
| `bado-kopa-nara` | **cajero** — persona del banco | `bado` (valor) + `kopa` (contenedor) + `nara` (persona) | bank clerk |
| `bado-kopa-meka` | **cajero automático** — máquina del banco | `bado` (valor) + `kopa` (contenedor) + `meka` (máquina) | cash machine |
| `gama-mede` | **pesar** — medir la masa | `gama` (masa) + `mede` (medir) | to weigh |
| `gama-mede-feke` | **balanza** — herramienta para medir la masa | `gama` (masa) + `mede` (medir) + `feke` (herramienta) | scale |
| `kema-lobe` | **paquete** — objeto cubierto | `kema` (objeto) + `lobe` (cubierta) | package |
| `kopa-goda` | **caja** — contenedor sólido | `kopa` (contenedor) + `goda` (estado sólido) | box |
| `kopa-duma` | **carrito** — contenedor móvil | `kopa` (contenedor) + `duma` (movimiento) | cart |
| `kema-seta-doke` | **inventario** — datos del conjunto de objetos | `kema` (objeto) + `seta` (conjunto) + `doke` (información) | inventory |
| `kema-seta-kuma` | **almacén** — casa del conjunto de objetos | `kema` (objeto) + `seta` (conjunto) + `kuma` (hogar) | warehouse |
| `pema-lu` | **entrega** — dar lejos | `pema` (dar) + `lu` (lejos) | delivery |
| `fadu-beka` | **garantía** — seguridad escrita | `fadu` (seguridad) + `beka` (escritura) | warranty |
| `telo-pema` | **devolver** — dar de regreso | `telo` (cambiar) + `pema` (dar) | to return an item |
| `kume-fedo-no` | **trueque** — intercambio sin pago | `kume` (intercambio) + `fedo` (pago) + `no` (negación) | barter |
| `dapa-bado` | **total a pagar** — suma de valor | `dapa` (suma) + `bado` (valor) | total |
| `kume-pose` | **puesto de venta** — posición de intercambio | `kume` (intercambio) + `pose` (posición) | stall |
| `bado-mado` | **contabilidad** — cálculo de valor | `bado` (valor) + `mado` (cálculo) | accounting |
| `bado-pu-seta` | **presupuesto** — conjunto de valor futuro | `bado` (valor) + `pu` (posterior) + `seta` (conjunto) | budget |
| `kera-fedo-nume` | **pedido** — deseo de comprar | `kera` (obtener) + `fedo` (pago) + `nume` (deseo) | order |

## Lote 12 — Cuerpo humano (43 términos)

| Forma | Significado | Partes | Inglés |
|---|---|---|---|
| `nara-bora` | **cuerpo humano** — cuerpo de persona | `nara` (persona) + `bora` (cuerpo) | human body |
| `bora-palo` | **órgano** — parte del cuerpo | `bora` (cuerpo) + `palo` (parte) | organ |
| `bora-kefe-kado` | **espalda** — lado del soporte del cuerpo | `bora` (cuerpo) + `kefe` (sostener) + `kado` (lado geométrico) | back |
| `maku-rela-go` | **hombro** — unión alta del brazo | `maku` (mano) + `rela` (unión) + `go` (arriba) | shoulder |
| `maku-rela-telo` | **codo** — cambio del brazo | `maku` (mano) + `rela` (unión) + `telo` (cambiar) | elbow |
| `maku-kefe` | **muñeca** — soporte de la mano | `maku` (mano) + `kefe` (sostener) | wrist |
| `maku-doma` | **palma** — centro de la mano | `maku` (mano) + `doma` (corazón) | palm |
| `maku-sena` | **huella dactilar** — signo de la mano | `maku` (mano) + `sena` (signo) | fingerprint |
| `kalu-rela` | **cadera** — unión de la pierna | `kalu` (pierna) + `rela` (unión) | hip |
| `kalu-gore-gume` | **muslo** — materia grande de la pierna | `kalu` (pierna) + `gore` (tamaño) + `gume` (materia) | thigh |
| `kalu-gune-rela` | **tobillo** — unión del pie | `kalu` (pierna) + `gune` (fin) + `rela` (unión) | ankle |
| `kalu-gune-palo` | **dedo del pie** — parte del pie | `kalu` (pierna) + `gune` (fin) + `palo` (parte) | toe |
| `kalu-gune-gu` | **talón** — abajo del pie | `kalu` (pierna) + `gune` (fin) + `gu` (abajo) | heel |
| `bora-doma` | **ombligo** — centro del cuerpo | `bora` (cuerpo) + `doma` (corazón) | navel |
| `bora-rela` | **cintura** — unión del cuerpo | `bora` (cuerpo) + `rela` (unión) | waist |
| `sabe-nado` | **garganta** — acceso de la boca | `sabe` (boca) + `nado` (acceso) | throat |
| `sabe-lobe` | **labio** — cubierta de la boca | `sabe` (boca) + `lobe` (cubierta) | lip |
| `loke-sabe-kado` | **mejilla** — lado de la cara | `loke` (ojo) + `sabe` (boca) + `kado` (lado geométrico) | cheek |
| `loke-go` | **frente** — arriba de los ojos | `loke` (ojo) + `go` (arriba) | forehead |
| `loke-nelo` | **ceja** — planta del ojo | `loke` (ojo) + `nelo` (planta) | eyebrow |
| `loke-lobe` | **párpado** — cubierta del ojo | `loke` (ojo) + `lobe` (cubierta) | eyelid |
| `loke-lobe-nelo` | **pestaña** — planta de la cubierta del ojo | `loke` (ojo) + `lobe` (cubierta) + `nelo` (planta) | eyelash |
| `sabe-nelo` | **barba** — planta de la boca | `sabe` (boca) + `nelo` (planta) | beard |
| `sabe-gu` | **mentón** — abajo de la boca | `sabe` (boca) + `gu` (abajo) | chin |
| `suma-suna-nado` | **vaso sanguíneo** — acceso de la sangre | `suma` (vida) + `suna` (agua) + `nado` (acceso) | blood vessel |
| `bora-suna-gase` | **riñón** — limpieza del agua del cuerpo | `bora` (cuerpo) + `suna` (agua) + `gase` (limpieza) | kidney |
| `fame-duma-kore` | **intestino** — camino de la comida | `fame` (comida) + `duma` (movimiento) + `kore` (lugar) | intestine |
| `bora-suna-kopa` | **vejiga** — contenedor del agua del cuerpo | `bora` (cuerpo) + `suna` (agua) + `kopa` (contenedor) | bladder |
| `go-gu-kefe` | **columna vertebral** — soporte vertical | `go` (arriba) + `gu` (abajo) + `kefe` (sostener) | spine |
| `doma-kopa-kefe` | **costilla** — soporte del pecho | `doma` (corazón) + `kopa` (contenedor) + `kefe` (sostener) | rib |
| `tume-kefe` | **cráneo** — soporte de la cabeza | `tume` (cabeza) + `kefe` (sostener) | skull |
| `bora-kefe-rela` | **articulación** — unión de huesos | `bora` (cuerpo) + `kefe` (sostener) + `rela` (unión) | joint |
| `bora-faro-rela` | **tendón** — unión del músculo | `bora` (cuerpo) + `faro` (fuerza) + `rela` (unión) | tendon |
| `sabe-suna` | **saliva** — agua de la boca | `sabe` (boca) + `suna` (agua) | saliva |
| `loke-suna-gume` | **lágrima** — materia del llanto | `loke` (ojo) + `suna` (agua) + `gume` (materia) | tear |
| `reka-sone-dore` | **voz** — forma del sonido al hablar | `reka` (comunicación) + `sone` (sonido) + `dore` (forma) | voice |
| `doma-kelo` | **latido** — ciclo del corazón | `doma` (corazón) + `kelo` (ciclo) | heartbeat |
| `suma-dure` | **edad** — duración de la vida | `suma` (vida) + `dure` (duración) | age |
| `bora-dabo-suna` | **orina** — agua de desecho del cuerpo | `bora` (cuerpo) + `dabo` (suciedad) + `suna` (agua) | urine |
| `bora-dabo-gume` | **excremento** — materia de desecho del cuerpo | `bora` (cuerpo) + `dabo` (suciedad) + `gume` (materia) | excrement |
| `naku-bo` | **embarazo** — hijo en el interior | `naku` (descendiente) + `bo` (interior) | pregnancy |
| `sura-bosa-sone` | **tos** — sonido del aire roto | `sura` (aire) + `bosa` (rotura) + `sone` (sonido) | cough |
| `sabe-lena-po` | **sonrisa** — risa menor | `sabe` (boca) + `lena` (agrado) + `po` (menos) | smile |

## Lote 13 — Cocina y alimentos (53 términos)

| Forma | Significado | Partes | Inglés |
|---|---|---|---|
| `suna-boga-dare` | **hervir** — hacer vapor del agua | `suna` (agua) + `boga` (estado gaseoso) + `dare` (hacer) | to boil |
| `mase-pore-dare` | **freír** — cocinar con grasa y fuego | `mase` (recurso) + `pore` (fuego) + `dare` (hacer) | to fry |
| `pore-kuma` | **horno** — casa de fuego | `pore` (fuego) + `kuma` (hogar) | oven |
| `pore-kuma-dare` | **hornear** — hacer en el horno | `pore` (fuego) + `kuma` (hogar) + `dare` (hacer) | to bake |
| `pore-salo-dare` | **asar** — hacer con llama | `pore` (fuego) + `salo` (luz) + `dare` (hacer) | to roast |
| `gume-rela-dare` | **mezclar** — hacer unión de materias | `gume` (materia) + `rela` (unión) + `dare` (hacer) | to mix |
| `lobe-delo` | **pelar** — tomar la cubierta | `lobe` (cubierta) + `delo` (tomar) | to peel |
| `nobe-pume` | **beber** — comer bebida | `nobe` (bebida) + `pume` (comer) | to drink |
| `fame-pema` | **servir comida** — dar comida | `fame` (comida) + `pema` (dar) | to serve food |
| `fure-pa-dare` | **calentar** — hacer caliente | `fure` (temperatura) + `pa` (más) + `dare` (hacer) | to warm up |
| `fure-po-dare` | **enfriar** — hacer frío | `fure` (temperatura) + `po` (menos) + `dare` (hacer) | to cool |
| `sabe-gume` | **condimento** — materia del sabor | `sabe` (boca) + `gume` (materia) | seasoning |
| `tabu-gume-suna` | **masa de harina** — harina con agua | `tabu` (pan) + `gume` (materia) + `suna` (agua) | dough |
| `pado-nelo-fame` | **grano** — semilla de comida | `pado` (comienzo) + `nelo` (planta) + `fame` (comida) | grain |
| `nede-fame-seta` | **ensalada** — conjunto de verdura | `nede` (verde) + `fame` (comida) + `seta` (conjunto) | salad |
| `lena-gume-fame` | **postre** — comida de azúcar | `lena` (agrado) + `gume` (materia) + `fame` (comida) | dessert |
| `fame-luda` | **salsa** — comida líquida | `fame` (comida) + `luda` (estado líquido) | sauce |
| `naku-nobe-mase` | **mantequilla** — grasa de la leche | `naku` (descendiente) + `nobe` (bebida) + `mase` (recurso) | butter |
| `nelo-maku-nobe` | **té** — bebida de hoja | `nelo` (planta) + `maku` (mano) + `nobe` (bebida) | tea |
| `mase-pore-kopa` | **sartén** — contenedor para freír | `mase` (recurso) + `pore` (fuego) + `kopa` (contenedor) | frying pan |
| `suna-fame-feke` | **cuchara** — herramienta de sopa | `suna` (agua) + `fame` (comida) + `feke` (herramienta) | spoon |
| `fame-kefe-feke` | **tenedor** — herramienta para sostener la comida | `fame` (comida) + `kefe` (sostener) + `feke` (herramienta) | fork |
| `nobe-kopa-gore` | **jarra** — contenedor grande de bebida | `nobe` (bebida) + `kopa` (contenedor) + `gore` (tamaño) | jug |
| `nobe-kopa-kose` | **botella** — contenedor cerrado de bebida | `nobe` (bebida) + `kopa` (contenedor) + `kose` (cerrar) | bottle |
| `delo-nuse-tabe` | **tabla de cortar** — superficie de cortar | `delo` (tomar) + `nuse` (vacío) + `tabe` (superficie de apoyo) | cutting board |
| `fame-foma` | **receta** — reglas de la comida | `fame` (comida) + `foma` (regla) | recipe |
| `fame-palo` | **ingrediente** — parte de la comida | `fame` (comida) + `palo` (parte) | ingredient |
| `fame-gore-po` | **porción** — comida pequeña | `fame` (comida) + `gore` (tamaño) + `po` (menos) | portion |
| `pore-so` | **crudo** — sin fuego | `pore` (fuego) + `so` (sin) | raw |
| `pore-ko` | **cocido** — con fuego | `pore` (fuego) + `ko` (con) | cooked |
| `fame-bosa` | **podrido** — comida rota | `fame` (comida) + `bosa` (rotura) | rotten |
| `lena-no-sabe` | **amargo** — sabor sin agrado | `lena` (agrado) + `no` (negación) + `sabe` (boca) | bitter |
| `pore-dare-nara` | **cocinero** — persona que cocina | `pore` (fuego) + `dare` (hacer) + `nara` (persona) | chef |
| `fame-fedo-kore` | **restaurante** — lugar de comida con pago | `fame` (comida) + `fedo` (pago) + `kore` (lugar) | restaurant |
| `tabu-kuma` | **panadería** — casa del pan | `tabu` (pan) + `kuma` (hogar) | bakery |
| `bora-gume-kuma` | **carnicería** — casa de carne | `bora` (cuerpo) + `gume` (materia) + `kuma` (hogar) | butcher shop |
| `palata` | **palta** — nombre adaptado | raíz nueva | avocado |
| `tomate` | **tomate** — nombre adaptado | raíz nueva | tomato |
| `seboea` | **cebolla** — nombre adaptado | raíz nueva | onion |
| `sanaorea` | **zanahoria** — nombre adaptado | raíz nueva | carrot |
| `terego` | **trigo** — nombre adaptado | raíz nueva | wheat |
| `ferekolo` | **frijol** — nombre adaptado | raíz nueva | bean |
| `abana` | **haba** — nombre adaptado | raíz nueva | broad bean |
| `arabeka` | **arveja** — nombre adaptado | raíz nueva | pea |
| `ako` | **ajo** — nombre adaptado | raíz nueva | garlic |
| `lemono` | **limón** — nombre adaptado | raíz nueva | lemon |
| `naranaka` | **naranja** — nombre adaptado | raíz nueva | orange |
| `manasana` | **manzana** — nombre adaptado | raíz nueva | apple |
| `uba` | **uva** — nombre adaptado | raíz nueva | grape |
| `kamoto` | **camote** — nombre adaptado | raíz nueva | sweet potato |
| `lechuga` | **lechuga** — nombre adaptado | raíz nueva | lettuce |
| `kafea` | **café** — nombre adaptado | raíz nueva | coffee |
| `kakao` | **cacao** — nombre adaptado | raíz nueva | cocoa |

## Lote 14 — Agricultura y campo (39 términos)

| Forma | Significado | Partes | Inglés |
|---|---|---|---|
| `taro-nelo-daro` | **agricultura** — trabajo de tierra y planta | `taro` (tierra) + `nelo` (planta) + `daro` (trabajo) | agriculture |
| `taro-nelo-nara` | **agricultor** — persona de tierra y planta | `taro` (tierra) + `nelo` (planta) + `nara` (persona) | farmer |
| `taro-nelo-kore` | **campo de cultivo** — lugar de tierra y planta | `taro` (tierra) + `nelo` (planta) + `kore` (lugar) | field |
| `taro-pose` | **terreno** — posición de tierra | `taro` (tierra) + `pose` (posición) | plot of land |
| `nelo-dare` | **cultivar** — hacer plantas | `nelo` (planta) + `dare` (hacer) | to cultivate |
| `pado-nelo-fena` | **sembrar** — poner semilla | `pado` (comienzo) + `nelo` (planta) + `fena` (poner) | to sow |
| `nelo-kera` | **cosechar** — obtener de la planta | `nelo` (planta) + `kera` (obtener) | to harvest |
| `nelo-kera-kema` | **cosecha** — objeto de cosechar | `nelo` (planta) + `kera` (obtener) + `kema` (objeto) | crop yield |
| `nelo-kera-tera` | **época de cosecha** — tiempo de cosechar | `nelo` (planta) + `kera` (obtener) + `tera` (tiempo) | harvest season |
| `nelo-suna-pema` | **regar** — dar agua a la planta | `nelo` (planta) + `suna` (agua) + `pema` (dar) | to irrigate |
| `taro-bure` | **arar** — abrir la tierra | `taro` (tierra) + `bure` (abrir) | to plough |
| `taro-fame-gume` | **abono** — materia para tierra fértil | `taro` (tierra) + `fame` (comida) + `gume` (materia) | fertilizer |
| `nelo-suna-duma` | **canal de riego** — movimiento de agua de las plantas | `nelo` (planta) + `suna` (agua) + `duma` (movimiento) | irrigation channel |
| `taro-bure-meka` | **tractor** — máquina de arar | `taro` (tierra) + `bure` (abrir) + `meka` (máquina) | tractor |
| `taro-bure-feke` | **arado** — herramienta de arar | `taro` (tierra) + `bure` (abrir) + `feke` (herramienta) | plough (tool) |
| `taro-delo-feke` | **pala** — herramienta para tomar tierra | `taro` (tierra) + `delo` (tomar) + `feke` (herramienta) | shovel |
| `taro-bosa-feke` | **azada** — herramienta de romper tierra | `taro` (tierra) + `bosa` (rotura) + `feke` (herramienta) | hoe |
| `nelo-bosa-feke` | **hoz** — herramienta de romper plantas | `nelo` (planta) + `bosa` (rotura) + `feke` (herramienta) | sickle |
| `ruma-nelo-kuma` | **granja** — casa de animales y plantas | `ruma` (animal) + `nelo` (planta) + `kuma` (hogar) | farm |
| `ruma-kopa` | **corral** — contenedor de animales | `ruma` (animal) + `kopa` (contenedor) | corral |
| `ruma-fame-daro` | **ganadería** — trabajo de animales de alimento | `ruma` (animal) + `fame` (comida) + `daro` (trabajo) | livestock farming |
| `ruma-fame-nara` | **pastor** — persona del ganado | `ruma` (animal) + `fame` (comida) + `nara` (persona) | herder |
| `ruma-fame-nelo` | **pasto** — planta del ganado | `ruma` (animal) + `fame` (comida) + `nelo` (planta) | pasture |
| `ruma-kuna-kuma` | **gallina** — pájaro de casa | `ruma` (animal) + `kuna` (cielo) + `kuma` (hogar) | hen |
| `ruma-naku-nobe` | **vaca** — animal de la leche | `ruma` (animal) + `naku` (descendiente) + `nobe` (bebida) | cow |
| `ruma-bume` | **oveja** — animal de ropa | `ruma` (animal) + `bume` (ropa) | sheep |
| `ruma-bume-gume` | **lana** — materia de la ropa animal | `ruma` (animal) + `bume` (ropa) + `gume` (materia) | wool |
| `ruma-mase` | **cerdo** — animal de grasa | `ruma` (animal) + `mase` (recurso) | pig |
| `ruma-duma-feke` | **caballo** — animal herramienta de movimiento | `ruma` (animal) + `duma` (movimiento) + `feke` (herramienta) | horse |
| `ruma-taro-go` | **llama andina** — animal de la montaña | `ruma` (animal) + `taro` (tierra) + `go` (arriba) | llama |
| `ruma-fadu` | **perro** — animal de seguridad | `ruma` (animal) + `fadu` (seguridad) | dog |
| `ruma-kuma-po` | **gato** — animal pequeño de casa | `ruma` (animal) + `kuma` (hogar) + `po` (menos) | cat |
| `ku-kalu-bosa` | **plaga** — insectos que rompen | `ku` (6) + `kalu` (pierna) + `bosa` (rotura) | pest |
| `nelo-bado-no` | **maleza** — planta sin valor | `nelo` (planta) + `bado` (valor) + `no` (negación) | weed |
| `nelo-suna-goda` | **helada** — hielo de las plantas | `nelo` (planta) + `suna` (agua) + `goda` (estado sólido) | frost |
| `pado-nelo-kuma` | **silo** — casa de semillas | `pado` (comienzo) + `nelo` (planta) + `kuma` (hogar) | granary |
| `tabu-gume-meka` | **molino** — máquina de harina | `tabu` (pan) + `gume` (materia) + `meka` (máquina) | mill |
| `suna-taro-gu` | **pozo** — agua bajo la tierra | `suna` (agua) + `taro` (tierra) + `gu` (abajo) | well |
| `nede-fame-kore` | **huerto** — lugar de verduras | `nede` (verde) + `fame` (comida) + `kore` (lugar) | vegetable garden |
