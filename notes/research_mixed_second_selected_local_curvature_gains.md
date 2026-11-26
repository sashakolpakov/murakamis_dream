# Local curvature gains for the second-selection budget

Research deduction, 6 November 2026. Explicit local curvature bounds
sharpen three gains in the second-selection central comparison.
They apply under the reference hypotheses below. An illustrative
saved box meets these numerical hypotheses but is geometrically
excluded by its next external coordinate; it supplies no admissible
central test. No reference, primitive, phase or source is reevaluated.

## 1. The reference hypotheses and the comparison

Consider an original reference for a first-unselected, second-selected
configuration with first flag \(\alpha\in\{0,1\}\), second type four,
and next flag \(\beta=0\). Keep all original reference conditions.
Write \(u_*,z_*,v_*\) for its ordinary coordinates and put
\[
 x_*=\Re z_*,\qquad c=\Im z_*,\qquad H=1/100.
 \tag{1}
\]
The [directional budget](research_mixed_second_selected_directional_budget.md),
Theorem 3, bounds the original main/main central rates, with both
boundary tangents retained, by
\[
 f_\nu-M\le T_\nu+\mathcal U(A)+\mathcal R_0(d)
                       +\mathcal Z_\nu(D_\nu;I_\nu),
 \quad I_1=[.22,.45],\quad I_0=[.4,.45].
 \tag{2}
\]
Here \(\nu=1\) is factorial and \(\nu=0\) is forced, and
\[
 T_1=\mathcal V-\pi/50,\qquad
 T_0=\mathcal V+g_H(x_*),\qquad
 g_h(t)=\Re g(t+ih).
 \tag{3}
\]
The primitive \(g\), the exact vertical cost \(\mathcal V\), the
forces \(A,d,D_\nu\), and the true centers are unchanged.
The other real targets remain free on their original plateau intervals.

Assume in addition the following local inequalities:
\[
 \begin{gathered}
 5/16<\Re u_*<63/200,\quad |\Im u_*|<9/200,\quad 0<A<33/200,\\
 1/3<\Re v_*<3/8,\quad |\Im v_*|<1/50,\quad d>0,\\
 .22<x_*<7/25,\qquad D_1<0.
 \end{gathered}
 \tag{4}
\]
These are hypotheses for the reusable bounds. They must be verified
on each new reference enclosure where the bounds are used.

## 2. The left-index gain

The original strip derivatives are
\[
 g_h''(t)=
 \frac{\pi\sin(2\pi t)}{\cosh(2\pi h)-\cos(2\pi t)},\qquad
 g'''(t+ih)=-\pi^2\csc^2(\pi(t+ih)).
 \tag{5}
\]
For \(t=\Re u_*\), the angle \(2\pi t-\pi/2\) lies between
\(\pi/8\) and \(13\pi/100<143/350\). Consequently
\[
 \sin(2\pi t)>\frac{224551}{245000},\quad
 -\cos(2\pi t)<\frac{143}{350},\quad
 \cosh(2\pi\Im u_*)<\frac{21}{20}.
 \tag{6}
\]
The first inequality is \(1-(143/350)^2/2\); the last follows
from \(2\pi|\Im u_*|<99/350\) and
\(\cosh q\le1+(q^2/2)/(1-q^2/12)\).
Using \(\pi>157/50\), equations (5)--(6) give
\[
             g_{\Im u_*}''(\Re u_*)>\frac{39}{20}.
 \tag{7}
\]
On the entire connecting interval \([\Re u_*,1/2]\),
\(\sin(\pi t)\ge\sin(5\pi/16)>13/16\). Indeed
\(\pi>25/8\) and
\(125/128-(125/128)^3/6>13/16\) prove the latter inequality.
Thus \(|g'''(t+i\Im u_*)|<(22/7)^2(16/13)^2<15\).
The left Bregman cost therefore satisfies, for every admissible
\(0\le\delta\le1/2-\Re u_*<3/16\),
\[
 \phi_u(\delta)\ge\frac{39}{40}\delta^2-\frac52\delta^3.
 \tag{8}
\]
The derivative of
\((33/200)\delta-(39/40)\delta^2+(5/2)\delta^3\)
is everywhere positive: its discriminant is \(-459/400\).
Enlarging only this polynomial's maximizing interval to \([0,3/16]\),
the positive-force restriction in the directional theorem gives
\[
 \mathcal U(A)\le
 \frac{33}{200}\frac3{16}
 -\frac{39}{40}\left(\frac3{16}\right)^2
 +\frac52\left(\frac3{16}\right)^3
 =\frac{2691}{204800}=:\overline U.
 \tag{9}
\]

## 3. The right-index and factorial selected gains

On the reference range for \(v_*\) in (4),
\[
 \sin(2\pi\Re v_*)>7/10,\quad
 -\cos(2\pi\Re v_*)<3/4,\quad
 \cosh(2\pi\Im v_*)<51/50.
 \tag{10}
\]
The trigonometric bounds follow from \(7/10<\sqrt2/2<3/4\);
the hyperbolic bound follows from the same series estimate at
\(q=22/175\). Hence
\(\Re\cot(\pi v_*)>70/177>15/53\).
The directional theorem's fixed-height refinement has
\(\kappa_0=30\pi/53>471/265\). Writing \(\overline d\) for
the saved upper endpoint of \(d\), enlarging the allowed downward
displacement to the whole real half-line gives
\[
             \mathcal R_0(d)\le
             \frac{\overline d^{\,2}}{2(471/265)}=:\overline R.
 \tag{11}
\]

Since \(D_1<0\) and \(g_H\) is convex on \(P=[.22,.45]\), the
factorial selected gain is attained at or below its true center.
Every relevant connecting interval lies in \([.22,.28]\). There
\[
 \sin(2\pi t)>98/100,\quad \cos(2\pi t)>-1/5,\quad
                  \cosh(2\pi H)<101/100.
 \tag{12}
\]
For the first two use \(|2\pi t-\pi/2|\le3\pi/50<33/175\),
\(\cos q\ge1-q^2/2\), and \(\sin q<q\); for the last use the
series bound at \(q=11/175\). Thus
\(2g_H''>2(157/50)(98/121)>5\).
If \(\underline D_1<0\) is the saved lower force endpoint, then
\[
          \mathcal Z_1(D_1;P)\le\underline D_1^{\,2}/10
                              =:\overline Z_1.
 \tag{13}
\]
For the forced gain retain its saved upper endpoint
\(\overline Z_0\) without alteration or truncation at zero.

## 4. Combination and an excluded-box illustration

The [central-budget vertical bound](research_mixed_second_selected_central_budget.md),
equation (12), applies to these original \(\beta=0\) references:
\[
 \mathcal V\le\frac{21\pi}{10}(H-c)^2
       \le\frac{33}{5}\overline\Delta^{\,2}=:\overline V,
 \qquad \overline\Delta=1/100-\underline c.
 \tag{14}
\]
Its proof uses the original stationary reference and retains the
chirp; it does not bound an arbitrary off-reference phase by dropping
its first height derivative.

**Proposition.** Under (4), replace the three gains in (2) by
\(\overline U,\overline R,\overline Z_1\) from (9), (11), and (13),
while keeping any proved upper bound \(\overline Z_0\) for the
signed forced gain. If \(\overline g\ge g_H(x_*)\), then the two
central deficits are at most
\(\overline V-157/2500+\overline U+\overline R+\overline Z_1\)
and
\(\overline V+\overline g+\overline U+\overline R+\overline Z_0\).
All original boundary tangents and unrestricted plateau targets
remain as in the directional theorem.

For an arithmetic illustration, node 288 of the
[pending scalar record](../repro/results/research-mixed-second-selected-pending-scalar-probe-attempt01.json),
SHA256
2f7640e7aefc655628b134ac50500e03b0971f2768b8f73c0df36a00b74b0f3c,
has \((\alpha,\beta)=(1,0)\), address 0011111110111111100101,
and auxiliary rectangle
\([115439/512000,461773/2048000]+
i[36243/1024000,9063/256000]\).
Its saved directed endpoints satisfy (4) and give
\[
 \begin{split}
 \underline c&=-59618346305/1099511627776,\\
 \overline d&=4097353905/17179869184,\qquad
 \underline D_1=-1039430537/4294967296,\\
 \overline g&=
 -422427354161622806885914878307375650007088500683/
 2923003274661805836407369665432566039311865085952,\\
 \overline Z_0&=
 786163152832799507558379079843734055977698025121/
 11692013098647223345629478661730264157247460343808 .
 \end{split}
 \tag{15}
\]
Here \(\overline g\) bounds \(g_H(x_*)\). Exact rational arithmetic gives
\[
 \begin{split}
 \overline V-\frac{157}{2500}+\overline U+\overline R+\overline Z_1
 &=-\frac{343952798191828602435835539}
          {593129230248427438840217600000}<-\frac1{2000},\\
 \overline V+\overline g+\overline U+\overline R+\overline Z_0
 &=-\frac{119981103973056521077889293022943154318570593644673547}
          {5736393926523793953949462968411410852149535231180800000}
   <-\frac1{2000}.
 \end{split}
 \tag{16}
\]
The first inequality uses \(\pi/50>157/2500\).
The respective upper bounds are approximately \(-.0005798952\)
and \(-.0209157714\); their signs are the exact comparisons in (16).

However, this box contains no admissible reference. Its saved next
external coordinate, denoted \(c_{\rm ext}\) to distinguish it from
the height \(c\), lies in
\[
 \left[\frac{1050214639}{4294967296},
       \frac{1331525037}{4294967296}\right]
 +i\left[\frac{555453115}{8589934592},
         \frac{1092931997}{8589934592}\right].
 \tag{17}
\]
The exact squared distance from this rectangle to the type-three
disk center \(.35-.01i\), minus \(.083^2\), is
\[
 \frac{327447290086775393061}{1152921504606846976000000}>0.
 \tag{18}
\]
Thus it misses \(K_3\); its positive imaginary lower endpoint also
misses \(K_4\), whose heights are at most \(-.001\).
The original provider's inconclusive disk guard did not certify
this elementary rectangular separation. Its retained status never
asserted existence of an admissible reference.

Accordingly (16) is only an illustration of the sharper scalar
arithmetic, not a successful nonvacuous central certificate.
The reusable results are the explicit gain estimates (9), (11),
and (13) and their stated conditional combination. The saved
record is unchanged; no other reference box, main/right-half-row
term or remaining frontier is covered here.
