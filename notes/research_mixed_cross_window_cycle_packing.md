# Mixed whole-CROSS and regular-window phase losses

31 October 2026. **Internally reviewed research theorem and conditional
source-rate criterion.** Root and a separate reader completed full
analytical reviews. This combines the original
whole-CROSS cofactor angular bound with regular moving windows on the same
face torus. The majorants below are exact finite source quantities. No
comparison of their product with the complete volume is assumed.

## 1. The whole-CROSS polynomial, with both parities retained

Put \(d=N-1\), \(\theta=\pi/N\), \(u=-4\sin^2(\pi\delta)\), and
\[
 a_r=4\cos^2((r+\tfrac12)\theta),\qquad
 s_r=2\sin(r\theta),\qquad A=x+y,\quad P=xy.
\]
All variables are the original four face variables of a port. Fix their
zero pattern, require \(A>0\), and let the positive entries range in a
fixed positive compact set. A zero variable stays exactly zero. In
particular this includes protected middle and protected outer patterns
allowed by the original marked source. It excludes two zero outer faces.

Write
\[
 P_N^\times(x,b,c,y;u)=(-1)^dH_{V_N,\mathrm{CROSS}}(x,b,c,y;u).
 \tag{1}
\]
The sign in (1) is part of the actual numerator convention; it has modulus
one and is restored when taking products of raw coupons. The
[exact factorization](actual_cross_cofactor_factorization.md), at the same
level \(N\), uses
\[
 \begin{aligned}
 R_0(b;u)&=1,\\
 R_j(b;u)&=b^j\prod_{r<j}(a_r+u)
     +s_j^2 A R_{j-1}(b;u)
     +s_js_{j-1}(a_{j-1}+u)P R_{j-2}(b;u).
 \end{aligned}\tag{2}
\]
The last summand is omitted at \(j=1\). For even \(N=2m\), set
\(D_b=R_{m-1}(b;u)\) and
\(E_b=(a_{m-1}+u)R_{m-2}(b;u)\). Then
\[
 P_N^\times=s_m^2 A D_bD_c
       +s_ms_{m-1}P(D_bE_c+E_bD_c).
 \tag{3}
\]
For odd \(N=2m+1\), put \(G_b=R_m(b;u)\) and keep
\(D_b=R_{m-1}(b;u)\). The formula is
\[
 P_N^\times=G_bG_c+u s_ms_{m+1}P D_bD_c.
 \tag{4}
\]
The second term of (4) is the original path which skips the central row;
its unused factor \(u\) remains. These are polynomial identities, also
when a diagonal or central factor vanishes. Every central summand contains
one cofactor from each of the \(b\)- and \(c\)-sides. No decomposition
into separately optimized face variables is made.

Define the positive endpoint value
\[
 B_N(L)=P_N^\times(L;0)>0.
 \tag{5}
\]
The zero-spectral recurrence has nonnegative coefficients. Positivity in
(5) follows from the first summand of (3), or from \(G_b(0)G_c(0)\) in
(4), since \(A>0\).

## 2. A finite majorant and the whole-port angular loss

The cofactor interpolation theorem gives, coefficient by coefficient,
\[
 |R_j(u)|_{\mathrm{coef}}
       \le C\log(N+1)R_j(0),\qquad -4\le u\le0,
       \quad 0\le j\le\lfloor d/2\rfloor.
 \tag{6}
\]
Together with the exact central comparisons in that theorem, it implies
\[
 |P_N^\times(L e^{i\vartheta};u)|
   \le M_N^\times(L):=C_0\log^2(N+1)B_N(L)
 \tag{7}
\]
for every face phase and every real \(\delta\). The constant can be
chosen uniformly over the fixed radius compact and all sufficiently large
levels of both parities. Protected zero variables need no assigned phase.

Here are the central comparisons explicitly. At even levels,
\[
 D_b(0)\ge s_{m-1}^2 A R_{m-2}(b;0),\qquad
 P\le A^2/4.
 \tag{8}
\]
Thus \(P D_b(0)R_{m-2}(c;0)\), and its reflection, are bounded by a
uniform multiple of \(A D_b(0)D_c(0)\), already a positive summand of
\(B_N\). At odd levels,
\[
 G_b(0)\ge s_m^2 A D_b(0),\qquad
 P D_b(0)D_c(0)\le\frac{1}{4s_m^4}G_b(0)G_c(0).
 \tag{9}
\]
The factors \(s_m,s_{m-1},s_{m+1}\) used here are bounded away from zero
at large \(N\). The remaining factors \(|u|\) and \(|a_{m-1}+u|\) in
(3)–(4) are bounded on the real spectral interval. This proves (7)
without discarding the odd skipped-central term or dividing by a possibly
zero diagonal.

For the supported incidences define the distance to common phase by
\[
 d_\times(\vartheta)
   =\min_{\varphi\in\mathbb T}
       \max_{f\in\operatorname{supp}(x,b,c,y)}
              |\vartheta_f-\varphi|_{\mathbb T}.
 \tag{10}
\]
Incidences are retained separately if two arguments happen to be the same
original face. For every fixed \(\eta>0\), there are \(c>0\),
\(C_1\ge1\), and \(N_0\) such that
\[
 |P_N^\times(L e^{i\vartheta};u)|
   \le C_1e^{-cN}M_N^\times(L)
       \quad\text{whenever }d_\times(\vartheta)\ge\eta,
 \tag{11}
\]
uniformly for all real \(\delta\) and \(N\ge N_0\).

To prove this, choose any positive outer incidence \(p\), which exists
because \(A>0\). Taking \(\varphi=\vartheta_p\) in (10) shows that
some supported incidence has circular distance at least \(\eta\) from
\(p\). If it is \(b\), the supported phases of \((x,b,y)\) are
separated; if it is \(c\), those of \((x,c,y)\) are separated. If it is
the other outer incidence, both sides are separated. The selected side
therefore has at least two positive entries. The
[actual cofactor angular theorem](actual_cross_cofactor_global_angular_gap.md)
gives
\[
 |R_j(\text{phased side};u)|
    \le C N^K e^{-\gamma N}R_j(\text{positive side};0)
 \tag{12}
\]
for each terminal cofactor on that side. Indeed all terminal indices in
(3)–(4) equal \(J\) or \(J-1\), with \(J=\lfloor d/2\rfloor\).
Apply (6) to the other side and (8)–(9) to each of the finitely many
central summands. This bounds the left side of (11) by
\(CN^{K'}e^{-\gamma N}B_N(L)\); absorb the polynomial into, for example,
\(e^{-\gamma N/2}\). A cofactor with one positive face is a monomial,
but cannot be the selected mismatched side. It consequently causes no
exception to this argument. If the whole port has only one supported
phase, the condition in (11) is empty.

Thus a whole CROSS port has alignment label zero at every supported
incidence. This is a whole-port conclusion from the exact central
factorization, not an assumption that the two cofactor phases can be
chosen independently.

## 3. Endpoint normalization and its rate

Let \(Q(x,b,y)\) denote the original absolute complete triangle potential
at \(\delta=0\), with homogeneity degree \(1/2\). Then, on the fixed
radius compact and fixed zero pattern,
\[
 \log B_N(L)=N\{Q(x,b,y)+Q(x,c,y)\}+O(\log N).
 \tag{13}
\]
In particular the exact majorant in (7) has a polynomial upper bound
\[
 M_N^\times(L)\le C N^K
       \exp\!\left[N\{Q(x,b,y)+Q(x,c,y)\}\right].
 \tag{14}
\]
This polynomial normalization is not needed for (11), but identifies its
source-rate interface without an unspecified exponential scalar.

For completeness, (13) follows from the existing endpoint cofactor packets
with a quantitative product estimate. For \(b>0\), including exactly one
zero outer weight, the
[interior-start packet](actual_cross_cofactor_interior_packet.md)
has its starting saddle in a fixed compact subset of \((0,1/2)\).
The finite prefix diagonal is bounded away from zero before that saddle,
and the positive tail root is bounded away from zero from there to the
terminal row. Their logarithms have uniform bounded derivatives on these
intervals. The finite-row shift is bounded, and the finite tail root
differs from its limiting root by \(O(N^{-1})\). Elementary
Euler–Maclaurin estimates therefore give
\(N\phi_N(t_N)=NQ(x,b,y)+O(1)\). The packet amplitude is a bounded
unit times \(\sqrt N\); hence
\(\log R_{J-k}(b;0)=NQ(x,b,y)+O(\log N)\), for fixed \(k\).

For \(b=0\) and \(xy>0\), the
[protected-middle packet](actual_cross_cofactor_protected_packet.md)
is a bounded nonzero amplitude times
\(\prod_{j=1}^n s_j\lambda_{j,+}\). The positive \(\lambda_{j,+}\)
is uniformly bounded away from zero even at the lower endpoint and differs
from a smooth limiting root by \(O(N^{-1})\). Its logarithmic sum has
bounded Riemann error. The remaining sine product has only the endpoint
logarithm: comparison with \(\log t\) gives Riemann error \(O(\log N)\).
The [absolute marked-action identity](actual_cross_cofactor_marked_action.md)
identifies the resulting integral with the same \(Q(0;x,y)\).
Finally, if \(b=0\) and exactly one outer weight is positive, (2) is the
literal monomial
\[
 R_n(0;0)=(x+y)^n\prod_{j=1}^n s_j^2,
 \qquad Q(x,0,y)=\tfrac12\log(x+y).
 \tag{15}
\]
The half-sine product again contributes only \(O(\log N)\). These cases
exhaust the allowed support patterns on either cofactor side. Apply their
estimates to (3) at \(u=0\), using (8) for the upper comparison and its
positive first term for the lower comparison. At odd levels (4) at zero
is exactly \(G_b(0)G_c(0)\). This proves (13).

## 4. Mixed cycles on the one original face torus

Take a fixed original source and one radius \(L_f>0\) per ordinary face.
Protected face variables are specialized to zero before coefficient
extraction. Select a set \(J\) of ports consisting of either:

- whole CROSS coupons satisfying the hypotheses above, with majorant
  \(\mathcal E_{e,N}=M_{e,N}^\times\) and zero incidence labels;
- literal regular moving windows satisfying the
  [four-positive theorem](research_regular_spectral_window_phase_exclusion.md)
  or the [one-protected-outer theorem](research_protected_outer_window_phase_exclusion.md),
  with \(\mathcal E_{e,N}=E_{e,N}\) and their actual endpoint-sign labels.
- fixed-start \(b=0\) or reflected fixed-stop \(c=0\) windows satisfying
  the [protected-middle theorem](research_protected_middle_window_phase_exclusion.md),
  again with their literal positive envelopes and only their three
  supported incidences. Their hypotheses require both outer weights and
  the other middle weight positive.

Each selected port now has the two bounds
\[
 |P_{e,N}|\le\mathcal E_{e,N},\qquad
 |P_{e,N}|\le C_e e^{-c_eN}\mathcal E_{e,N}
                  \quad\text{if }d_e\ge\eta,
 \tag{16}
\]
where \(d_e\) is distance to its supported alignment. For CROSS this
is (10); for a window subtract its prescribed \(0/\pi\) incidence
labels before minimizing over a common phase. All constants are obtained
at the same fixed threshold \(\eta\).

Use the original supported incidence multigraph, retaining repeated
incidences. For a nonempty finite collection \(\mathcal C\) of odd-label
cycles, put \(\eta=\pi/(4r_{\max})\) and let
\[
 \kappa_{\mathcal C}=
 \max\left\{\sum_{C\in\mathcal C}\lambda_C:
       \lambda_C\ge0,\quad
       \sum_{C\ni e}\lambda_C\le c_e\ \text{for every }e\in J\right\}.
 \tag{17}
\]
The [fractional cycle-packing proof](research_regular_window_cycle_packing.md)
uses only (16), so applies unchanged. CROSS vertices can carry paths
between moving-window vertices, including across a protected middle
whose zero incidence is absent. A cycle containing only CROSS vertices
has even label and supplies no such obstruction.

At unselected ports let \(M_{e,N}\) be any certified phase-uniform
majorants for their actual polynomials. For the unchanged original target
exponents \(t_f(N)\), Cauchy extraction on the one shared torus gives
\[
 \boxed{\displaystyle
 \left|\left[\prod_f z_f^{t_f(N)}\right]
                    \prod_e P_{e,N}(z)\right|
 \le C e^{-\kappa_{\mathcal C}N}
       \frac{\prod_{e\in J}\mathcal E_{e,N}(L)
             \prod_{e\notin J}M_{e,N}(L)}
            {\prod_f L_f^{t_f(N)}}.}
 \tag{18}
\]
Raw numerator signs, any external source character and all additional
source prefactors retain their actual moduli. There is no new power of
\(N\), a changed face target, or an independent radius per incidence
in (18).

## 5. Scope of the rate criterion

The whole-CROSS contribution to the logarithmic majorant in (18) is
exactly \(Q(x,b,y)+Q(x,c,y)\) by (13). The moving-window contribution
is its own original positive envelope. They are not identified with each
other. If the normalized logarithmic limsup of the entire positive
quotient in (18) is \(B_L\), its actual shared coefficient has upper
rate \(B_L-\kappa_{\mathcal C}\). Thus
\[
 B_L-\kappa_{\mathcal C}<\Phi_D,
 \tag{19}
\]
is a conditional strict source-rate certificate whenever the original
complete rate \(\Phi_D\) is known.

No uniform margin in (19), no exhaustive window cover, and no universal
bound by \(\Phi_D\) have been proved here. A family of polynomially
many pieces still needs the uniform finite-level errors and constants
specified in the cycle-packing criterion. Compatible phase systems,
uncovered irregular windows, and the remaining source sectors require
their own estimates. The statement here is for real spectral variables;
a complex-strip version must also budget the unconditional Bernstein
growth of all noncontracting factors.

The finite central identities and cofactor angular theorem used above
have their own original-source audits. This note composes their proved
estimates analytically; it makes no claim to a new physical-matrix or
asymptotic numerical audit.
