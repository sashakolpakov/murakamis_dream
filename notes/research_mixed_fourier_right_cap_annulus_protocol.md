# A fixed algebraic crossing test for the actual Fourier endpoint

Unexecuted proof and protocol, 7 November 2026. This test addresses
the correlated endpoint family, not the false inclusion of the
independent whole \(D_4\) disk. It uses the original saved enclosure
of \(Y=K\) as a bound input and only rational polynomial arithmetic.
It evaluates no exponential, logarithm, root, gain, or finite source.
The fixed polynomial filters below have not been tested.

If every prescribed crossing segment is excluded, the actual
auxiliary leg belongs to the old typed source domain \(K_3\).
That would remove one source-domain obligation. It would not pay
the outgoing halfweight remainder or prove the whole right-cap
bound.

## 1. The sufficient annulus and the connected actual family

Keep the exact correlated family and all original lifts of
[the scalar endpoint theorem](research_mixed_fourier_right_cap_correlated_endpoint.md).
The incoming leg \(a\) ranges over
\(\mathcal K=K_3\cup K_4\). Write
\[
 A=e^{-2\pi ia},\quad S=e^{-2\pi is},\quad Q=e^{-2\pi iq},
 \qquad B=e^{-2\pi i\beta_K(q)}.
 \tag{1}
\]
The original coupled equations give
\[
 \begin{split}
 B&=\frac{1-YQ}{Y+(1-2Y)Q},\\
 S&=1+Y^{-1}-Q-\frac{Y^{-1}-1}{Q},\\
 A&=\frac{1-SQ}{S(1-SQ)+(1-S)^3}.
 \end{split}
 \tag{2}
\]
The last vertex is ordinary type four. Both \(s,q\) belong to
\[
 O_4=\{|z-(.30-.052i)|\le.060,\quad
                         -.102\le\Im z\le-.001\}.
 \tag{3}
\]
The external input belongs to its full original \(K_\alpha\);
its type is not replaced by the type of the last vertex.

Consider the sufficient assertion
\[
                         2/3<|B|<3/2 .
 \tag{4}
\]
The already proved boundary update gives
\(|\beta_K(q)-(.35-.01i)|<.082<.083\).
Also
\[
 e^{.13\pi}>\frac32 .
 \tag{5}
\]
An exact witness is \(.13\pi>2041/5000\), using
\(\pi>157/50\), and
\[
 1+x+x^2/2+x^3/6-\frac32
 =\frac{2137369921}{750000000000}>0,
 \qquad x=2041/5000 .
 \tag{6}
\]
Thus (4) implies \(|\Im\beta_K(q)|<.065\).
The original ordinary type-three enclosure
\(O_3=P_3\cap\{-.065\le\Im b\le.068\}\) is contained
in \(K_3\), including its slanted side, by
[the typed-envelope theorem](research_mixed_typed_last_row_envelopes.md),
equations (5)--(6). This proves that (4) is sufficient.

The actual family is connected. Each \(K_\alpha\) is convex,
and the point \(.325-.031i\) lies in their intersection.
Existence, original zero lifts and uniqueness glue the last-vertex
critical branch over their union. The original alternating input
\(a=z_3^*\) belongs to \(K_3\), and its output is
\(s=q=z_4^*\), \(\beta_K(q)=z_3^*\).
The original paired-source heights give
\(-.03<\Im z_3^*<.015\). Consequently this anchor satisfies
(4): \(e^{.06\pi}<5/4<3/2\) and
\(e^{.03\pi}<28/25<3/2\), by the already proved elementary
bounds in the enlarged-rectangle theorem.

It is therefore enough to exclude the two circles
\[
                             |B|=2/3,\qquad |B|=3/2
 \tag{7}
\]
from the actual family. No pointwise assertion about every point
of a containing \(Q\)-rectangle is required. This is a
crossing argument along the connected actual branch.

## 2. Fixed rational necessary filters

For either \(Z=S\) or \(Z=Q\), (3) implies the following
six strict inequalities:
\[
 \begin{split}
 |Z|&>21/40,& |Z|&<500/503,&
 -\Im Z&>2/5,\\
 -\Re Z-\Im Z/15&>0,&
 \Re Z-5\Im Z/6&>0,&
 1/16-\Re Z&>0 .
 \end{split}
 \tag{8}
\]
These are necessary outer enclosures of the typed image;
they are not claimed equivalent to its disk and height filters.
Here are elementary proofs fixing their constants before any test.

First \(.204\pi<321/500\), and the positive exponential
series gives, for \(0<x<3\),
\[
 e^x\le1+x+\frac{x^2}{2(1-x/3)}.
 \tag{9}
\]
At \(x=321/500\) the right side is
\(249449/131000<40/21\), with difference
\(1571/2751000\). Hence \(|Z|>21/40\).
In the other direction
\[
 |Z|\le e^{-\pi/500}<\frac1{1+3/500}=\frac{500}{503}.
 \tag{10}
\]

For the angular bounds put \(v=7\pi/25\).
One has \(879/1000<v<22/25\).
The alternating sine and cosine series yield
\[
 \begin{split}
 \sin v&>
 \frac{879}{1000}-\frac{(22/25)^3}{6}
      +\frac{(7/8)^5}{120}-\frac{(9/10)^7}{5040}
                         >\frac{96}{125},\\
 \cos v&<
 1-\frac{(879/1000)^2}{2}+\frac{(22/25)^4}{24}
                         <\frac{16}{25}.
 \end{split}
 \tag{11}
\]
Every comparison in (11) is rational after the first elementary
angle bounds. On \(.24\le\Re z\le.36\), the smallest
\(\sin(2\pi\Re z)\) is \(\sin v\). Thus
\(-\Im Z>(21/40)(96/125)=252/625>2/5\).
Also \(\cot v<5/6\), which gives the left sector in (8).
The right sector follows from
\[
 \tan(\pi/50)
 <\frac{11/175}{1-(11/175)^2/2}<\frac1{15}.
 \tag{12}
\]
Finally the negative-height bound is retained in the real-coordinate
estimate:
\[
 \Re Z\le e^{-\pi/500}\sin(\pi/50)
 <\frac{\pi/50}{1+\pi/500}<\frac1{16};
 \tag{13}
\]
the last inequality is \(159\pi<500\), implied by
\(\pi<22/7\). Merely omitting the radial factor in (13)
would not prove this constant.

For the incoming exponent, the two typed sets give
\[
 .24\le\Re a\le.433,\qquad -.108\le\Im a\le.068.
 \tag{14}
\]
The following five strict necessary filters therefore hold:
\[
 \begin{split}
 |A|&>1/2,& |A|&<43/28,&-\Im A&>1/5,\\
 -\Re A-\Im A/15&>0,&
 \Re A-9\Im A/4&>0 .
 \end{split}
 \tag{15}
\]
Indeed \(.216\pi<17/25\) and the upper bound (9) there is
\(5739/2900<2\). Also \(.136\pi<3/7\) and (9) there
is \(43/28\). The smallest sine on (14) is
\(\sin(.134\pi)>\sin(21/50)>2/5\), using
\(21/50-(21/50)^3/6>2/5\).
This proves the imaginary bound. The right sector is again (12);
the left sector follows from
\[
 \tan(.134\pi)>\frac{21}{50}
                  +\frac{(21/50)^3}{3}>\frac49 .
 \tag{16}
\]
These necessary conditions use the union of both typed inputs,
not a false claim that their exponential images coincide.

There are also two necessary filters on the crossing variable
itself. The proved disk of radius \(.082\) gives
\(.268<\Re\beta_K(q)<.432\). On either circle \(|B|=R\),
\[
                   -\Re B>R/10,\qquad -\Im B>2R/5 .
 \tag{16a}
\]
Indeed \(-\cos(2\pi\Re\beta)\ge\sin(.036\pi)>1/10\)
and \(\sin(2\pi\Re\beta)\ge\sin(.136\pi)>2/5\).
For the first, use \(.036\pi>27/250\) and
\(27/250-(27/250)^3/6>1/10\). The second follows
from the same \(21/50\) sine bound used above.

## 3. Clear the original rational equations before enclosing

For each \(R\in\{2/3,3/2\}\), and each \(k=0,1,2,3\), use
the exact quarter-circle parametrization
\[
 d(t)=1-it,\qquad n(t)=R\,i^k(1+it),\qquad
 B(t)=n(t)/d(t),\qquad 0\le t\le1 .
 \tag{17}
\]
The eight charts cover both circles, with closed shared endpoints.
No trigonometric sampling or floating-point proposal is involved.
Define the complex polynomials
\[
 \begin{split}
 U&=d-Yn,&V&=Yd+(1-2Y)n,\\
 D&=YUV,&N&=(Y+1)UV-YU^2-(1-Y)V^2,\\
 E&=DV-NU,&
 N_A&=ED^2,\qquad
 D_A=NED+(D-N)^3V .
 \end{split}
 \tag{18}
\]
Where their denominators are nonzero, the original rational
identities (2) give
\[
                 Q=U/V,\qquad S=N/D,\qquad A=N_A/D_A.
 \tag{19}
\]
The Möbius transformation in (2) is its own inverse, so the
first equality is the correct orientation, not a new root.
The maximum degrees of these numerator/denominator pairs are
one, two and seven. The maximum degree of any cleared
real polynomial below is consequently fourteen.

All denominators in (19) are nonzero at an actual crossing.
One has \(Y\ne0,1\) and \(d(t)\ne0\). The two linear
polynomials \(U,V\) cannot vanish together, because the
Möbius determinant is \(-(1-Y)^2\ne0\).
At an actual point \(V\ne0\), since \(Q\) is finite, and
\(U\ne0\), since \(Q\ne0\). Hence \(D\ne0\).
Finally
\[
 \frac{D_A}{D^3V}
       =S(1-SQ)+(1-S)^3=\frac{1-SQ}{A}\ne0,
 \tag{20}
\]
because \(|S|,|Q|<1\) and \(A\ne0\).
This proves the required denominator exclusions on the actual
family, without trying to divide by a potentially singular
interval on an unrelated part of a circle.

For a pair \((n_z,d_z)\) from (19), put
\[
 T_z=|d_z|^2,\quad R_z=|n_z|^2,\quad
 X_z=\Re(n_z\overline{d_z}),\quad
 I_z=\Im(n_z\overline{d_z}).
 \tag{21}
\]
On the real parameter interval these are real polynomials.
The six polynomials corresponding to (8), in this fixed order,
are
\[
 \begin{split}
 R_z-(21/40)^2T_z,\quad
 (500/503)^2T_z-R_z,\quad
 -I_z-\tfrac25T_z,\quad
 -X_z-I_z/15,\quad
 X_z-5I_z/6,\quad
 T_z/16-X_z .
 \end{split}
 \tag{22}
\]
The five corresponding to (15) are
\[
 R_A-T_A/4,\quad
 (43/28)^2T_A-R_A,\quad
 -I_A-T_A/5,\quad
 -X_A-I_A/15,\quad
 X_A-9I_A/4 .
 \tag{23}
\]
Prepend to (22)--(23) the two polynomials
\[
 -\Re(n\overline d)-\tfrac R{10}|d|^2,\qquad
 -\Im(n\overline d)-\tfrac{2R}5|d|^2 .
 \tag{23a}
\]
They encode (16a), retaining the complete eight-chart cover.
Every one of the nineteen polynomials is strictly positive
at an actual crossing. Thus a uniform negative upper for any
one of them excludes that entire chart segment from the actual
family. No claim about the sign of a rational expression at
its poles is made. The polynomial tests themselves remain
defined there.

## 4. Fixed saved-input arithmetic protocol

The sole analytic bound input is the full interval field
constants.K of
[the original boundary-update record](../repro/results/research-mixed-fourier-boundary-update.json),
SHA-256
5d4cb057cb82ca4fff826ad768012480fd6f51afe66d3f5c632e48983cf17514.
It encloses the rational expression for \(K\) on the entire
original certified algebraic root square. The reader must verify
the record's passed status, original root/source association,
unchanged before/after bindings, both finite rational endpoint
intervals, and all inherited file hashes. It must not substitute
midpoints or reconstruct \(K\) from an approximate root.

Before testing crossings, verify the displayed rational witnesses
in (6), (9)--(16), including their endpoint substitutions, by
integer/fraction arithmetic. Their trigonometric and exponential
implications are inherited from the elementary proofs above;
no special function is reevaluated.

The fixed inventory is:

* the eight charts (17), ordered by \(R=2/3,3/2\), then
  \(k=0,1,2,3\);
* exactly 64 closed subintervals
  \([j/64,(j+1)/64]\), \(j=0,\ldots,63\), per chart;
* all nineteen polynomials, ordered as the two \(B\) filters,
  the six \(Q\) filters, the six \(S\) filters, and the five
  \(A\) filters;
* degree fourteen for every Bernstein conversion, with zero
  padding rather than a data-dependent degree choice.

Construct the coefficients of (18), then (21)--(23), using
complex rational interval polynomial arithmetic. Preserve the
shared real parameter \(t\) as a polynomial until this construction
is complete. The one original \(Y\) interval remains the bound
input at every multiplication; independent uses may enlarge an
enclosure but may never shrink it. Conjugation in (21) conjugates
coefficients, since \(t\) is real.

On a fixed cell substitute \(t=j/64+u/64\), \(0\le u\le1\),
using exact binomial expansion. If the resulting coefficient
intervals are \(c_0,\ldots,c_{14}\), the degree-fourteen
Bernstein intervals are
\[
 b_k=\sum_{j=0}^k c_j
           \frac{\binom{k}{j}}{\binom{14}{j}},
                         \qquad 0\le k\le14 .
 \tag{24}
\]
Their largest upper endpoint bounds the polynomial on the whole
cell. This follows because the Bernstein basis is nonnegative
and sums to one on \([0,1]\). Interval endpoints here are exact
rational bounds, not rounded displayed decimals.

Compute and save all bounds even after a cell has an exclusion.
There are exactly 512 cells, 9,728 polynomial upper bounds and
145,920 Bernstein coefficient intervals. A cell is excluded if
at least one of its nineteen uppers is strictly negative;
retain the first such filter in the fixed order as its witness.
Every other polynomial and every closed endpoint remains recorded.
No interval subdivision, alternate chart, constant adjustment,
new filter, precision refinement, or retry is permitted.
Fallback is none.

The future implementation is standard-library-only and has no
evaluator import. It must save exclusively to a new prescribed
output path, preserve every partial/failure record, and hash
all input files before and after. A malformed or changed input,
invalid rational construction, or missing cell is a calculation
failure. Any nonexcluded cell makes the outcome inconclusive;
it is not a counterexample to the correlated containment.
All 512 cells must pass before an annulus flag can be true.
No execution is authorized by this protocol document.

## 5. Exact consequence of a successful complete result

If the fixed result excludes all cells, equations (18)--(23)
show that neither circle (7) intersects the actual family.
Connectedness and the alternating anchor then prove (4) for
every incoming \(a\in\mathcal K\). Equations (5)--(6)
and the old \(O_3\subset K_3\) theorem give
\[
                       \beta_K(q(a))\in K_3 .
 \tag{25}
\]
This is an assertion only about the original correlated family.
The independent-disk counterexample remains true and immutable.

A successful result would let the complete ordinary conditional
source theorem use these actual external inputs. It would not
remove the \(+\Re g(q)/2\) Bregman remainder detailed in
Section 5 of the correlated-endpoint theorem, pay an outgoing
physical tail or contour join, or prove the whole right cap.
An inconclusive result establishes none of (4) or (25), and
cannot be used to alter this fixed protocol after inspection.
