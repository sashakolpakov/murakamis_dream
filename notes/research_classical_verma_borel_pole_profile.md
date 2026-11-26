# The canonical Verma Borel germ at a simple Alexander pole

Private written proof, 18 November 2026.

The actual classical Verma completion of [C] is Gevrey one on every
compact meridian set avoiding its Alexander poles. This follows from
finite total-index sectors of the original cut source, followed by
polynomial continuation in its grading. No analytic summation of the
infinite generic-quantum source is assumed.

At a simple Alexander pole where a supplied actual operator has a
transverse abelian/nonabelian node, its highest polar coefficients are
forced. Their scaled Borel series extends jointly across the pole and
has an explicit square-root restriction there. This is an exact germ
of the canonical coefficients. It does not identify a Laplace sum,
continue the joint germ to its prospective moving singularities, or
select a geometric coefficient of the root-of-unity invariant.

## 1. The source, coordinates, and assertions

Fix the zero-framed knot braid of [C], with \(b\) strands, word length
\(\ell\), writhe \(w\), and \(c=b-1-w\). Its permutation is one cycle,
so \(c\) is even. Write

\[
 h=\log Q,\qquad q=e^{h/2},\qquad
 x=x_0e^{-h/2},\qquad x_0^2=Y.
 \tag{1}
\]

Thus \(Y=Qx^2\) is the original natural meridian held fixed. In the
notation of [C], put

\[
 \mathscr W_K(h,Y)=\mathcal W_K(1-e^h,Y)
                 =\sum_{j\ge0}h^jW_j(Y).
 \tag{2}
\]

These \(W_j\) are coefficients in \(h\), rather than the coefficients
in \(1-Q\) used in [C]. Its rationality theorem implies

\[
 W_j\in\frac{\mathbb Q[Y^{\pm1}]}{\Delta_K(Y)^{2j+1}},
 \qquad W_0=\Delta_K^{-1}.
 \tag{3}
\]

Indeed an order-\(j\) coefficient after the analytic substitution
\(1-Q=1-e^h\) involves only the old orders at most \(j\).

**Actual-source Gevrey assertion.** For every compact
\(K\Subset\mathbb C^*\setminus\{\Delta_K=0\}\), there are finite
constants \(C_K,A_K>0\), independent of \(j\), such that

\[
                    \sup_K|W_j|\le C_K A_K^j j!.
 \tag{4}
\]

Let \(\alpha\ne0\) be a simple Alexander root. In particular
\(\alpha\ne1\). Suppose a supplied actual finite difference operator
annihilating (2) has coefficients holomorphic near \((h,Y)=(0,\alpha)\):

\[
 \mathcal P=\sum_{i=0}^d p_i(h,Y)T^i,
 \qquad Tf(Y)=f(e^hY),\qquad
 P(Y,L)=\sum_i p_i(0,Y)L^i.
 \tag{5}
\]

The explicit node conditions used below are

\[
 P(Y,1)\equiv0,\quad P_L(\alpha,1)=0,\quad
 P_{LL}(\alpha,1)\ne0,\quad P_{YL}(\alpha,1)\ne0.
 \tag{6}
\]

All derivatives in (6) refer to the displayed left-ordered symbol.
Set

\[
 r=\Delta_K'(\alpha)^{-1},\qquad
 A=\frac{\alpha^2}{2}P_{LL}(\alpha,1),\qquad
 B=\alpha P_{YL}(\alpha,1).
 \tag{7}
\]

**Canonical pole-profile assertion.** With \(z=Y-\alpha\),

\[
 c_j:=\left.z^{2j+1}W_j(\alpha+z)\right|_{z=0}
      =r(2j-1)!!(A/B)^j,\qquad (-1)!!=1.
 \tag{8}
\]

Moreover the series

\[
 \mathcal B^{\rm pole}(z,\eta)
   =\sum_{j\ge0}z^{2j+1}W_j(\alpha+z)\frac{\eta^j}{j!}
 \tag{9}
\]

defines a jointly holomorphic germ at \((0,0)\), and its restriction is

\[
 \boxed{\ \mathcal B^{\rm pole}(0,\eta)
         =r(1-2A\eta/B)^{-1/2}.\ }
 \tag{10}
\]

The square root in (10) has value one at \(\eta=0\). Conditions (6)
are checked conditions on the actual operator. A simple Alexander
root alone is not asserted to supply them or to identify the other
local branch with the geometric component.

## 2. A finite-sector estimate for the literal source

Assume first \(m=b-1\ge1\). Choose \(0<\rho\le1/4\) and \(X\ge1\)
bounding both \(|x_0|\) and \(|x_0|^{-1}\) on the compact being used.
Put \(\bar X=Xe^{\rho/2}\). At fixed total input index \(T_0\ge0\),
every intermediate index in the source is at most \(T_0\). On

\[
                   |h|\le\rho/(T_0+1),
 \tag{11}
\]

the moving \(x\) in (1) satisfies \(|x|,|x|^{-1}\le\bar X\).

For a positive crossing, the Gaussian coefficient in [C, (2)] is
a polynomial in \(Q\) with nonnegative integer coefficients, degree
\(n(a-n)\), and value \({a\choose n}\) at \(Q=1\). Therefore

\[
 |{a\brack n}_{e^h}|
 \le {a\choose n}\exp\!\left(\frac{\rho T_0}{4}\right).
 \tag{12}
\]

Here \(n(a-n)\le T_0^2/4\); if \(|Q|\le1\), the same estimate is
immediate without the exponential factor. The negative crossing uses
the identical bound with its second input index in place of \(a\).
The Cartan powers \(Q^{(a-n)b'}\) and \(Q^{-ab'}\) each have modulus
at most \(\exp(\rho T_0/4)\). The exponents in every color-product
factor have absolute value at most \(T_0\), so each such factor has
modulus at most \(1+\bar X^2e^\rho\). Finally the Laurent \(x\)
monomial costs at most \(\bar X^{T_0}\).

Summing the binomial bound over the actual allowed transfers gives
the following column-sum bound for both signed crossings on this
finite homogeneous sector:

\[
 \|R^\pm\|_1\le\mathfrak A^{T_0},\qquad
 \mathfrak A=\bar X e^{\rho/2}(2+\bar X^2e^\rho).
 \tag{13}
\]

There is no canceled denominator estimate in (12)--(13). In particular
the cases \(n=0,a\), \(T_0=0\), and \(Q=1\) use the literal polynomial
coefficients. The word costs \(\mathfrak A^{\ell T_0}\). Its ordinary
pivot \(Q^{-T_0}\) has modulus at most \(e^\rho\), and the original
framing scalar \(x^c\) costs at most \(\bar X^{|c|}\). There are
\({T_0+m-1\choose m-1}\) external traced inputs of this degree.
Consequently the exact coefficient \(V_{T_0}(h,Y)\) of the source
grading obeys

\[
 |V_{T_0}(h,Y)|\le
 \bar X^{|c|}e^\rho {T_0+m-1\choose m-1}
                         \mathfrak A^{\ell T_0}
 \quad\text{on (11)}.
 \tag{14}
\]

Each \(V_{T_0}\) is a finite original cut contraction, holomorphic in
\(h\). Cauchy's estimate on (11) gives a factor
\((T_0+1)^j\rho^{-j}\) for its order-\(j\) coefficient.
Choose \(0<a<1\), a grading radius
\(0<r_\tau\le\min(1/2,a\mathfrak A^{-\ell})\), and \(t>0\) with
\(ae^t<1\). The elementary exponential-series inequality
\((T_0+1)^j\le j!t^{-j}e^{t(T_0+1)}\) yields

\[
 \sup_{|\tau|\le r_\tau}|\mathscr V_j(Y,\tau)|
 \le C_0 C_1^j j!,\qquad
 C_0=\frac{\bar X^{|c|}e^{\rho+t}}{(1-ae^t)^m},\quad
 C_1=(\rho t)^{-1}.
 \tag{15}
\]

Here \(\mathscr V_j\) is the coefficient in \(h\) after the moving
meridian substitution (1). The summation uses the generating function
\(\sum_{T_0\ge0}{T_0+m-1\choose m-1}v^{T_0}=(1-v)^{-m}\).
It sums already defined normal coefficients. It does not assert a
common nonzero \(h\)-disk of convergence for the entire generic-\(h\)
graded source; the disks (11) shrink with the sector.

For \(b=1\) the braid is empty and the knot source is identically one.
Then (4) is immediate and there is no Alexander root to consider.

## 3. Grading-one continuation with a single factorial

Put \(\mathcal D(Y,\tau)=D_\beta(x_0,\tau)\), on a chosen local
square-root chart. The no-head differential argument of [C] gives

\[
 \mathscr V_j(Y,\tau)=
 \frac{\mathscr P_j(Y,\tau)}{\mathcal D(Y,\tau)^{2j+1}},
 \qquad \deg_\tau\mathscr P_j\le2jm.
 \tag{16}
\]

Here the numerator is holomorphic in the chosen meridian chart.
For clarity, the degree bound follows directly as well. An order-\(j\)
coefficient is a sum of polynomial differential insertions of order
at most \(2j\) before the same classical substitution. Such an insertion
is a sum of products of at most \(2j\) degree-zero vector fields.
For \(d\le2j\) vector fields, its trace differentiates the inverse
determinant at most \(d\) times. Every determinant derivative has
grading degree at most \(m\): the matrix
\(\tau L_\beta E_0\), where \(E_0=\operatorname{diag}(0,1,\ldots,1)\),
and all its left-substitution deformations have
rank at most \(m\). On denominator \(\mathcal D^{d+1}\), the numerator
therefore has degree at most \(dm\). Multiplication by
\(\mathcal D^{2j-d}\) proves (16).

The same argument applies directly with \(h\) as parameter. Expanding
each signed coefficient along (1) preserves the order-\(j\) polynomial
index degree at most \(2j\): the extra \(x\)-monomial normal has degree
at most its order, and the color-product logarithmic coefficient has
degree at most its order plus one, exactly as in [C, Section 2].
Thus (16) does not require a derivative estimate that could add another
factorial. Equivalently, the finite meridian chain rule in [C] gives
the same bound. Square-root independence is its exact source parity.

On a compact \(K\) avoiding the Alexander divisor, let

\[
 H=\max\left(1,\sup_{Y\in K,|\tau|=r_\tau}|\mathcal D(Y,\tau)|\right),
 \qquad d_K=\inf_{Y\in K}|\mathcal D(Y,1)|>0.
 \tag{17}
\]

Indeed \(\mathcal D(Y,1)=x_0^c\Delta_K(Y)\), with the exact original
unit. A polynomial of degree at most \(D\), bounded by \(M\) on
\(|\tau|=r_\tau\le1/2\), has value at \(\tau=1\) bounded by
\(2M r_\tau^{-D}\), by Cauchy's coefficient bounds and the finite
geometric sum. Applying this to (16) and then dividing by its actual
determinant gives

\[
 \sup_K|W_j|
 \le 2C_0\frac{H}{d_K}
       \left[C_1\left(\frac{H}{d_K}\right)^2r_\tau^{-2m}\right]^j j!.
 \tag{18}
\]

This proves (4). All constants may depend on the fixed braid and
compact. A compact may be covered by finitely many square-root charts;
both choices obey the same bounds. No estimate uniform through an
Alexander zero has been used.

## 4. The actual transport forces the highest poles

Let \(P_1(Y,L)=\sum_i[h]p_i(h,Y)L^i\). The order-\(h\) equation of
\(\mathcal P\mathscr W_K=0\), using \(P(Y,1)=0\), is exactly

\[
 YP_L(Y,1)W_0'(Y)+P_1(Y,1)W_0(Y)=0.
 \tag{19}
\]

Since \(W_0\sim r/z\), (6) and (19) give

\[
 P_1(\alpha,1)=B.
 \tag{20}
\]

Expand the finite shifts directly as a formal differential operator:

\[
 \mathcal P=\sum_{n\ge1}h^n\mathcal L_n,
 \qquad \operatorname{ord}\mathcal L_n\le n.
 \tag{21}
\]

The order-zero term is zero as a differential operator, because
\(P(Y,1)\equiv0\). All coefficients of \(\mathcal L_n\) are holomorphic
near \(z=0\). Equations (6), (7), and (20) give

\[
 \mathcal L_1=(Bz+O(z^2))\partial_z+(B+O(z)),\qquad
 \mathcal L_2=(A+O(z))\partial_z^2
                         +\text{terms of order at most one}.
 \tag{22}
\]

For the second coefficient, \(T^i=e^{ihY\partial_Y}\) and
\(\sum_i i^2p_i(0,Y)=P_{LL}(Y,1)+P_L(Y,1)\). This proves the
\(A\) in (22), including the factor \(1/2\) and the original ordering.

At order \(h^{j+1}\), \(j\ge1\), the equation is

\[
 \sum_{n=1}^{j+1}\mathcal L_n W_{j+1-n}=0.
 \tag{23}
\]

By (3), \(\mathcal L_nW_{j+1-n}\) for \(n\ge3\) has pole order at
most \(2j+3-n\le2j\). Thus it cannot contribute to order
\(z^{-2j-1}\). At that order, (22) gives exactly

\[
       -2jB c_j+2j(2j-1)A c_{j-1}=0.
 \tag{24}
\]

Since \(B\ne0\), (24), starting with \(c_0=r\), proves (8).
In particular all these highest poles are present, not only bounded
above by the rational-loop denominator theorem.

If the supplied operator is the original normal-state operator
\(B_{\rm norm}\) annihilating \((Y-1)\mathscr W_K\), use
\(\mathcal P=B_{\rm norm}\circ(Y-1)\) in (5).
This retains its actual gauge. At \(\alpha\ne1\) its classical
symbol is multiplied by the unit \(Y-1\); at the node both derivatives
in (7) are multiplied by the same nonzero value. Thus \(A/B\) and
(8) are unchanged. No global peripheral factor is discarded.

## 5. A jointly holomorphic Borel germ on the pole chart

Choose \(R>0\) so that the meridian disk \(|Y-\alpha|\le R\)
meets neither \(Y=0\) nor another Alexander root, and contains
no pole of the operator coefficients.
Every

\[
                  a_j(z)=z^{2j+1}W_j(\alpha+z)
 \tag{25}
\]

is holomorphic on this disk, by (3). Apply (4) on its boundary circle:
\(|W_j|\le C A_0^j j!\). The maximum principle then gives

\[
 \sup_{|z|\le R}|a_j(z)|
                    \le CR(R^2A_0)^j j!.
 \tag{26}
\]

Consequently (9) converges normally on smaller products with
\(|\eta|<(R^2A_0)^{-1}\), and defines a joint holomorphic germ across
\(z=0\). Substitution of (8) gives

\[
 \mathcal B^{\rm pole}(0,\eta)
 =r\sum_{j\ge0}\frac{(2j-1)!!}{j!}(A\eta/B)^j
 =r(1-2A\eta/B)^{-1/2}.
 \tag{27}
\]

For \(z\ne0\) in the common local domain, this is literally the scaled
canonical Borel transform

\[
 \mathcal B^{\rm pole}(z,\eta)
  =z\,\mathcal B_h\mathscr W_K(\alpha+z,z^2\eta),\qquad
 \mathcal B_h\mathscr W_K(Y,\xi)=\sum_jW_j(Y)\xi^j/j!.
 \tag{28}
\]

No choice of summation or contour entered (25)--(28). The restriction
has its explicit square-root branch point at
\(\eta_*=B/(2A)\ne0\). This establishes the analytic continuation and
singularity of that one-variable restriction, not joint continuation
of (9) up to \((0,\eta_*)\), or a singularity at nearby nonzero \(z\).

The location also has a classical calibration. The other normalized
local branch has
\(L=1-2P_{YL}z/P_{LL}+O(z^2)\). For the difference action defined by
\(dS=\log L\,d\log Y\), relative to the abelian branch, integration
gives \(S=-\eta_*z^2+O(z^3)\). This matches the quadratic scale in
(28). It does not identify this branch as geometric or give its
coefficient in the actual source.

## 6. Scope and proof source

The highest-pole recursion concerns the canonical \(q\to1\) source
of [C]. It is not the fixed-level residue with denominator
\(\Delta_K(Y^N)\). The fixed-circle estimate (18) is an actual-source
coefficient estimate, while (27) is an exact evaluation of its Borel
germ on the exceptional divisor. Neither is a remainder estimate for
an analytic generic-\(q\), grading-one period.

No Borel continuation for nonzero \(z\), lateral Laplace identification,
source-cycle deformation, nonzero geometric intersection, or
large-level lower bound has been proved. In particular the local
node assumptions do not replace the original arbitrary-short-filling
target by a new class of knots.

The only proof direct is the following complete text:

| Label | Complete source | SHA256 |
|---|---|---|
| C | notes/research_classical_verma_rational_loops.md | f88f5fc4d1eb0f68f9270e581bd0e1bfd43c669cef989d9813f6000feb4e3659 |

C supplies the literal source, its no-head differential realization,
original cut and pivot normalization, rational-loop pole orders,
canonical natural meridian, and actual operator compatibility.
The finite-sector estimates, numerator degree, local differential
calculation, and Borel extension are proved above. The archived
formal_a_curve_period_torsor already contains the general formal
two-branch node scaling; that formal calculation is rederived here
and is not an additional proof premise. The double-factorial
simple-pole pattern and the corresponding error-function transition
are not claimed as new universal phenomena. The assertions here are
the canonical source normalization, fixed-circle Gevrey estimate,
and joint pole-scaled Borel germ under (6).
No literature proof, numerical
calculation, test, or build is used. Frozen notes and public manuscripts
are unchanged.
