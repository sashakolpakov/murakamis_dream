# Exact turn defects of original rational-word states

Private written deduction, 10 November 2026. Every original rational
word applied to the unit cap lies on the null cone of the full
Frobenius form. This gives an exact, level-independent obstruction
to almost-invariance under the original turn, including after a
unitary Fourier change of coordinates. It also gives a positive
leakage bound for averages that contain that turn.

The null-cone identity is a consequence of the existing original
adjoint formula. The new quantitative consequences below concern
these actual states, not arbitrary test vectors. They do not say
that an original marked cap observation vanishes, and do not give a
counterexample to a geometric or volume asymptotic.

## 1. Full original algebra and its two pairings

Fix \(N\ge2\), put \(D=N-1\), \(q=e^{\pi i/N}\), and retain
\[
 \mathcal A_N=\mathbb C[z]/(2T_N(z/2)+2),\qquad
 e_j(z)=S_j^{-2}\prod_{r=0}^{j-1}(c_r-z),
 \quad c_r=2\cos((2r+1)\pi/N).
\tag{1}
\]
Here \(S_j=\prod_{r=1}^j2\sin(\pi r/N)\). Polynomial symbols
\(e_j\) are distinguished from coordinate columns \(\mathbf e_j\).
The original full trace and genuine turn satisfy
\[
 \phi_N(e_i e_j)=\delta_{i+j,D},\qquad
 \mathsf T e_j=e_{D-j},\qquad
 J_{ij}=\delta_{i+j,D},\quad J^*=J=J^{-1}.
\tag{2}
\]
For \(F=\sum f_je_j\), coefficient reflection is
\(F^\sharp(z)=\overline{F(\bar z)}\). Since the basis is real,
\[
 \phi_N(F^\sharp G)=f^*Jg,\qquad
 \phi_N(F^\sharp\mathsf T G)=f^*g.
\tag{3}
\]
Thus the second expression, with its specified turn, is the positive
Newton inner product. The first expression is the original
Hermitian Frobenius form and is indefinite.

Let \(M\) be multiplication by the original positive crossing,
including its scalar \(\kappa_N=q^{D^2/2}\). The exact full-algebra
identities in [the Newton metric source](actual_newton_turn_positive_gram.md),
Sections 2--4, give
\[
 M^*=JM^{-1}J,\qquad M^*JM=J.
\tag{4}
\]
Indeed multiplication is symmetric for the bilinear Frobenius
pairing, and \(R^\sharp=R^{-1}\) in the full quotient. The latter
identity uses both the unit nodal values and their purely imaginary
logarithmic first derivatives. It is not merely an equality on
distinct nodes. The same form-preservation holds for \(J\), since
\(J^*JJ=J\).

For any fixed rational word \(W_N\) in \(J\) and signed powers of
\(M\), define its actual state and polynomial by
\[
 f_N=W_N\mathbf e_0,\qquad
 F_N(z)=\sum_{j=0}^D(f_N)_j e_j(z).
\tag{5}
\]
All generators are invertible, so \(f_N\ne0\). The word is fixed
before the limit in \(N\). The identities below are in fact exact
at each level for every such word. Original unit framing factors
may multiply (5); none of the conclusions changes.

## 2. Isotropy and the exact turn defect

**Theorem 1.** Every state (5) satisfies
\[
 \boxed{\quad
 f_N^*Jf_N=0,\qquad
 \phi_N(F_N^\sharp F_N)=0,\qquad
 \phi_N(F_N^\sharp\mathsf T F_N)=\|f_N\|_2^2>0.
 \quad}
\tag{6}
\]
For every complex number \(\lambda\),
\[
 \boxed{\quad
 \|Jf_N-\lambda f_N\|_2^2
                  =(1+|\lambda|^2)\|f_N\|_2^2.
 \quad}
\tag{7}
\]
In particular the relative defect is exactly \(\sqrt2\) for
every unit phase \(\lambda\). With \(P_\pm=(I\pm J)/2\),
\[
                   \|P_+f_N\|_2^2=\|P_-f_N\|_2^2
                                      =\tfrac12\|f_N\|_2^2.
\tag{8}
\]

*Proof.* Form-preservation is stable under products and inverses,
so (4) gives \(W_N^*JW_N=J\). Since \(N\ge2\),
\(\mathbf e_0^*J\mathbf e_0=0\). This proves the first equality
in (6), and (3) proves the other two. Expand the square in (7),
using \(\|Jf_N\|_2=\|f_N\|_2\) and the vanishing cross term.
The orthogonal projection formulas give (8). \(\square\)

This does not set either original cap observation to zero. Those
observations are
\[
                  F_N(c_0)=(f_N)_0,
                    \qquad \phi_N(F_N)=(f_N)_D.
\tag{9}
\]
For example \(W_N=M\) has coefficients
\((f_N)_j=\kappa_N(-q)^j\); both observations in (9) have
modulus one. Its reflected unturned product in (6) is nevertheless
zero. A nonzero normalization multiplying that product cannot
convert it into the positive quantity in (6).

The two products in (6) are different exact contractions. The
extra turn is part of the positive contraction's actual diagram.
Neither contraction is silently identified with the intended
Kashaev closing of an arbitrary word, and no knot-type or
hyperbolicity assertion is attached to the vanishing product.

## 3. Fourier changes, approximate states and positive averages

The obstruction is unchanged by a unitary Fourier or other unitary
change of coefficients. More precisely, for a unitary \(U_N\),
put \(g_N=U_Nf_N\) and \(J'_N=U_NJU_N^*\). Equation (7) holds
with \(g_N,J'_N\) in place of \(f_N,J\). Comparing with an
untransformed different operator would change the question.

For an invertible, possibly nonunitary frame \(S_N\), put
\(g_N=S_Nf_N\) and \(J'_N=S_NJS_N^{-1}\). The elementary
operator-norm inequalities give, for \(|\lambda|=1\),
\[
 \frac{\|(J'_N-\lambda I)g_N\|_2}{\|g_N\|_2}
       \ge\frac{\sqrt2}{\|S_N\|_2\|S_N^{-1}\|_2}.
\tag{10}
\]
Thus an exponentially small relative turn defect in this frame
requires an exponentially large condition number. For instance
a defect at most \(e^{-cN}\) forces
\(\operatorname{cond}_2(S_N)\ge\sqrt2e^{cN}\).
This statement retains the frame cost; it does not preclude a
useful nonunitary frame with a separately justified source budget.

The exact defect is also stable under relative approximations.
If \(\|\widehat f_N-f_N\|_2\le\epsilon\|f_N\|_2\), with
\(0\le\epsilon<1/\sqrt2\), the triangle inequality gives
\[
 \frac{\|J\widehat f_N-\lambda\widehat f_N\|_2}
      {\|\widehat f_N\|_2}
 \ge\frac{\sqrt2-2\epsilon}{1+\epsilon},
                         \qquad |\lambda|=1.
\tag{11}
\]
In particular an approximation with vanishing relative error
cannot become almost invariant under this turn.

Normalize \(a_N=f_N/\|f_N\|_2\), and let
\(\rho_N=a_Na_N^*\). Equation (6) says that \(a_N\) and
\(Ja_N\) are orthogonal. Consider any positive average
\[
 \mathcal P_N(X)=\sum_{r=1}^s p_rG_{r,N}XG_{r,N}^*,
 \qquad p_r>0,\quad \sum_rp_r=1,
\tag{12}
\]
that contains \(J\) (or a unit phase times \(J\)) with total
weight \(p_J>0\). The other matrices may be original words;
the following conclusion does not require them to be unitary.

**Corollary 2.** In trace norm,
\[
                 \|\mathcal P_N(\rho_N)-\rho_N\|_1\ge p_J.
\tag{13}
\]

*Proof.* Put \(Q_N=I-\rho_N\). It is an orthogonal projection,
and each summand in
\[
 \operatorname{tr}\bigl[Q_N\mathcal P_N(\rho_N)\bigr]
          =\sum_rp_r\|Q_NG_{r,N}a_N\|_2^2
\tag{14}
\]
is nonnegative. The turn contribution is \(p_J\), whereas
\(\operatorname{tr}(Q_N\rho_N)=0\). Trace-norm duality
with \(\|Q_N\|=1\) proves (13). \(\square\)

This average is not asserted to be trace preserving. If it is
instead divided by its output trace \(t_N>0\), the same proof
gives the lower bound \(p_J/t_N\). One cannot omit this changing
normalization. In particular (13) rules out vanishing residual
for the unrescaled average when \(p_J\) is bounded below.

## 4. Consequence for the short-filling strategy

The original algebra already supplies a finite-source compiler for
every fixed Conway expression. The
[marked corridor obstruction](research_marked_short_corridor_kernel_obstruction.md)
also shows why arbitrary adjacent short powers cannot be replaced
by known single-power kernels or positive three/four paths while
discarding their turns or boundary adapters.

Theorems (6)--(13) rule out a further specific shortcut: actual
rational-word cap states are not almost invariant, even up to
phase, under their original unitary turn, and their pure-state
densities are not almost stationary for the positive averages
(12). This is a source-wide statement before branching. It does
not assume a candidate geometric eigenvalue or a norm asymptotic.

A geometric quasimode for another operator is a different matter.
The earlier [original-observation theorem](research_original_almost_invariance_and_observation.md)
already gives actual geometric Casimir quasimodes with exponentially
small cap observations, and an exact adjoint residual whose endpoint
overlap consumes its entire gain. The present exact defect does
not replace those observation calculations.

Likewise the [shifted Gaussian observation estimate](research_shifted_gaussian_observation.md)
uses a localized annihilation operator on an actual shifted contour,
not the turn in (7). It remains a possible source-specific route.
Its localized norm, original observation, and complementary currents
still need their own estimates. No universal lower bound for those
observations follows from the positive norm in (6).

Products at arborescent branch vertices need not be word actions on
the unit. This note does not extend (6) to arbitrary branching
tensors. Failure of the proposed universal mechanism already on
rational-word states is enough to exclude it as an automatic
argument for every short component. No failure of geometric
cancellation estimates, of the volume conjecture, or of the
finite-exception objective is inferred.

## Direct source bindings

The sources and the portions invoked above were read directly.
The duplicate search found the original indefinite-form identities,
but not the quantitative turn defect or positive-average leakage
recorded here. No mathematical numerical evaluation, saved-value
arithmetic, import, compilation, test, or frozen-source edit was used.

| Source | SHA-256 |
|---|---|
| actual_newton_turn_positive_gram.md | d8b21fa8db909120035e86e997a0e02cb84f8dce2dcf6fb244bb5c85c17e28a3 |
| research_arbitrary_power_source_compilation.md | 55e2de84870cfd20dac5922791dbc2bed54909439dfbf4663f17c70a1089445f |
| research_original_almost_invariance_and_observation.md | 66f4c93efa35425444fbdf90728dcfd254496f3d17f48a7cf6310867fde2cc15 |
| research_marked_short_corridor_kernel_obstruction.md | 031c722e0a87856498912417add3f6bafaa2b50af2309436b1cff7bd411c1670 |
| research_shifted_gaussian_observation.md | 2d0c2e0766e3b01caff5f88cbf9dcf63518dedb20b549d31451837d8063b8df2 |
