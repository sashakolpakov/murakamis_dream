# The actual full-clock family has a uniform initial Borel germ

Private written proof, 18 November 2026.

Keep the fixed highest-cut knot braid and its integral path-index lattice
from [M]. Inserting the whole clock \(Q^{m\cdot k}\) gives an initial
Borel family whose radius is independent of the complex clock parameter
\(m\). Its dependence on \(m\) is entire of exponential type, with type
\(O(|Y-\alpha|)\) in the pole chart. At an actual
simple two-branch node as in [G], all these full clocks have the same
exceptional square-root restriction.

The proof concerns the initial canonical germ. It does not continue an
inserted minor to the moving divisor or identify a leading clock ratio
with a classical character. In particular it does not remove a
characteristic cofactor from [M]'s marked equations.

## 1. Exact source and clock parameters

Fix a \(b\)-strand braid with one-cycle permutation, its original highest
input/output cut index zero, ordinary pivots and zero framing. Write
\[
 h=\log Q,\qquad x=x_0e^{-h/2},\qquad x_0^2=Y.
 \tag{1}
\]
Let \(k\in\mathbb Z^s\) be [M]'s fixed integral coordinates on the lattice
of all matching equations. For \(m\in\mathbb C^s\), define the formal
canonical source
\[
 \mathscr W_m(h,Y)
 =\mathcal W_\beta(1-e^h,Y;e^{hm_1},\ldots,e^{hm_s})
 =\sum_{j\ge0}h^jW_{j,m}(Y).
 \tag{2}
\]
The logarithm \(h\) in (1) fixes this exponential for nonintegral \(m\).
For integral \(m\), the inserted path factor is literally
\(Q^{m\cdot k}\). Equation (2) retains its whole exponential. It is not
a bounded-degree replacement of that factor on indices of size \(1/h\).

At a fixed external total index \(T\), every intermediate physical
label is between zero and \(T\), and every signed transfer has absolute
value at most \(T\). Each \(k_i\) is a fixed integral linear function of
these labels, by [M, Section 1]. There is consequently a constant
\(K_\beta\ge0\), depending only on this coordinate choice and word, with
\[
                 \|k\|_\infty\le K_\beta T.
 \tag{3}
\]
This includes negative coordinates and every supported path. The sector
\(T=0\) has \(k=0\). Marks are diagonal insertions at fixed word stages;
they change neither the allowed paths nor their cut and framing factors.

We prove the following uniform bound. For every compact
\(K\Subset\mathbb C^*\setminus\{\Delta_K=0\}\), there are constants
\(C_K,A_K>0\) and \(c_\beta\ge0\), independent of \(j,m\), such that
\[
 \sup_{Y\in K}|W_{j,m}(Y)|
       \le C_K e^{c_\beta\|m\|_1} A_K^j j!
 \quad(j\ge0,\ m\in\mathbb C^s).
 \tag{4}
\]
The subscript \(K\) on the Alexander polynomial denotes the knot, as in
the direct sources. The compact in (4) does not contain an Alexander
zero. A one-strand empty braid has source one and satisfies all these
statements trivially; it has no Alexander node to consider below.

## 2. Polynomial clock degree and the sharper pole filtration

Let \(V_m(h,Y;\tau)\) denote the graded source before setting
\(\tau=1\). Expanding the exact exponential in one finite sector gives
\[
 [h^j]V_m
 =\sum_{d=0}^j\frac1{d!}
       [h^{j-d}]V\bigl[(m\cdot k)^d\bigr].
 \tag{5}
\]
Here brackets inside \(V\) mean insertion into the original path
summand. Thus every coefficient is a polynomial in \(m\) of total
degree at most \(j\). Formula (5) is an exact coefficient identity for
the full clock, not a truncation made before the coefficient is taken.

The fixed-\(Y\), order-\(r\) source in [G, Sections 2--3] is a sum of
degree-zero differential operators of order at most \(2r\), followed by
the same classical linear substitution. A degree-\(d\) index polynomial
adds at most \(d\) Euler insertions. Transport through the invertible
local substitutions preserves differential order. The cut projector is
retained and is never inverted. Therefore the degree-\(d\) part in (5)
has differential order at most
\[
                         2(j-d)+d=2j-d.
 \tag{6}
\]
The moving meridian, original pivot and framing are already included
in [G]'s fixed-\(Y\) order estimate.

Put \(n=b-1\) and use the unmarked classical determinant
\[
 \mathcal D(Y,\tau)
   =\det(I-\tau L_\beta(x_0)T_0),\qquad
 T_0=\operatorname{diag}(0,1,\ldots,1).
 \tag{7}
\]
The determinant trace calculation in [M, Section 3] and
[G, Section 3], applied with (6), gives
\[
 [h^j]V_m
     =\frac{\mathscr P_{j,m}(Y,\tau)}
             {\mathcal D(Y,\tau)^{2j+1}},
 \qquad \deg_\tau\mathscr P_{j,m}\le 2jn.
 \tag{8}
\]
Indeed a differential operator of order at most \(r\) has denominator
\(\mathcal D^{r+1}\) and numerator grading degree at most \(rn\).
For the degree-\(d\) term use \(r=2j-d\), then multiply the numerator
by \(\mathcal D^d\). Its degree is at most \(2jn\).
At \(h=0\) every clock mark is one, so the determinant in (7) is
unmarked, independently of \(m\).

At grading one, the exact identity
\(\mathcal D(Y,1)=x_0^c\Delta_K(Y)\) has the original framing unit,
where \(c=b-1-\operatorname{wr}(\beta)\) is even. The same staggered
parity conjugation commutes with all marks. Hence the coefficients in
(2) are rational in \(Y\), independent of its square-root chart. More
precisely, if \(W_{j,m}^{[d]}\) is the homogeneous degree-\(d\) part
in \(m\), then
\[
 W_{j,m}^{[d]}
 \in
 \frac{\mathbb Q[Y^{\pm1},m_1,\ldots,m_s]_d}
      {\Delta_K(Y)^{\,2j-d+1}},
 \qquad 0\le d\le j.
 \tag{9}
\]
Temporary meridian denominators cancel by the same finite grading
coefficient argument used in [M]. In particular
\[
 W_{j,m}-W_{j,0}\ \text{has Alexander pole order at most }2j
 \quad(j\ge1),\qquad W_{0,m}=\Delta_K^{-1}.
 \tag{10}
\]

## 3. Uniform Gevrey bound for the whole clock

Use a fixed \(0<\rho\le1/4\) in [G]'s finite-sector estimate. On
its actual Cauchy disk
\[
                         |h|\le\rho/(T+1),
 \tag{11}
\]
equation (3) gives, for every path,
\[
 |e^{h\,m\cdot k}|
 \le \exp\!\left(\rho K_\beta\|m\|_1\,\frac{T}{T+1}\right)
 \le e^{\rho K_\beta\|m\|_1}.
 \tag{12}
\]
Consequently [G, (14)] holds for the marked finite sector after
multiplication by precisely this last bound. No division by a crossing
entry and no infinite generic-\(h\) trace is used.

Cauchy estimation on (11), followed by the small-grading sum in
[G, (15)], therefore gives constants \(C_0,C_1,r_\tau>0\), independent
of \(m,j\), with
\[
 \sup_{Y\in K,\ |\tau|\le r_\tau}
       |[h^j]V_m(h,Y;\tau)|
 \le C_0 e^{\rho K_\beta\|m\|_1} C_1^j j!.
 \tag{13}
\]
Choose \(r_\tau\le1/2\). The source sum here is a sum of normal
coefficients already defined by finite sectors. It is not a claim of
a common \(h\)-disk for the unsummed generic-\(h\) source.

On the chosen meridian charts put
\[
 H=\max\!\left(1,\sup_{Y\in K,\ |\tau|=r_\tau}
                         |\mathcal D(Y,\tau)|\right),
 \qquad d_K=\inf_{Y\in K}|\mathcal D(Y,1)|>0.
 \tag{14}
\]
Multiply (13) by \(\mathcal D^{2j+1}\). The result is the polynomial
in (8), of degree at most \(2jn\). Cauchy's coefficient estimate for
that polynomial, evaluated at \(\tau=1\), gives
\[
 \sup_K |W_{j,m}|
 \le 2C_0\,\frac H{d_K}\,e^{\rho K_\beta\|m\|_1}
   \left[C_1(H/d_K)^2r_\tau^{-2n}\right]^j j!.
 \tag{15}
\]
This proves (4), with \(c_\beta=\rho K_\beta\).
Finitely many meridian charts suffice for a compact. Both square-root
choices give the same actual source. In particular the Gevrey type
\(A_K\), not merely its finiteness on bounded \(m\)-sets, is independent
of the clock parameter.
The number \(\rho>0\) may be chosen arbitrarily small; this decreases
\(c_\beta\) at the cost of changing the Gevrey constants.

## 4. The initial family at an actual simple two-branch node

Let \(\alpha\ne0\) be a simple Alexander root. Let
\(\mathcal P=\sum_i p_i(h,Y)\mathsf T^i\) be a supplied actual
annihilator of the unmarked source, with coefficients holomorphic
near \((0,\alpha)\), where \(\mathsf T f(Y)=f(e^hY)\).
Put \(P(Y,L)=\sum_i p_i(0,Y)L^i\), and assume precisely
the node conditions [G, (6)]:
\[
 P(Y,1)\equiv0,\quad P_L(\alpha,1)=0,\quad
 P_{LL}(\alpha,1)P_{YL}(\alpha,1)\ne0.
 \tag{16}
\]
Use [G]'s constants
\[
 r=\Delta_K'(\alpha)^{-1},\qquad
 A=\frac{\alpha^2}2P_{LL}(\alpha,1),\qquad
 B=\alpha P_{YL}(\alpha,1),\qquad \eta_*=\frac B{2A}.
 \tag{17}
\]
Choose \(R>0\) so \(|Y-\alpha|\le R\) contains no other Alexander
zero and avoids zero. Put \(z=Y-\alpha\). By (9),
\[
 a_{j,m}(z)=z^{2j+1}W_{j,m}(\alpha+z)
 \tag{18}
\]
is holomorphic on this disk and polynomial in \(m\). Apply (4) on
the boundary circle. For constants \(C,A_0\) independent of \(m,j\),
\[
 \sup_{|z|=R}|W_{j,m}(\alpha+z)|
       \le C e^{c_\beta\|m\|_1}A_0^j j!.
 \tag{19}
\]
Write \(W_{j,m}=\sum_\nu W_{j,\nu}m^\nu\), with
\(d=|\nu|\le j\). Multivariable Cauchy estimates at radii
\(\nu_i/c_\beta\) for \(\nu_i>0\), and limiting radii zero for
\(\nu_i=0\), give
\[
 \sup_{|z|=R}|W_{j,\nu}(\alpha+z)|
 \le C A_0^j j!\,
       \frac{(e c_\beta)^d}{\prod_i\nu_i^{\nu_i}}
 \le C A_0^j j!\frac{(e c_\beta)^d}{\nu!}.
 \tag{19a}
\]
Empty factors are one. If \(c_\beta=0\), the entire bound (19)
makes every nonconstant coefficient zero, and the same conclusion
holds directly.

By (9), \(z^{2j-d+1}W_{j,\nu}(\alpha+z)\) is holomorphic.
The maximum principle applied to this function, followed by the
multinomial formula, proves on \(|z|\le R\)
\[
\begin{split}
 |a_{j,m}(z)|
 &\le CR(R^2A_0)^j j!
       \sum_{d=0}^j\frac{
          (e c_\beta |z|\|m\|_1/R)^d}{d!}\\
 &\le CR(R^2A_0)^j j!
                  e^{c_*|z|\|m\|_1},
 \qquad c_*=\frac{e c_\beta}{R}.
\end{split}
 \tag{19b}
\]
The clock-degree extraction has introduced no \(j\)-dependent
factor beyond the already present Gevrey bound.
Thus
\[
 \mathcal B_m^{\rm pole}(z,\eta)
    =\sum_{j\ge0} a_{j,m}(z)\frac{\eta^j}{j!}
 \tag{20}
\]
converges jointly for \(|z|<R\), \(|\eta|<(R^2A_0)^{-1}\), and
all \(m\in\mathbb C^s\). More precisely,
\[
 |\mathcal B_m^{\rm pole}(z,\eta)|
   \le\frac{CR}{1-R^2A_0|\eta|}
                    e^{c_*|z|\|m\|_1}.
 \tag{20a}
\]
Thus its clock exponential type is at most \(c_*|z|\), and the
Borel radius is independent of \(m\). The proof keeps a fixed
meridian circle while extracting clock coefficients; no circle
shrinking with \(j\) or \(m\) is used.

For \(z\ne0\), (20) is literally
\[
 \mathcal B_m^{\rm pole}(z,\eta)
       =z\,\mathcal B_h\mathscr W_m(\alpha+z,z^2\eta).
 \tag{21}
\]
Equation (10) makes \(a_{j,m}(0)=a_{j,0}(0)\). The actual unmarked
highest-pole formula in [G] therefore proves the exact restriction
\[
 \boxed{\displaystyle
    \mathcal B_m^{\rm pole}(0,\eta)
       =r(1-\eta/\eta_*)^{-1/2}
       \quad\text{for every }m\in\mathbb C^s.}
 \tag{22}
\]
The branch at \(\eta=0\) has value one. More generally, (9) shows that
the homogeneous degree-\(d\) part of \(a_{j,m}(z)\) is divisible by
\(z^d\). In particular the difference of (20) and its unmarked member
is divisible by \(z\) as a joint holomorphic germ.

Equivalently the substitution \(m=\nu/z\), initially for \(z\ne0\),
extends (20) to a joint holomorphic germ in \((z,\eta)\), entire in
\(\nu\), with exponential type at most \(c_*\) in \(\nu\). This is
another formulation of (19a)--(19b); its restriction at \(z=0\)
for nonzero \(\nu\) is not asserted to be (22).

## 5. Scope and complete proof sources

All marks in (2) are retained through the actual source. The same
initial profile does not establish the same continued minor or a
multiplicative clock evaluation at fixed nonzero \(z\). It gives no
uniform continuation around a characteristic cofactor of [M]'s
diagonal, no inserted finite-cutoff asymptotic, and no geometric
character or physical scalar lower bound.

The square-root assertion uses the simple two-branch conditions (16).
For a higher collision, the coarse pole estimate (9) alone gives
neither its sharper pole filtration nor its exceptional profile.

The following complete texts were read in full, and their used
implications checked:

| Label | Complete direct source | SHA256 |
|---|---|---|
| M | notes/research_marked_verma_full_certificate_transport.md | a2d94711bb80e69139e25b4932f0878440934c0586ddd0535dc24fcfd61987b4 |
| G | notes/research_classical_verma_borel_pole_profile.md | 6ba957d7a521524f370cb3bdd90ab30338bff8c13960ae6ca1825d08260c77d2 |

Only written mathematics, source reads and hash checks were used.
Frozen proofs and public documents are unchanged.
