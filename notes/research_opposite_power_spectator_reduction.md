# Opposite powers with the original spectator and closing retained

Private written proof, 16 November 2026.

An opposite pair of the original operators cancels in the original
Frobenius closing. With an additional spectator, it conjugates that
spectator instead. This gives a polynomial bound for fixed-degree
insertions and fixed physical-row values after the next turn.
It does not give the corresponding first-normal initialization.

The reality, Frobenius self-adjointness and positive Newton metric
used here are archived identities. The application below keeps the
actual opposite-power product, its spectator and all physical jets.

## 1. Source conventions and exact reduction

For every \(N\ge2\), put
\[
 D=N-1,\quad q=e^{\pi i/N},\quad \eta=(-1)^D,\quad
 \kappa=q^{D^2/2},\quad P_N(Z)=2T_N(Z/2)+2,
\]
\[
 \mathcal A_N=\mathbb C[Z]/(P_N),\qquad
 e_j(Z)=S_j^{-2}\prod_{a<j}(c_a-Z),\quad
 c_a=2\cos((2a+1)\pi/N),\quad
 S_j=\prod_{a=1}^j2\sin(a\pi/N).
\]
Here \(S_0=1\), and \(T_N\) is Chebyshev's polynomial.
Distinct physical rows are indexed by
\(0\le j\le J_N=\lfloor D/2\rfloor\); they are double,
except for \(c_{J_N}=-2\) at odd \(N\).
The original turn \(T\), crossing \(R\), trace and kernel satisfy
\[
 Te_j=e_{D-j},\qquad \phi_N(e_i e_j)=\mathbf1_{i+j=D},
 \qquad \phi_N(p)=\eta N^2[Z^D]\operatorname{can}p,
\]
\[
 K_N(w,Z)=\sum_{j=0}^D e_j(w)e_j(Z),\qquad
 (Tp)(w)=\phi_{N,Z}(K_N(w,Z)p(Z)).
 \tag{1}
\]
The notation \(\operatorname{can}\) means the remainder of degree
at most \(D\). Products in \(\mathcal A_N\) retain the full double
roots. Free parameters are ordinary scalars, not quotient variables.

Write
\[
 f^\sharp(Z)=\overline{f(\overline Z)},\qquad
 C f=\operatorname{can}(Zf),\quad
 V_n=\kappa^n T M_{R^{-n}}T,\quad
 D_n=V_nCV_{-n},\qquad n\in\mathbb Z .
 \tag{2}
\]
Here \(M_a\) denotes multiplication by \(a\) in the quotient.
The full Hermite reality identity is \(R^\sharp=R^{-1}\).
Together with the real Newton basis, it gives
\[
                    (V_nf)^\sharp=V_{-n}f^\sharp .
 \tag{3}
\]
This includes the original crossing carrier: conjugation changes
\(\kappa^n\) to \(\kappa^{-n}\).

**Theorem 1.** For arbitrary complex \(f,g\in\mathcal A_N\), any
ordinary polynomial \(h\), and every integer \(n\),
\[
 \boxed{\quad
 \phi_N\!\left(h(V_nf)(V_{-n}g)\right)
                    =\phi_N\!\left(f\,h(D_n)g\right).
 \quad}
 \tag{4}
\]
The coefficients of \(h\), including any exterior parameters,
are held fixed in the operator substitution. In particular
\[
                  \phi_N((V_nf)(V_{-n}g))=\phi_N(fg).
 \tag{5}
\]
The identity also holds coefficientwise with additional shared
ordinary parameters and after their fixed derivatives.

*Proof.* The bilinear form \(\mathcal B(f,g)=\phi_N(fg)\) is
nondegenerate by (1). Its adjoint is bilinear, without complex
conjugation. Multiplication is self-adjoint for this form, and
\[
 \phi_N((Te_i)e_j)=\mathbf1_{i=j}=\phi_N(e_iTe_j).
\]
Consequently \(V_n\) is self-adjoint for \(\mathcal B\).
Also \(V_nV_{-n}=I\), with the carriers canceling exactly.
Transfer the first \(V_n\) across the pairing:
\[
 \phi_N((V_nf)M_hV_{-n}g)
       =\phi_N(fV_nM_hV_{-n}g).
\]
Since \(M_h=h(C)\), conjugation gives
\(V_nM_hV_{-n}=h(D_n)\). This proves (4), and \(h=1\)
gives (5). These are full quotient identities; no distinct-node
replacement or division by a value has occurred. \(\square\)

Only the matched operators \(V_n,V_{-n}\) were removed in
(5). A vanishing sum of reciprocals among a longer list of
different powers is not an operator cancellation identity.

## 2. Full jets and the two different positive observations

Suppose \(Q^\sharp=Q\), set \(a=V_nQ\), and form the actual product
\[
                  P=\operatorname{can}(a a^\sharp)
                    =\operatorname{can}((V_nQ)(V_{-n}Q)).
 \tag{6}
\]
At every double physical root \(c\),
\[
                P(c)=|a(c)|^2,\qquad
                P'(c)=2\operatorname{Re}(a'(c)\overline{a(c)}).
 \tag{7}
\]
At the odd simple root \(-2\), only its value \(|a(-2)|^2\)
is prescribed and used. Formula (7) is the full product rule.
Canonical reduction changes neither entry of a double jet.
The ordinary product \(a a^\sharp\) is nonnegative on the real
interval, but its canonical representative need not be.

The original closing is exactly
\[
                         \phi_N(P)=\phi_N(Q^2).
 \tag{8}
\]
It is not a positive norm on all inputs. If
\(a=\sum a_j e_j\), then
\[
                    \phi_N(a^\sharp a)
                        =\sum_{j=0}^D\overline{a_j}a_{D-j}.
 \tag{9}
\]
For example \(a=e_0-e_D\) gives \(-2\), whereas
\(e_0+e_D\) gives \(2\), at every \(N\ge2\).
The archived positive Newton Gram instead is
\[
                    \phi_N(a^\sharp Ta)=\sum_{j=0}^D|a_j|^2.
 \tag{10}
\]
The turn in (10) is part of that specified source.

Turning the entire product and then closing is yet another exact
observation. From (1), \(\phi_N(Tp)=p(c_0)\), so
\[
                         \phi_N(TP)=|a(c_0)|^2.
 \tag{11}
\]
This proves nonnegativity of this one endpoint observation, not its
nonvanishing or a norm estimate for \(TP\). In contrast,
\((TP)(c_0)=\phi_N(P)\) is the unturned closing (8).
These two operations are not interchanged.

## 3. Polynomial trace bounds and fixed physical-row values

Use the real norm of the ordinary canonical representative on
\([-2,2]\). For two canonical polynomials,
\[
                  |\phi_N(fg)|\le C N^3
                              \|f\|_{\mathbb R}\|g\|_{\mathbb R}.
 \tag{12}
\]
Indeed the ordinary product has degree at most \(2D\). Its
trigonometric coefficients under \(Z=-2\cos t\) are bounded
by its real norm, and there are \(O(N)\) of them. Exact
full-Hermite Fourier folding has only a fixed number of alias
blocks, with bounded weights in this degree range. Thus
\(\|\operatorname{can}(fg)\|_{\mathbb R}
 \le CN\|f\|_{\mathbb R}\|g\|_{\mathbb R}\).
The highest monomial coefficient of a degree-\(D\) polynomial
on \([-2,2]\) is bounded by its real norm, by its Chebyshev
expansion. Apply the trace formula in (1) to get (12).
This argument uses full-normal folding, not value interpolation.

The pinned operator theorem gives, for every fixed integer \(n\),
\[
                            \|D_n\|\le C_nN^{4|n|}.
 \tag{13}
\]
The case \(n=0\) is included by the bounded multiplication
operator \(C\). The finitely sized case \(N=2\) is included
in the constant.

**Corollary 2.** Let \(n,d\) be fixed and
\(h_N(Z)=\sum_{k=0}^d h_{k,N}Z^k\), with
\(\sum_k|h_{k,N}|\le C_hN^b\). Then
\[
 \left|\phi_N\!\left(h_N(V_nf_N)(V_{-n}g_N)\right)\right|
 \le C_{n,d,h}N^{3+b+4|n|d}
                     \|f_N\|_{\mathbb R}\|g_N\|_{\mathbb R}.
 \tag{14}
\]
In particular this is polynomial whenever the two input norms
are polynomial.

*Proof.* Equation (13) bounds
\(\|h_N(D_n)g_N\|_{\mathbb R}\) by
\(C_{n,d,h}N^{b+4|n|d}\|g_N\|_{\mathbb R}\).
Use (4) and then (12). \(\square\)

For the actual endpoint application take any two fixed products
\[
 f_N=\operatorname{can}\prod_{\ell=1}^{r}
       K_N(2\cosh(\alpha_\ell/N),Z),\qquad
 g_N=\operatorname{can}\prod_{\ell=1}^{s}
       K_N(2\cosh(\beta_\ell/N),Z).
 \tag{15}
\]
Here \(r,s\) and the complex parameter bounds are fixed.
The endpoint-product source proves polynomial real norms,
uniformly on such bounded parameter sets. Consequently (5)
and (14) give polynomial bounds for the literal original
closing and all the stated fixed-degree insertions. This
includes equal real inputs \(f_N=g_N=Q_N\).
No absolute value is inserted inside the source.

There is also a useful value consequence for the next turn.
Put \(P_N^{\rm pair}=\operatorname{can}((V_nf_N)(V_{-n}g_N))\).
For every fixed row cutoff \(j_0\),
\[
 \max_{0\le j\le j_0}
                   |(TP_N^{\rm pair})(c_j)|\le C N^p
 \tag{16}
\]
for all sufficiently large \(N\), uniformly in (15).
Indeed (1) and (4) give the exact formula
\[
 (TP_N^{\rm pair})(c_j)
                   =\phi_N\!\left(f_N K_N(c_j,D_n)g_N\right).
 \tag{17}
\]
Since \(e_k(c_j)=0\) for \(k>j\), the polynomial
\(K_N(c_j,Z)\) has degree \(j\). Its coefficients have
polynomial size for fixed \(j\), directly from the finite
products defining \(e_k\). Corollary 2 proves (16).

These bounds persist under fixed derivatives in the exterior
microscopic parameters: use the identities on a larger bounded
complex parameter set and Cauchy's formula. Derivatives in the
original \(w=2\cosh(\alpha/N)\) cost only fixed powers of \(N^2\).
Indeed the source is even in \(\alpha\), and with
\(\beta=\alpha^2\) the map
\(\beta\mapsto N^2(2\cosh(\sqrt\beta/N)-2)=\beta+O(N^{-2})\)
has a uniformly regular analytic inverse on each fixed smaller
bounded domain for large \(N\). Cauchy estimates in \(\beta\)
give the assertion.
No derivative with respect to the output color is inferred.

## 4. An exact single-kernel calibration

The ordinary evaluation reproducer is
\[
 \delta_w(Z):=(TK_N(w,\cdot))(Z)
                 =\frac{P_N(Z)-P_N(w)}{\eta N^2(Z-w)}.
 \tag{18}
\]
Here the quotient is an ordinary polynomial, also at \(Z=w\).
For a direct verification, the right side has trace one.
If \(p(Z)=p(w)+(Z-w)q(Z)\) has degree at most \(D\), then
\(\deg q<D\) and \(\phi_N(q)=0\), so its pairing with \(p\)
is \(p(w)\). The dual Newton expansion
\(\sum e_j(w)e_{D-j}(Z)\) has the same property; nondegeneracy
of (1) proves (18).

Therefore, at every \(N\ge2\) and every signed integer \(n\),
\[
 \boxed{\quad
 \phi_N((V_nK_N(w,\cdot))(V_{-n}K_N(w,\cdot)))
     =\phi_N(K_N(w,\cdot)^2)
     =\eta\frac{P_N'(w)}{N^2}.
 \quad}
 \tag{19}
\]
Indeed \(\phi_N(K_N(w,\cdot)K_N(z,\cdot))=\delta_w(z)\);
let \(z=w\). With \(w=2\cosh(\alpha/N)\), (19) becomes
\[
                         \eta\,\frac{\sinh\alpha}
                                           {N\sinh(\alpha/N)}.
 \tag{20}
\]
The expression is interpreted by its removable values, in particular
it is exactly \(\eta\) at \(\alpha=0\). It is an entire identity
in \(\alpha\), as follows from the polynomial Chebyshev derivative.
For real \(|\alpha|\le A\),
\[
        1\le \frac{\sinh\alpha}{N\sinh(\alpha/N)}
                  \le \frac{\sinh A}{A},
 \tag{21}
\]
where the last ratio is one when \(A=0\). The lower inequality
uses \(\sinh(Nx)\ge N\sinh x\) for \(x\ge0\). By evenness
assume \(\alpha\ge0\) for the upper inequality; it uses
\(\sinh(\alpha/N)\ge\alpha/N\) and monotonicity of
\(\sinh\alpha/\alpha\). This checks both parities and both
power signs without changing the original factor \(\eta\).

## 5. The retained large-degree channel and source scope

For an arbitrary ordinary output color \(z\), the next turn is
exactly
\[
 (TP_N^{\rm pair})(z)
                     =\phi_N(f_N K_N(z,D_n)g_N).
 \tag{22}
\]
At a physical row its first spectral normal is instead
\[
 (TP_N^{\rm pair})'(c_j)
   =\phi_N\!\left(
      f_N\,[\,\partial_zK_N(z,D_n)\,]_{z=c_j}g_N\right).
 \tag{23}
\]
At a double physical root it has degree exactly \(D-j\):
in \(\sum_k e_k'(c_j)e_k(Z)\), the terms with \(k>D-j\)
vanish because both occurrences \(c_j=c_{D-j}\) are in
the Newton product, whereas \(e_{D-j}'(c_j)\ne0\).
Thus its degree grows linearly with \(N\) even for fixed \(j\),
and (16) does not supply polynomial
first-normal initialization. Likewise a full free kernel or
an original crossing coupon has degree \(O(N)\). Substituting
that degree into (14) does not yield a polynomial bound.
The exact formulas remain valid, with all their normals.

In particular a closing with \(h=R^\sigma\) retains the
operator \(R^\sigma(D_n)\) on the right of (4); it is not
deleted. The identity is also valid for any other specified
closing coupon, with its original scalar coefficients held fixed.
It provides neither a uniform norm bound for the open opposite
product nor a source coefficient on a characteristic branch.
The single-kernel nonvanishing (19)--(21) is a statement about
that exact closing, not an arbitrary attached exterior.

## 6. Coverage and direct sources

The full Newton reality, adjoint identities and distinction between
the indefinite Frobenius closing and the positive turned Gram
are already established in the first source. The new assembly
is (4), its microscopic-product and fixed-degree consequences,
and the explicit identification of the normal insertion left by
the next turn. No new positivity structure is proposed.

Complete direct-source reads are retained at these unchanged pins;
the directly used implications and hashes were rechecked:

* [Original Newton turn, reality and Gram](actual_newton_turn_positive_gram.md),
  SHA256 d8b21fa8db909120035e86e997a0e02cb84f8dce2dcf6fb244bb5c85c17e28a3.
  Its complete text was freshly reread in this author sequence.
* [Exact signed operator conjugation](research_unit_turn_finite_band_branching_operator.md),
  SHA256 31d9f574c7dc3aaac07e4eb50c131b3328be46b3c2a2ef46f9dae7f0c4ddb9cb.
  Its retained complete read and exact real operator bound are used.
* [Actual full endpoint products](research_endpoint_two_half_plane_relative_source.md),
  SHA256 985fa3331379c3877734f28773d314b667ee87fa63314a5ef4513a3fe128d194.
  Its retained complete read, polynomial product norms and full-normal
  Fourier folding are used.

Only written mathematics and source-text/hash reads were used.
No mathematical program, test, numerical experiment or compilation
was run. Frozen notes and public manuscripts are unchanged.
