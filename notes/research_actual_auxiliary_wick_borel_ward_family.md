# An actual auxiliary Borel family for the matrix Ward equations

Private written proof, 18 November 2026.

Creation and differentiation coupons give a controlled generating
family for the off-diagonal insertions of the original highest-cut
trace. Its quantum coefficients are Gevrey one on compact auxiliary
sets. At a simple Alexander pole, simultaneous square-root scaling
of the two coupons gives a jointly holomorphic initial Borel family,
with all original clocks retained.

The matrix Ward equations close formally on this generating family.
They use no inverse occupation coordinate and no inverse of the
highest-cut projector. The result does not assert convergence of
their infinite differential operators after Borel transformation,
or continuation of this new family to a moving minor.

## 1. The original word with explicit auxiliary coupons

Use the source of [H] in the natural coordinate \(Y=Qx^2\),
\(Q=e^h\), and write \(x_0^2=Y\). Its exact coefficientwise
operator expression is
\[
 \mathscr W_m(h,Y)=x_0^c
       \operatorname{Tr}\!\left[e^{D(h,Y,m)}\Gamma(B(Y))\right],
 \quad
 B=L_\beta(x_0)T_0,\quad T_0=\operatorname{diag}(0,1,\ldots,1).
 \tag{1}
\]
All clocks use the same fixed stage realization and linear
specialization as in [H]. This realization is kept when a coupon
changes the matching constraints. The original pivots and framing
are in \(D\), with the scalar \(x_0^c\) outside.

Let \(Z_1,\ldots,Z_b\) be the polynomial variables, and let
\(\partial_i=\partial/\partial Z_i\). Introduce independent
complex auxiliary vectors \(s,t\in\mathbb C^b\). Define
\[
 \mathcal Z_m(h,Y;s,t;\tau)
   =x_0^c\operatorname{Tr}
      \left[e^{s\cdot Z}e^D e^{t\cdot\partial}
                                      \Gamma(\tau B)\right].
 \tag{2}
\]
First take (2) degree by degree in the grading \(\tau\), then
expand in \(h\). At any fixed grading degree \(T\), only equal
total creation and annihilation degrees contribute to the trace,
and each is at most \(T\). Thus that sector is a finite coupon
contraction. At \(s=t=0\) it is exactly the original source.

This is also a literal coupon placement in the original word.
Writing \(L=L_\beta(x_0)\) and \(\mathcal U_h=e^D\Gamma(L)\)
for its original relative-word adapter, one has
\[
 e^{s\cdot Z}e^D e^{t\cdot\partial}\Gamma(\tau L T_0)
   =e^{s\cdot Z}\mathcal U_h
               e^{(L^Tt)\cdot\partial}\Gamma(\tau T_0).
 \tag{3}
\]
Indeed \(\Gamma(L)^{-1}\partial_i\Gamma(L)
=\sum_jL_{ij}\partial_j\).
Only the classical invertible \(L\) is used in this rewriting;
\(T_0\) is never inverted. The same highest cut and trace remain.
At nonzero probe degree these are explicitly augmented source
contractions with affine matching defects, not scalar clock
derivatives disguised as diagonal insertions.

Let \(f(h,Z,P,m)\) be the ordinary normal symbol of \(e^D\).
By [H] it has
\[
 f=e^V,\qquad V=\sum_{j\ge1}h^jV_j,\qquad
 \deg_P V_j+\deg_m V_j\le j+1,\quad \deg_mV_j\le j,
 \tag{4}
\]
monomialwise, with equal \(Z\)- and \(P\)-degrees.
The normal symbol in (2) is exactly
\(e^{s\cdot Z+t\cdot P}f\): multiplication on the left by
\(e^{s\cdot Z}\) and on the right by \(e^{t\cdot\partial}\)
creates no normal-order contraction.

For \([h^j]f=f_j\), a monomial with mark degree \(a\) and equal
\(Z,P\)-degree \(d\) satisfies
\[
                         a\le j,\qquad d+a\le2j .
 \tag{5}
\]
To check this, expand the ordinary exponential of (4). A product
of \(v\le j\) positive-order vertices has combined degree at most
\(j+v\le2j\). All coefficients in (4)--(5) are holomorphic on
the local meridian chart \(Y\ne0,1\).

## 2. Exact Wick expression and grading continuation

Put
\[
 K_\tau=I-\tau B,\qquad D_\tau=\det K_\tau,\qquad
                    C_\tau=\tau B(I-\tau B)^{-1}.
 \tag{6}
\]
The exact trace rule in [H] gives
\[
 \mathcal Z_m
       =\frac{x_0^c}{D_\tau}\,
           \mathbb E_{C_\tau}
                      \left[e^{s\cdot Z+t\cdot P}f\right].
 \tag{7}
\]
Here \(\mathbb E_C\) pairs \(P_i\) with \(Z_j\) by \(C_{ij}\).
The identity first holds in formal grading, so it also defines
the original coefficientwise rational continuation.

For a polynomial \(g\), the generating-exponential identity proves
\[
 \mathbb E_C[e^{s\cdot Z+t\cdot P}g(Z,P)]
   =e^{t^TCs}\,
       \mathbb E_C[g(Z+C^Tt,P+Cs)].
 \tag{8}
\]
This is an algebraic Wick identity; it assumes no positive measure.
By (5), at order \(h^j\) the second factor in (8) is a polynomial
in \(s,t,m\), with total auxiliary degree at most \(4j\).
It uses at most \(4j\) covariance factors.

Write \(m_0=b-1\); \(B=L_\beta T_0\) has rank at most \(m_0\).
Both \(D_\tau\) and each numerator entry of
\(C_\tau=(K_\tau^{-1}-I)\) have grading degree at most \(m_0\).
Consequently
\[
 e^{-t^TC_\tau s}[h^j]\mathcal Z_m
        =\frac{P_j(Y,\tau;s,t,m)}{D_\tau^{\,4j+1}},
 \qquad \deg_\tau P_j\le4jm_0 .
 \tag{9}
\]
The coefficients of \(P_j\) are holomorphic on the chosen meridian
chart. They are polynomial in the auxiliary vectors and in \(m\).
To verify the degree, a term with \(q\le4j\) covariance factors
has numerator degree at most \(qm_0\); multiplication by
\(D_\tau^{4j-q}\) gives the displayed common degree bound.
The scalar \(x_0^c\) is retained.

Define the grading-one coefficient by evaluating (9) at \(\tau=1\)
and restoring \(e^{t^TC_1s}\). No analytic infinite trace at
generic nonzero \(h\) is assumed. Write this actual coefficientwise
completion as
\[
                   \mathcal Z_m(h,Y;s,t)=\sum_{j\ge0}h^jZ_{j,m}(Y;s,t).
 \tag{10}
\]
It is entire in \(s,t\) at each order, and polynomial in \(m\).
The coefficients can have an exponential singularity at an
Alexander pole when the unscaled probes are nonzero; that
singularity has not been ignored.

## 3. A finite-sector Gevrey bound with the original cut

Fix compact meridian charts away from \(Y=0,1\), and compact
auxiliary sets. On the degree-\(T\) sector use the same disk
\[
                            |h|\le\rho/(T+1)
 \tag{11}
\]
as in [G]. Its signed crossing estimates, original pivot, and
framing bound are uniform on this disk. The finite relative
classical substitutions in (1) add at most a fixed geometric
factor \(C^T\).
Each original stage clock \(e^{hm\cdot k}\) costs at most
\(e^{C_1\|m\|_1}\), since the fixed word bounds every relevant
linear index form by a constant times \(T\).

The annihilation coupon obeys, on an input monomial of degree \(T\),
\[
            \|e^{t\cdot\partial}Z^\gamma\|_1
                 =\prod_i(1+|t_i|)^{\gamma_i}
                 \le(1+\|t\|_\infty)^T .
 \tag{12}
\]
The creation coupon has coefficient sum at most
\(e^{\|s\|_1}\); restricting to the degree needed for the trace
only decreases this bound. All intermediate degrees after the
annihilation coupon are at most \(T\).
The factor \(\Gamma(B)\) also costs at most a fixed geometric
factor per degree. Bounding the number of traced basis vectors by
\(\binom{T+b-1}{b-1}\), without replacing the projector, gives
\[
 |[\tau^T]\mathcal Z_m(h,Y;s,t;\tau)|
    \le C_2 e^{C_1\|m\|_1}
               \binom{T+b-1}{b-1}C_3^T
 \quad\text{on (11)}.
 \tag{13}
\]
The constants are uniform on the chosen compact auxiliary sets.

Cauchy estimation in \(h\) adds
\((T+1)^j\rho^{-j}\).
Choose a sufficiently small grading radius and use
\((T+1)^j\le j!a^{-j}e^{a(T+1)}\), with a fixed \(a>0\),
to sum (13). It follows that on that grading circle
\[
        |[h^j]\mathcal Z_m|
                   \le C_4 A_0^j j!\,e^{C_1\|m\|_1}.
 \tag{14}
\]
On the small grading circle \(C_\tau\) is uniformly bounded.
Multiplication by \(e^{-t^TC_\tau s}\) preserves (14) up to
a compact-set constant.

Now let the meridian compact avoid the Alexander divisor as well.
Multiplication by \(D_\tau^{4j+1}\), polynomial Cauchy propagation
of the degree-\(4jm_0\) numerator in (9), and division by the
nonzero \(D_1^{4j+1}\) give
\[
 \boxed{\quad
 \sup |Z_{j,m}(Y;s,t)|
             \le C_5 A_1^j j!\,e^{C_1\|m\|_1}.
 \quad}
 \tag{15}
\]
Restoring \(e^{t^TC_1s}\) costs only a compact-set constant.
All propagation losses are exponential in \(j\), as in [G];
there is only one factorial. This proves a joint initial Borel
germ on compact meridian and auxiliary sets. Its radius can depend
on the auxiliary compact, but is independent of \(m\).

## 4. The auxiliary Borel seed through a simple pole

Let \(\alpha\ne0,1\) be a simple Alexander zero and \(z=Y-\alpha\).
The original covariance and scalar have
\[
 C_1(z)=\frac{uv^T}{z}+G(z),\qquad
       \frac{x_0^c}{D_1(z)}=\frac{r(z)}z,\qquad r(0)=r\ne0 .
 \tag{16}
\]
The fixed vectors \(u,v\) have nonzero rank-one product. Their
individual coordinates may vanish. No normalization \(v^Tu=1\)
is required.

Scale both probes as \(s=\sqrt z\,a,\ t=\sqrt z\,b\).
The source has equal total degrees in \(s\) and \(t\), by the
degree-preserving trace, so this expression is independent of the
choice of \(\sqrt z\). Its classical exponential is
\[
                  e^{t^TC_1s}=e^{z b^TC_1(z)a},
 \tag{17}
\]
which is holomorphic through \(z=0\).

Consider a monomial of \(f_j\) with mark degree \(q\) and
equal symbol degree \(d\le2j-q\). In (8), let \(c_0\) of its
pairs be contracted and leave the other \(2d-2c_0\) legs as
covariance means. Each contraction has pole at most one in \(z\);
each mean after the probe scaling has pole at most one in
\(\sqrt z\). The total pole is therefore at most \(d\).
The exponent is integral, since the number of remaining legs
is even. Including the scalar pole in (16), this proves
\[
 z^{\,2j+1-|\gamma|}
 [m^\gamma]Z_{j,m}(\alpha+z;\sqrt z\,a,\sqrt z\,b)
               \quad\text{is holomorphic through }z=0.
 \tag{18}
\]
Its dependence on \(a,b\) is entire. This argument uses the exact
Wick expansion, including all hard contractions.

Choose a fixed small circle \(|z|=r_0\) avoiding every other pole.
Apply (15) there with the scaled probes in a prescribed compact.
Optimized Cauchy extraction in each clock coordinate gives
\[
 \left|[m^\gamma]Z_{j,m}\right|
       \le C_6 A_2^j j!\,\frac{c^{|\gamma|}}{\gamma!},
                         \qquad |\gamma|\le j.
 \tag{19}
\]
For instance choose radius \(\gamma_i/C_1\) for a positive
coordinate and use \(\gamma_i!\le\gamma_i^{\gamma_i}\).
The constant \(c\) can be taken independent of \(j,\gamma\).
By the maximum principle applied to (18), the corresponding
holomorphic expression is bounded on the disk by
\[
       C_6 r_0(r_0^2A_2)^j j!\,
                         \frac{(c/r_0)^{|\gamma|}}{\gamma!}.
 \tag{20}
\]
Consequently
\[
 \mathcal F(z,\eta,\nu;a,b)
    :=\sum_{j\ge0}z^{2j+1}
       Z_{j,\nu/z}(\alpha+z;\sqrt z\,a,\sqrt z\,b)
                                      \frac{\eta^j}{j!}
 \tag{21}
\]
has a jointly holomorphic extension through \(z=0,\eta=0\).
For \(z\ne0\), this is exactly \(z\) times the Borel transform
of (10), evaluated at Borel variable \(\xi=z^2\eta\),
clocks \(m=\nu/z\), and the displayed probes. The grading
has already been set to one in (10).
For each compact auxiliary set there is one positive product
radius valid for all \(\nu\in\mathbb C^d\). Explicitly (20) sums to
\[
 |\mathcal F|
   \le \frac{C_6r_0}{1-r_0^2A_2|\eta|}
                    \exp\!\left((c/r_0)\|\nu\|_1\right).
 \tag{22}
\]
At \(a=b=0\) this is the original full-clock Borel seed.
At \(\eta=0,z=0\) it exposes the full covariance residue:
\[
                  \mathcal F(0,0,\nu;a,b)
                       =r\,e^{(b^Tu)(v^Ta)} .
 \tag{23}
\]
Thus the auxiliary seed retains the kernel-pair directions without
requiring nonzero occupation components of \(\mu\).

## 5. Closed formal matrix Ward equations

Set \(\tau=1\), \(K=I-B\), \(C=B(I-B)^{-1}\), and interpret
all statements first coefficientwise in \(h\), away from the
Alexander divisor. Wick integration by parts gives
\[
 \mathbb E_C[Z_jg]=\sum_iC_{ij}\mathbb E_C[\partial_{P_i}g],
 \qquad
 \mathbb E_C[P_i g]=\sum_jC_{ij}\mathbb E_C[\partial_{Z_j}g].
 \tag{24}
\]
Applying (24) to \(g=e^{s\cdot Z+t\cdot P}e^V\) proves the exact
closed auxiliary system
\[
\begin{split}
 K^T\partial_s\mathcal Z_m
   &=B^T\left[t+V_P(h,Y,\partial_s,\partial_t,m)\right]\mathcal Z_m,\\
 K\partial_t\mathcal Z_m
   &=B\left[s+V_Z(h,Y,\partial_s,\partial_t,m)\right]\mathcal Z_m.
\end{split}
 \tag{25}
\]
The polynomial \(V_{P_i}\) or \(V_{Z_j}\) at each normal order
acts by \(Z\mapsto\partial_s,\ P\mapsto\partial_t\), on the
source to its right. Its meridian and clock coefficients are
not differentiated. Equation (25) is coefficientwise finite,
since \(V\) starts at positive \(h\)-order.
It retains all auxiliary moments in one generating family.

In particular put
\[
 M_{ij}=\frac{x_0^c}{\det K}\mathbb E_C[P_i Z_jf],
 \qquad
 N_{ab}=\frac{x_0^c}{\det K}
                         \mathbb E_C[\partial_{Z_a}\partial_{P_b}f].
 \tag{26}
\]
Twice applying (24) gives
\[
 M=C\,\mathscr W_m+CNC,\qquad
                  \boxed{K M K=B K\,\mathscr W_m+B N B.}
 \tag{27}
\]
Here \(M_{ij}=\partial_{s_j}\partial_{t_i}\mathcal Z_m|_{s=t=0}\).
Moreover
\(\partial_{Z_a}\partial_{P_b}f
=(V_{Z_aP_b}+V_{Z_a}V_{P_b})f\), so \(N=O(h)\).
All these identities are identities of the actual source
coefficients; they require no inverse of \(B\) or \(T_0\).

The equations do not identify off-diagonal \(M_{ij}\) with
diagonal clock derivatives. They use the explicit coupons (2)--(3)
to retain those affine-defect sources. At \(h=0\) the usual
classical kernel-pair block is visible, but this alone is not an
analytic inverse for the quantum system.

Specifically, (4) bounds differential degree, not the sizes of
all coefficients of \(V_j\). Equation (25) is not yet a normally
convergent differential-Volterra equation on the continued Borel
family. Proving that operator estimate, and transporting this
auxiliary family to the moving marked minor, remain additional
steps. The actual initial germ (21) does not supply them merely
by formal differentiation.

## 6. Complete proof directs

| Label | Complete proof source | SHA256 |
|---|---|---|
| H | notes/research_actual_hard_wick_soft_reduction.md | b528230f79ceea7a9a812ac600bcb55e9ba7819a465218761e0f81fdd317002b |
| G | notes/research_classical_verma_borel_pole_profile.md | 6ba957d7a521524f370cb3bdd90ab30338bff8c13960ae6ca1825d08260c77d2 |

H supplies the actual marked word, ordinary normal-symbol filtration,
highest-cut Wick functional and rank-one covariance residue.
G supplies the literal finite-sector source estimate and its
grading-continuation method. Only its unconditional Gevrey part
is used; no transverse scalar node condition is needed here.
The coupon placement, auxiliary degree and pole budgets, joint
Borel seed, and closed formal Ward equations are proved above.

Only written mathematics, source reads and hash checks were used.
Frozen notes and public manuscripts are unchanged.
