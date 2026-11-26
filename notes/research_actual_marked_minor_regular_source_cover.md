# The full marked minor on the regular cover of the actual source

Private written proof, 18 November 2026.

The literal finite word determines an analytic stationary cover on
which all its quantum amplitude coefficients continue with uniform
Gevrey bounds on compact sets. This constructs continuation of the
full marked odd minor, rather than only its leading coefficient or
an unmarked scalar transport equation. The construction keeps the
original highest cut, pivot, framing, and all independent marks.

The domain is the regular cover of the actual finite stationary
construction. On the attached nonabelian component with a fold seed,
an algebraic representation slice supplies generic lifts to this
cover, with a discrete excluded set on its logarithmic cover.
An arbitrary prescribed arc need not avoid that set. Nor does the
construction continue the complete original primitive-prefix sum
or its relative cap.

## 1. The initial actual germ and the cover to be constructed

Fix the finite highest-cut source of [G], with
\[
 Q=e^h,\qquad Y=\alpha+z,\qquad \alpha\ne0,1,\qquad
 \Delta_K'(\alpha)\ne0.
 \tag{1}
\]
No scalar-operator node hypothesis is needed for the coefficient
construction or for the critical-divisor identity below. Keep the
same rank-one splitting
\[
 C(Y)=B(I-B)^{-1}=\frac{uv^T}{Y-\alpha}+G(Y),\qquad
 r(Y)=\frac{Y-\alpha}{\Delta_K(Y)}.
 \tag{2}
\]
The functions \(G\) and \(r\) initially have their holomorphic
values at \(\alpha\); \(C\) retains its displayed rank-one pole.
The constant residue factors \(u,v\) and the original matrix
\(B=L_\beta T_0\) are never replaced.

The initial source phase and amplitude of [G] are
\[
 f(Y,x)=(Y-\alpha)x-\Psi_0(Y,x,0),\qquad
 a(h,Y,x,m)=\sum_{j\ge0}h^j a_j(Y,x,m),
 \tag{3}
\]
where \(\Psi_0(Y,x,0)=O(x^2)\),
\[
 \|a_j\|\le MC^j j!,\qquad
 a_0=\exp\{A_0(Y,x)+m\cdot\Theta(Y,x)\}\ne0.
 \tag{4}
\]
Here \(x\) is the soft variable, independent marks are denoted
\(\mathbf t\), and the original clocks are \(\mathbf t=hm\).
All matching-lattice specializations use the original fixed linear
map. The coefficient disks are common to all \(j\), and (4) is
uniform on each prescribed compact set of clocks.

We define a regular source cover by the literal operations, not by
assuming continuation of (3)--(4). Its charts record:

* the branches of \(Y^{1/2}\), the literal endpoint logarithms and
  their principal integrals;
* solutions of the finitely many Poisson stationary equations and
  normal-product stationary equations used for the original word;
* the original hard stationary solution using (2), with independent
  marks retained;
* the logarithms and determinant square roots continued from the
  initial normalization.

Retain only points where the literal coefficient functions are
holomorphic, \(G\) is holomorphic, \(r\) is nonzero, and every
stationary Jacobian used in this finite construction is invertible.
Take the component of the analytic continuation of these charts
containing the initial germ. All lifts, including repeated visits
to the same projected point, are retained. Section 2 makes the
literal coefficient domain explicit; Section 3 constructs the
quantum coefficients on this cover.

**Theorem.** On every compact zero-mark lift in this regular source
cover, with smaller regular mark thickenings, the
hard logarithm coefficients and source amplitudes satisfy
\[
 \|\Psi_a\|\le MC^a a!,\qquad \|a_j\|\le M'C'^j j!.
 \tag{5}
\]
The constants depend on the compact lift and clock compact, and not
on the quantum order.

Let a compact path in its zero-mark critical locus start at an
actual fold minor of [G], and suppose \(f_{xx}\ne0\) along it and
the meridian is a local parameter on that path. The full marked
odd minor has analytic continuation along the path, with a common
positive transverse radius after finite shrinking. Its leading
coefficient is nonzero and its marked/unmarked ratio is
\(\exp(m\cdot\Theta_g)\). All coefficients, not just that ratio,
are the continuations of the initial actual minor.

The theorem is a construction on a specified maximal regular
source cover. It does not identify that cover with the whole
regular part of an algebraic character component.

## 2. Continuing the literal quantum coefficients

The scalar functions in the actual factorial and color products are
\[
 F_0(s)=\log\frac{e^s-1}{s},\qquad
 F_\pm(Y,s)=\log\frac{1-Y^{\pm1}e^s}{1-Y^{\pm1}}.
 \tag{6}
\]
Their initial logarithms vanish at \(s=0\). Continue these germs,
and their integrals, along their actual endpoint lifts. The first
function is regular at zero and is continued away from the nonzero
points \(2\pi i\mathbb Z\); the latter two are continued away from
\(1-Y^{\pm1}e^s=0\). Also exclude \(Y=0,1\). This describes
logarithm covers; it does not reset logarithms after a loop.

For any of these functions \(F\), every fixed offset \(c\), and
the scaled endpoint \(s=hL\), the exact formal regrouping is
\[
 \sum_{r=0}^{L-1}F(h(r+c))
 =\frac1h\int_0^s F(t)\,dt+
 \sum_{a\ge1}h^{a-1}\frac{B_a(c)}{a!}
       \{F^{(a-1)}(s)-F^{(a-1)}(0)\}.
 \tag{7}
\]
For \(F_\pm\) the parameter \(Y\) is held fixed in each derivative.
To verify (7), expand \(F(s)=\sum_{j\ge0}F_js^j\) and use
\[
 \sum_{r=0}^{L-1}(r+c)^j
  =\frac{B_{j+1}(L+c)-B_{j+1}(c)}{j+1}.
 \tag{8}
\]
The coefficient with \(a\) is
\(B_a(c)j!/[a!(j+1-a)!]\) for \(a\le j+1\), exactly the
derivative in (7); its constant-endpoint term cancels when required.
Thus (7) is an identity of the original formal coefficients, not
an asymptotic replacement of the finite product.

On a compact continued endpoint chart, take a common positive
Cauchy buffer \(\delta\). The finite offset set satisfies
\(|B_a(c)|/a!\le C_0^{a+1}\), and Cauchy estimation gives
\[
 \sup |F^{(a-1)}|\le M\delta^{-(a-1)}(a-1)!.
 \tag{9}
\]
Equation (7) therefore continues every literal defect potential
\(V_a\) and bounds it by \(MC^a a!\), uniformly on smaller
neighborhoods of that compact. The endpoint at zero is retained
with its initial value; continuation of the other endpoint does
not replace it by another branch at zero.

The actual signed products are differences of finitely many such
intervals, at the fixed linear endpoints in [P, (15)--(16)].
The Cartan monomials and the fixed-\(Y\) drift are polynomial or
analytic corrections and have the same bound. Hence (7)--(9)
continue all lower quantum defects as well as the principal
potentials. Vanishing occupation coordinates cause no new pole:
the removable value of \(F_0\) at zero was retained.

## 3. Finite stationary construction and uniform graph bounds

For each local kernel the continued Poisson solution is
\[
 s_i=U_i\exp(\partial_iV_0(s)).
 \tag{10}
\]
Its Jacobian is invertible exactly where
\(I-\operatorname{diag}(s)V_0''(s)\) is invertible. There is no
inverse \(s_i\). Formula [D, (21)] translates to this stationary
solution; its centered Poisson functional is exactly the cross-Wick
functional with covariance
\[
 K_\times=\begin{pmatrix}0&I\\I&0\end{pmatrix}
 \tag{11}
\]
and principal potential
\[
 V_0(s+X)-V_0(s)-\nabla V_0(s)\cdot X
                 +\sum_i s_i(e^{\Xi_i}-1-\Xi_i).
 \tag{12}
\]
This is an identity first at the original germ. Every coefficient
after stationary translation is an analytic expression in the
continued data, so it continues that identity on the same lift.

For a normal product, or a hard contraction, the corresponding
stationary equation is
\[
 u=q+K\nabla P_0(u).
 \tag{13}
\]
The covariance \(K\) can be singular. After translation, absorb
the quadratic part with
\[
 J=\det(I-KP_0''(u))^{-1/2},\qquad
 K_{\rm eff}=(I-KP_0''(u))^{-1}K.
 \tag{14}
\]
The determinant branch and its logarithm are the continued
original ones. No covariance inverse is required. Equations
(10), (13), and their unit conditions are precisely the finite
stationary charts in Section 1. In a star product, \(K\) is the
fixed cross covariance; in the hard contraction it is the block
covariance of the original \(G(Y)\).

We check that compact continuation preserves the all-order bound.
On a buffered compact regular chart, all stationary values,
derivatives of the principal potentials, and entries of
\(K_{\rm eff}\) are uniformly bounded. The continued literal
potentials have the bounds of Section 2. The residual principal
vertices after (14) have field degree at least three. A quantum
vertex of defect \(a\ge1\) and positive field degree \(q\) has
coefficient bounded by \(C^{a+q}a!\). Constants are split out
before taking the connected logarithm.

For a connected residual vacuum graph with \(v\) vertices and
\(e\) pairs, its defect is
\[
 d=\sum a_i+e-v+1,\quad g=e-v+1\ge0,\quad
 \sum_i(q_i+2a_i-2)=2d-2.
 \tag{15}
\]
Thus \(v\le2d-2,\ e\le3d-3,\ \sum a_i\le d\).
The pairing count with the exponential's \(1/v!\) obeys
\[
 \frac{(2e)!}{2^e e!v!}\le4^e g!,\qquad
                    g!\prod_i a_i!\le d!.
 \tag{16}
\]
Valence and defect compositions, field colors, and bounded
covariance entries cost only \(C^d\), as in [D, Section 3].
Every coefficient is a finite graph sum after quadratic
resummation. Therefore it is holomorphic on the regular cover
and bounded by \(MC^d d!\) on the chosen compact chart.
The separately retained constants and \(\log J\) obey the same
estimate.

This argument is applied in the original finite order through
the local Poisson kernels, normal products, independent marks,
pivot, framing, and regular hard contraction. Finite induction
gives a common coefficient neighborhood at every regular point.
A compact lifted set has a finite cover by such neighborhoods;
take their maximum constants. This proves the first bound in (5).
It also proves coefficientwise agreement on overlaps: the finite
graph expressions continue the original germs and use their
same lifted stationary solutions and determinant branches.

Independent marks remain near zero during this argument. Their
quadratic terms and all stationary equations are analytic there;
the unit conditions persist on sufficiently small mark disks.
After \(\mathbf t=hm\), mark Cauchy extraction and exponentiation
give the second bound in (5), by exactly the finite compositions
and factorial inequality in [G, Section 3]. On each clock compact
the disks are common to every quantum order. The leading term
continues as \(a_0=e^{A_0+m\Theta}\), and is a unit.

Balancedness is an analytic identity of the original coefficients
and continues with them. Near a critical path with \(x=AB_s\ne0\),
one may choose either nonzero soft field as a local slice for
\((A,B_s)\mapsto(\lambda A,\lambda^{-1}B_s)\). The coefficients
then remain analytic functions of \(x\). Near the initial zero
point the balanced power-series argument of [D, (28a)] applies.
If both soft fields vanish in a regular chart, use their balanced
analytic expansion there instead. This defines the same continued
functions \(\Psi_a(Y,x,\mathbf t)\).

## 4. The short-bank formula for the actual marked odd minor

On the initial chart [G] proves
\[
 \mathfrak b_m(Y,x)=r(Y)\left[
 \frac{a_0(Y,x,m)}{f_x(Y,x)}
 +\sum_{j\ge1}\frac1{(j-1)!}
       \int_0^x(f(Y,x)-f(Y,t))^{j-1}a_j(Y,t,m)\,dt\right].
 \tag{17}
\]
This is the actual Borel source pulled back to its phase surface.
Let \(x_+(Y,\rho)\) and \(x_-(Y,\rho)\) be the two inverse points
near a regular critical point \(x_g(Y)\), where
\[
 f(Y,x_\pm)=\xi_g(Y)+\rho,\qquad \xi_g=f(Y,x_g).
 \tag{18}
\]
Continue the sheet ordering from the initial actual minor.
Subtract (17) at these two points. Every original prefix cancels
because its integrand has the same terminal value
\(\xi=\xi_g+\rho\). Thus twice the odd minor is exactly
\[
\begin{split}
 2b_{o,m}={}&r(Y)\left[
       \frac{a_0(Y,x_+,m)}{f_x(Y,x_+)}
      -\frac{a_0(Y,x_-,m)}{f_x(Y,x_-)}\right]\\
 &+r(Y)\sum_{j\ge1}\frac1{(j-1)!}
       \int_{x_-}^{x_+}
       \bigl(\xi_g+\rho-f(Y,t)\bigr)^{j-1}a_j(Y,t,m)\,dt.
\end{split}
 \tag{19}
\]
The short path in (19) lies in the continued local coefficient
chart. This identity does not replace either full primitive
in (17) by one based at the critical point.

Take a local analytic Morse coordinate \(v\) with
\[
 f(Y,x(Y,v))=\xi_g(Y)+v^2,\qquad
                  x_\pm=x(Y,\pm\sqrt\rho).
 \tag{20}
\]
The graph bounds give
\(\|a_j(Y,x(Y,v),m)x_v(Y,v)\|\le MC^j j!\)
on a common buffered \(v\)-disk. For \(|v|\le\varepsilon\),
the \(j\)-th integral in (19) is bounded by
\[
           2\varepsilon Mj C^j(2\varepsilon^2)^{j-1}.
 \tag{21}
\]
Hence the sum converges normally if \(2C\varepsilon^2<1\).
It is odd and holomorphic in \(v\). The first line of (19)
has only its simple \(v^{-1}\) pole. Consequently
\[
 b_{o,m}(Y,\rho)=\rho^{-1/2}A_m(Y,\rho),\qquad
 A_m(Y,0)=\frac{r(Y)}2
            a_0(Y,x_g(Y),m)x_v(Y,0)\ne0.
 \tag{22}
\]
The leading marked/unmarked ratio is \(e^{m\Theta_g(Y)}\).

Cover the compact critical path by finitely many buffered
stationary and Morse charts. Subdivide it so consecutive centers
belong to a common smaller chart. On each overlap the continued
phase and every amplitude coefficient agree by Section 3.
The short paths can be chosen homotopic inside that common
coefficient chart; their integrands are holomorphic there.
Thus (19) agrees coefficientwise and, by normal convergence,
as a joint analytic function. This glues the full minor.
The finite minimum of the transverse radii is positive.
The sheet ordering, action value, and determinant normalization
are carried from the initial germ and never independently reset.

This proves continuation of the actual marked minor germ, even
when no scalar annihilator for the marked family has been chosen.
It does not assert continuation of both full source branches:
their common, canceled prefix is additional data.

## 5. The external equation on the general critical divisor

There is an exact consequence already on the initial phase surface,
without a Morse or finite critical multiplicity assumption. Use
the original finite Laurent polynomials \(D,N\) and matching form
\(H\) of [H, (4)]. Its actual external row is
\[
 D(Y,\mathsf E)\mathsf T\mathscr W_m
    =e^{ch/2}\mathsf E^{H/2}N(Y,\mathsf E)\mathscr W_m,
 \quad \mathsf T:Y\mapsto e^hY,\quad
       \mathsf E_i:m\mapsto m+e_i.
 \tag{23}
\]
The common-phase rewriting in [H, Section 2] uses
\[
 a^{(s)}=\frac{r(e^{sh}Y)}{r(Y)}
    \exp\!\left[-\frac{f(e^{sh}Y,x)-f(Y,x)}h\right]
                          a(h,e^{sh}Y,x,m).
 \tag{24}
\]
Cauchy estimation on a common \(h\)-disk proves that its
coefficients are Gevrey with the same type of bound (5), and
\[
                 a_0^{(s)}=e^{-sYf_Y}a_0 .
 \tag{25}
\]
That proof uses no critical-point nondegeneracy. Apply [G]'s
coefficient reconstruction with this amplitude. Its pullback is
\(r(a_0^{(s)}/f_x+\text{holomorphic})\).
Every positive canonical primitive is holomorphic on the phase
surface, since \(g_j\,d\xi=a_j\,dx\). Its original endpoint
constants are included. In particular the nonconstant terms
of the framing factor in (23) contribute no pole.

The finitely many clock translates have common reconstruction
disks. Pull back the exact row, multiply by \(f_x\), and restrict
to its critical divisor. Its unit numerator gives
\[
 \boxed{\quad
 e^{-Yf_Y}D(Y,e^{\Theta(Y,x)})
       =e^{(H/2)\cdot\Theta(Y,x)}N(Y,e^{\Theta(Y,x)})
                 \quad\text{on }f_x=0 .
 \quad}
 \tag{26}
\]
Near the initial point \(D\) is a unit, since
\(D(\alpha,\mathbf1)
 =(1-\alpha^{-1})^{\ell_+}(1-\alpha)^{\ell_-}\ne0\).
Thus the source peripheral value there is
\[
                \mathcal R(Y,e^\Theta)=e^{-Yf_Y}.
 \tag{27}
\]
The cleared identity (26) continues on the regular source cover
by analytic uniqueness. The quotient form holds wherever its
continued \(D\) is nonzero. On a regular critical graph,
\(S_g(Y)=-f(Y,x_g(Y))\) gives
\(YS_g'=-Yf_Y\), recovering [H].

If the critical divisor is vertical \(Y=\alpha\), then
\(\Psi_0(\alpha,x,0)\equiv0\) by [G]. Jointly
\(\Psi_0(Y,x,0)=O(x^2)\), so on that divisor
\[
              -Yf_Y=-\alpha x+O(x^2).
 \tag{28}
\]
The actual peripheral value in (27) is therefore nonconstant
there. This statement identifies the source rational peripheral
expression; preferred topological longitude labeling on a
general vertical branch requires the separate representation
and flag comparison, not a two-branch derivative formula.

## 6. Generic lifts from the attached algebraic component

For this section retain a fold seed and the irreducible attached
representation component supplied by [L]. Begin at a sufficiently
small nonzero seed, so the meridian eigenvalues are distinct and
all the stationary determinants above are units. We construct
lifts from this component, rather than assume them.

Place the ordered cut eigenlines at the coordinate axes, as in
[L, Section 6]. Diagonal conjugation is the only remaining
effective gauge. Choose an input field \(f_j\ne0\) at the seed
and set it equal to its nonzero seed value by that gauge.
The Gauss formulas express \(f_j\) rationally in the framed
representation matrices. After clearing their unit denominators,
this is an algebraic slice. Near the seed its character quotient
is the smooth one-dimensional germ proved in [L]. Take the
irreducible algebraic curve of that slice containing this germ,
and its normalization. Its peripheral image is the same attached
A-curve. This construction need not give a chart for every
representation of that component.

On this normalized curve the framed representation matrices and
\(x_0=-M\) are meromorphic. Every stage is obtained by the original
finite Hurwitz word. Its Gauss factors are rational wherever the
prescribed principal minors are nonzero. Thus all stage \(K,e,f\)
are meromorphic functions on a nonempty open subset of the curve.
Remove their coefficient poles, \(Y=0,1\), and the other
Alexander zeros in (2). The functions excluded here are
nonzero at the chosen seed.

Pass to a connected path cover carrying the logarithms continued
from that seed. In each strand set
\[
 t=\log(x_0/K),\qquad Z=f,\qquad
 P=\frac{e}{\varphi_Y(t)},\qquad
 \varphi_Y(t)=\frac{(1-e^t)(1-Ye^{-t})}{x_0t}.
 \tag{29}
\]
The original value at \(t=0\) is \(x_0-x_0^{-1}\ne0\).
The Casimir relation gives
\(ef=t\varphi_Y(t)\), so \(ZP=t\) exactly.
For a positive crossing its transfer is
\[
 N=-\log(1-e_1f_2);
 \tag{30}
\]
for a negative crossing it is
\(N=\log(1-(K_1/K_2)e_2f_1)\).
The other two Poisson variables are the corresponding input
occupation and the over-output occupation, exactly as in [P].
Remove the zeros of these algebraic logarithm arguments and
any nonremovable zeros of \(\varphi_Y\).

All these fields are holomorphic functions of logarithms and
meromorphic algebraic data on the retained cover. If an occupation
is identically zero, its continued logarithm is identically zero
and the removable value in (29) is used. It is not excluded by
writing a quotient on a dense chart. The endpoint singularities
in (6) are excluded only when they are nonremovable. Their
exponentiated conditions are algebraic in the stage variables.
None is identically singular on the attached lift, since it is
regular on the original seed neighborhood.

The finite local identities in [P] and [L] imply that these fields
solve the original local Poisson and canonical matching equations.
One can also check them without reconstructing a new phase:
their exponentiated equations are exactly the signed Gauss maps,
with \(e^N\) given by (30). The unwrapped logarithms keep the
original equation branches. Partial normal-product stationary
variables are the same intermediate coherent fields, followed
by the specified invertible classical linear substitutions.
Thus they too are supplied by this representation lift.

Here is the hard-stationary check, which is needed in addition to
the local crossing checks. Write \(L=L_\beta(x_0)\), let \(p\)
be the input momentum vector, \(Z\) the closed creation vector,
and \(P=Lp\). For the relative whole-word phase \(\mathcal P\),
the type-two equations give on the closed tuple
\[
 \mathcal P_P=L^{-T}Z-Z,\qquad
 \mathcal P_Z=p-Lp.
 \tag{31}
\]
They retain the two zero cut fields. Whenever \(I-B\) is
invertible, the original closing equations are
\(P=C\mathcal P_Z,\ Z=C^T\mathcal P_P\).
Define
\[
 A=\frac{u^T\mathcal P_P}{Y-\alpha},\qquad
 B_s=\frac{v^T\mathcal P_Z}{Y-\alpha}.
 \tag{32}
\]
Using (2) gives exactly
\[
 Z=vA+G^T\mathcal P_P,\qquad
 P=uB_s+G\mathcal P_Z .
 \tag{33}
\]
These are the hard stationary equations. No additional hard
solution is postulated. Where \(AB_s\ne0\), their envelope
identities give \(\Psi_x=Y-\alpha\), hence \(f_x=0\).

All intermediate stationary Jacobians can now be evaluated on
this known lift. Their entries are holomorphic or meromorphic
expressions in the continued endpoint functions and fields.
For later compositions, implicit derivatives are obtained by
inverting the earlier Jacobians; this gives the same conclusion
inductively. Every determinant is nonzero near the seed. Its
zeros or poles on this connected one-dimensional cover are
therefore discrete. The same is true of \(AB_s\), of \(f_{xx}\),
and of the meridian derivative, since each is nonzero at the
chosen seed. Remove these discrete sets as well.

This proves that the remaining lifted critical curve lies in
the regular source cover of Section 1. The exclusions are
locally finite: there are finitely many stationary operations,
and each retained function is meromorphic on the corresponding
logarithmic chart. A connected Riemann surface remains path
connected after removal of a closed discrete set; explicitly,
a compact path meets finitely many excluded points and can be
detoured in disjoint coordinate disks. Thus generic lifted
points of this attached component can be joined to the seed
by compact regular source paths. Section 4 constructs the
actual full marked minor along every such path.

This is not a claim that a particular prescribed path avoids
the exclusions, or that the chosen algebraic slice covers all
points of the component. In particular \(M=\pm1\), including
the complete meridian, is excluded. No limit to that endpoint
or uniform bound across an unbounded family of short cores
has been proved.

## 7. What is and is not transported

The regular cover is explicit in terms of the literal endpoint
functions, the finite stationary equations, and their determinants.
The theorem constructs its quantum amplitudes and marked minor.
It does not assume those amplitudes as independent WKB data.

Section 6 constructs generic lifts on the attached component, but
intermediate generating charts may still degenerate on a prescribed
smooth character arc. To cross these exclusions would require
source-preserving chart changes or their limiting analysis. For
uniform families of short cores, the additional input would have
to control these same finite coefficient charts and determinant
buffers, with the original highest cut retained. The existence
of an initial attached seed for every such core is also not claimed.

Likewise (19) cancels a prefix only in a difference. Continuing
the full source (17) requires its actual original-prefix sums
and their other action singularities. Continuing the relative
cap additionally requires its fixed \(\xi=0,R\) boundaries and
observation-pole data. They are not supplied by this local
bank-to-bank formula. The nonzero continued minor therefore
implies neither a physical-cycle coefficient nor a scalar lower
bound or finite-exception theorem.

## 8. Complete proof directs

| Label | Complete proof source | SHA256 |
|---|---|---|
| D | notes/research_actual_symbol_factorial_deficiency.md | a757e1ac8f6e62268cd7c2d681758a0258394661181026aace2cd516f4ca3359 |
| G | notes/research_actual_borel_phase_surface.md | ba682a18ac0ae3efa05ffbc7e6fef02c128800ccbbffda1867756ba5a8275429 |
| H | notes/research_actual_minor_quantum_meridian_action.md | 07b219d56ad42157ae6b2282c5bc0a73f3baf79c0c5dfc17fa07dfe145d2e822 |
| P | notes/research_actual_analytic_principal_phase.md | 9ae7b5df2dbd955ee6ac4580590d9f21d1b1750bcdd6c5085e7322251ab70bcb |
| L | notes/research_selected_minor_preferred_longitude.md | 50448b8688d3a7b2f4245787f6ddc07eb7afecaf94391c11c0b735ea6afdbb9c |

D supplies the literal defect and finite graph formulas; their
continued coefficient bounds are proved here. P supplies the
literal finite stationary construction and its original
normalization. G supplies the actual endpoint reconstruction
and coefficient identification. H supplies the exact external
row and common-phase shift, with its original framing.
L supplies the attached algebraic representation germ, regular
Gauss inverse, original highest-cut closure, and peripheral flag.
No external proof, mathematical program, test, or build is used.
Frozen notes and public manuscripts are unchanged.
