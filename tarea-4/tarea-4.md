# Tarea 4: Bonos II

Fecha: 15 de abril de 2026

### Ejercicio 1

**Considere un bono con valor facial de $1,000 que madura al 105 en 7 años y fue emitido el 7 de noviembre de 2023. Ofrece una tasa cupón del 8.6% pagadera cuatrimestral y un rendimiento del 8% nominal trimestral.**

Establecemos las variables y tasas que usaremos en este ejercicio.

- $F=1,000$
- $C = 1000*1.05=1,050$
- $r = 0.086/3 \approx 0.028\overline{6}$ efectiva cuatrimestral
- $i_{\text{trim}} = 0.08/4 =0.02$ efectiva trimestral. Buscamos la efectiva cuatrimestral:

$$
(1+i_\text{cuat})^3 = (1+i_\text{trim})^4 \Longrightarrow i_\text{cuat}=(1+i_\text{trim})^{4/3}-1
$$

$$
i = (1+0.02)^{4/3}-1 \approx 1.026755-1 =0.026755 \quad \text{efectiva cuatrim}
$$

- Valor del cupón: $F\cdot r = 1.000 \cdot 0.028\overline{6} = 28.\overline{6}$
- Como los bonos son cuatrimestrales (3 bonos por año), entonces el plazo es $n =7*3 = 21$ periodos.
- Además establecemos las fechas de:
Emisión: 07-Nov-2023
Vencimiento: 07/Nov/2030

a) ¿Cuál será el precio de mercado de este bono al día de hoy? Resuelva por método semi-teórico y convención actual/360.

Establecemos que la fecha de valuación (hoy) es 15/Abr/2026.

Los bonos son cuatrimestrales. Las fechas de pago de bono son:

- 07/Nov
- 07/Mar
- 07/Jul

Por lo tanto, la fecha del último pago de cupón al momento de la valuación, fue en el tiempo $t=$ 07/Mar/2026. Sabemos que hay un total de 21 cupones o periodos, y que al día de hoy han transcurrido 2 años y 1 cuatrimestre (7 cupones pagados), por lo que aún restan $21-7 = 14$ cupones.

Entonces, calculamos el precio del bono en la última fecha de pago $B_t$ con $n=14$, usando la fórmula básica:

$$
B_t = (F\cdot r) \cdot \left( \frac{1-(1+i)^{-n}}{i} \right) + C \cdot (1+i)^{-n}
$$

$$
= (28.\overline{6}) \cdot \left( \frac{1-(1+0.26755)^{-14}}{0.26755} \right) + 1050 \cdot (1+0.26755)^{-14}
$$

$$
\approx 331.093817 + 725.52725 \approx 1.056.62
$$

Ahora realizamos el conteo de días desde la última fecha de pago hasta el día de hoy, considerando la convención act/360:

- Del 07/Mar/2026 al 31/Mar/2026 → 24 días
- Del 01/Abr/2026 al 15/Abr/2026 → 15 días
- Conteo total de 39 días

Como los periodos son cuatrimestrales, y la convención establece 360 días por año, se tiene que el cuatrimestre tiene $360/3 = 120$ dias. Calculamos la fracción del periodo $k$:

$$
k = \frac{39}{120}=0.325
$$

Aplicamos el método semi-teórico, y calculamos los valores del precio sucio y el cupón/interés acumulado:

- Flat price: $B_f =B_t (1+i)^k = 1,056.62 \cdot (1+0.026755)^{0.325} = 1,065.725961$
- Accrued coupon: $I_a =k \cdot Fr = 0.325 \cdot 28.\overline{6} \approx 9.32$

Finalmente obtenemos el precio de mercado (limpio) del bono al día de hoy:

$$
B_m = B_f-I_a = 1,065.725961-9.32 \approx \mathbf{1056.40}
$$

b) El 13 de febrero de 2026, el Banco Novo compró en el mercado secundario un lote de 1,000,000 de bonos como el descrito. ¿Cuál fue el precio que tuvo que pagar por el lote si pagó el precio teórico? Resuelva por método práctico y convención actual/actual.

Del inciso anterior, sabemos las fechas de pago. Si la valuación se hace hoy (13/Feb/2026), tenemos que la última fecha de pago fue en $t =$ 07/Nov/2025, con 6 cupones ya pagados y $n=21-6 =15$ cupones restantes. Calculamos $B_t$:

$$
B_t = (28.\overline{6}) \cdot \left( \frac{1-(1+0.26755)^{-15}}{0.26755} \right) + 1050 \cdot (1+0.26755)^{-15}
$$

$$
\approx 350.49+706.54 = 1,057.03
$$

Realizamos el nuevo conteo de días. Como lo haremos por la convención actual/actual:

- Contamos los días reales de todo el cuatrimestre (entre $B_t$ y $B_{t+1}$), es decir entre las fechas de pago de cupón al momento de la valuación (del 07/Nov/2025 al 07/Mar/2026):
    - Del 07/Nov/2025 al 31/Nov/2025 → 23 días
    - Del 01/Dic/2025 al 31/Dic/2025 → 31 días
    - Del 01/Ene/2026 al 31/Ene/2026 → 31 días
    - Del 01/Feb/2026 al 28/Feb/2026 → 28 días
    - Del 01/Mar/2026 al 07/Mar/2026 → 7 días
    - Conteo total de 120 días.
- Contamos los días reales transcurridos:
    - Del 07/Nov/2025 al 31/Nov/2025 → 23 días
    - Del 01/Dic/2025 al 31/Dic/2025 → 31 días
    - Del 01/Ene/2026 al 31/Ene/2026 → 31 días
    - Del 01//Feb/2026 al 13/Feb/2026 → 13 días
    - Conteo total de 98 días

Por lo tanto, la fracción de periodo es:

$k =\frac{98}{360} = 0.81\overline{6}$

Calculamos el precio teórico (por el que pago el banco) del bono con el método práctico:

$$
B_f=B_t(1+ik) = 1,057.03(1+0.026755 \cdot0.81\overline{6}) \\
\approx 1,057.03(1.021849) = 1,080.12
$$

Ese es el precio de un solo bono. Por lo que el pago total por el lote de 1,000,000 de bonos es de:

$$
\text{Pago total} =1,080.12 \cdot 1,000,000 = 1,080,120,000
$$

c) El Banco Novo revendió la mitad de su lote el 24 de marzo de 2026 para pagar obligaciones pendientes. ¿Cuánto recibió por la acumulación de cupones ganados a esa fecha? Utilize el método teórico y convención 30/360.

El momento de valuación es la fecha 24/Mar/2026, por lo que la última fecha de pago fue en $t=$ 07/Mar/2026. Como solo se nos pide calcular el acumulado de cupones, solo necesitamos calcular el valor del cupón acumulado.

Para ello necesitamos saber el valor de la fracción $k$ (respecto a un cuatrimestre). Usamos convención 30/360 para el conteo de días desde $t$ hasta el día de valuación:

$$
360(2026-2026) + 30 (3-3) + (24-7) =0+0+17 =17 \text{ dias} \\ \quad \\
k = \frac{17}{120} = 0.141\overline{6}
$$

Mediante el método teórico, calculamos el valor de un cupón acumulado:

$$
I_a =F\cdot r \cdot \left[ \frac{(1+i)^k -1}{i} \right]
$$

$$
= 28.\overline{6} \cdot \left[ \frac{(1+0.026755)^{0.141\overline{6} }- 1}{0.026755} \right] \approx 4.015236
$$

Como el banco vendió la mitad del lote (500,000 bonos), el total recibido por la acumulación de cupones fue de:

$$
\text{Total recibido} = 4.015236 \cdot 500,000 = 2,007,618
$$

d) El día 1 de abril de 2026 el Banco Novo le pidió a un broker que publicara la venta de los bonos que le restaban y el broker publicó en la Bolsa el precio de dichos bonos. ¿Qué preció apareció en las pantallas de la Bolsa? Utilize el método teórico y convención act/360.

La valuación se hace el 01/Abr/2026. Necesitamos calcular el precio en pantallas, es decir el precio limpio (market price) ubicado entre las fechas de pago. El último pago fue nuevamente en $t=$ 07/Mar/2026.

Hacemos el conteo de días desde la fecha del último pago hasta el día de valuación, con la convención act/360:

- Del 07/Mar/2026 al 31/Mar/2026 → 24 días
- Del 01/Abr/2026 al 01/Abr/2026 → 1 día
- Conteo total de 25 días

La convención nos dice que el cuatrimestre tiene 120 días, entonces $k =\frac{25}{120}=0.208\overline{3}$.

El valor del bono en el tiempo $t=$ 07/Mar/2026 es el mismo que obtuvimos en el inciso a, $B_t = 1056.62$. Entonces, mediante el método teórico, calculamos el precio sucio y el cupón acumulado:

- $B_f =B_t (1+i)^k = 1,056.62 \cdot (1+0.026755)^{0.208\overline{3}} \approx 1,057.802668$
- $I_a =k \cdot Fr = 0.208\overline{3} \cdot 28.\overline{6} \approx 5.972$

Calculamos el precio limpio en pantallas:

$$
B_m = B_f-I_a = 1,057.802668-5.972 \approx 1,051.83
$$

e) El día 1 de abril, en su oferta anterior, vendió 400,000 bonos. Finalmente, el 5 de abril de 2026 el Banco Novo logró revender los últimos 100,000 bonos que le quedaban y los colocó a un precio 8% más alto que el precio teórico. ¿Cuánto recibió por la venta de dichos bonos el 5 de abril?

Se nos pide calclar el nuevo precio del bono (8% más alto) sobre el precio teórico. Este último es el precio sucio. Definiremos el valor de las variables.

La valuación o fecha de venta se hace el 05/Abr/2026, por lo que la última fecha de pago fue en $t=$ 07/Mar/2026. Como no se nos especifica la convención, usamos la del banquero (act/360), usada en el inciso anterior:

- Del 07/Mar/2026 al 31/Mar/2026 → 24 días
- Del 01/Abr/2026 al 05/Abr/2026 → 5 día
- Conteo total de 29 días

La convención nos dice que el cuatrimestre tiene 120 días, entonces $k =\frac{29}{120}=0.241\overline{6}$.

Al igual que el anterior inciso (mismo último pago), usamos $B_t = 1056.62$.

Con el método teórico calculamos el precio teórico o precio sucio:

$$
B_f =B_t (1+i)^k = 1,056.62 \cdot (1+0.026755)^{0.241\overline{6}} \approx 1,063.383626
$$

El banco logró colocar esos bonos a un precio 8% sobre el precio teórico, por lo que el precio colocado de cada bono es de:

$$
B_f' = B_f \cdot 1.08 = 1,063.383626 \cdot 1.08 = 1,148.454317
$$

FInalmente el total de la venta por los 100,000 bonos es aproxamadamente de:

$$
1,148.454317 \cdot 100,000 = 114,845,431.70
$$

### Ejercicio 2

**Considere un bono con valor nominal de $1,000 que ofrece una tasa cupón del 10% pagadero semestral cupones liquidables el 15 de febrero y el 15 de agosto, cuya fecha de maduración es el 15 de agosto de 2030. El bono retribuye un rendimiento del 8% efectivo semestral.**

Definimos el valor de nuestras variables:

- $F = C = 1,000$ (asumimos redención a la par)
- $r^{(2)} = 0.1$ pagadero semestral, entonces $r=\frac{0.1}{2}=0.05$ efectiva semestral
- Valor del cupón: $F\cdot r = 50$
- Fechas de pago: 15/Feb, 15/Ago
- Maduración o vencimiento: 15/Ago/2030
- $i=0.08$ efectiva semestral

a) Considere la convención Actual/Actual y el método teórico y calcule el precio de mercado hoy (9 de abril de 2026).

La valuación se hace al día de hoy 09/Abr/2026. El último cupón se pago en $t=$ 15/Feb/2026. Desde $t$ a la fecha de maduración (15/Ago/2030), quedan $n=9$ semestres o cupones pendientes. Se nos pide calcular el precio mercado al día de hoy entre estas dos fechas.

Calculamos el precio del bono en el periodo $t$ con la fórmula básica:

$$
B_t = (50) \cdot \left( \frac{1-(1+0.08)^{-9}}{0.08} \right) + 1000 \cdot (1+0.08)^{-9}
$$

$$
\approx 312.344395 +500.248967 \approx 812.59
$$

Realizamos el conteo de días desde $t$ hasta el día de hoy considerando la convención Act/Act:

- Para el conteo de días transcurridos:
    - Del 15/Feb/2026 al 28/Feb/2026 → 13 días
    - Del 01/Mar/2026 al 31/Mar/2026 → 31 días
    - Del 01/Abr/2026 al 09/Abr/2026 → 9 días
    - Conteo total de 53 días
- Para el conteo de días reales del semestre actual (desde $t$ hasta $t+1$):
    - Del 15/Feb/2026 al 28/Feb/2026 → 13 días
    - Del 01/Mar/2026 al 31/Mar/2026 → 31 días
    - Del 01/Abr/2026 al 30/Abr/2026 → 30 días
    - Del 01/May/2026 al 31/May/2026 → 31 días
    - Del 01/Jun/2026 al 30/Jun2026 → 30 días
    - Del 01/Jul/2026 al 31/Jul/2026 → 31 días
    - Del 01/Ago/2026 al 15/Ago/2026 → 15 días
    - Conteo total de 181 días

Por lo que la fracción de periodo es $k =\frac{53}{181} \approx0.292817$.

Aplicamos método teórico y calculamos el flat price y el accrued coupon:

- $B_f =B_t (1+i)^k = 812.59 (1+0.08)^{\frac{53}{181}} \approx 831.11$
- $I_a = Fr \cdot \left[ \frac{(1+i)^k-1}{i} \right] = 50 \cdot \left[ \frac{(1+0.08)^{0.292817}-1}{0.08} \right] \approx 14.24$

Por lo tanto el precio de mercado es de:

$$
B_m = B_f -I_a = 831.11-14.24 = 816.87
$$

b) Considere la convención Actual/Actual y el método semi-práctico. Calcule el flat price para venderlo el día de entrega de esta tarea (15 de abril de 2026).

La valuación se hace en el día 15/Abr/2026. El último cupón se pago en $t=$ 15/Feb/2026. Desde $t$ a la fecha de maduración (15/Ago/2030), quedan $n=9$ semestres o cupones pendientes. Se nos pide calcular el precio flat o sucio al día de valuación entre estas dos fechas.

Notemos que como $t$ es la misma que el inciso anterior, tenemos que el mismo valor $B_t =812.59$.

Usamos convención Act/Act. Ya que el semestre actual es el mismo que el iniciso anterior, sabemos que el mismo tiene 181 días, solo falta calcular los días transcurridos con la nueva fecha de valuación:

- Del 15/Feb/2026 al 28/Feb/2026 → 13 días
- Del 01/Mar/2026 al 31/Mar/2026 → 31 días
- Del 01/Abr/2026 al 15/Abr/2026 → 15 días
- Conteo total de 59 días

Entonces $k = \frac{59}{181} \approx 0.325966$. Aplicamos el método semi-práctico para el cálculo del precio sucio:

$$
B_f = B_t (1+i)^k = 812.59(1+0.08)^{0.325966}\approx 833.23
$$

c) Considere la convención del banquero. Calcule cual será el precio limpio al 8 de septiembre de 2026.

La valuación se hace en el día 08/Sep/2026. El último cupón se pagó en $t=$ 15/Ago/2026. Desde $t$ a la fecha de maduración (15/Ago/2030), quedan $n=8$ semestres o cupones pendientes. Se nos pide calcular el precio limpio al día de valuación entre estas dos fechas.

Calculamos el precio del bono en el periodo $t$ con la fórmula básica:

$$
B_t = (50) \cdot \left( \frac{1-(1+0.08)^{-8}}{0.08} \right) + 1000 \cdot (1+0.08)^{-8}
$$

$$
\approx 287.332 + 540.569 \approx 827.60
$$

Realizamos el conteo de días trascurridos desde $t$ hasta el día de valuación considerando la convención del banquero (Act/360):

- Del 15/Ago/2026 al 31/Ago/2026 → 16 días
- Del 01/Sep/2026 al 08/Sep/2026 → 8 días
- Conteo total de 24 días

En esta convención, si se tiene 360 días por año, entonces hay 180 días por semestre. Por lo que $k =\frac{24}{180} \approx 0.1\overline{3}$.

Como no se nos menciona el método, asumimos teórico. Calculamos el precio sucio y el cupón acumulado:

- $B_f =B_t (1+i)^k = 827.60 (1+0.08)^{0.1\overline{3}} \approx 836.136$
- $I_a = Fr \cdot \left[ \frac{(1+i)^k-1}{i} \right] = 50 \cdot \left[ \frac{(1+0.08)^{0.1\overline{3}}-1}{0.08} \right] \approx 6.446$

Por lo tanto el precio limpio es:

$$
B_m = B_f -I_a = 836.136-6.446 \approx 829.69
$$

### Ejercicio 3

**Considere un bono con F = $10,000 que redime al 95, cuya tasa cupón es del 12% pagadero cuatrimestral que ofrece un rendimiento del 15% nominal bimestral. El pago de los cupones es cada 10 de febrero, 10 de junio y 10 de octubre. Madura hasta el 10 de febrero de 2027. Con los métodos y convención señalados, calcule el precio flat y market al que se debe vender hoy 9 de abril del 2026.**

Primero, definimos el valor de nuestras variables.

- $F =10,000$
- $C = 10,000 \cdot 0.95 = 9,500$
- $r^{(3)} = 0.12$ pagadero cuatrimestral, por lo que $r=\frac{0.12}{3} = 0.04$ efectiva cuatrimestral
- $i^{(6)} = 0.15$ nominal bimestral, por lo que $i_\text{bim} =\frac{0.15}{6} = 0.025$ efectiva bimestral. Necesitamos la efectiva cuatrimestral, entonces:

$$
(1+i_\text{bim})^6 = (1+i_\text{cuat})^3 \quad \Longrightarrow \quad i_\text{cuat} = (1+i_\text{bim})^{6/3}-1
$$

$$
i = (1+0.025)^2-1 = 0.050625 \quad  \text{efectiva cuatrimestral}
$$

- Valor del cupón: $F\cdot r = 10,000 \cdot 0.04 = 400$
- Fecha de pagos: 10/Feb, 10/Jun, 10/Oct
- Maduración: 10/Feb/2027
- Fecha de valuación (hoy): 09/Abr/2026
- Fecha de último pago: $t =$  10/Feb/2026
- Cupones/cuatrimestres restantes (desde $t$ hasta la maduración): $n =3$

Independientemente del método y la convención, el valor del bono en el periodo $t$ (con fórmula básica) es:

$$
B_t = 400 \cdot \left[ \frac{1 - (1.050625)^{-3}}{0.050625} \right] + 9500 \cdot (1.050625)^{-3}
$$

$$
B_t \approx 1088.2624 + 8191.5346 \approx 9,279.79
$$

a) Convención act/act y método práctico

Realizamos el conteo real de días, desde $t =$  10/Feb/2026, con act/act:

- Para los días transcurridos (i.e. hasta hoy):
    - Del 10/Feb/2026 al 28/Feb/2026 → 18 días
    - Del 01/Mar/2026 al 31/Mar/2026 → 31 días
    - Del 01/Abr/2026 al 09/Abr/2026 → 9 días
    - Conteo total de 58 días
- Para los días reales del cuatrimestre actual (i.e. hasta $t+1$):
    - Del 10/Feb/2026 al 28/Feb/2026 → 18 días
    - Del 01/Mar/2026 al 31/Mar/2026 → 31 días
    - Del 01/Abr/2026 al 30/Abr/2026 → 30 días
    - Del 01/May/2026 al 31/May/2026 → 31 días
    - Del 01/Jun/2026 al 10/Jun/2026 → 10 días
    - Conteo total de 120 días

Entonces la fracción de periodo cuatrimestral es $k= \frac{58}{120}$.

Usando el método práctico, calculamos los precios flat y market junto con el cupón acumulado:

- $B_f = B_t(1+ik) = 9,279.79 (1+0.050625 \cdot \frac{58}{120}) \approx 9506.85$
- $I_a = k \cdot Fr = \frac{58}{120} \cdot 400 = 193.\overline{3}$
- $B_m = B_f - I_a = 9506.85-193.\overline{3} \approx 9,313.51$

b) Convención 30/360 y método teórico

Realizamos el conteo real de días, desde $t =$  10/Feb/2026, con 30/360:

- Para los días transcurridos (i.e. hasta 09/Abr/2026):

$360(2026-2026) +30(04-02)+(09-10) = 0+30(2)+(-1) =60-1$= 59 días

- El cuatrimestre en 30/360 tiene $\frac{360}{3}=120$ días.

Entonces la fracción de periodo cuatrimestral es $k= \frac{59}{120}$.

Usando el método teórico, calculamos los precios flat y market junto con el cupón acumulado:

- $B_f = B_t(1+i)^k = 9,279.79 (1+0.050625)^{\frac{59}{120}} \approx 9507.87$
- $I_a = Fr \cdot \left[ \frac{(1+i)^k-1}{i} \right] = 400 \cdot \left[ \frac{(1+0.050625)^{\frac{59}{120}}-1}{0.050625} \right] \approx 194.19$
- $B_m = B_f - I_a = 9507.87-194.19 \approx 9,313.68$

c) Convención del banquero (act/360) y el método semi-teórico

Usando act/360:

- Por el inciso a), sabemos que el conteo de días transcurridos es de 58 días.
- Por el inciso b), sabemos que el conteo de días del cuatrimestre actual es de 120 días.

Entonces la fracción de periodo cuatrimestral es $k= \frac{58}{120}$.

Usando el método teórico, calculamos los precios flat y market junto con el cupón acumulado:

- $B_f = B_t(1+i)^k = 9,279.79 (1+0.050625)^{\frac{58}{120}} \approx 9503.95$
- $I_a = k \cdot Fr = \frac{58}{120} \cdot 400 = 193.\overline{3}$
- $B_m = B_f - I_a = 9503.95-193.\overline{3} \approx 9,310.61$

### Ejercicio 4

**A 40-year bond is purchased at a discount. The bond pays annual coupons. The amount for accumulation of discount in the 15th coupon is 194.82. The amount for accumulation of discount in the 20th coupon is 306.69. Calculate the amount of discount in the purchase price of this bond.**

Tenemos un bono con descuento el cual da cupones anuales (40 en total), el cual solo se nos da el número de periodos y la cantidad de descuento en dos periodos distintos. Se nos pide calcular el total acumulado de descuento, es decir la diferencia entre el precio de compra y la redención, misma que en una tabla de amortización representa la suma total las acumulaciones de descuento durante la vida del bono. Usando estos datos podemos construir una parte de dicha tabla de amortización:

| Año (t) | Descuento (A_t) |
| --- | --- |
| 0 |  |
| … | … |
| 15 | $ 194.82 |
| … | … |
| 20 | $ 306.69 |
| … | … |
| Total acumulado | ? |

Recordemos una definición de descuento en el tiempo $t$, la cual tiene un comportamiento de interés compuesto respecto a la tasa de rendimiento en una tabla de amortización:

$$
A_{t+1} = A_{t} \cdot (1+i) \quad \Longrightarrow \quad A_{t+k} = A_{t} \cdot (1+i)^{k}
$$

Como queremos encontrar el acumulado total, y sabiendo que los descuento son una serie de pagos a través del tiempo, cuyo crecimiento es de interés compuesto, esto quiere decir que el acumulado total es una anualidad. 

Ya tenemos el valor de $n=40$, ahora falta encontrar el monto de la renta periódica la cual es el primer descuento $(A_1)$ y la tasa de rendimiento anual $i$.

Sabiendo que $A_{15} =194.82$, y que $A_{20} = 306.69$, expresamos estos terminos usando la definición anterior:

$$
A_{20} = A_{15}(1+i)^5 \quad \text{con } k=5
$$

Despejamos la tasa de rendimiento anual y desarollamos:

$$
i = \left( \frac{A_{20}}{A_{15}} \right)^{1/5}-1 = \left( \frac{306.69}{194.82} \right)^{1/5}-1 \approx 0.0949
$$

Ahora calculamos la primera acumulación de descuento utilizando la misma propiedad con cualquier acumulación de descuento que ya tenemos (en particular usaremos $A_{15}$) :

$$
A_{15} = A_1(1+i)^{14} \quad \Longrightarrow A_1 = \frac{A_{15}}{(1+i)^{14}} = \frac{194.82}{(1+0.0949)^{14}} \approx 54.75
$$

Finalmente calculamos el acumulado total del descuento del bono con la definición de anualidad. Para ello, notemos que la suma modela un crecimiento respecto a la tasa i, por lo que usaremos el valor futuro de la anualidad:

[Linea de tiempo]

$$
\sum_{t=1}^{40}A_t = A_1 + A_1(1+i)^1 + ... + A_1(1+i)^{40} 
\\ \quad \\
= A_1 \cdot s_{\overline{40}|0.0949} = A_1 \cdot \left[ \frac{(1+i)^n-1}{i} \right]
\\ \quad \\
= 54.75 \cdot \left[ \frac{(1+0.0949)^{40} -1}{0.0949} \right] \approx 21,104.91

$$

### Ejercicio 5

**Considera un bono que redime al 110 y tiene valor par de $1,000. Ofrece cupones con una tasa del 7% pagadero semestral y un rendimiento del 9% nominal trimestral. El bono redime en 4 años. Realice 3 gráficas de valor en libros, precio limpio y precio sucio semanal para este bono (es decir, tome 52 puntos por cada año) considerando:
a) Método teórico
b) Método práctico
c) Método semipráctico
Para el primer medio año grafique las tres curvas de precio flat sobrepuestas. ¿Qué sucede?**

Definimos el valor de las variables:

- $F=1,000$
- $C=1,000\cdot 1.10 = 1,100$
- $r^{(2)} = 0.07$ pagadero semestral por lo que $r= \frac{0.07}{2} =0.035$ efectiva semestral
- $i^{(4)}=0.09$ nominal trimestral por lo que $i_\text{trim} = \frac{0.09}{4}=0.0225$ efectiva trimestral. Buscamos la tasa equivalente efectiva semestral:

$$
i = (1+i_\text{trim})^2 -1 = (1+0.0225)^2 \approx 0.0455
$$

- La vida del bono es de 4 años. Como los cupones son semestrales, entonces tenemos un total de $n = 8$ periodos/cupones.

### Ejercicio 6

**Considere un bono Call con valor facial de $10,000 que ofrece cupones del 9% convertible semestral que ofrece rendimiento del 6% nominal semestral y redime al 120. Se emite hoy y puede ser redimido a partir de la fecha de pago de cupón 15 y en los subsecuentes hasta el 20. ¿Cuál será su precio de emisión?**

Definimos nuestras variables:

- $F = 10,000$
- $C = 10,000(1.20) = 12,000$
- $r^{(2)} = 9\%$ convertible semestral, por lo que: 
$r = 0.09/2 = 0.045$ efectiva semestral
- $i^{(2)}=6\%$ nominal semestral, por lo que: 
$i = 0.06/2 = 0.03$ efectiva semestral
- Valor del cupón: $F\cdot r = 10,000(0.045) = 450$ (semestrales)

Se nos menciona que el bono puede ser redimido en cualquier fecha de pago, desde el semestre 15 al 20, por lo que $n = \{15,16,17,18,19,20\}$.

Como la redención puede realizarse en diferentes periodos (y precios), considerando que este es un bono de tipo Call, el emisor puede decidir cuándo redimir, por lo que buscará pagar el precio más bajo posible. De esta forma, el precio de emisión de un bono Call se definirá como el precio mínimo que está dispuesto a pagar el emisor.

Notemos que la tasa cupón modificada:

$$
g = \frac{Fr}{C}=\frac{450}{12,00} = 0.0375
$$

Comparando las tasas vemos que $g>i(0.0375>0.03)$, es decir que el bono se vende con prima, y cuando un bono Call se vende con prima, el emisor está perdiendo dinero conforme transcurre el tiempo ya que está pagando cupones más altos que los que exige el mercado actual. Por lo tanto, el emisor deseará pagar el bono cuanto antes ejerciendo su opción de redimir en la fecha más temprana posible. Esta fecha es el semestre 15, por lo que el precio de emisión se hará bajo este periodo.

Verifiquemos lo anterior, calculando algunos precios del bono $P(n)$ con diferentes fechas de pago redención $n$:

- $P(15) = 450 \cdot s_{\overline{15}|0.03} + 12,000(1+0.03)^{-15} \approx 13,074.41$
- $P(16) = 450 \cdot s_{\overline{16}|0.03} + 12,000(1+0.03)^{-16} \approx 13,130.49$
- $\vdots$
- $P(20) = 450 \cdot s_{\overline{20}|0.03} + 12,000(1+0.03)^{-20} \approx 13,338.97$

Es claro que el precio que el emisor debe pagar por el bono aumenta conforme pasa el tiempo. Como se mencionó anteriormente, el bono Call beneficiará al emisor, por lo que el precio de emisión del bono es de $13,074.41$.

### Ejercicio 7

**Ahora considere que el bono del ejercicio 6 es Put en lugar de Call. ¿Cuál será su precio de emisión?**

Trabajamos bajo las mismas variables del bono, incluyendo mismas fechas de redención y por consecuente, el mismo cálculo de precios para $P(15), P(16),..., P(20)$.

Esta vez, el bono se clasifica como Put. En este tipo de bono, a diferencia de bono Call, buscará beneficiar al inversionista por sobre el emisor. Recordemos que este bono se vende con prima, esto quiere decir que el bono está pagando con sus cupones más de lo que ofrece el mercado $(g>i)$, por lo tanto el inversionista querrá retener el bono el mayor tiempo posible para seguir cobrando sus cupones y obtener un mejor rendimiendo por su dinero. Justamente, así se define el precio de emisión de un bono Put: es el precio máximo que el inversor puede obtener. Del iniciso anterior, se concluye que este precio es $P(20) = 13,338.97$.

### Ejercicio 8

**Considere un bono con valor par de $1,000 que ofrece cupones del 10% anual y que ofrece rendimiento del 6.5% nominal trimestral y redime a decisión del emisor: al 95, al final de los años del 11 al 15; a la par, al final de los años 16 al 20; y al 110, al final de los años 21 al 25. Calcular el precio de emisión.**

Definimos nuestras variables:

- $F = 1,000$
- $r = 0.1$ efectiva anual
- $i^{(4)}=0.065$ nominal trimestral, por lo que:
$i_\text{trim}=0.065/4=0.01625$ efectiva trimestral.
Buscamos la tasa anual, entonces:
$i=(1+i_\text{trim})^4-1=(1+0.01625)^4-1 \approx 0.0666$
- Valor del cupón: $F\cdot r = 1,000(0.1) = 100$ (por año)
- Fechas / años de redención: $n=\{11,12,...,24,25\}$
- Valor de redención:
    - $C_1 = 1,000(0.95) = 950$
    cuando $n= \{ 11,...,15 \}$
    - $C_2 = F =1,000$ (redime a la par)
    cuando $n= \{ 16,...,20 \}$
    - $C_3 = 1,000(1.1) = 1,100$
        
        cuando $n= \{ 21,...,25 \}$
        

Se nos menciona que este bono, el emisor tiene el derecho o la posibilidad de redimir las fechas o periodos de pago indicados, por lo que se trata de un bono Call. Queremos saber el precio de emisión, por lo que buscaremos el menor precio de valuación posible para este bono.

Revisemos cada tasa cupón modificada por cada bloque de periodos con distinta redención, y realizamos la comparación con la tasa de mercado $i=0.0666$, para saber si existe algún bloque en el que conviene buscar el menor precio de valuación:

- Cuando $n= \{ 11,...,15 \}$, con valor de redención $C_1$:

$$
g_1 = \frac{Fr}{C_1} = \frac{100}{950}\approx 0.1052 \quad \Longrightarrow \quad g_1 >i
$$

- Cuando $n= \{ 16,...,20 \}$, con valor de redención $C_2$:

$$
g_2 = \frac{Fr}{C_2} = \frac{100}{1000}= 0.1 \quad \Longrightarrow \quad g_2>i
$$

- Cuando $n= \{ 21,...,25 \}$, con valor de redención $C_3$:

$$
g_1 = \frac{Fr}{C_3} = \frac{100}{1100}\approx 0.0909 \quad \Longrightarrow \quad g_3>i
$$

Como $g>i$ en todos los bloques de redención, podemos decir que el bono se comporta siempre como un bono con prima, ofreciendo al inversor rendimientos más altos por sobre las tasas de mercado, haciendo que el emisor pierda dinero conforme pasa más tiempo. Ya que el emisor tiene la decisión, solo es necesario fijarnos en las fechas de redención más próximas para que el emisor liquide el bono.

Ya que cada bloque de fechas tiene distinto valor de redención, verificaremos el primer año de cada bloque (no será necesario revisar las demás fechas porque ya vimos que los años que le siguen solo aumentan el precio del bono):

- Cuando la redención es $C_1$ y el emisor liquida en $n=11$, el precio es:

$$
P(11) = 100 \cdot s_{\overline{11}|0.0666} + 950(1+0.0666)^{-11} \approx 1,229.63
$$

- Cuando la redención es $C_2$ y el emisor liquida en $n=16$, el precio es:

$$
P(16) = 100 \cdot s_{\overline{16}|0.0666} + 1000(1+0.0666)^{-16} \approx 1,322.04
$$

- Cuando la redención es $C_3$ y el emisor liquida en $n=21$, el precio es:

$$
P(21) = 100 \cdot s_{\overline{21}|0.0666} + 1100(1+0.0666)^{-21} \approx 1,394.95
$$

El precio de emisión del bono es el menor de estas valuaciones, es decir 1,229.63.

### Ejercicio 9

**¿Cuál será el precio de emisión del bono del ejercicio 8 si el bono redime a decisión del inversionista?**

Bajo el mismo bono y valuaciones, nos ponemos en el lugar del inversionista. Queremos obtener el mayor rendimiento posible del bono. Sabiendo que este bono se vende con prima $(g>i)$ en todos sus bloques de redención, entonces nuestro objetivo es conservar el bono y seguir cobrando todos los cupones que se puedan, por lo que decidiremos redimir hasta el último periodo disponible.

Como tenemos diferentes valores de redención, confirmaremos nuestra elección al verificar cuál es el máximo precio de emisión calculado resultado de evaluar al año final de cada bloque de redención distinto:

- Cuando la redención es $C_1$ y el emisor liquida en $n=11$, el precio es:

$$
P(15) = 100 \cdot s_{\overline{15}|0.0666} + 950(1+0.0666)^{-15} \approx 1,290.69
$$

- Cuando la redención es $C_2$ y el emisor liquida en $n=16$, el precio es:

$$
P(20) = 100 \cdot s_{\overline{20}|0.0666} + 1000(1+0.0666)^{-20} \approx 1,362.09
$$

- Cuando la redención es $C_3$ y el emisor liquida en $n=21$, el precio es:

$$
P(25) = 100 \cdot s_{\overline{25}|0.0666} + 1100(1+0.0666)^{-25} \approx 1,420.01
$$

El precio de emisión del bono es la mayor de estas valuaciones, es decir 1,420.01

### Ejercicio 10

**Considere un bono con valor par de $10,000 que ofrece cupones del 9% anual y que ofrece rendimiento del 12% nominal semestral y redime, a decisión del inversionista: a la par al final de los años del 7 al 10; al 110 al final de los años 11 al 15; y al 120 al final de los años 16 al 20. Calcule el precio de emisión del bono.**

Definamos las variables:

- $F = 10,000$
- $r=9\% = 0.09$ anual efectiva
- $i^{(2)}=12\%$ nominal semestral, por lo que
$i_{sem} = 0.12/2 = 0.06$ efectiva semestral.
Buscamos la tasa anual, entonces: 
$i= (1+i_{sem})^2 -1 =(1+0.06)^2 -1 \approx0.1236$ efectiva anual
- Valor del cupón: $F \cdot r = 10,000(0.09) = 900$ (anuales)
- Fechas / años de redención: $n=\{7,8,...,19,20\}$
- Valor de redención:
    - $C_1 = 10,000$ (a la par)
    cuando $n= \{ 7,...,10 \}$
    - $C_2  =10,000(1.1) = 11,000$
    cuando $n= \{ 11,...,15 \}$
    - $C_3 = 10,000(1.2) = 12,000$
        
        cuando $n= \{ 16,...,20 \}$
        

Cuando la decisión de redención es por parte del inversionista, el bono es de tipo Put. Analizamos la tasa cupón modificada de cada bloque de fechas:

- Cuando $n= \{ 7,...,10 \}$, con valor de redención $C_1$:

$$
g_1 = \frac{Fr}{C_1} = \frac{900}{10,000}= 0.09 \quad \Longrightarrow \quad i > g_1
$$

- Cuando $n= \{ 11,...,15 \}$, con valor de redención $C_2$:

$$
g_2 = \frac{Fr}{C_2} = \frac{900}{11,000}= 0.1 \quad \Longrightarrow \quad i > g_2
$$

- Cuando $n= \{16,...,20 \}$, con valor de redención $C_3$:

$$
g_1 = \frac{Fr}{C_3} = \frac{900}{12,000} = 0.075 \quad \Longrightarrow \quad i>g_3
$$

Como $i>g$ en toda fecha de redención, el bono se vende con descuento: las tasas de mercado están pagando más alto que lo paga este bono, la ganancia se recupera en el pago de redención y no en el pago de cupones, por lo que mientras el inversionista siga alargando la vida del bono, irá perdiendo dinero con cada cupón cobrado, por lo tanto, como es un bono Put, el inversionista deseara activar el pago de redención lo más pronto posible. El bono Put establece el precio de emisión con el precio máximo que el inversionista puede obtener.

Valuamos el bono, en cada inicio de fecha de cada bloque de redención distinta:

- Cuando la redención es $C_1$ y el emisor liquida en $n=7$, el precio es:

$$
P(7) = 900 \cdot s_{\overline{7}|0.1236} + 10,000(1+0.1236)^{-7} \approx 8.483.92
$$

- Cuando la redención es $C_2$ y el emisor liquida en $n=11$, el precio es:

$$
P(11) = 900 \cdot s_{\overline{11}|0.1236} + 11,000(1+0.1236)^{-11} \approx 8,313.44
$$

- Cuando la redención es $C_3$ y el emisor liquida en $n=16$, el precio es:

$$
P(16) = 900 \cdot s_{\overline{16}|0.1236} + 12,000(1+0.1236)^{-16} \approx 8,012.71
$$

El precio de emisión del bono es la mayor de estas valuaciones, es decir 8,483.92