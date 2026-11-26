# Formal coefficients along the marked positive source component

Private written proof, 22 November 2026.

The geometric formal coefficients of the initialized contour source are
finite rational Gaussian expressions. Their continuation needs less
logarithmic data than the action. For any supplied positive unit-charge
primitive target, the original positive tangent domain supplies a marked
regular path and a one-complex-parameter neighborhood on which every
coefficient continues. The leading coefficient is nonzero at the target.
In this class the polynomial upper-bound criterion therefore has no
additional formal-coefficient or leading-unit hypothesis to discharge.

No global upper estimate, quantum-cycle coefficient, or new filling class
is proved. A positive lift of an arbitrary short hyperbolic filling is
not assumed to exist.

## 1. The full independent-variable formal calculation

Fix a finite original same-index graph with selected vertices \(I\),
\(m=|I|\ge1\). Let \(E\) be all retained original edges, \(e=|E|\),
and \(d=e+m\). Every selected vertex has at least one incidence.
Loops count twice; repeated edges remain distinct. Outside angles
are fixed at zero. Edges with both endpoints outside \(I\) remain
exact complete-kernel factors: their wires have \(q_e=1\), \(x_e=1/4\)
and \(H_e=8\pi\), with their usual factorial and Gaussian densities.
They are not dropped. Fix real powers \(n_v\) before \(N\to\infty\);
integral powers are the actual physical ones.

Retain independent original variables \(x_e,t_v\), and put
\[
 w_v=\tan(t_v/2),\qquad q_e=\cot(\pi x_e),\qquad
 z_{e,v,\pm}=\tfrac12-x_e\pm t_v/(2\pi).
 \tag{1}
\]
An outside endpoint has \(t_v=w_v=0\). The original incidence phase is
\[
 b_0(x,t)=-J(\tfrac12-x+t/(2\pi))
          -J(\tfrac12-x-t/(2\pi))-2J(x),\qquad
 J'(z)=\Log(2\sin\pi z),\qquad J(1/2)=0.
\]
On its marked local branches the full phase is
\[
 \Phi_{\boldsymbol\chi}(x,t)=
   \sum_{(e,v)}b_0(x_e,t_v)
   +\sum_{v\in I}\left(\frac{in_vt_v^2}{4\pi}-i\chi_vt_v\right).
 \tag{2}
\]
The incidence sum has two terms for every edge. At a full critical
point the selected wire sheet satisfies
\[
                     q_e^2=1+w_v^2+w_u^2\quad(e=vu).
 \tag{3}
\]
All derivatives below are taken in the independent variables of (1)
before imposing (3). In particular no fold wire is differentiated
as an eliminated function of its endpoint angles.

Let \(H=-\Phi''\) in those \(d\) independent variables, and put
\(\Delta=\det H\). On a marked critical chart suppose
\[
 (1+w_v^2)(1+q_e^2)\ne0,\qquad
 q_e+w_v\ne0,\quad q_e-w_v\ne0,\qquad \Delta\ne0
 \tag{4}
\]
for every relevant incidence. The conditions at an outside endpoint
have their literal meaning. On (3), the incidence conditions follow
from \(1+w_u^2\ne0\).

**Formal coefficient statement.** Continue the determinant root from
the actual initialized germ. Every coefficient of its full stationary
expansion is holomorphic on the resulting regular determinant-root
cover. Its leading coefficient is
\[
 a_0=\left(\frac{i}{\pi}\right)^m(2\pi)^{d/2}
       \frac{A(x,t)}{\sqrt{\Delta}},\qquad
 A(x,t)=\prod_{v\in I}\sin t_v
                    \prod_e\frac1{4\sin^2(\pi x_e)}
       =\prod_{v\in I}\frac{2w_v}{1+w_v^2}
                    \prod_e\frac{1+q_e^2}{4}.
 \tag{5}
\]
Where all selected \(w_v\ne0\), each \(a_j/a_0\) is a rational function
of \(q,w\), with constants depending on the fixed graph and powers.
The coefficients \(a_j\) themselves have no pole forced by \(w_v=0\).
Nor is \(q_e=0\) a forbidden divisor when (4) and \(\Delta\ne0\) hold.
This last assertion does not prove regularity of an unspecified fold.

Here is a direct construction. The centered factorial expansion in the
pinned source gives the incidence defects
\[
 C_{r,e,v}=
 -\frac{B_{2r}(1/2)
       \{J^{(2r)}(z_{e,v,+})+J^{(2r)}(z_{e,v,-})\}
              +2B_{2r}J^{(2r)}(x_e)}{(2r)!},
 \qquad C_r=\sum_{(e,v)}C_{r,e,v}.
 \tag{6}
\]
Here \(B_k(z)\) is the Bernoulli polynomial and \(B_k=B_k(0)\).
It is an actual uniform all-order factorial expansion near the
initializer. Away from that neighborhood (6) defines its formal
coefficient continuation, not an asserted asymptotic for the exact
factorial on arbitrary complex domains.

For \(r\ge1\), \(J^{(2r)}(z)\) is a polynomial in \(\cot(\pi z)\),
with fixed powers of \(\pi\). Moreover
\[
 \cot(\pi z_{e,v,+})=\frac{1-q_ew_v}{q_e+w_v},\qquad
 \cot(\pi z_{e,v,-})=\frac{1+q_ew_v}{q_e-w_v}.
 \tag{7}
\]
Thus every \(C_r\) is rational under (4). The independent-variable
derivations are
\[
 \partial_{x_e}=-\pi(1+q_e^2)\partial_{q_e},\qquad
 \partial_{t_v}=\tfrac12(1+w_v^2)\partial_{w_v}.
 \tag{8}
\]
They preserve this field. Every derivative of \(\Phi\) of order at
least two is rational as well: a second derivative removes each
sine logarithm, the crossing term contributes only its fixed
quadratic coefficient, and the charge term has no second derivative.

For completeness, write \(h=N^{-1}\), let \(p=(x,t)\) be the critical
point, and let \(\Phi_k(\xi)\) be the degree-\(k\) Taylor term of
\(\Phi(p+\xi)\). Define the normalized Gaussian functional by
\[
                  \mathcal W_H(e^{l^T\xi})
                       =e^{l^TH^{-1}l/2}.
 \tag{9}
\]
The formal coefficients are exactly those of
\[
 \left(\frac{i}{\pi}\right)^m\frac{(2\pi)^{d/2}}{\sqrt{\Delta}}\,
 \mathcal W_H\!\left[
 A(p+\sqrt h\,\xi)
 \exp\left\{\sum_{k\ge3}h^{k/2-1}\Phi_k(\xi)
       +\sum_{r\ge1}h^{2r-1}C_r(p+\sqrt h\,\xi)\right\}\right].
 \tag{10}
\]
Odd Gaussian moments vanish, so only integer powers of \(h\) remain.
At each fixed order only finitely many Taylor terms and pairings
occur. They use derivatives in (8), the rational phase derivatives,
and entries of \(H^{-1}\). Formula (10) proves the assertion, including
holomorphy at a selected \(w_v=0\): it never divides by \(A(p)\).
Dividing afterward by the nonzero expression (5) gives the rational
ratio statement.

## 2. Identification with the actual initialized coefficients

The initial identification retains the original polynomial source.
At each discrete index the canonical halfwire satisfies
\[
                        B_N(j/N,t)=e_j(-2\cos t)
 \tag{11}
\]
as an ordinary polynomial identity. Near its original interior wire
saddle the two halfwires have the actual expansion
\[
 B_N(x,t_v)B_N(x,t_u)
  =\frac{e^{N\{b_0(x,t_v)+b_0(x,t_u)\}}}
           {4N^2\sin^2(\pi x)}
       \exp\left\{\sum_{r\ge1}N^{-(2r-1)}
                       (C_{r,e,v}+C_{r,e,u})\right\}.
 \tag{12}
\]
The expansion is meant to any fixed order with its remainder, on
the initial compact regular chart.

The original local finite-sum argument encloses the retained indices
with the cotangent residue kernel. Its constant mode has coefficient
exactly \(+N\) times the wire integral; its nonconstant modes, endpoint
connectors and omitted index tails have a strict exponential gap.
This is the finite-sum calculation in the regular low-source proof.
Only that local calculation is used here, not its zero-power subtree
theorem: at completeness the wire is \(x=1/4\), all normalized
factorial arguments are \(1/4\), and the wire second derivative is
\(-8\pi\). They retain their regularity and strict local gaps near
the actual small-charge seed. The all-order factorial expansion
therefore applies to that same finite-index calculation.
The actual small-charge theorem estimates the remaining original
rows and all mixed angular currents. The pattern-adapted all-plus
family retains these estimates and removes just the factor \(2^{-m}\)
from the central horizontal cosine.

Consequently its actual all-order seed coefficients come from (12)
followed by the angular Gaussian expansion. Formal Gaussian
integration in successive variable groups equals the full rule (10).
One elementary verification is to test the quadratic Gaussian on
\(e^{l^T\xi}\): completing the wire square gives the same inverse
quadratic form and determinant as the block Schur formula. Expansion
in \(l\) proves equality for every polynomial moment, hence at every
fixed Taylor order.

The powers are \(N^{2m}\) from the angular traces, \(N^{-e}\) from the
paired halfwire factors and index prefactors, and \(N^{-d/2}\) from
the full Gaussian. Their product is \(N^\beta\), where
\[
                            \beta=\frac{3(m-e)}2.
 \tag{13}
\]
This proves (5) with its actual constant and marks, not only up to a
nonzero function. Both level parities have the same formal calculation;
their exact rational trace denominators differ only in terms already
exponentially small at the seed.

No global factorial substitution for the off-endpoint contour family
has been made. Its ordinary polynomial numerator, frozen heights,
removed rows and vertical currents remain the prescribed ones.
Only the known seed coefficients have been identified and continued.

## 3. The positive tangent domain and its original marks

Let \(\mathcal P\) be the domain of selected tangent configurations
\(w\), with outside tangents zero, at which every original edge is
positive. Use the original inverse-tangent strip
\[
 \mathcal A=\mathbb C\setminus
               (i[1,\infty)\cup-i[1,\infty)),\qquad
 t_v=2\arctan w_v,\quad |\Re t_v|<\pi.
 \tag{14}
\]
The positive-wire contraction lemma proves independent-coordinate
contraction within \(\mathcal P\). In particular it is open,
star shaped about zero, and contractible. Here \(\mathcal P\) means
the actual positive-edge domain, not the larger product neighborhoods
constructed elsewhere for contour reachability.

On \(\mathcal P\), use the principal roots and original wire branches
\[
 q_e=\sqrt{1+w_v^2+w_u^2},\quad \Re q_e>0,\qquad
 x_e=\frac1{2\pi i}\Log\frac{q_e+i}{q_e-i},\quad x_e(0)=\tfrac14.
 \tag{15}
\]
They have \(0<\Re x_e<1/2\). All \(1+w_v^2\), \(q_e\pm i\) and
\(q_e\pm w_v\) are units, the last by
\((q_e+w_v)(q_e-w_v)=1+w_u^2\).
Contractibility therefore supplies the canonical return logarithms
\[
 r_{v,e}=\tfrac12\Log\frac{q_e+w_v}{q_e-w_v},\qquad r_{v,e}(0)=0,
 \qquad
 \mathcal P_v(t)=\sum_{e\ni v}r_{v,e}-\frac{in_vt_v}{2}.
 \tag{16}
\]
Every incidence and original power is retained.

For \(F_e=b_0(x_e,t_v)+b_0(x_e,t_u)\), the unexponentiated wire
equation is \(F_{e,x}=0\) on this graph.
Its exponential equals one by (3), its initial value is zero,
and its continued value is discrete and continuous on connected
\(\mathcal P\); hence it stays zero. The angular derivatives of the
original phase are
\[
             \Phi_{t_v}=-\mathcal P_v/\pi-i\chi_v.
 \tag{17}
\]
These are the marked equations, not just their multipliers.
The critical edge actions have derivatives \(-r_{v,e}/\pi\).
Their closed holomorphic one-forms have unique primitives on the
contractible domain, normalized at the original complete action.
They give the same continued phase as (2), anchored there at
\(eM_\infty\), with \(M_\infty\) the original complete edge action.
No logarithm or action constant is reset.

To check full regularity, let \(K_e\) be the original edge matrix.
For these complex symmetric matrices, \(\Re\) denotes the Hermitian part.
\[
 K_e=\frac1{q_e}
       \begin{pmatrix}1+w_v^2&-w_vw_u\\
                       -w_vw_u&1+w_u^2\end{pmatrix}.
 \tag{18}
\]
The positive-edge theorem gives \(\Re K_e>0\).
With \(B_e\) the real incidence pullback to selected variations,
including repeated entries for a loop,
\[
 \mathcal P_t=\frac12\sum_eB_e^TK_eB_e
                         -\frac i2\operatorname{diag}(n_v).
 \tag{19}
\]
Since the powers are real and every selected vertex is incident,
\(\Re\mathcal P_t>0\). The wire Hessian block is diagonal with units
\[
                  H_e=\frac{2\pi q_e(1+q_e^2)^2}
                               {(1+w_v^2)(1+w_u^2)}.
 \tag{20}
\]
Its Schur complement in the full \(H\) is
\(\mathcal P_t/\pi\), by (17). Thus \(\Delta\ne0\) everywhere
on \(\mathcal P\), including zero selected tangents.
The seed determinant root extends uniquely over this contractible
domain. Formula (10) therefore defines every \(a_j\) holomorphically
on \(\mathcal P\).

There is a global charge chart, not merely a local inverse. The
positive-edge comparison, summed over all incidences, gives for any
two distinct configurations in \(\mathcal P\)
\[
       \Re\sum_{v\in I}\delta\mathcal P_v\,
                                  \overline{\delta t_v}>0.
\]
The fixed real-power term has zero real contribution to this pairing.
Hence \(\boldsymbol\chi=i\boldsymbol{\mathcal P}/\pi\) is injective,
also for complex charges. Its Jacobian is invertible by (19), so it
is a biholomorphism onto an open contractible complex charge domain
\(\mathcal C_{\mathbf n}\). The critical action and all the \(a_j\)
descend holomorphically to this domain, with their original marks.

An independent vertex sign flip preserves \(\mathcal P\), changes
only \(\chi_v\) to \(-\chi_v\), and leaves all other charges unchanged.
This follows from (15)--(16) and the canonical zero logarithms.
Injectivity then proves \(\chi_v=0\) if and only if \(w_v=0\).
Thus (5) has precisely the coordinate charge hyperplanes as its
zero set on \(\mathcal C_{\mathbf n}\); no vanishing order is asserted.

Suppose a target in this domain satisfies the original unit-charge
primitive equations \(\mathcal P_v=-\pi i\), with their canonical
logs. Then every selected \(w_v\ne0\). Indeed \(w_v=0\) gives
\(t_v=0\) and every \(r_{v,e}=0\): the zero-coordinate slice contracts
to completeness, where these zero logarithms are fixed. It would
give \(\mathcal P_v=0\), a contradiction. Formula (5) proves that
the target leading coefficient is a unit. Intermediate zeros of
\(a_0\), for example at completeness, do not obstruct continuation
of the formal coefficients.

## 4. A one-parameter marked full critical curve

Choose the actual small positive-charge seed for these same fixed
powers, and let \(w^*\) be any supplied target as just specified.
Both points have all selected coordinates nonzero. Contract each
along its radial arm into a sufficiently small product polydisk
contained in \(\mathcal P\), stopping before zero. Connect the two
contracted points coordinate by coordinate inside the corresponding
punctured disks. The two radial arms and this connector give a compact
continuous path in \(\mathcal P\cap(\mathbb C^*)^m\).
Approximate it uniformly by a fixed Bernstein polynomial vector
\(p(s)\) preserving its endpoints.
Such approximation follows directly from uniform continuity: in
the Bernstein average, the mass at distance at least \(\delta\)
from \(s\) is at most \(1/(4M\delta^2)\), while the remaining
oscillation is bounded by the path's continuity modulus at \(\delta\).
Taking the fixed degree \(M\) large keeps the image inside
\(\mathcal P\cap(\mathbb C^*)^m\), since the compact path has positive
distance from its complement. This degree is unrelated to the level \(N\).

By compactness a complex stadium \(D\) around \([0,1]\) can be chosen
so that \(p(D)\subset\mathcal P\cap(\mathbb C^*)^m\). On it define
\[
 w(s)=p(s),\quad t(s)=2\arctan w(s),\qquad
 \chi_v(s)=\frac{i}{\pi}\mathcal P_v(t(s)).
 \tag{21}
\]
These independent complex charges equal the chosen small seed vector
at \(s=0\) and \(\mathbf1\) at \(s=1\). Equations (15), (17), (21)
give a full critical point of the original phase for every \(s\in D\).
Let \(S(s)\) be its marked critical value. It is holomorphic, as are
all coefficients \(a_j(p(s))\), and \(a_0(p(s))\) is a unit throughout
\(D\). Its charge curve lies in the single global chart
\(\mathcal C_{\mathbf n}\).
The construction never requires a common real charge path or a path
with fixed filling periods.

Freeze the initialized contour family's heights, cuts and currents
once at the seed. The actual family used along the curve is
\[
 \mathscr G_N(s)=
   \mathfrak Z_{N,\mathbf+}(\mathbf n,\boldsymbol\chi(s);\mathbf0),
 \qquad
 \varepsilon_N=\prod_v e^{\pi in_v(N-1)^2/(4N)}.
 \tag{22}
\]
It is holomorphic on \(D\), with the actual all-order initializer
near \(s=0\), and it has the original endpoint
\(Z_N^{\rm original}=\varepsilon_N\mathscr G_N(1)\).
The formal coefficients just constructed are exactly the analytic
continuations of that initializer.

## 5. The remaining upper estimate

We apply the general analytic theorem in Section 1 of the polynomial
upper-bound criterion, with \(e\) and \(\beta\) counting every retained
edge as above. The exact complete-kernel factors from outside-only edges
and their Gaussian expansions are included in this normalization.
That theorem now applies if
\[
 \sup_K\left|N^{-\beta}e^{-NS(s)}\mathscr G_N(s)\right|
                   \le C_KN^{B_K}\qquad(K\Subset D),
 \tag{23}
\]
or if its local complex-area \(L^2\) version holds. It gives the
full asymptotic expansion throughout \(D\), and in particular
\[
 Z_N^{\rm original}
   =\varepsilon_NN^\beta e^{NS(1)}
                              \{a_0(p(1))+O(N^{-1})\}.
 \tag{24}
\]
Within this supplied positive-target class, the formal continuation,
regular marked path and target leading unit required by that criterion
have thus been constructed. Estimate (23) has not been proved.
The source in it is the same frozen ordinary-polynomial contour
representative, with every original current retained.

No global one-phase asymptotic for individual exact factorials is
inferred from their formal coefficients. No free cardinal end or
reversed-index edge is assigned the phase (2). Outside data remain
complete; a general incoming-boundary initializer is not supplied.
Nor is a positive lift of every hyperbolic short filling established.
For a knot conclusion the original source identification, peripheral
marking and equality \(2\pi\Re S(1)=\operatorname{Vol}\) must still
be retained or proved. There is no new volume lower bound here.

## Complete direct sources

The proof uses the following complete matching source texts. All
coefficients and marks are those of these versions.

- Factorial amplitude, 380 lines:
  [research_two_square_factorial_amplitude.md](research_two_square_factorial_amplitude.md),
  995c38d1cc6fcd5a1a1306601778ce6068b5f1d766364216e7cdd933f344290f.
- Full independent phase, 411 lines:
  [research_unsummed_two_square_morse_lift.md](research_unsummed_two_square_morse_lift.md),
  82ad7a75e6ab2857bbebb2f003f7e182ab1f26da1cf425f579106cdad11d15dd.
- Original local finite index sum, 351 lines:
  [research_regular_zero_subtree_low_source.md](research_regular_zero_subtree_low_source.md),
  06e4b7c14e3a61616dea61642103e2d2803709fcd465ae9860258119db3299d1.
- Initialized actual contour family, 370 lines:
  [research_pattern_adapted_polarized_heat_initializer.md](research_pattern_adapted_polarized_heat_initializer.md),
  a27c25dae7f3be3f1ef52fb369ecca822b0896a4b034450131e05b12423c2694.
- Positive tangent contractions and original wire marks, 531 lines:
  [research_positive_wire_product_contour.md](research_positive_wire_product_contour.md),
  5646f2d6b2a8dfa2d8c49662d17f19f3743fc4efcaf3c3685c6a899975a4c230.
- Original positive edge matrix, 678 lines:
  [research_positive_edge_global_monotonicity.md](research_positive_edge_global_monotonicity.md),
  da5129c7110190035eedb8249d4004dd06b5a7555e78d948234d8de50fa17500.
- Polynomial-loss continuation criterion, 289 lines:
  [research_polarized_polynomial_upper_criterion.md](research_polarized_polynomial_upper_criterion.md),
  1a7ca165e0bc3b6e115566859e2a780079389d3004e6915ff396eb7c9ca47d9a.

