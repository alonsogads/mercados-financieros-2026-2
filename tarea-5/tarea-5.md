# Tarea 5: Curvas de interés

## Teoría

1. **Describe con tus propias palabras, ¿qué es una curva de tasas de interés?**

Una curva de tasas de interés es, en esencia, una gráfica que nos muestra cuánto cuesta el dinero dependiendo de cuánto tiempo lo pidamos prestado o lo invirtamos. Si graficamos en el eje $X$ el tiempo (o plazo al vencimiento) y en el eje $Y$ la tasa de rendimiento que ofrece el mercado, obtenemos esta curva. En condiciones normales, la curva va hacia arriba (es decir una pendiente positiva). Esto se debe por ejemplo, a que si se presta dinero a 10 años, se asume más riesgo (como inflación o impago) que si lo presto la misma cantidad a 1 año, y por consecuencia se exige que se pague a una tasa mayor. Esta curva es nuestra referencia principal para saber cómo percibe el mercado la economía a futuro y para valuar cualquier otro instrumento de deuda.

1. **¿Qué es una tasa spot?**

Una tasa spot, que suele denotar como $s_t$, es la tasa de interés real que el mercado nos ofrece hoy para una inversión que dura exactamente hasta el tiempo $t$, asumiendo que no hay ningún pago intermedio. Es decir, es el rendimiento exacto de un bono cupón cero.

Formalmente, si conocemos el precio actual $P$ de un bono cupón cero que promete pagar un valor nominal $F$ al final del periodo $t$, obtenemos la tasa spot despejando de la ecuación básica de valor presente:

$$
P= \frac{F}{(1+s_t)^t} \quad \Longrightarrow \quad s_t= (\frac{F}{P})^{1/t}-1
$$

Al no haber cupones de por medio, esta ecuación nos da el costo real del dinero para ese plazo exacto, sin tener que preocuparnos por a qué tasa vamos a reinvertir las ganancias intermedias.

1. **¿Cuál es la diferencia entre las tasas spot y la tasa de rendimiento "yield" de un bono?**

La principal diferencia es que la tasa spot es exacta para un solo pago en el futuro, mientras que el *Yield to Maturity* (YTM) es solo un promedio. Cuando un bono paga cupones, el YTM calcula una sola tasa (una TIR) para descontar todos esos pagos, asumiendo teóricamente que cada vez que cobramos un cupón, inmediatamente se reinvierte a esa misma tasa YTM. Como sabemos, eso rara vez pasa en el mundo real porque las tasas cambian todo el tiempo. En cambio, si usamos tasas spot, cada flujo de efectivo del bono se descuenta con su propia tasa $s_t$ correspondiente a su año $t$ , dándonos una valuación limpia sin el la suciedad que genera el pago de los cupones.

1. **¿Qué es la estructura temporal de tasas de interés?**

La estructura temporal se refiere específicamente a la relación que existe entre las tasas spot ($s_t$) y sus diferentes plazos de maduración ($t$), asumiendo que el riesgo es exactamente el mismo o bien que sean libres de riesgo. Tener la estructura temporal es fundamental porque nos da una un conjunto de tasas libres de la distorsión de los cupones, permitiéndonos valuar cualquier portafolio o derivado descontando cada flujo de efectivo al precio exacto que tiene el dinero en ese punto del tiempo.

La estructura temporal de tasas de interés se define como la relación que existe entre el tiempo de maduración $t$ de una inversión y su tasa de rendimiento real, es decir, su tasa spot, asumiendo que el riesgo es exactamente el mismo o bien que sean libres de riesgo, es decir aplicables exclusivamente a bonos cupón cero para diferentes plazos. A diferencia de una curva de tasas que promedia instrumentos con distintos pagos intermedios, la estructura temporal nos proporciona el costo exacto del dinero para cada periodo individual. Esta relación es indispensable al momento de valuar instrumentos financieros, ya que nos obliga a descontar cada flujo de efectivo futuro utilizando la tasa específica que le corresponde en el tiempo exacto en que ocurre, garantizando así un precio justo para el instrumento.

1. **¿Qué es una tasa forward?**

Una tasa forward, o tasa a plazo ($f$), es una tasa de interés que se fija o acuerda el día de hoy, pero que va a aplicar para una inversión o préstamo que ocurrirá en el futuro (por ejemplo, pactar hoy a qué tasa se emitirá un instrumento del año 2 al año 3). Para el cálculo de estas tasa, la lógica es que invertir directo a un plazo largo $t+k$ debe dar exactamente el mismo dinero que invertir a un plazo corto $t$ y luego reinvertir ese capital durante $k$ tiempo a la tasa forward.

Formalmente, la tasa forward se obtiene a partir de las tasas spot de esos dos plazos:

$$
(1 + S_t)^t \cdot (1 + f)^k = (1 + S_{t+k})^{t+k} \Longrightarrow f = \left[ \frac{(1 + s_{t+k})^{t+k}}{(1 + s_t)^t} \right]^{1/k} - 1
$$

Despejando $f$, obtenemos la expectativa real que tiene el mercado hoy sobre cuáles serán las tasas de interés en el futuro.

1. **Investiga qué dice la Teoría de curvas de tasas de Prima por Liquidez. Incluye la fuente.**

La Teoría de la Prima por Liquidez argumenta que, por naturaleza, los inversionistas son adversos al riesgo y tienen una fuerte preferencia por mantener su dinero en instrumentos a corto plazo, ya que estos les otorgan mayor flexibilidad financiera y los protegen de la incertidumbre macroeconómica. Si un emisor quiere convencer a un inversionista de invertir su capital en un bono a largo plazo, debe compensarlo económicamente por el riesgo asumido (como posibles fluctuaciones en las tasas de interés o la inflación a lo largo de esos años). Por lo tanto, esta teoría postula que la tasa de interés a largo plazo no es simplemente un promedio de las tasas de corto plazo esperadas, sino que se le debe sumar obligatoriamente un "premio" o prima por liquidez para volverla atractiva. Esta prima tiene un valor positivo y va aumentando conforme crece el plazo de maduración de la inversión, lo que explica de manera económica por qué la curva de tasas de interés en la vida real casi siempre tiene una pendiente ascendente.

**Fuente:** StudySmarter. (s.f.). *Teoría de la Prima por Liquidez*. Recuperado de [https://www.studysmarter.es/resumenes/economia/macroeconomia/teoria-de-la-prima-por-liquidez/](https://www.studysmarter.es/resumenes/economia/macroeconomia/teoria-de-la-prima-por-liquidez/)

1. **Investiga qué dice la Teoría de curvas de tasas de Segmentación del Mercado. Incluye la fuente.**

La Teoría de la Segmentación del Mercado se fundamenta en la idea de que los mercados financieros están estrictamente divididos o segmentado en diferentes plazos o que operan de manera independiente. En lugar de concebir la estructura temporal como un flujo continuo, esta teoría argumenta que cada horizonte de inversión funciona como un segmento aislado. Esto se debe a que los participantes del mercado tienen necesidades, perfiles de riesgo y planeación muy marcados, lo que los lleva a preferir operar exclusivamente en su segmento ideal y a no sustituir plazos, sin importar si otro horizonte ofrece temporalmente un mayor rendimiento. En consecuencia, el comportamiento de las tasas de interés para un plazo específico no se ve influenciado por las expectativas de otros plazos, sino que se determina única y exclusivamente por la interacción directa de la oferta y la demanda de fondos dentro de ese mismo segmento de mercado.

**Fuente:** [1] StudySmarter. (s.f.). *Teoría de la Segmentación del Mercado: Conceptos, Ejemplos*. Recuperado de [https://www.studysmarter.es/resumenes/economia/macroeconomia/teoria-de-la-segmentacion-del-mercado/](https://www.studysmarter.es/resumenes/economia/macroeconomia/teoria-de-la-segmentacion-del-mercado/)