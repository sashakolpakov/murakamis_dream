# A prepared-cap rectangle containing the inherited typed images

Research deduction, 7 November 2026. The original typed critical maps
already give enough image information for the prepared three-four cap
if its main contour is allowed a larger height range. The real box,
the exact source, and every physical-tail rate stay unchanged. The
enlargement preserves strict phase accretivity, the original analytic
symbol and the four gradient strips. It requires no new root or image
calculation. Critical existence is still conditional on the strict
Fourier boundary-update inclusion, and no physical or alias sign is
asserted here.

## 1. The domain and the existing image statements

Keep the exact function \(G_{34,N}=v(-2)^TA_3A_4h(y)\), phase
\(\mathcal F_{\mathrm{cap}}\) and amplitude
\(b_{\mathrm{cap}}\) of
[the prepared-cap source theorem](research_mixed_prepared_three_four_cap_source.md).
In the coordinate order \((s,t,p,q)\), set
\[
\begin{split}
 E_c&=[27/100,49/100]+i[-11/200,1/25],\\
 T_*&=[11/50,1/2]+i[-9/125,21/1000],\\
 R_*&=[1/5,21/50]+i[-51/500,3/200],\\
 \mathscr R_*&=E_c\times T_*\times R_*^2.
\end{split}
\tag{1}
\]
Its real box is exactly
\[
 C_{\mathrm{cap}}=[.27,.49]\times[.22,.5]\times[.2,.42]^2.
\tag{2}
\]
Only the \(t,p,q\) height intervals differ from the first
prepared-source rectangle.

The remaining boundary-update inclusion is the explicit condition
\[
 \beta_K(D_4)\subset\operatorname{int}D_3,
 \qquad
 \beta_K(q)=-\frac1{2\pi i}
      \operatorname{Log}\frac{1-Ke^{-2\pi iq}}
                   {K+(1-2K)e^{-2\pi iq}}.
\tag{3}
\]
All notation and original branches in (3) are those of
[the Fourier boundary-update theorem](research_mixed_fourier_boundary_update.md).
That theorem proves whole-disk regularity and the zero logarithmic
lift; (3) is its separate, still conditional, strict inclusion.

**Proposition 1.** If (3) holds, the original critical point of the
prepared three-four phase at \(y=x_0\) lies strictly inside
\(\mathscr R_*\). The endpoint auxiliary is the original
\(u_c(s)\). No further root-image certificate is required for
this inclusion.

*Proof.* The boundary-update fixed point retains an auxiliary inverse
leg \(b\in D_3\). The two update groups for the word \(34\)
are precisely the original type-three endpoint map at external input
\(p\in D_4\), and the original ordinary type-four map
\(B_1(t,b)=(p,q)\) on \(D_3\times D_3\).

[The endpoint-image corollary](research_mixed_open_word_endpoint_rectangles.md)
was extracted from every leaf of the four full typed input-disk maps,
before any specialization to an open-word solution. Therefore it
applies to this endpoint map and gives
\[
\begin{split}
 s&\in(.376,.438)+i(-.019,.037)\subset\operatorname{int}E_c,\\
 t&\in(.278,.391)+i(-.072,.021)\subset\operatorname{int}T_*,\\
 u&\in(.218,.242)+i(.049,.077).
\end{split}
\tag{4}
\]
Its source theorem identifies \(u=u_c(s)\) with the original
zero logarithmic lift.

Section 1 of
[the universal critical-height theorem](research_mixed_cyclic_critical_height_bounds.md)
first proves the following image bounds for every original full typed
bidisk map of type four:
\[
 |z-(.30-.052i)|<.06,
                  \qquad -.102<\Im z<-.001.
\tag{5}
\]
Only afterward does that proof specialize the images to cyclic fixed
points. Its harmonic maximum argument uses the independently proved
holomorphic map on the whole bidisk. Thus (5) applies directly to
\(B_1(t,b)\), not by treating the prepared prefix as a cycle.
In particular \(.24<\Re p,\Re q<.36\), and (5) places
both coordinates strictly in \(R_*\).
All equations at this fixed point are original source equations by
the boundary-update theorem. This proves the claim. \(\square\)

The stronger five-window height conclusion in the same source is
not used: a two-letter prefix does not meet its window hypotheses.

## 2. Strict accretivity survives the larger heights

**Proposition 2.** On a neighborhood of \(\mathscr R_*\), and
for \((y,w)\) in a sufficiently small fixed neighborhood of
\((x_0,-2)\), there is \(\mu_*>0\) such that
\[
             -\Re\mathcal F_{\mathrm{cap}}''\succeq\mu_* I_4.
\tag{6}
\]

*Proof.* At complete ordinary color use the exact decomposition
\[
 \mathcal F_{\mathrm{cap}}
 =\Psi_0(s,t)+V(t,p)+V(p,q)-g(p)+2\pi itp+\ell_q(y),
 \qquad V(z,z')=g(z+z')-g(z)-g(z').
\tag{7}
\]
Lemma 1 of
[the cap upper-target extension](research_mixed_cap_upper_target_extension.md)
proves \(-\Re\Psi_0''\succ(\pi/200)I_2\) on
\(E_c\times([.22,.5]+i[-.108,.021])\). This contains
the full \((s,t)\) product in (1).

For each \(z\) among \(t,p,q\), one has
\(.2\le\Re z\le.5\) and \(|\Im z|\le.102\).
The elementary identity for \(\Im\cot\pi z\) implies
\[
 |\Im\cot\pi z|<1
 \quad\Longleftrightarrow\quad
       \cos(2\pi\Re z)<e^{-2\pi|\Im z|}.
\tag{8}
\]
Here
\[
 \cos(2\pi\Re z)\le\cos(2\pi/5)
        =\frac{\sqrt5-1}{4}<\frac13<\frac12
        <e^{-.204\pi}.
\tag{9}
\]
Indeed \(.204\pi<561/875<2/3<\log2\), using
\(\pi<22/7\) and
\(\log(1+x)>2x/(2+x)\) at \(x=1\).
All pair sums have real part in \((0,1)\).
The [original complex triangle criterion](research_mixed_boundary_strip_bounds.md),
Section 1, therefore gives a positive definite negative real Hessian
for \(V(p,q)\), and a positive semidefinite one for \(V(t,p)\).
The latter assertion includes \(\Re t=.5\) by continuity.
The two own real coordinates of \(V(p,q)\) stay strictly below
one half; compactness gives a uniform positive floor for that pair.

The term \(-g(p)\) adds a nonnegative diagonal form and the
chirp adds zero to the real Hessian. Finally \(\Re q\ge.2>
\Re x_0\), \(\Re(q-x_0)<1/2\), so
\[
 -\Re\ell_{q,qq}(x_0)
       =-\frac{2\pi\Im(Ke^{-2\pi iq})}
                     {|1-Ke^{-2\pi iq}|^2}>0.
\tag{10}
\]
The cap form covers \((s,t)\); \(V(p,q)\) covers the other
two variables. Their sum proves a strict uniform floor on the compact
product. Holomorphy and compactness preserve a smaller floor on the
stated neighborhoods. \(\square\)

## 3. The exact finite symbol also remains in its proved domain

This enlargement is not merely a phase continuation. The same exact
finite row interpolation remains available on the whole product.
The relevant factorial arguments have real ranges
\[
\begin{array}{c|c}
 \text{argument}&\text{real range}\\ \hline
 s+t&[.49,.99]\\
 t+p&[.42,.92]\\
 p+q&[.4,.84]\\
 t,p,q&[.2,.5]\text{ as a common containing interval}.
\end{array}
\tag{11}
\]
They therefore stay in compact subsets of the original strip
\(0<\Re z<1\). The exact sine-factorial interpolation and its
uniform expansion hold on arbitrary complex compact subsets of that
strip, by Sections 1 and 4 of
[the complex-factorial construction](exact_factorial_interpolation_and_complex_contours.md).
The larger negative heights introduce no additional restriction there.

The ordinary endpoint factor is still exactly
\(D_N(s)^{-1}C_N(s,w)\); its nonzero packet on a neighborhood
of \(E_c\times\{-2\}\) is
[the endpoint rectangle theorem](research_mixed_endpoint_cap_rectangle.md).
The off-grid identity with the literal complete Newton source is the
one already retained in the prepared-cap source theorem.

The only remaining root-Pochhammer denominator depends on \(q,y\).
Throughout (1), its upper height is unchanged, so the inherited bound
\[
              |K|<1,\qquad |Ke^{-2\pi iq}|
                          \le |K|e^{.03\pi}<7/10
\tag{12}
\]
still holds. Both arguments belong to the compact unit-disk domain of
[the exact root-Pochhammer interpolation](research_root_pochhammer_interpolation.md),
Propositions 1--2 and equation (9). This preserves its exact lattice
values, resonant terms, nonvanishing and uniform holomorphic expansion.
The same strict bounds hold on small fixed neighborhoods. In particular
no assertion for \(|Ke^{-2\pi iq}|\ge1\) is needed.

Consequently the complete row interpolant, including its original
outside scalar, has exactly the unchanged expansion
\[
 \kappa^3N^{-3}b_{\mathrm{cap}}(s,t,p,q;y,w)
       e^{N\mathcal F_{\mathrm{cap}}(s,t,p,q;y,w)}
                    (1+O(N^{-1})),
\tag{13}
\]
uniformly on (1), with its original nonzero amplitude from equation
(18) of the prepared-cap source theorem. Every fixed derivative of
the normalized error is uniform on smaller neighborhoods. All exact
interpolants and the original carrier retain both level parities.
Equation (13) is a statement about the interpolated rows, not their
entire sum.

## 4. Contour consequences and remaining comparisons

The four gradient estimates in Section 2 of
[the critical-curve theorem](research_mixed_prepared_three_four_cap_critical_curve.md)
depend only on the real ranges in (11), the original \(u_c(s)\)
on \(E_c\), and the incidence branch. They do not require the four
outer stationary equations or their earlier height bounds. Therefore
the same strict inequalities \(|\Im\partial_j
\mathcal F_{\mathrm{cap}}|<2\pi\) hold on (1).
Compactness preserves a smaller positive margin for nearby parameters.

The complete physical-tail reduction in
[the coherent tail theorem](research_mixed_prepared_cap_physical_tail_reduction.md)
uses only the real box (2), so it is unchanged. The simultaneous
contour argument can use the enlarged heights, with all joins retained.
Its eight single-height alias comparisons must use precisely
\[
 h_{s,-}=-.055,\quad h_{s,+}=.04,\qquad
 h_{t,-}=-.072,\quad h_{t,+}=.021,\qquad
 h_{p,-}=h_{q,-}=-.102,\quad h_{p,+}=h_{q,+}=.015.
\tag{14}
\]
No old numerical alias bound is transported to these new faces.

If (3) is proved, Propositions 1--2 and (13) provide the needed
interior root, strict curvature and exact local symbol on one common
product. The resulting local current has its own action and nonzero
coefficient, with normalization \(\kappa^3N^{-1}\). To identify
that current with the whole prepared cap still requires strict physical
and alias comparisons against this new critical action. A full-period
outgoing envelope and whole-message propagation remain separate as
well. No whole-source or knot-family conclusion follows here.
