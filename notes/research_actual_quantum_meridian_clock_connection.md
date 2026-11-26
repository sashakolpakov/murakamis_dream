# A boundary-free quantum meridian connection on the actual clock period

Private written proof, 18 November 2026.

The original highest-cut word has an exact first-order external
meridian equation whose clock denominator is a local analytic unit.
The unit is defined on a whole spectral polydisk. Consequently its
inverse acts on the actual Cauchy-period quotient, rather than only
on a chosen contour representative.

This pays one analytic block of the joint source equations. It does
not divide the internal Ward equations, produce a finite-meridian
clock character, or identify a physical geometric coefficient.

## 1. The source, with all indices and framing retained

Fix the knot braid and the integral matching lattice of [J]. Write
\[
 Q=q^2=e^h,\qquad Y=Qx^2,\qquad
 c=b-1-\operatorname{wr}(\beta)\in2\mathbb Z.
 \tag{1}
\]
The lattice coordinates are \(k\in\mathbb Z^d\). Every crossing input
and transfer is an integral linear form in \(k\). The original
summand, zero outside its fixed support cone, is
\[
 \mathcal I(Q,x,\tau;k)
   =x^c\tau^{T(k)}Q^{-T(k)}
                    \prod_{\text{crossings}}R^\pm.
 \tag{2}
\]
The two cut indices remain zero. The ordinary pivots and zero-framing
scalar in (2) have not been moved into a new closing functional.
Every fixed total-index sector is finite.

Use all independent clock weights \(Q^{m\cdot k}\). Let
\(\mathscr W_m(h,Y)\) denote the coefficientwise grading-one
completion of their original sum. By [F,J], this completion is
obtained from the same finite-sector identities; it is not an
arbitrarily chosen solution of their equations.

Let \(\mathsf T\) send \(x\) to \(qx\), or \(Y\) to \(QY\), with
\(h,m\) fixed. Let
\[
                    \mathsf E_i f(m)=f(m+e_i).
 \tag{3}
\]
For an integral linear form \(a(k)\), write
\(X^a=\prod_iX_i^{a(e_i)}\), and likewise \(\mathsf E^a\).
Negative exponents are allowed.

At a positive crossing with inputs \(a,b'\) and transfer \(n\),
the literal entry [F, (2)] gives
\[
 \frac{R^+(Q,qx)}{R^+(Q,x)}
  =q^{-a-b'+n}
          \frac{1-Y^{-1}Q^{a-n}}{1-Y^{-1}Q^a}.
 \tag{4}
\]
At a negative crossing it gives
\[
 \frac{R^-(Q,qx)}{R^-(Q,x)}
  =q^{a+b'-n}
          \frac{1-YQ^{n-b'}}{1-YQ^{-b'}}.
 \tag{5}
\]
For example, in (4) the color product has start
\(x^{-2}Q^{a-n}\). Replacing \(x\) by \(qx\) decreases its start
exponent by one, so its ratio is
\((1-x^{-2}Q^{a-n-1})/(1-x^{-2}Q^{a-1})\).
Substitution \(x^{-2}=Q/Y\) proves the displayed formula.
For (5), increasing the start exponent of
\((x^2Q^{1-b'};Q)_n\) by one gives its displayed ratio.
The Gaussian and Cartan factors do not change in either formula.
These are generic ratios; below their denominators are cleared.

Define the integral matching-lattice form
\[
 H(k)=\sum_-(a+b'-n)+\sum_+(-a-b'+n).
 \tag{6}
\]
It is even on the entire matching lattice. Indeed the sign change
\(x\mapsto-x\) in each crossing is its output/input ratio for
the staggered sign \((-1)^{\sum_j j a_j}\). These ratios telescope
on each closed matching path with the original cut. This uses only
the matching equations, not positivity or summation. Thus \(H/2\)
is an integral linear form; this is also the pathwise parity
calculation in [F,T].

Put
\[
\begin{split}
 D(Y,X)&=\prod_+(1-Y^{-1}X^a)
                         \prod_-(1-YX^{-b'}),\\
 N(Y,X)&=\prod_+(1-Y^{-1}X^{a-n})
                         \prod_-(1-YX^{n-b'}),\\
 \mathcal R(Y,X)&=X^{H/2}\frac{N(Y,X)}{D(Y,X)}.
\end{split}
 \tag{7}
\]
The index letters in these products are the forms at their respective
crossings, rather than extra independent variables.

## 2. The exact external row has no support-boundary factor

Multiplying (4)--(5), with the original prefactor in (2), gives
the cleared identity
\[
 D(Y,X)\,\mathcal I(Q,qx,\tau;k)
       =Q^{c/2}X^{H/2}N(Y,X)\,\mathcal I(Q,x,\tau;k),
 \qquad X_i=Q^{k_i}.
 \tag{8}
\]
It holds on the whole zero-extended lattice. On the supported cone
it is the proper product identity just proved, initially at generic
parameters and then after Laurent-polynomial continuation. Outside
the cone both entries vanish. The external shift changes no label,
transfer inequality, or support face. In particular (8) requires no
factor \(\Theta_v\) of [J].

The original \(x^c\) contributes \(q^c=Q^{c/2}\). The pivot
\(Q^{-T}\), total-index grading, and clock weights are unchanged.
There is no additional quantum dimension or closing normalization.
The forced vacuum columns and rows remain those of [J].

Multiplication by \(X_i\) under the clock sum is \(\mathsf E_i\).
Summing each finite grading sector in (8), and retaining its displayed
left ordering, proves
\[
 \boxed{\quad
 D(Y,\mathsf E)\,\mathsf T\mathscr W_m
       =Q^{c/2}\mathsf E^{H/2}N(Y,\mathsf E)\mathscr W_m .
 \quad}
 \tag{9}
\]
To justify the grading-one statement, first expand the graded
identity in \(h\). Its coefficients are rational in the grading
variable, with the polynomial clock dependence of [J]. The identity
therefore evaluates at grading one for generic \(Y\), and then
continues meromorphically coefficientwise. No infinite grading
sum is evaluated without that adapter.

Equation (9) is an actual first-order external equation before any
scalar elimination. For a supplied normal gauge
\(V_m=(Y-1)\mathscr W_m\), its exact row instead reads
\[
 (Y-1)D(Y,\mathsf E)\,\mathsf T V_m
       =(QY-1)Q^{c/2}\mathsf E^{H/2}N(Y,\mathsf E)V_m .
 \tag{10}
\]
Thus the normal gauge is not silently confused with the reduced
source. Both gauge factors are units near \(h=0,\ Y_0\ne1\).
The result below is stated for the reduced source (9).

## 3. A full-polydisk unit, not a contour-only inverse

Fix any \(Y_0\ne0,1\), write \(Y=Y_0+z\), and fix a spectral radius
\(R_*>0\). On the closed polydisk \(|\theta_i|\le R_*\), set
\[
                   X_i=e^{z\theta_i}.
 \tag{11}
\]
Let \(\ell_+\) and \(\ell_-\) be the numbers of signed crossings.
As \(z\to0\), uniformly on this whole polydisk,
\[
 D(Y_0+z,e^{z\theta}),\ N(Y_0+z,e^{z\theta})
    \longrightarrow
       d_0=(1-Y_0^{-1})^{\ell_+}(1-Y_0)^{\ell_-}\ne0.
 \tag{12}
\]
For an explicit local estimate, each form \(v\) appearing in (7)
satisfies
\[
 |e^{zv\cdot\theta}-1|
 \le |z|\,\|v\|_1R_*
                  e^{|z|\|v\|_1R_*}.
 \tag{13}
\]
Restrict first to \(|z|<|Y_0|/2\). The variation of \(Y\) and
\(Y^{-1}\), together with (13), bounds the variation of each factor
in (7) by \(C|z|\), for a finite constant depending only on this
word, \(Y_0\), and \(R_*\). Taking it smaller than half
\(\min(|1-Y_0|,|1-Y_0^{-1}|)\) makes every factor a unit.
The same holds on a slightly larger polydisk after shrinking \(z\).
Consequently
\[
 D,\ D^{-1},\ N,\ N^{-1},\ \mathcal R,\ \mathcal R^{-1}
 \tag{14}
\]
are holomorphic and uniformly bounded there. The Laurent monomial
in \(\mathcal R\) becomes \(e^{z(H/2)\cdot\theta}\), also a unit.
Empty crossing products cause no exception.

Here is the exact period-quotient implication of (14).
For the product torus \(\mathbb T_R=\{|\theta_i|=R\}\), define
\[
 \Pi_R(g)(\nu)=\frac1{(2\pi i)^d}
       \int_{\mathbb T_R}e^{\nu\cdot\theta}g(\theta)
                                          \,d\theta_1\cdots d\theta_d.
 \tag{15}
\]
One may start with continuous densities with their supremum norm.
The kernel is closed, since
\[
 |\Pi_R(g)(\nu)|\le R^d\|g\|_\infty e^{R\|\nu\|_1}.
 \tag{16}
\]
If \(\Pi_R(g)=0\), every polynomial moment of \(g\) vanishes,
by differentiating (15) at \(\nu=0\).
If \(a(\theta)\) is holomorphic on a neighborhood of the full
closed polydisk, the Taylor series of
\(a(\theta)e^{\nu\cdot\theta}\) converges normally on the torus.
Its integral against \(g\) is therefore zero. Thus
\[
                 a\,\ker\Pi_R\subseteq\ker\Pi_R.
 \tag{17}
\]
If \(a^{-1}\) is holomorphic on the same full polydisk, multiplication
by \(a\) is a two-sided inverse operation on the quotient, with
operator bounds \(\|a\|_\infty\) and \(\|a^{-1}\|_\infty\).
Nonvanishing only on the torus would not prove (17).

This quotient is available for the actual source, not merely for
formal symbols. Suppose on a parameter chart an entire clock family
obeys \(|f(\nu)|\le M e^{C\|\nu\|_1}\). Optimized Cauchy estimation
in each nonzero multiindex coordinate gives
\[
                    |\partial_\nu^\gamma f(0)|
                                  \le M(eC)^{|\gamma|},
 \tag{18}
\]
increasing \(C>0\) if needed. Indeed use radius \(\gamma_i/C\)
and \(\gamma_i!\le\gamma_i^{\gamma_i}\). Therefore the canonical
multivariate exterior density
\[
 g_f(\theta)=\sum_{\gamma\ge0}
              \partial_\nu^\gamma f(0)\,
                                \theta^{-\gamma-\mathbf1}
 \tag{19}
\]
converges normally for all \(|\theta_i|>eC\). For \(R>eC\),
\[
             \|g_f\|_{\mathbb T_R}\le M(R-eC)^{-d},
       \qquad \Pi_R(g_f)=f.
 \tag{20}
\]
The reconstruction follows termwise from (15). The same statements
are joint in holomorphic parameters with uniform \(M,C\).
In zero lattice dimension the sums and periods are scalar, and
the quotient argument is unnecessary.

The actual continued full-clock family of [A] has exactly the
uniform entire-clock bound required here on each smaller continued
compact chart. A fixed linear change of clocks in [A] only changes
\(C\). Choose \(R>eC\), and then shrink \(z\) for (12)--(14).
This order of choices retains a single radius for all clock values.

## 4. The actual Borel connection and its continuation

For the analytic source application use the original simple-node
charts supplied by [A], with \(Y_0=\alpha\), and write
\[
 h=z^2\epsilon,\qquad m=\nu/z,\qquad
 F(z,\eta,\nu)
       =z\,\mathcal B_h\mathscr W_{\nu/z}(\alpha+z,z^2\eta).
 \tag{21}
\]
Its holomorphic extension through \(z=0\) is part of that source
theorem. The algebraic row and the unit statement themselves did
not require a node or an Alexander hypothesis.

Let \(I f(\eta)=\int_0^\eta f(t)\,dt\), continued with the original
path history. The exact internal Borel actions are
\[
 \mathsf E_i\longmapsto e^{z\partial_{\nu_i}},
       \qquad Q^{c/2}\longmapsto e^{(c/2)z^2I}.
 \tag{22}
\]
The external shift keeps the original \(h,m\) fixed. On the formal
rescaled source it acts, with \(z_1=e^{z^2\epsilon}(\alpha+z)-\alpha\),
as
\[
 \frac z{z_1}
 F_{\rm formal}\left(z_1,\epsilon(z/z_1)^2,\nu z_1/z\right).
 \tag{23}
\]
In particular it is not an external translation with \(\nu\)
held fixed. Denote the Borel transform of this actual formal action
by \(\widehat{\mathsf T}F\).

Applying the Borel dictionary to (9) first in its initial germ gives
\[
 D(\alpha+z,e^{z\partial_\nu})\,\widehat{\mathsf T}F
  =e^{(c/2)z^2I}
          e^{z(H/2)\cdot\partial_\nu}
                      N(\alpha+z,e^{z\partial_\nu})F .
 \tag{24}
\]
There is a convergent analytic realization of its left division:
\[
 \boxed{\quad
 \widehat{\mathsf T}F
       = e^{(c/2)z^2I}\,
                  \mathcal R(\alpha+z,e^{z\partial_\nu})F .
 \quad}
 \tag{25}
\]
Precisely, apply multiplication by
\(\mathcal R(\alpha+z,e^{z\theta})\) to any period representative
of \(F\). Statements (14)--(20) make this bounded and independent
of the representative. Multiplication by \(D^{-1}\) proves (25)
on the quotient. All finite clock translations in (24) have exactly
their spectral multipliers \(e^{zv\cdot\theta}\).

For completeness the scalar exponential in (25) also converges
with every original primitive constant retained. On any fixed
finite continued \(\eta\)-path from zero, of length \(L\), a bounded
density \(g\) satisfies
\[
            \|I^n g\|\le \|g\|\,L^n/n!.
 \tag{26}
\]
This follows by the ordered path simplex, or by its single-integral
kernel \((\eta-\xi)^{n-1}/(n-1)!\).
Thus \(e^{a z^2 I}\) and \(e^{-a z^2I}\), \(a=c/2\), converge
normally and have norm at most
\[
                       e^{|a||z|^2 L}.
 \tag{27}
\]
They are inverse operators, by absolutely convergent multiplication
of their series. Integrating a path family in \(\ker\Pi_R\) stays
in that kernel, so they also act on the period quotient.
The multipliers in (14) are independent of \(\eta\) and commute
with these primitives. This proves a bounded two-sided connection
block, with its framing factor retained.

On the initial germ the right side of (25) has the formal series
of (23). One can verify uniqueness before invoking any analytic
continuation: each fixed normal-order source coefficient is polynomial
in the clocks. On polynomials of any bounded degree,
\(D(Y,e^{z\partial_\nu})\) is triangular by degree, with constant
diagonal \(D(Y,\mathbf1)\ne0\). It therefore has a unique polynomial
inverse. The spectral inverse above agrees with that inverse, since
its Taylor multiplier acts by the same finitely many derivatives
on each polynomial. The original cleared identity identifies every
coefficient. Thus (25) has not chosen another solution of (24).
On any of [A]'s
finite continued paths it provides its joint analytic continuation.
Use a common slightly smaller chart and fixed spectral torus along
that path. The original history from zero remains in (26), including
any loops. Nearby paths and overlapping charts agree by analytic
uniqueness of that germ and its retained history.

Nothing here asserts a bounded global operator
\(\exp(\widehat{\mathcal D})\) on arbitrary analytic functions.
The analytic continuation just proved is that of its actual
source action (23), supplied by the exact row (25).
Likewise the universal unit at a general \(Y_0\ne0,1\) does not
assert additional Borel domains: the actual domains used in this
application are those already proved in [A].

## 5. The source-derived classical longitude map

The rational map \(\mathcal R(Y,X)\) in (7) has
\[
                  \mathcal R(Y,\mathbf1)=1.
 \tag{28}
\]
Let \(U(k)=u\cdot k\) and \(N_{\rm tr}(k)=n\cdot k\) be the
integral forms in [T]:
\[
 U=\tfrac12\left[\sum_-(a+b'-n)-\sum_+(a+b'+n)\right],
                 \qquad N_{\rm tr}=\sum_{\rm all}n .
 \tag{29}
\]
Direct logarithmic differentiation of (7) gives
\[
 \left.\partial_{\log X}\log\mathcal R(Y,X)\right|_{X=\mathbf1}
          =u+\frac{Y}{Y-1}n=\beta(Y).
 \tag{30}
\]
For a positive crossing the contribution is
\((-a-b'+n)/2+n/(Y-1)\), which equals
\((-a-b'-n)/2+Yn/(Y-1)\).
For a negative crossing it is
\((a+b'-n)/2+Yn/(Y-1)\).
Their sum is exactly (30), including both signs.

At a simple Alexander root, [T] proves for the displacement vector
\(\mu\) of the full marked determinant
\[
                         \beta(\alpha)\cdot\mu=-\alpha.
 \tag{31}
\]
The exceptional character in [A] has spectral point
\(\theta_*=\mu/(2\sigma)\). Since (28) is constant in \(Y\),
the Taylor expansion of the actual map is
\[
 \log\mathcal R(\alpha+z,e^{z\theta_*})
                         =-\frac{\alpha}{2\sigma}z+O(z^2).
 \tag{32}
\]
This is a leading calibration at the actual exceptional character;
it does not evaluate the full finite-\(z\) source at one spectral point.

One may check its agreement with the simple partner of the actual
unmarked operator without assuming a classical character map.
Let a left-ordered analytic annihilator of the reduced source have
classical symbol \(P(Y,L)\), with
\[
 P(Y,1)=0,\quad
 A=\frac{\alpha^2}{2}P_{LL}(\alpha,1)\ne0,\quad
 B=\alpha P_{YL}(\alpha,1)\ne0.
 \tag{33}
\]
The simple-pole leading source is \(W_0=r/z\).
The order-\(h\) equation forces \(P_L(\alpha,1)=0\) and the
subprincipal value \(P_1(\alpha,1)=B\).
Its leading transport near the pole is
\(B(z\partial_z+1)\).
The order-\(h^2\) top second derivative coefficient is \(A\).
Since [F] bounds the pole of \(W_1\) by three, its cubic coefficient
\(c_1\) satisfies
\[
                      -2B c_1+2A r=0.
 \tag{34}
\]
On the other hand [A]'s unmarked exceptional profile is
\(r(1-4\sigma\eta)^{-1/2}\), whose linear coefficient is \(2r\sigma\).
Thus \(\sigma=A/(2B)\). Factoring \(P=(L-1)V\) at the transverse
node gives \(V_Y=P_{YL}\), \(V_L=P_{LL}/2\), and hence
\[
                   \ell'(\alpha)
                     =-\frac{2P_{YL}}{P_{LL}}
                     =-\frac{\alpha}{2\sigma}.
 \tag{35}
\]
Equation (32) therefore matches this source-selected first derivative.
A normal-state gauge \(Y-1\) is a nonzero local unit at \(\alpha\);
one first converts its actual operator to the reduced source before
this calculation. No scalar right factor has been substituted.

## 6. Scope and complete proof directs

The row (9), the rational longitude map, and the whole-polydisk
clock unit are valid for the original word in arbitrary lattice
dimension. Their local unit locus includes every \(Y_0\ne0,1\)
near \(X=\mathbf1\). Equation (25) applies them to the actual
continued full-clock family supplied by [A].

The conclusion is a bounded external quantum-meridian connection.
Internal shifts still carry their original boundary factors and
highest-vacuum constraints. No non-forced internal factor has been
canceled, and no auxiliary E/F module has been asserted closed.
The period quotient has not been replaced by an unprojected density.
The marked moving minor, finite-\(z\) multiplicative clock amplitude,
geometric character identification, and physical scalar lower bound
remain separate questions.

The complete proof directs, read in full with their used implications
checked, are:

| Label | Complete proof source | SHA256 |
|---|---|---|
| F | notes/research_classical_verma_rational_loops.md | f88f5fc4d1eb0f68f9270e581bd0e1bfd43c669cef989d9813f6000feb4e3659 |
| J | notes/research_highest_cut_joint_clock_equations.md | a2cf72961c37d6c96625bf8ff85ab94776ef328fcacc1f78c82bb9b9a7f16e2d |
| T | notes/research_classical_clock_torus_meridian_adapter.md | 7fbcc973a55eb6f38156b9efb0b18121bc248e5e0d60ed213728ad19f53fc515 |
| A | notes/research_full_clock_outer_borel_continuation.md | 8bec9e7934ba671d3dee836cb32dde3870113ed3e95348a83c39ac9e33b611f0 |

Only written mathematics, text reads and hash checks were used.
Frozen notes and public manuscripts are unchanged.
