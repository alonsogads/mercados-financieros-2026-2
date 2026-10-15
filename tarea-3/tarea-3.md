# Tarea 3: Bonos I

1. Describe los bonos con las siguientes características:

a) P < C = F

Es un **bono comprado con descuento y redimible a la par.** La igualdad C = F redime a la par, es decir que se paga al final, el valor nominal del bono. Sin embargo, la desigualdad P < F indica que se pagó menos por el bono hoy en comparación al valor nominal, por lo que la ganancia se obtiene en el periodo final (C - P > 0), indicando que es un bono con descuento.

b) C = P > F

Es un **bono comprado con premio y redimible con premio**. Se paga más de su valor nominal para adquirirlo $(P>F)$, por lo que sus ganancias se reflejan en el pago de cupones. Por otro lado, tenemos que se se devuelve al final lo mismo que se pagó por el bono (C - P = 0), entonces se confirma que todo el rendimiento depende exclusivamente de los cupones.

c) F = P < C

Es un **bono comprado a la par y redimible con premio**. Se paga hoy exactamente la misma cantidad que indica el documento ( F = P). Además al vencimiento, el emisor se compromete a devolver más dinero del que se prestó (C > F), por lo que el rendimiento recae sobre la redención.

d) P = C < F

Es un **bono comprado con descuento y redimible con descuento**. Aquí pagamos menos del valor nominal (P < F), haciendo que dependamos fuertemente del rendimiento de los cupones, sobre todo porque el pago de redención también es menor que el valor nominal ya que C - P = 0.

1. Calcula el precio de un bono (con las cuatro fórmulas) que paga cupones con tasa de 12% pagadera trimestral cuyo valor nominal es de $1,500. El plazo del bono es de año y medio y la tasa de rendimiento es del 5.2% nominal semestral.

Como el problema no menciona un valor de redención distinto, asumiremos que se redime a la par (C = F = 1,500).

Determinamos nuestra tasa cupón efectiva $r$. Como la que se nos da es nominal pagadera trimestral, buscaremos que todas las variables estén expresadas respecto a trimestres:

$$
r=\frac{r^{(4)}}{4} = \frac{0.12}{4}=0.03 \text{ efectiva trimestral}
$$

Determinamos la tasa de rendimiento efectiva trimestral a partir de una nominal semestral:

$$
i_{\text{sem}}=\frac{i^{(2)}}{2} = \frac{0.052}{2} = 0.026\text{ efectiva semestral} \\ \quad \\
\Longrightarrow (1+i_\text{trim})^2 = (1+i_\text{sem}) \quad  \text{Usamos tasas equivalentes}
\\ \quad \\
i=\sqrt{(1+0.026)}-1 \approx 1.012916  -1\approx 0.012916 \text{ efectiva trimestral}
$$

Determinamos el plazo del bono $n$ (en semestres):

$$
n=1.5 \text{ años}  \cdot \frac{4 \text{ trimestres}}{\text{1 año}} = 6\text{ semestres}
$$

También calculamos algunas términos útiles:

- Pago del cupón: $F \cdot r = 1,500 \cdot 0.03 = 45$
- Factor de descuento exponenciado a la $n$:

$$
v^ n= \left( \frac{1}{1+i} \right)^n =(1+0.012916)^{-6} \approx 0.92589
$$

1. Cálculo con fórmula básica

$$
P = (F \cdot r) \cdot a_{\overline{n}|i} + C \cdot v^n  =(F \cdot r) \left[ \frac{1 - v^n}{i} \right] + C \cdot v^n \\ \quad \\
 = 45 \cdot \left[ \frac{1 - 0.92589}{0.012916} \right] + 1,500 \cdot (0.92589) \approx 1,647.03
$$

b. Cálculo con fórmula de Makeham

- $K = C \cdot v^n \approx 1,500 \cdot 0.92589 = \mathbf{1,388.835}$
- $g = \frac{F \cdot r}{C} = \frac{45}{1,500} = \mathbf{0.03}$ (Como redimen a la par $g=r$)

$$
P = K + \frac{g}{i}(C - K) \\ \quad \\
\approx 1,388.835 + \frac{0.03}{0.012916} \cdot (1,500 - 1,388.835)\approx1,647.03
$$

c. Cálculo con fórmula del Monto Base (Base Amount)

- Calculamos el monto base: $G = \frac{F \cdot r}{i} = \frac{45}{0.012916} \approx \mathbf{3,484.0507}$

$$
P = G + (C - G)v^n \\ \quad \\
= 3,484.0507 + (1,500 - 3,484.0507) \cdot 0.92589 \approx 1,647.03

$$

d. Cálculo con fórmula de Premio / Descuento

$$
P = C + a_{\overline{n}|i}\cdot (F\cdot r - C\cdot i) = C+\left[ \frac{1 - v^n}{i} \right]\cdot (F\cdot r - C\cdot i) \\ \quad \\
=1,500+\left[ \frac{1 - 0.92589}{0.012916} \right]\cdot (1,500\cdot0.03-1500\cdot 0.012916) \approx 1647.03
$$

1. Considere un bono con valor facial de $1000 que madura al 98 en 4 años y es emitido hoy (13 de marzo de 2026). El bono ofrece una tasa cupón del 9% pagadera semestral y un rendimiento del 9% nominal cuatrimestral.

a)  ¿Cuál será el valor teórico de este bono hoy?

Identificamos las variables:

- $F=1000$
- $C=F\cdot 0.98 = 1000 \cdot 98 = 980$  (porque “madura al 98”)
- Como la tasa cupón es pagadera semestral buscamos la efectiva semestral:

$$
r=\frac{r^{(2)}}{2}=\frac{0.09}{2}=0.045 \text{ efectiva semestral}
$$

- Buscamos tasa de rendimiento efectiva semestral $(i_\text{sem}=i)$:

$$
i_\text{cuatrim} = \frac{i^{(3)}}{3  }=\frac{0.09}{3}=0.03 \text{ efectiva cuatrimestral} \\ \quad \\
\Longrightarrow  (1+i_\text{sem})^2 = (1+i_\text{cuatrim})^3 \\ \quad \\
\Longrightarrow i = \sqrt{(1+i_\text{cuatrim})^3}-1 = \sqrt{(1+0.03 )^3}-1=0.045335 \text{ efectiva semestral}
$$

- Calculamos la duración en semestres: $n =$ 4 años * $\frac{\text{2 semestres}}{1 \text{año}} =$ 8 semestres

Calculamos el precio teórico:

$$
P = (F \cdot r) \cdot a_{\overline{n}|i} + C \cdot v^n  =(F \cdot r) \left[ \frac{1 - (1+i)^{-n}}{i} \right] + C \cdot (1+i)^{-n} \\ \quad \\
= (1000\cdot 0.045) \left[ \frac{1 - (1+0.045335)^{-8}}{0.045335} \right] + 980\cdot (1+0.045335)^{-8} \\ \quad \\
\approx 45  \cdot (6.58686) +687.351  \approx 983.76

$$

b) Considere el mismo bono del caso descrito salvo que la tasa de rendimiento irá cambiando, tomando valores desde 1% (nominal cuatrimestral) incrementando 1% hasta llegar al 10% y obtener los diez precios. Graficar, en el eje de las X la tasa de inteŕes y en eje de las Y el precio del bono. ¿Qué puede interpretar la gráfica?

Para obtener los diez precios, debemos iterar el cálculo iterando la tasa de rendimiento nominal pagadera cuatrimestral $i^{(3)}$ desde 1% hasta 10% (eje X), luego realizamos la conversión de la tasa efectiva semestral equivalente $i$ y así obtener el precio del bono correspondiente $P$ (eje Y).

- Sea $x = i^{(3)}$. Se graficaran los valores de $x\in\{1,2,...,9,10\}$.
- Como el bono es pagadera semestral, conviene calcular para fines de visualización, la tasa de rendimiento efectiva semestral $i(x)$ de cada tasa nominal $x$:

$$
(1+i_\text{sem})^2 = (1+ i_\text{cuatrim})^3 \Longleftrightarrow (1+i_\text{sem})^2 = (1+ \frac{i^{(3)}}{3})^3
\\ \quad \\
\Longrightarrow i= \sqrt{(1+ \frac{i^{(3)}}{3})^3} -1 \quad \text{tasa de rendimiento efectiva semestral}
\\ \quad \\
\Longrightarrow i(x) = \sqrt{\left(1+ \frac{x}{3}\right)^3} -1 \quad
$$

- Por lo tanto el precio del bono en función de la tasa de rendimiento efectiva $P(i(x))$ es:

$$
P =(F \cdot r) \left[ \frac{1 - (1+i)^{-n}}{i} \right] + C \cdot (1+i)^{-n} \\ \quad \\
= (1000\cdot 0.045) \left[ \frac{1 - (1+i)^{-8}}{i} \right] + 980\cdot (1+i)^{-8} \\ \quad \\
= 45 \left[ \frac{1 - (1+i)^{-8}}{i} \right] + 980\cdot (1+i)^{-8} \\ \quad \\
\Longrightarrow P(i(x)) = 45 \left[ \frac{1 - (1+i(x))^{-8}}{i(x)} \right] + 980\cdot (1+i)^{-8} \\ \quad \\
$$

| **Iteración** | **Tasa Nominal (j)** | **Tasa Efectiva Semestral (isem)** | **Precio del Bono (P)** |
| --- | --- | --- | --- |
| 1 | 1% | 0.5008% | **$1,293.66** |
| 2 | 2% | 1.0016% | **$1,249.00** |
| 3 | 3% | 1.5037% | **$1,206.51** |
| 4 | 4% | 2.0066% | **$1,165.55** |
| 5 | 5% | 2.5103% | **$1,126.31** |
| 6 | 6% | 3.0149% | **$1,088.59** |
| 7 | 7% | 3.5203% | **$1,052.30** |
| 8 | 8% | 4.0265% | **$1,017.38** |
| 9 | 9% | 4.5336% | **$983.76** *(Nuestro inciso a)* |
| 10 | 10% | 5.0414% | **$951.59** |

La gráfica demuestra que cuando la tasa de interés exigida por el mercado sube, el precio del bono baja (ya que recordemos que la tasa cupón quedo fija). El bono pierde valor porque sus cupones fijos de 45 pesos se vuelven menos atractivos frente a un mercado que ahora paga mejores rendimientos.

c) Considere el mismo bono del caso descrito en b) con el rendimiento inicial de 8% nominal cuatrimestral salvo que la tasa cupón irá cambiando, tomando valores desde 4% (pagadera semestral) incrementando 1% hasta llegar al 13% pagadera semestral y obtener los diez precios. Graficar, en el eje de las X la tasa cupón y en el eje de las Y el precio del bono. ¿Qué puede interpretar de la gráfica?

Ahora la tasa de rendimiento es fija. Por lo que la gráfica comparara la tasa cupón nominal semestral $r^{(2)}$ (eje X) y su respectivo precio del bono $P$ (eje Y).

- Sea $x = r^{(2)}$. Se graficaran los valores de $x\in\{4,3,...,12,13\}$.
- Buscamos la función de tasa efectiva semestral $r(x)$ del cupón en base a la nominal $x$:

$$
r=r_\text{sem} = \frac{r^{(2)}}{2} \Longrightarrow r(x) = \frac{x}{2}
$$

Además determinamos la tasa de rendimiento efectiva semestral a partir de $i^{(3)}=8\%$:

$$
(1+i_\text{sem})^2 = (1+i_\text{cuatrim})^{3} \Longrightarrow i_\text{sem} = \sqrt{ \left(1+\frac{i^{(3)}}{3}\right)^{3}}-1 \\ \quad \\
i=\sqrt{ \left(1+\frac{0.08}{3}\right)^{3}}-1 = 0.040265 \text{ efectiva semestral}
$$

- Por lo tanto el precio del bono en función de la tasa cupón efectiva $P(r(x))$ es:

$$
P =(F \cdot r) \left[ \frac{1 - (1+i)^{-n}}{i} \right] + C \cdot (1+i)^{-n} \\ \quad \\
= (1000\cdot r) \left[ \frac{1 - (1+0.040265)^{-8}}{0.040265} \right] + 980\cdot (1+0.040265)^{-8} \\ \quad \\
= (1000\cdot r)(6.725383) +714.618379 = 6725.383\cdot r +714.618379
\\ \quad \\
\Longrightarrow P(r(x)) = 6725.383\cdot r(x) +714.618379
$$

Es una línea recta con pendiente positiva. Esto significa que a medida que el bono ofrece una mejor tasa cupón, su precio sube proporcionalmente.

d) ¿Qué puede concluir al analizar los incisos b) y c)?

En el **inciso c**, vimos que mover la Tasa Cupón genera una **línea recta**. Esto se debe a que la tasa cupón r solo multiplica a la anualidad en el numerador de la formula básica, es decir crece linealmente.

En el **inciso b**, vimos que mover el Rendimiento del Mercado i, genera una **curva. . Esto se debe a que la i se encuentra en el denominador y elevada a potencias negativas (exponencial). por lo que moverla impica cambios exponenciales.**

La conclusión es que **el factor riesgo en inversión de bonos no radica en el cupón que se promete, sino en los movimientos de las tasas de interés de la economía**, porque esas tasas de mercado devaluán o premian el precio del instrumento de forma exponencial y no lineal.

1. A 10,000 par value 10-year bond with 8% annual coupons is bought at a premium to yield an annual effective rate of 6%. Calculate the interest portion of the 7th coupon.
- Valor nominal (Per value): $F = 10,000$
- Asumismos redención a la par: $C= 10,000$
- Plazo original: $n=10$ años
- Taza cupón (coupon rate):  $r=8\%$ efectiva anual
- Taza de rendimiento (yield rate): $i=6\%$ efectiva anual

El problema pide calcular la porción de interés del séptimo cupón. De acuerdo a una tabla de amortización, el interés en cualquier periodo $(t)$ se calcula multiplcando el Saldo o Valor en Libros del periodo anterior $(S_{t-1})$ por la tasa de mercado $(i)$. Sea $t=7$, entonces:

$$
I_t = S_{t-1} \cdot i \quad  \Longrightarrow \quad I_7=S_6 \cdot 0.06
$$

Necesitamos el valor en libros en el periodo (año 6), es decir justo después de cobrar el sexto cupón. Usaremos el método prospectivo para hallar cuanto vale el bono exactamente en el año 6 en base a los flujos que faltan por pagarse. 

Si el bono dura 10 años en total, aún faltan 10-6= 4 años por cobrar. Usando la fómula básica buscamos el valor del bono en el año 6 es:

$$
S_6 = (F \cdot r) \cdot a_{\overline{4}|i} + C \cdot (1+i)^{-4} 
\\ \quad \\
= 800 \cdot \left[ \frac{1 - (1.+0.06)^{-4}}{0.06} \right] + 10,000 \cdot (1.06)^{-4}
\\ \quad \\
\approx800(3.465106) + 10,000(0.792093) \approx 10,693.02
$$

Entonces el interés:

$$
I_7= 10,693.02 \cdot 0.06 = 641.58
$$

1. You have decided to invest in Bond X, an n-year bond with semi-annual coupons and the following characteristics:
i) Par value is 1000
ii) The ratio of the semi-annual coupon rate, r, to the desired semi-annual yield rate, i, is 1.03125
iii) The present value of the redemption value is 381.50.
Given (1+i)^(-n) = 0.5889, calculate the Price of Bond X.
- $F =1000$
- El valor presente de redención: $K=381.50$
- $\frac{r}{i}=1.03125$, con $r,i$ tasas efectivas semestrales
- Duración total: $n$ años
- Total de cupones: $n$ años * $\frac{2 \text{ cupones}}{\text{año}}$ = $2n$ cupones (por semestre)
- Factor de descuento: $v^n = (1+i)^{-n} = 0.5889$

Usando la formula de monto base, veamos que el monto base $G$:

$$
G = \frac{F \cdot r}{i}= F \cdot \frac{r}{i} = 1000(1.03125) = 1,031.25
$$

Notemos además, que el factor de descuento $v^n$ solo contempla $n$ semestres, por lo que para valuar el bono completo necesitamos este factor para $2n$ semestres:

$$
v^{2n}=(v^2)^2 = (0.5889)^2 \approx 0.346803
$$

Y por definición del valor presente de la redención, obentemos $C$:

$$
K = C\cdot v^{\text{total\_cupones}} \quad \Longrightarrow \quad 381.50 = C\cdot v^{2n} \\ \quad \\
C = \frac{381.50}{0.34803}\approx 1,093.29
$$

Finalmente obtenemos el precio del bono X por el periodo total (en $2n$ semestres):

$$
P = G + (C - G)\cdot v^{2n} \\ \quad \\
= 1,031.25 + (1,093.29-1.031.25)\cdot 0.346803 \approx 1,052.76
$$

1. Project P requires an investment of 4000 today. The investment pays 2000 one year from today and 4000 two years from today.
Project Q requires an investment of X two years from today. The investment pays 2000 today and 4000 one year from today.
The net present values of the two projects are equal at an annual effective interest rate of 10%.
Calculate X.
- $i = 10\%$ efectivo anual
- $\text{VPN}_{P} = \text{VPN}_{Q}$

Identificamos los flujos de efectivo del proyecto P en el tiempo:

$t=0$             1               2
     |——-——-|————--|
-4000          2000          4000

La ecuación del VPN del proyecto P:

$$
\text{VPN}_{P} = -4000+2000(1+0.1)^{-1} + 4000(1+0.1)^{-2} \approx 1123.9669
$$

Identificamos los flujos de efectivo del proyecto Q en el tiempo:

$t=0$             1               2
     |——-——-|————--|
 2000          4000            -X

La ecuación del VPN del proyecto Q:

$$
\text{VPN}_{Q} = 2000 + 4000(1+0.1)^{-1} -X(1+0.1)^{-2} \approx 5636.3636 - \frac{X}{1.21}
$$

Igualamos ambas ecuaciones:

$$
\text{VPN}_{P} = \text{VPN}_{Q} \quad \Longrightarrow \quad 1123.9669 = 5636.3636 - \frac{X}{1.21} 
\\ \quad \\
X = (5636.3636 - 1123.9669) (1.21) \approx 5460
$$

1. You are given the following information with respect to a bond:
i) Par value: 1000
ii) Term to maturity: 3 years
iii) Annual coupon rate: 6% payable annually
You are also given that the one, two, and three year annual spot interest rates are 7%, 8%, and 9% respectively.
Calculate the value of the bond.
- $F=C = 1000$
- Plazo: $n= 3$ años
- Tasa cupón: $r = 6\%$ anual
- Valor del cupón: $F\cdot r = 1000 \cdot 0.06 = 60$
- Tasas spot: $i_1 = 7\%, \quad i_2 = 8\%, \quad i_3 = 9\%$

Esta vez, en lugar de utilizar una única tasa de mercado, se nos dan tasas spot, las cuales son simplemente el rendimiento exacto que el mercado exige hoy para un flujo de efectivo que ocurrirá en un momento específico $t$ en el futuro. Por lo tanto, ya no usaremos la anualidad ya que la tasa $i$ya no es constante. El flujo de dinero en el tiempo es el siguiente:

$t=0$             1               2                 3
     |——-——-|————--|—————|
                     60              60          1000+60

Calculamos el valor presente de los flujos para obtener el valor del bono:

$$
P = \frac{60}{(1+0.07)^1} + \frac{60}{(1+0.08)^2} + \frac{1060}{(1+0.09)^3}
\\ \quad \\
\approx 56.07476 + 51.44033 + 818.51448 \approx 926.02957
$$

1. Bill buys a 10-year 1000 par value bond with semi-annual coupons paid at an annual rateo f 6%. The Price assumes an annual nominal yield of 6%, compounded semi-annually.
As Bill receives each coupon payment, he immediately puts the money into an account earning interest at an annual effective rate of i.
At the end of 10 years, immediately after Bill receives the final coupon payment and the redemption value of the bond, Bill has earned an annual effective yield of 7% on his investment in the bond.
Calculate i.