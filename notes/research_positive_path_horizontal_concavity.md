# Every positive path saddle lies in a horizontal concavity rectangle

Research proof, 3 November 2026. Frozen manuscripts are unchanged.

For a positive circle-tree path, the geometric saddle lies in the
horizontal concavity domain whenever every integer power is at least
three. The earlier sufficient thresholds of six at a terminal and
eight at a degree-two vertex are therefore unnecessary for this
geometric conclusion. The proof uses the actual period equations,
including their imaginary parts. It is not a consequence of the
height bound alone.

This locates and compares the geometric phase on one rectangle for
paths of arbitrary length. A nonzero contribution of the original
finite quantum cycle, and bounds for its other parts, remain separate
requirements.

## 1. Statement and inputs

Consider the finite positive paths of the
[fractional-charge theorem](research_positive_path_fractional_charge_cube.md).
All selected powers satisfy \(n_v\ge3\), the charges satisfy
\(0\le\chi_v\le1\), and the stipulated complete outside endpoint
is retained. At an active vertex write
\[
 t_v=a_v-iH_v,\qquad 0<a_v<\pi,\qquad H_v>0.
 \tag{1}
\]
A zero-charge vertex has angle zero. Every incidence has its original
return
\[
 r_{vw}=k_{vw}+ig_{vw}
   =\operatorname{arsinh}\!\bigl(\tan(t_v/2)\cos(t_w/2)\bigr),
 \quad
 \sum_w k_{vw}=\frac{n_vH_v}{2},\quad
 \sum_w g_{vw}=\frac{n_va_v}{2}-\pi\chi_v .
 \tag{2}
\]
The original branch has \(k_{vw}>0\) at an active vertex and
\(-\pi/2<g_{vw}<\pi/2\). An absent incidence contributes zero.

The [cosine-phase maximum principle](research_geometric_phase_maximum_principle.md),
Theorem 5, proves on this family that
\[
 \beta_v:=\arg\cos(t_v/2),\qquad
                0\le\tan\beta_v<\frac1{\sqrt2}.
 \tag{3}
\]
Its proof uses the already established height bound \(H_v<23/20\);
it does not assume the theorem below.

**Theorem 1.** Every active vertex satisfies
\[
 -1<\Im\tan(t_v/2)<0.
 \tag{4}
\]
Equivalently,
\[
 \cos a_v>-e^{-H_v},\qquad
 a_v<T_v:=\arccos(-e^{-H_v}),\qquad
                         \Re(e^{it_v})>-1.
 \tag{5}
\]
The assertion holds throughout the charge cube and is independent
of the number of vertices and their individual powers.

The equivalence follows from
\[
 -\Im\tan((a-iH)/2)=\frac{\sinh H}{\cos a+\cosh H}.
 \tag{6}
\]
The denominator is positive. Subtracting \(\sinh H\) from it gives
\(\cos a+e^{-H}\).

## 2. Two consequences of the return arguments

We give the scalar estimates used in the proof. Put
\[
 b=\frac1{\sqrt2},\qquad B=\frac{\sinh H}{\sin a},\qquad
 \kappa=\frac{\sqrt{1+b^2}-1}{\sqrt{1+b^2}+1}
                       =5-2\sqrt6<\frac{11}{108}.
 \tag{7}
\]
The last comparison follows from
\(3\cdot97^2=28227<28322=2\cdot119^2\).
For every active vertex, the argument estimate from (3) gives
\[
                 a\le\frac{2\pi\chi}{n}+\kappa\sin a.
 \tag{8}
\]
Here is the deduction, so that the precise charge dependence is
explicit. The argument of the product in (2) is at most
\(\arctan b-\arctan B\). If \(B\ge b\), every \(g\le0\).
If \(0<B<b\), the identity
\(\tan g=\tanh k\,\tan\arg(\sinh r)\) gives
\[
 g\le k\frac{b-B}{1+bB}.
\]
Sum over incidences and use (2), followed by
\(H\le\sinh H=B\sin a\). The maximum of
\(B(b-B)/(1+bB)\) on \([0,b]\) is \(\kappa\), proving (8).

When \(B\ge b\), there is a stronger estimate. Define
\[
 d=\frac{B-b}{1+bB}\ge0,\qquad
                         f_d(k)=\arctan(d\tanh k).
 \tag{9}
\]
The original return arguments imply \(-g\ge f_d(k)\).
The function \(f_d\) is increasing, concave, and zero at zero,
since
\[
 f_d''(k)=
 -\frac{2d(1+d^2)\tanh k\,\operatorname{sech}^2 k}
              {(1+d^2\tanh^2 k)^2}\le0.
 \tag{10}
\]
For nonnegative \(k_i\) with sum \(S>0\), concavity gives
\(f_d(k_i)\ge(k_i/S)f_d(S)\). Therefore the period equations yield
\[
 \pi\ge\pi\chi
   \ge\frac{na}{2}+\arctan\!\left(d\tanh\frac{nH}{2}\right)
   \ge\frac{3a}{2}+\arctan\!\left(d\tanh\frac{3H}{2}\right).
 \tag{11}
\]
The last inequality uses \(n\ge3\). These estimates retain the
actual sum of returns; they do not presume that its two terms
are equal.

## 3. Excluding the boundary of the rectangle

Suppose (4) fails at a vertex. Set
\[
 u=e^{-H},\qquad
 a_0=\arccos(-u),\qquad
 B_0=\frac{\sqrt{1-u^2}}{2u}.
 \tag{12}
\]
Then (6) gives \(a\ge a_0>\pi/2\), and consequently \(B\ge B_0\).
Moreover,
\[
 \tan^2\beta
   =\tanh^2(H/2)\tan^2(a/2)
   \ge \tanh^2(H/2)\frac{1+u}{1-u}
   =\frac{1-u}{1+u}.
 \tag{13}
\]
Equation (3) forces \(u>1/3\). We consider two ranges.

**First range: \(u\ge1/2\).** Here \(a\ge a_0\ge2\pi/3\).
If \(B\ge b\), all the return imaginary parts are strictly
negative by (3), so \(a<2\pi\chi/n\le2\pi/3\), a contradiction.
Otherwise \(B_0\le B<b\) implies \(u>1/\sqrt3\), hence
\(a\ge a_0>\arccos(-1/\sqrt3)\). But (8), (7), and
\(\sin a\le\sqrt3/2\) give
\[
 a<\frac{2\pi}{3}+\frac{11\sqrt3}{216},
 \qquad
 \cos a>-\frac12-\frac{11}{144}
          =-\frac{83}{144}>-\frac1{\sqrt3}.
 \tag{14}
\]
For the cosine bound use
\(\cos(2\pi/3+x)\ge-1/2-\sqrt3\,x/2\) on this short
positive interval. The final strict comparison is
\(3\cdot83^2=20667<20736=144^2\).
This contradicts the lower bound on \(a\).

**Second range: \(1/3<u<1/2\).** Now \(B_0\ge\sqrt3/2>b\).
The function \(d(B)=(B-b)/(1+bB)\) increases, and \(a\ge a_0\).
Equation (11) would require
\[
 \frac{3a_0}{2}
  +\arctan\!\left[
       \frac{B_0-b}{1+bB_0}\frac{1-u^3}{1+u^3}
                  \right]\le\pi.
 \tag{15}
\]
We prove the strict reverse inequality throughout the closed
interval \(1/3\le u\le1/2\).

Put \(s=\sqrt{1-u^2}\) and \(r=\sqrt{(1+u)/(1-u)}
=\tan(a_0/2)\). The angle \(\pi-3a_0/2\) lies in
\([0,\pi/2)\). Its tangent is
\[
 \tan(\pi-3a_0/2)
       =r\,\frac{3-r^2}{3r^2-1}
       =\frac{1+u}{s}\frac{1-2u}{1+2u}.
 \tag{16}
\]
All denominators below are positive. Strict reversal of (15)
is therefore equivalent to
\[
 \frac{s-\sqrt2u}{2u+s/\sqrt2}\frac{1-u^3}{1+u^3}
       >\frac{1+u}{s}\frac{1-2u}{1+2u}.
 \tag{17}
\]
After multiplying out, (17) becomes \(\sqrt2 P>sQ\), where
\[
 \begin{split}
 P&=(1+u)(1+3u^2)(2u^3-u^2-u+1),\\
 Q&=(1+3u^2)(1+u-u^2-2u^3).
 \end{split}
 \tag{18}
\]
Both polynomials are positive on \([1/3,1/2]\): their final
factors are bounded below by \(1-u-u^2\ge1/4\) and
\(1-u^2-2u^3\ge1/2\), respectively. Squaring preserves the
desired inequality, and exact factorization gives
\[
 2P^2-(1-u^2)Q^2=(1+u)(1+3u^2)^2 R(u),
 \tag{19}
\]
where
\[
 R(u)=12u^7-21u^5+3u^4+15u^3-3u^2-3u+1.
 \tag{20}
\]
For a direct positivity proof put \(x=6u-2\in[0,1]\).
The Bernstein expansion is
\[
 R((2+x)/6)=\sum_{j=0}^7 b_j\binom7j x^j(1-x)^{7-j},
 \tag{21}
\]
with
\[
 (b_0,\ldots,b_7)=
 \left(\frac{130}{729},\frac{547}{3402},
 \frac{260}{1701},\frac{167}{1080},
 \frac{209}{1260},\frac{125}{672},
 \frac3{14},\frac14\right).
 \tag{22}
\]
Every coefficient is strictly positive and the Bernstein basis
sums to one. Thus \(R>0\) on the whole interval. Equations
(19), (18), and (17) prove the strict reverse of (15).
This final contradiction proves Theorem 1.

## 4. Consequence for the joint geometric phase

Fix a charge vector with positive active coordinates and let
\(t_v^*=a_v-iH_v\) be its original geometric solution. Zero-charge
vertices may be kept as fixed complete vertices. Retain the original
edge phase and define
\[
 \Phi(\mathbf t)=
 \sum_{e=vw}\psi(t_v,t_w)
   +\sum_{v\ {\rm active}}
       \left(\frac{in_vt_v^2}{4\pi}-i\chi_vt_v\right).
 \tag{23}
\]
Outside complete angles are zero, and the complete edge constants
are retained in the sum.

**Corollary 2.** The saddle lies in
\[
 \mathcal R_H=\prod_{v\ {\rm active}}(0,T_v),\qquad
 T_v=\arccos(-e^{-H_v}).
 \tag{24}
\]
On the fixed-height contour \(\mathbf t=\mathbf r-i\mathbf H\)
over this rectangle, \(\Re\Phi\) is strictly concave. Its unique
maximum is \(\mathbf a\). On every closed subrectangle
\(P\subset\mathcal R_H\) containing \(\mathbf a\), there is
\(\kappa_P>0\) such that
\[
 \Re[-2\pi\Phi''(\mathbf r-i\mathbf H)]
       \succeq\kappa_P\,\operatorname{diag}_v(\deg v),
 \qquad \mathbf r\in P.
 \tag{25}
\]
Consequently
\[
 \Re\Phi(\mathbf r-i\mathbf H)
 \le\Re\Phi(\mathbf t^*)
        -\frac{\kappa_P d_{\min}}{4\pi}
                            \|\mathbf r-\mathbf a\|^2.
 \tag{26}
\]
The complex Hessian at the saddle is nonsingular.

*Proof.* Theorem 1 supplies membership in (24). The assertions
then follow from Theorem 3 of
[the joint edge-Hessian theorem](research_edge_hessian_and_phase_response.md#6-joint-concavity-for-a-finite-graph-of-edges).
That theorem applies to every fixed finite graph on its rectangle;
its proof sums the positive real edge Hessians, and the filling
terms have purely imaginary second derivatives. \(\square\)

For each fixed path and fixed positive charges, a subrectangle
containing the saddle exists. No lower bound for \(\kappa_P\)
uniform in arbitrary path length or in charges approaching zero
is asserted. The location statement (4) itself has the full
uniform scope of Theorem 1.

The corollary compares the continued geometric phase. It does not
replace a full finite kernel by this phase at arbitrary complex
angles, and does not put a nonzero coefficient on its original
quantum cycle. The latter still needs a source representation and
estimates for all complementary pieces of that cycle.

## 5. Reproduction of the algebraic comparisons

Run

~~~sh
python3 experiments/verify_positive_path_horizontal_concavity.py
~~~

The [script](../experiments/verify_positive_path_horizontal_concavity.py)
uses exact rational arithmetic to check the factorization (19),
the eight coefficients (22), and the scalar comparisons in (7)
and (14). Its [record](../repro/results/research-positive-path-horizontal-concavity.json)
checks these finite algebraic steps. The all-path assertion follows
from the written period and phase argument.
