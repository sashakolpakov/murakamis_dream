# A complete 44 prefix with an unrestricted safe middle

Private written deduction, 10 November 2026. The complete first-period
message has a calibrated upper profile on the whole old second
plateau. Its loss is the minimum of the old quadratic loss and the
strict first-period remainder gap. This supplies an actual left
boundary estimate for the clean-closing-edge theorem.

Consequently an arbitrary safe middle, with every original selection,
seam and right state retained, may be added after the complete first
period. The intervening physical boundary strips remain unselected
plateau. The new middle sectors have the original occupation gap;
the complete-prefix remainder also retains its own separate gap.
No estimate for a departing second symbol or an invariant norm for
all unrestricted literal messages is inferred.

## 1. The exact prefix and its clipped plateau profile

Fix an actual positive three/four open word \(n_j=3+\epsilon_j\),
\(\epsilon_j\in\{0,1\}\), of length \(m\ge3\)
beginning with \(44\), with original retained reference
\(r_j=a_j+ic_j\). Put
\[
 h=m-1,\qquad k_4=\sum_{j=1}^m\epsilon_j,\qquad
 P=[11/50,9/20],\qquad
 \kappa_0=1/2500000,\qquad \kappa=1/20000 .
 \tag{1}
\]
All reference hypotheses, markings and logarithmic lifts are those
of [pointwise prefix replacement](research_mixed_four_four_pointwise_prefix_replacement.md).
In particular the second target on its plateau is
\(z_2=x_2+ic_2\), \(x_2\in P\), at its actual negative height.
The attached following reference at \(m=3\) is included in that input.

Retain its exact polynomials
\[
\begin{split}
 f_N(w,Y)&=f_{44,N}(w,Y)
   =N\operatorname{CT}_X
       [U_{1,N}(w,X)d_N(X)(1+X^{-N})C_{1,N}(X,Y)],\\
 I_N(w,z)&=N\int_{P+ic_1}
       U_{1,N}(w,e^{-2\pi ia})d_N(e^{-2\pi ia})
       C_{1,N}(e^{-2\pi ia},e^{-2\pi iz})\,da,\\
 R_N(w,z)&=f_N(w,e^{-2\pi iz})-I_N(w,z).
\end{split}
 \tag{2}
\]
All three are polynomials of degree at most \(N-1\) in the
outgoing exponential \(Y=e^{-2\pi iz}\). The heights and endpoints
of \(I_N\) are fixed. The notation \(I_N(w,Y),R_N(w,Y)\) below
means those same polynomials, not a continuation from local data.
The first line includes both first Fourier alternatives exactly,
with its original positive density \(N\,da\).

Let \(L_1,\phi_j,\Pi\) be the original allocated phases from
[the full plateau theorem](research_mixed_full_unselected_plateau.md).
Set
\[
\begin{aligned}
 M_{12}&=\Re\{L_1(r_1)+\phi_2(r_1,r_2)\},&
 p_R&=\partial_2\phi_2(r_1,r_2),\\
 \Lambda(x_2)&=M_{12}+\Re p_R(x_2-a_2),\\
 \gamma&=\min\{\kappa_0(a_1-11/50)^2,
                   \tfrac{\kappa_0}{2}(9/20-a_1)^2\}>0,\\
 \chi_2(x_2)&=\min\{\kappa_0(x_2-a_2)^2,\gamma\}.
\end{aligned}
 \tag{3}
\]

**Lemma 1.** On the entire second plateau, for every \(\tau>0\),
\[
\begin{array}{rcl}
 |I_N(w,Y)|\,|d_N(Y)|^{1/2}
 &\le& C_\tau N^{A_\tau}
  e^{N\{\Lambda(x_2)-\kappa_0(x_2-a_2)^2+\tau\}},\\
 |R_N(w,Y)|\,|d_N(Y)|^{1/2}
 &\le& C_\tau N^{A_\tau}e^{N\{\Lambda(x_2)-\gamma+\tau\}},\\
 |f_N(w,Y)|\,|d_N(Y)|^{1/2}
 &\le& C_\tau N^{A_\tau}e^{N\{\Lambda(x_2)-\chi_2(x_2)+\tau\}} .
\end{array}
 \tag{4}
\]
Both level parities and sufficiently small fixed ordinary-color
disks about \(-2\) are included. The constants and disks may
depend on the fixed actual word and prescribed allowance.

*Proof.* The first two complete supporting planes in equation (5)
of the plateau theorem give, before the \(a\)-integration,
\[
 |U_1d_N(X)C_1|\,|d_N(Y)|^{1/2}
 \le C_\tau N^{A_\tau}
 e^{N\{\Lambda(x_2)-2\kappa_0(x_1-a_1)^2
                       -\kappa_0(x_2-a_2)^2+\tau\}} .
 \tag{5}
\]
The internal first marginal cancels at the actual reference.
Integrate over \(P+ic_1\), retain the density \(N\,da\), and
absorb its polynomial cost to prove the first line of (4).
The second line is Proposition 1, equation (8), of pointwise
prefix replacement. It is already pointwise for every \(x_2\in P\);
no inequality has been recovered by dividing a whole-word integral.
Add these two estimates using (2), and enlarge their common
polynomial prefactor. This proves the third line.
All allocations are products of moduli, including at zeros. No
Fourier polynomial is divided out. \(\square\)

## 2. Exact left-state propagation along an unchanged plateau strip

Choose a safe ordinary cut \(p\ge4\) in the sense of
[the actual-open boundary reduction](research_mixed_open_boundary_comparison_reduction.md).
Require coordinates \(2,\ldots,p\) to be unselected plateau
symbols, and let all physical boundary arguments
\(z_2,\ldots,z_{p-1}\) have their original heights. This latter
condition follows from the protected-neighbor construction in
Section 3, even if a bad symbol occurs immediately after \(p\).
Write \(d_j=x_j-a_j\).

For \(Z=f,I,R\), define the actual left modulus
\[
 L_{Z,N}
 =|Z_N(w_L,X_2)|
    \prod_{j=3}^{p-1}|C_{\epsilon_j,N}(X_{j-1},X_j)|
    \prod_{j=2}^{p-2}|d_N(X_j)|^{\epsilon_j}
                   |d_N(X_{p-1})|^{\epsilon_{p-1}/2}.
 \tag{6}
\]
The outgoing half in (4) and the incoming half on factor three
restore the full coordinate-two weight. Subsequent halves restore
each internal integer weight; the last cut half is retained.
There is no asymptotic or scalar redefinition in (6).

Use the original left action and cut marginal
\[
 M_L=\Re\left\{L_1(r_1)+\sum_{j=2}^{p-1}
                      \phi_j(r_{j-1},r_j)\right\},\qquad
 P_{p,a}=\partial_1\phi_p(r_{p-1},r_p),
 \tag{7}
\]
and define the calibrated finite boundary rate, before its synthetic
closing term, by
\[
 G_{L,Z,N}=N^{-1}\log L_{Z,N}-M_L+
              \Re\{P_{p,a}(z_{p-1}-r_{p-1})\},
 \qquad \log0=-\infty .
 \tag{8}
\]
Put
\[
 Q_L=\kappa_0\left\{d_2^2+
                2\sum_{j=3}^{p-2}d_j^2+d_{p-1}^2\right\},
 \quad
 \ell_f=\chi_2(x_2),\quad
 \ell_I=\kappa_0d_2^2,\quad \ell_R=\gamma .
 \tag{9}
\]

**Lemma 2.** For any prescribed aggregate allowance,
\[
 G_{L,Z,N}\le-\ell_Z-Q_L+
                    \tau+O_{\tau,m}(\log N/N),\qquad Z=f,I,R .
 \tag{10}
\]

*Proof.* Multiply the corresponding line of (4) by the complete
ordinary planes from factors \(3,\ldots,p-1\). The first remaining
linear coefficient is \(p_R+\partial_1\phi_3(r_2,r_3)=0\).
The subsequent linear terms cancel by the original stationary
equations, and the last one cancels \(P_{p,a}\) in (8).
The constants are exactly (7). Factor three supplies one
coordinate-two quadratic; every intervening coordinate has two
incidences, and the cut coordinate has one. Their sum is (9).
The already integrated first coordinate is not charged again.
Distribute one total tolerance among the finite number of factors
and intersect their color disks. This proves (10). \(\square\)

In particular the complete prefix gives a neutral calibrated
left state, \(G_{L,f}\le0\) at the rate level, on every such
independent plateau strip. The remainder state has the strict
additional loss \(\gamma\). No periodic reference or change to
the original cut tangent has been made.

## 3. The reduced source and its genuine hybrid graph

Now use safe middle edges \(p,\ldots,q\), \(q\ge p\), with the
original eight-vertex reference halo inside \([6,m-5]\). These
are precisely the safety conditions of the actual-open reduction.
Put
\[
 I=[p-2,q+1],\qquad
 T_L=\{p-2,p-1,p\},\quad T_R=\{q-1,q,q+1\},\qquad
 F=[p+1,q-2].
 \tag{11}
\]
A reversed interval is empty; overlapping protected symbols are
one physical symbol. Every remaining symbol outside \(F\), from
coordinate two through \(h\), is unselected with real coordinate
in \(P\). Symbols in \(F\) range over their entire original
periods and all type-compatible selections.

Perform the exact first-period contraction (2) before choosing the
remaining graph. On coordinates \(2,\ldots,h\), use the original
row-dependent periodic hybrid formula from
[the split-cutoff source](research_mixed_split_cutoff_hybrid_contour.md),
equations (2)--(4), with its fixed collar width. The missing
left neighbor has baseline cutoff one, and the missing right
neighbor has the original endpoint baseline cutoff one. Equivalently
set the removed first symbol to its baseline solely in this
height formula. The selected height of any remaining selected
type-four row is the original \(7/500\), not the height used
earlier to estimate a first-coordinate current.

Write the resulting graph as
\[
 z_j=x_j+i\widehat{\mathcal H}_{\sigma,j}(\mathbf x),
 \qquad 2\le j\le h,\qquad
 J_\sigma(\mathbf x)=
       \det(I+iD\widehat{\mathcal H}_\sigma(\mathbf x)).
 \tag{12}
\]
The variables \(x_j\) outside \(F\) range over \(P\), and those
inside \(F\) over \([0,1]\). In particular \(z_2=x_2+ic_2\):
its own and neighboring cutoffs are one. All physical left
boundary arguments through \(p-1\), and all physical right
boundary arguments from \(q\), have their actual fixed heights.
The inward protected symbols \(p,q-1\) may retain a neighbor's
attenuation; they belong to the middle source, not to the fixed
physical boundary products. Every middle four-symbol stencil is
the original one used in the clean-closing comparison.

For \(Z=f,I,R\), retain the complex reduced integrand
\[
 \widehat{\mathscr J}_{Z,\sigma,N}
 =Z_N(w_L,X_2)
    \prod_{j=3}^{h}C_{\epsilon_j,N}(X_{j-1},X_j)
    \mathcal V_{\epsilon_m,N}(w_R,X_h)
    \prod_{j=2}^{h}D_j,\qquad
 D_j=d_N(X_j)^{\epsilon_j}X_j^{-N\sigma_j}.
 \tag{13}
\]
Only selections in \(F\) are summed. Every terminal row, its
whole weight and its Fourier alternatives remain inside
\(\mathcal V_{\epsilon_m,N}\).
The exterior scalar is
\[
 \widehat S_N=\kappa_N^{m+k_4}N^{m+k_4-2}.
 \tag{14}
\]
Indeed the original terminal-contracted scalar is
\(S_N=\kappa_N^{m+k_4}N^{m+k_4-1}\), by equation (13) of
[terminal contraction](research_mixed_reversed_cap_assembly.md),
and \(f_N\) includes the density \(N\) of the removed first
integral. Thus \(\widehat S_N=S_N/N\), including its unit
carrier. A polynomial degree bound does not produce this scalar.

The graph is piecewise Lipschitz, periodic in every free real
coordinate, and has a Jacobian bounded independently of \(N\)
for the fixed word and collar. One can check this directly as
in split-cutoff equation (6): take
\[
 C_*=\max\{7/500,|c_2|,\ldots,|c_h|\},\quad
 K_\rho=\max\{50,\rho^{-1}\},\quad B=C_*(40+K_\rho).
 \tag{15}
\]
A row with its own coordinate below \(1/10\) is identically
zero on each differentiability piece. Elsewhere only the own
right-cutoff derivative and one minimizing-neighbor derivative
occur. Thus its absolute row sum is at most \(B\), and
\[
                         |J_\sigma|\le(1+B^2)^{(h-1)/2}.
 \tag{16}
\]
This bound uses the actual open heights. No narrower cyclic
height bound is substituted. Ties are handled by the same
almost-everywhere convention as the original graph.

Define \(\mathcal K_{Z,N}\) as \(\widehat S_N\) times the sum
of the integrals of (13) multiplied by \(J_\sigma\), over
these real domains and selections. Exact linearity gives
\[
                  \mathcal K_{f,N}=\mathcal K_{I,N}+\mathcal K_{R,N}.
 \tag{17}
\]
It is a full first-period contraction of the original source on
this specified remaining graph. It is not a pointwise identification
with an old moving two-coordinate graph before that contraction.

For the \(I\) term, reinsert its first integration in (2).
There \(x_1\in P\) and \(\sigma_1=0\), so every cutoff involving
that coordinate is one. The original graph has \(z_1=x_1+ic_1\),
and all later heights are independent of \(x_1\). Its Jacobian
splits as \(1\oplus J_\sigma\). Also
\(\widehat S_N N=S_N\). Consequently \(\mathcal K_{I,N}\)
is exactly the original restricted source of the clean-closing
theorem, with first coordinate unselected \(P\). This verifies
the source identity, not just an agreement of action rates.

## 4. Arbitrary middle propagation and its occupation loss

For \(j\in F\), use the original occupation
\[
 p_j=\min\{1,\sigma_j+
       400(\operatorname{clamp}_P x_j-a_j)^2\}.
 \tag{18}
\]
Every selected or nonplateau free symbol has \(p_j=1\) on
these safe references. Define the remaining boundary quadratic
\[
 Q_\partial^{44}
 =Q_L+\kappa_0\left\{d_q^2+
                         2\sum_{j=q+1}^{h}d_j^2\right\}.
 \tag{19}
\]
The two physical boundary products are disjoint, even if the
protected triples overlap.

**Theorem 3.** For any \(\tau>0\), both level parities and
sufficiently small fixed ordinary-color disks,
\[
 |\widehat{\mathscr J}_{Z,\sigma,N}|
 \le C_{m,\tau}N^{A_{m,\tau}}
  \exp N\left\{M-\ell_Z-Q_\partial^{44}
                     -\kappa\sum_{j\in F}p_j+\tau\right\},
 \qquad Z=f,I,R ,
 \tag{20}
\]
where
\(\Phi(\mathbf z)=L_1(z_1)+
\sum_{j=2}^{h}\phi_j(z_{j-1},z_j)+\Pi(z_h)\)
is the unchanged whole-word allocated action,
\(M=\Re\Phi(\mathbf r)\), and \(\ell_Z\) is given in (9).

*Proof.* The right physical boundary is the original complete
unselected contracted one. Equation (5) of the plateau theorem
gives its calibrated rate at most
\(-\kappa_0\{d_q^2+2\sum_{j=q+1}^{h}d_j^2\}\).
The left rates are (10), with exactly the original \(M_L\)
and cut tangent.

Lemma 1 and equations (11)--(12) of
[clean closing-edge completion](research_mixed_clean_closing_edges_completion.md)
give on these protected triples
\[
 D\ge-A_p-E_q+\kappa\sum_{j\in F}p_j,\qquad
 \mathcal B_L+\mathcal B_R-D
       \le G_L+G_R-\kappa\sum_{j\in F}p_j .
 \tag{21}
\]
All four synthetic closing stencils remain unchanged. Their exact
losses are retained separately from the free occupation charges;
no protected occupation is reserved a second time. This is the
free-only comparison, not the differently defined full
\(D_\theta\) reservation.

Substitution of (10) and the right plane into (21) proves (20).
Every internal affine term cancels by the actual stationary
equations. The baseline constants of the integrated prefix are
still \(M_{12}\), so the constants add to the original \(M\).
The middle sources, right labels, true Fourier alternatives,
seams and heights are exactly those already used in (21).
Split one aggregate tolerance among all finite sources and the
color disks. The complete holomorphic expressions in (13)
permit fixed color derivatives on smaller disks by Cauchy;
no modulus halfweight is differentiated. \(\square\)

In particular the complete first-period remainder propagates with
its strict \(\gamma\):
\[
 |\mathcal K_{R,N}|
     \le C_{m,\tau}N^{A_{m,\tau}}e^{N(M-\gamma+\tau)} .
 \tag{22}
\]
The fixed selection count, graph Jacobian, volumes and scalar
(14) cost only the displayed prefactor. Empty \(F\) and
overlapping protected triples cause no exception to this estimate.

## 5. The enlarged source has the same nonzero coefficient

Let \(\mathcal H_N\) be the complete first-period source in
[the full first-period theorem](research_mixed_initial44_full_first_period.md),
with every other retained coordinate unselected on \(P+ic_j\).
Inside the integral defining \(\mathcal K_{f,N}\), take the
sector where every free symbol is also unselected and in \(P\).
Every remaining height is then the actual fixed height and
\(J_\sigma=1\). Exact contraction (2) and scalar (14) show that
this sector is precisely \(\mathcal H_N\).

On every other sector at least one free symbol is selected or
outside \(P\), so its occupation is one. The \(f\) case of
(20) retains \(\ell_f=\chi_2\ge0\) and \(Q_\partial^{44}\ge0\).
Thus, for every total allowance,
\[
 |\mathcal K_{f,N}-\mathcal H_N|
 \le C_{m,\tau}N^{A_{m,\tau}}e^{N(M-\kappa+\tau)} .
 \tag{23}
\]
No cancellation is needed between these newly added middle
sectors. When \(F\) is empty the difference is zero exactly.

The full first-period theorem already has the original nonzero
plateau asymptotic. Choose a fixed allowance smaller than the
gap in (23), shrink the common color disks, and divide by its
original nonzero leading term. The normalized error is
exponentially small and holomorphic. It follows that
\[
 \mathcal K_{f,N}(\mathbf w)
 =\kappa_N^{m+k_4}N^{-3/2}A_m(\mathbf w)
          e^{N\mathcal F_m(\mathbf w)}
              \{1+O_{\mathrm{hol}}(N^{-1})\},
 \qquad A_m\ne0 .
 \tag{24}
\]
The action, coefficient, Gaussian branch, marking, orientation
and all fixed normalized ordinary-color jets are unchanged.
The middle extension uses its own occupation gap \(\kappa\);
it does not consume or replace the smaller prefix gap \(\gamma\).
Equation (22) is the separate propagation statement for that
particular original remainder.

For the conservative admissible cuts \(p=16,\ q=m-15\), the
free middle is \(F=[17,m-17]\), nonempty for \(m\ge34\).
The first retained coordinate is now complete, coordinates
\(2,\ldots,16\) remain unselected plateau, and the last sixteen
retained coordinates remain unselected plateau. Shorter words
are covered only when the general safe-cut hypotheses hold;
otherwise the earlier first-period theorem is unchanged.

This is a source-specific propagation result on the actual open
reference. It does not identify the periodic triple-state potential
with a norm for an arbitrary polynomial message. In particular
coordinate two, and every intervening boundary coordinate before
a safe cut, still obeys its independent plateau restriction.
A selected, seam or right state there is a different boundary
source problem. The exact operators \(\mathsf T_{\alpha\beta}\)
on unrestricted messages, later complete periods, bounded short
words without safe cuts, ordinary closing and the finite-exception
objective retain their separate obligations. No knot conclusion
is asserted.

## Direct source versions

| Direct source | SHA-256 |
|---|---|
| research_mixed_four_four_pointwise_prefix_replacement.md | 2a4a86ced4bb326baa2ca24bfd6f9c6846103070f4a0731f663ef6d2303a89b7 |
| research_mixed_full_unselected_plateau.md | abd5dcddc9ed5057b6658bd8b7b60922540fd664c0c5c794135b19c1678c62a6 |
| research_mixed_clean_closing_edges_completion.md | cc5b75d521fe648ab5aa0974e162de02b14fb814fc628635a1126349df5dfca9 |
| research_mixed_open_boundary_comparison_reduction.md | 5d3f875a6c1a7e0c2c9840c16674dc8ad5921bf0f2312202cb26f278c86c72ce |
| research_mixed_split_cutoff_hybrid_contour.md | 6318c11366520ff2080b47028ce3ef8196d0835df2a21d0d7d5a504a80b1cc67 |
| research_mixed_reversed_cap_assembly.md | 79d44dfbcfe8c598783f27a49dea5bc716cc62e0a2c4762a238f3b2afffd244c |
| research_mixed_initial44_full_first_period.md | 2c7609442313d67b28a5a79374d3712c352fa04092d4756a6f90803ce40cbda7 |

The complete written proof and directly used source implications
were read, and all source hashes checked. No mathematical numerical
evaluation, saved-value arithmetic, import, test, compilation or
frozen-source edit was used. Independent proof and direct-source
review is required before adoption.
