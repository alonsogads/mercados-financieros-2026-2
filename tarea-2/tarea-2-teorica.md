# Tarea 2: Acciones y metrícas de estados financieros reales

## Acciones y Métricas con Estados Financieros Reales

### Parte teórica

1. Defina ROA y explique que mide dentro del desempeño de una empresa.

ROA (Return on Assets / Rendimiento sobre los Activos) mide la eficacia general de la administración para generar utilidades con los activos disponibles de la empresa.

$$
\text{ROA} = \frac{\text{Utilidad neta}}{\text{Activos totales}}
$$

Esta métrica nos dice cuántos centavos de utilidad neta se generan por cada peso invertido en los activos de la empresa. Un ROA alto indica que la empresa gestiona al máximo sus activos para generar ganancias. Si una empresa tiene un ROA bajo, significa que tiene demasiados activos improductivos o que sus costos operativos son demasiado altos.

1. Defina el ROE y explique porque es importante para los accionistas.

ROE (Return on Equity / Rendimiento sobre el Capital Contable) mide el rendimiento obtenido sobre la inversión de los accionistas en la empresa.

$$
\text{ROE}=\frac{\text{Utilidad neta}}{\text{Capital contable}}
$$

A diferencia del ROA que evalúa a la empresa en su totalidad (activos totales), el ROE aísla y evalúa específicamente el dinero que pertenece a los dueños, es decir, el capital contable ($\text{activos} - \text{pasivos}$).

1. ¿Qué indica que la diferencia entre ROA y ROE sea muy grande?

Una diferencia sustancial entre el ROE y el ROA indica un alto grado de apalancamiento, es decir, que la empresa está financiando la mayor parte de sus operaciones e inversiones con deuda (pasivos) en lugar de usar el dinero de los accionistas (capital).

$$
\text{ROE}= \text{ROA}\times \frac{\text{Activos Totales}}{\text{Capital contable}}
$$

Si una empresa tiene mucha deuda (pasivos muy altos), su Capital Contable será muy pequeño en proporción a sus Activos Totales. Por lo que, al dividir Activos entre un Capital muy pequeño, el aplancamiento se vuelve un número muy grande. Como resultado, cualquier ganancia generada por los activos (ROA) se multiplica, disparando el ROE. Y aunque pudiera parecer una buena noticia (porque maximiza el rendimiento sobre los activos). también es una señal de alerta, ya que indica que la empresa ha asumido un alto riesgo financiero. Si las tasas de interés suben o las ventas caen, la deuda podría llevar a la empresa a la quiebra.

1. ¿Puede existir una empresa con ROA alto y ROE bajo? Explique.

Como $\text{Activos} = \text{Pasivos} + \text{Capital}$ , y asumiendo que una empresa no puede tener pasivos negativos ( $\text{Pasivos} \ge 0$ ), entonces los Activos siempre serán mayores o iguales al Capital ( $\text{Activos} \ge \text{Capital}$ ). Y como:

$$
\text{ROA} = \frac{\text{Utilidad neta}}{\text{Activos totales}} \quad ; \quad \text{ROE}=\frac{\text{Utilidad neta}}{\text{Capital contable}}
$$

Por lo tanto, si la Utilidad Neta es positiva, generalmente tenemos $ROA \le ROE$.

Sin embargo, si es posible bajo ciertas circunstancias. Un ejemplo es si tenemos capital contable negativo, es decir si una empresa ha acumulando deudas con anterioridad volviendo al capital contable negativo. Por lo que sí de pronto, la empresa genera una utilidad neta positiva y haciendo posible un ROA alto con un ROE bajo (negativos).

1. ¿Qué indicador consideraría más importante para analizar una empresa de retail?

Para una empresa de *retail* (comercio minorista),el modelo de negoco se caracteriza por tener márgenes de ganancia neta muy bajos, por lo que su éxito depende de vender volúmenes masivos de mercancía lo más rápido posible.

El ROA permite evaluar exactamente eso, qué tan eficiente es la administración para convertir esa masiva infraestructura física (tiendas, centros de distribución) y su rotación de inventario en utilidades.

1. ¿Qué indicador consideraría más importante para analizar un banco? 

El negocio principal de un banco es el apalancamiento: captan depósitos del público (pasivos o deuda para el banco) y usan ese dinero para otorgar créditos (activos para el banco). Debido a que operan casi enteramente con dinero ajeno, su base de activos es enorme en comparación con su capital contable. Por esta razón matemática, el ROA de un banco suele ser muy pequeño. 

Por otro lado, el ROE muestra que tan grande es el rendimiento obtenido después de haber considerado este gran apalancamiento.

1. ¿Qué indicador consideraría más importante para analizar una empresa de consumo?

Las empresas de bienes de consumo masivo (como Coca-Cola o Bimbo), su mayor ventaja suele radicar en su gran demanda. Estas empresas suelen tener flujos de efectivo muy estables y predecibles. Esta estabilidad les permite asumir niveles de deuda estratégica muy eficientes para financiar sus operaciones o recomprar acciones. Por lo tanto, el ROE analiza como se utiliza esa estabilidad y el apalancamiento financiero para maximizar el rendimiento de los accionistas.

Suponga la siguiente información para este y los siguientes cuatro ejercicios:

|  | Grupo Bimbo | América Móvil | Banorte |
| --- | --- | --- | --- |
| ROA | 5.77% | 4.3% | 2.7% |
| ROE | 10.33% | 17% | 28% |
1. Determinar el multiplicador financiero (apalancamiento).

Recordemos que:

$$
\text{Apalancamiento} = \frac{\text{Activos Totales}}{\text{Capital Contable}} = \frac{\text{ROE}}{\text{ROA}}
$$

Por lo que:

- Grupo Bimbo

$$
\frac{\text{ROE}}{\text{ROA}} = \frac{10.33\%}{5.77\%} = 1.8242
$$

- America Movil

$$
\frac{\text{ROE}}{\text{ROA}} = \frac{17\%}{4.3\%} = 3.9534
$$

- Banorte

$$
\frac{\text{ROE}}{\text{ROA}} = \frac{28\%}{2.7\%} = 10.3703
$$

1. ¿Cuál es la empresa más apalancada?

Banorte. Tal como se analizo con anterioridad, esto significa que gran parte de los activos que controla Banorte no son pagados con dinero de sus accionistas, sino que están financiados mediante pasivos (deuda).

1. ¿Cuál depende más de eficiencia operativa?

Bimbo. Tiene el ROA más alto (5.77%) y el multiplicador más bajo (1.8242), indicando que la mayor parte de la ganancia que llega a los accionistas, es gracias al eficaz uso de sus activos para generar utilidades.

1. ¿Cuál tiene mayor riesgo financiero? 

El riesgo financiero aumenta en proporción al nivel de deuda, y Banorte es la que tiene el apalancamiento más alto. Aunque se debe considerar que el apalancamiento es una naturaleza propia de los bancos, por lo que, es posible, que America Movil es la que asumiria el mayor riesgo corporativo ya que el apacalamiento no es la base de su modelo de negocio.

1. ¿Por qué Banorte tiene un ROE muy alto y un ROA bajo?

Como se explico en ejercicios anteriores, esto ocurre por la naturaleza del modelo de negocio bancario:

- El ROA es bajo, ya que la mayoria de los activos de un banco son en su inmensa mayoría, los créditos y préstamos que otorga al público. Por lo que el total de utilidades entre la gran cantidadad de activos, será un porcentaje bajo.
- El ROE es alto, ya que como vimos, el dinero que usa Banorte para prestar no es de los dueños del banco, sino de sus clientes. Al requerir muy poco Capital Contable, su nivel se apalancamiento es alto, y por lo tanto multiplica en gran medida al ROA.