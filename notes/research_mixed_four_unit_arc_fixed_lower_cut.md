# A fixed lower cut for the conditional critical point

Private written deduction, 10 November 2026. The original conditional
critical point stays above the real cut \(2/25\) while the incoming
unit-circle coordinate runs from \(1/2\) to \(7/8\). This supplies
a fixed left edge for a prewall contour on the remaining interval.
It is a critical-point estimate, not a finite-sum bound.

## 1. Domain and the original critical equation

Let
\[
 1/2\le a\le7/8,\qquad b=z+id,\qquad
 11/50\le z\le9/20,\qquad -51/500\le d\le-1/1000,
 \qquad X=e^{-2\pi ia},\quad Y=e^{-2\pi ib}.
 \tag{1}
\]
These are the actual outgoing targets used in
[the complete far-right pair theorem](research_mixed_initial44_near_endpoint_complete_pair.md).
In particular \(1/2<|Y|<1\). For the lower bound, use
\(-2\pi d\le51\pi/250<2/3<\log2\).
The last logarithm comparison follows from the positive
\(\operatorname{artanh}\) series at \(1/3\).

The [unit incoming branch theorem](research_mixed_four_conditional_unit_incoming_branch.md)
gives the original simple upper root
\[
 v(v-X)(v-Y)=X(v-1)^3,\qquad
 s=\frac{\Log v}{2\pi i}=u+ih,\qquad 0<u<1-a ,
 \tag{2}
\]
and the original zero logarithmic lift
\[
 Q_s(s;a,b)=0,\qquad
 Q(s;a,b)=g(a+s)+g(b+s)-3g(s)-g(a)-g(b)+2\pi ias ,
 \tag{3}
\]
where \(g'(w)=\Log(1-e^{-2\pi iw})\) on \(0<\Re w<1\).
All three arguments in (3) lie in that strip. Put
\[
 U=e^{2\pi h}=|v|^{-1},\qquad
 \alpha_R(V)=\Arg(1-Re^{-iV}),\qquad 0<V<2\pi .
 \tag{4}
\]
The argument in (4) is the continuous original strip argument.
The critical equation retains
\[
 \Im Q_s=\alpha_U(2\pi(a+u))
       +\alpha_{|Y|U}(2\pi(z+u))
       -3\alpha_U(2\pi u)+2\pi a .
 \tag{5}
\]

**Theorem 1.** Throughout (1),
\[
                  \frac{2}{25}<u<1-a,\qquad
                  \frac15<|v|<2 .
 \tag{6}
\]
The strict inequalities are uniform on the compact parameter set
(1). In particular the critical point has a positive distance
from both real cuts \(2/25\) and \(1-a\).

## 2. Elementary radius bounds

If \(|v|\ge2\), then \(U\le1/2\). Each of the three logarithmic
arguments in (5) has modulus at most \(\pi/6\): the circle
centered at one with radius at most \(1/2\) subtends that angle.
The outgoing radius is also at most \(1/2\). Hence
\[
 \Im Q_s\ge2\pi a-5\pi/6\ge\pi/6>0,
\]
contradicting (3). Thus \(U>1/2\).

For the other radius bound, \(w=1/v\) satisfies the monic polynomial
\[
 w^3+(Y-3)w^2+(2-Y/X)w+(1/X-1)=0 .
 \tag{7}
\]
Its coefficient moduli are at most \(4,3,2\). If \(|w|\ge5\),
then \(|w|^3>4|w|^2+3|w|+2\): the difference is positive
at five and increasing thereafter. This contradicts (7).
Thus \(U<5\), proving the radius assertions.

## 3. A small real part is impossible at large height

Suppose for contradiction that \(0<u\le2/25\).
First take \(U\ge8/5\) and set \(\beta=\arcsin(U^{-1})<\pi/4\).
For \(0<V<2\pi\),
\[
 \alpha_U(V)=\pi-V+\Arg(1-U^{-1}e^{iV}),\qquad
 |\Arg(1-U^{-1}e^{iV})|\le\beta .
 \tag{8}
\]
These sums have the original arguments: both factors lie in their
continuous half-plane branches, and their product is
\(1-Ue^{-iV}\).

For every positive radius \(R\), the outgoing argument obeys
\[
 \alpha_R(2\pi(z+u))\le14\pi/25 .
 \tag{9}
\]
Indeed for an angle below \(\pi\), its argument increases with
the radius to the limit \(\pi-2\pi(z+u)\le14\pi/25\);
for an angle at or above \(\pi\), its argument is nonpositive.
Insert (8)--(9) into (5):
\[
 \Im Q_s
 \le-2\pi+4\pi u+\frac{14\pi}{25}+4\beta
 <-2\pi+\frac{8\pi}{25}+\frac{14\pi}{25}+\pi
 =-\frac{3\pi}{25}<0 .
 \tag{10}
\]
This again contradicts (3).

## 4. A small real part is impossible at the remaining heights

It remains to consider \(1/2<U<8/5\).
Write \(w_0=(U-1)^2\), and introduce squared moduli
\[
 A=|1-Ue^{-2\pi i(a+u)}|^2,\quad
 B=|1-|Y|Ue^{-2\pi i(z+u)}|^2,\quad
 D=|1-Ue^{-2\pi iu}|^2 .
 \tag{11}
\]
The exact critical equation requires
\[
                         |e^{Q_s}|^2=\frac{AB}{D^3}=1.
 \tag{12}
\]
The incoming carrier has modulus one.

We shall prove instead that \(AB>D^3\). The following elementary
bounds hold throughout the assumed range \(0<u\le2/25\):
\[
 A>w_0+\frac{U}{16},\qquad
 D<w_0+\frac{U}{4},\qquad
 B>1+\frac{U^2}{4}-\frac U5,\qquad B>\frac{24}{25}.
 \tag{13}
\]
For the first bound, \(1/2<a+u\le191/200\), so
\(\cos(2\pi(a+u))\le\cos(9\pi/100)\).
If \(t=9\pi/100\), then \(27/100<t<3/10\) and
\[
 2(1-\cos t)\ge t^2-t^4/12
 >\frac{8667}{120000}>\frac1{16}.
\]
For the second, \(\sin(\pi u)<1/4\). A convenient exact witness is
\[
 \arcsin(1/4)\ge\frac14+\frac1{384}
    =\frac{97}{384}>\frac{44}{175}>\frac{2\pi}{25}.
\]
The arcsine inequality follows by integrating
\((1-t^2)^{-1/2}\ge1+t^2/2\).
For the two outgoing bounds, \(z+u\in[11/50,53/100]\), whence
\(\cos(2\pi(z+u))<1/5\).
The maximum cosine on that interval is
\(\sin(3\pi/50)<1/5\).
Thus \(B>1+(|Y|U)^2-(2/5)|Y|U\).
Completing the square gives \(B>24/25\).
Since \(|Y|U>U/2\ge1/4>1/5\), the same quadratic is increasing
there and gives the other outgoing bound in (13).

For \(1/2\le U\le5/4\), convexity gives
\[
 D< U^2-\frac74U+1\le\frac38,\qquad
 A>U^2-\frac{31}{16}U+1
       =\left(U-\frac{31}{32}\right)^2+\frac{63}{1024}.
\]
Consequently
\[
 AB>\frac{63}{1024}\frac{24}{25}
    =\frac{189}{3200}>\frac{27}{512}>D^3.
 \tag{14}
\]
The middle difference is \(81/12800>0\).

For \(5/4\le U\le8/5\), one has \(0\le w_0<2/5\), and
\[
 A>w_0+5/64,\qquad D<w_0+2/5,\qquad
 B>73/64>9/8.
\]
The polynomial
\[
 F(w)=\frac98(w+5/64)-(w+2/5)^3
 \tag{15}
\]
is concave for \(0\le w\le2/5\).
Both endpoint values are positive:
\[
 F(0)=45/512-8/125>0,\qquad
 F(2/5)=1377/2560-64/125>0 .
\]
Therefore \(F(w_0)>0\), which again proves \(AB>D^3\).
This contradicts (12) and completes the proof of \(u>2/25\).
The unit incoming branch theorem already gives \(u<1-a\).
Its continuity on the compact set (1) makes the strict gaps
uniform. \(\square\)

The theorem permits choosing a fixed sufficiently small positive
offset from the moving incoming wall, while keeping the same critical
point between that offset cut and \(2/25\). It does not estimate
the resulting finite contour, its weighted corrections, or the
physical rows outside it. Those are separate source estimates.

## Direct source versions

| Direct source | SHA-256 |
|---|---|
| research_mixed_four_conditional_unit_incoming_branch.md | b6c8fdaffd436ec82670ec864629d93d36e7c7a8ae7e81033b684e3f86e92e43 |
| research_mixed_initial44_near_endpoint_complete_pair.md | 4a481d134c93b8bb11bed2406253cec046f6e04a95339b1b48a8594469bc7712 |

The proof uses only hand algebra and analytic inequalities. No
mathematical numerical evaluation, saved-value arithmetic, test,
import, compilation or frozen-source change is used. Independent
full proof and direct-source review is required before adoption.
