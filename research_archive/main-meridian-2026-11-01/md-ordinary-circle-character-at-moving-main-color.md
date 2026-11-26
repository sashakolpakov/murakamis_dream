# The ordinary auxiliary circle at a moving main meridian

Private source adapter, 1 November 2026. No repository file is changed.

The ordinary auxiliary circle keeps the same Chebyshev polynomial when the main target colors move. This statement concerns the literal encircling operator, including its auxiliary pivotal trace. It does not assert that the whole tangle source has a uniform geometric bound.

## 1. Exact operator and its full-normal specialization

Fix \(q=e^{\pi i/N}\), \(Q=q^2\), and an ordinary auxiliary module \(A_j\), \(1\le j\le N\). Its weights are \(j-1-2a\), \(0\le a<j\), and its closing pivot is the actual
\[
g_j=K_j^{1-N}=(-1)^{j-1}K_j.
\tag{1}
\]
Use the same block-monodromy braid and closing direction as in `notes/actual_crossing_circle_source_and_filling.md`, Section 1. No division by the auxiliary dimension is made. The two target factors may now have independent nilpotent highest roots \(x_1,x_2\); after the calculation they may be specialized to the equal or opposite roots required by the typed compiler.

The exact result is
\[
\boxed{\quad L_j=(-1)^{j-1}U_{j-1}(\Omega/2).\quad}
\tag{2}
\]
Here \(U_0=1\), \(U_1(\Omega/2)=\Omega\), and
\(U_{j+1}=\Omega U_j-U_{j-1}\). The polynomial in (2) is independent of the target roots.

To prove this without discarding repeated channels, first choose the two target roots independently in the generic set where their tensor product is the direct sum of \(N\) distinct typical highest-weight summands. This is the generic highest-vector decomposition used in the intrinsic cut/Casimir calculation. On a summand with highest root \(w\), choose the block-braiding order in which the first nilpotent factor acts by the target raising operator. It kills the highest vector. In the returning crossing, a positive lowering transfer cannot contribute to its highest coefficient. The two Cartan factors and the standard auxiliary pivot therefore give exactly
\[
\sum_{a=0}^{j-1}(qw)^{j-1-2a}
=U_{j-1}\!\left(\frac{qw+q^{-1}w^{-1}}2\right).
\tag{3}
\]
The loop is an intertwiner, so its action on that simple summand is determined by this highest coefficient. The Casimir eigenvalue there is \(qw+q^{-1}w^{-1}\). Distinctness of the generic Casimir values gives the full matrix identity with standard pivot \(K_j\); (1) inserts its required sign.

The actual matrix entries are regular Laurent functions of the independent nonzero target roots. In the finite mixed universal crossings only auxiliary transfer indices below \(j\le N\) occur; their factorial denominators are \([r]!\) with \(r<N\), all nonzero at this root. The target nilpotent matrices have polynomial raising coefficients in their highest roots and inverse roots. Hence the identity extends from the generic set to every specialization of these roots. In particular it holds at
\[
x=-q^{-1}q^s,\quad y=-q^{-1}q^{-s},
\]
for both equal-color and opposite-color target pairs, including the persistent double Casimir nodes of the latter. This is continuation of the full physical matrix identity, not interpolation of its distinct values after specialization.

For the other ordered target orientations, transport this same loop by the actual rigid dualities. The Casimir is fixed by the antipode and is natural under the braiding carriers. Therefore (2) transports as the same polynomial in the corresponding target Casimir. No replacement of the main modified cut, no new framing adjustment, and no independent carrier scalar is introduced. This assertion keeps the prescribed encircling direction and framing; it does not replace an unrelated inverse braid word by the displayed word without its geometric duality.

## 2. Polynomial size of this specified coupon

The polynomial in (2) has degree \(j-1<N\), so it is already its canonical representative in either target quotient. On the complete real interval,
\[
\|U_{j-1}(z/2)\|_{[-2,2]}\le j\le N.
\tag{4}
\]
Markov's inequality bounds its derivative by a fixed polynomial in \(N\). Thus its full complete spectral-jet norm is polynomial, uniformly over all auxiliary colors \(1\le j\le N\). Its fixed-polynomial coefficients have no hidden main-meridian deformation. This is stronger than a claim about its values alone, but it does not assert that the Newton coefficient norm is polynomial.

## 3. The precise coefficient-cone consequence

Suppose an actual typed input has fixed canonical polynomial \(E_s\), and a fixed-power crossing coupon \(R_s^\varepsilon\) has the already established polynomial canonical norm on a fixed disk before the first ordinary-color resonance. Let
\[
F_s=R_s^\varepsilon L_jE_s
\]
be multiplied in its appropriate same-color quotient. Fixed-degree Chebyshev folding gives a polynomial cost for reducing this finite product. The top-coefficient functional and full spectral norm are polynomially related on canonical representatives. Consequently
\[
|\phi_s(e_k*_sF_s)|
\le C N^C\|e_k\|_{\mathrm J}\|E_s\|_{\mathrm J},
\tag{5}
\]
uniformly in \(j\), with constants allowed to depend on the fixed crossing power and parameter disk. The polynomial factors in this step must use the actual physical crossing bound; they are not deduced from an arbitrary moving-basis interpolation through a resonance.

The exact fixed-frame turn and the unchanged Frobenius metric give its output coefficient
\[
[e_k]\mathscr T_s^{\mathrm{fix}}F_s
=\frac{\gamma_N(s)W_{d-k}(s)}{H_N(s)}\,
     \phi_s(e_k*_sF_s).
\tag{6}
\]
The prefactor is uniformly bounded on every fixed disk \(|s|\le R<1\). Since the complete basis satisfies
\[
\|e_k\|_{\mathrm J}\le\operatorname{poly}(N)
\begin{cases}
\exp\{Ng(k/N)\},&k\le\lfloor d/2\rfloor,\\
1,&k>\lfloor d/2\rfloor,
\end{cases}
\tag{7}
\]
(5)–(7) supply the same low/high coefficient cone for this decorated module when \(\|E_s\|_{\mathrm J}\le\exp\{N(F+o(1))\}\).

This is an operator coefficient upper bound at the supplied input budget \(F\). It does not identify that budget with the action of a filled knot, prove a far-auxiliary-color deficit, or establish a limiting regular main-meridian profile. Those require the additional source estimates for the full contraction.
