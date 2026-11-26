# A uniform Gaussian integral for the normalized Conway minimum

23 November 2026. Research note. The manuscripts and earlier final
notes remain unchanged.

The source minimum is a polynomial of degree four, although its number
of variables grows with the quantum level. This permits a uniform
comparison with a positive integral. In particular the inverse
temperature can be chosen as \(N^4\), simultaneously with the quantum
level \(N\). The comparison keeps the Gaussian determinant, whose
dimension-independent bound was proved previously.

This closes the simultaneous-limit qualification in the earlier
Gaussian calculation. It does not evaluate the minimum. An absolute
error of polynomial size can still exceed an exponentially small
minimum, so the result does not prove a volume lower bound.

## 1. The original normalized source

Use the full Newton boundary spaces and the Hilbert--Schmidt budgets
of the [normalized source](research_convex_normalized_conway_source.md).
If the fixed literal Conway expression has \(s\) proper vertices,
put \(D=Ns\), and identify its packets with \(\mathbb C^D\).
Here \(N\ge2\) is the quantum level. All repeated-root derivatives
remain in these spaces.

Write the original normalized maps as \(\Phi_v\), and put
\[
 G_v(x)=\Phi_v((x_c)_c)-x_v,\qquad
 E(x)=\|G(x)\|^2+|cx|^2,\qquad \sigma=\frac1{16}.
 \tag{1}
\]
The row \(c\) is the original marked closing row at the top packet,
divided by its recorded budget. No cap, phase, or framing factor is
changed. Each normalized local tensor has Hilbert--Schmidt norm at
most \(\sigma\). The feasible set \(\mathcal D\) is the product of
the packet unit balls.

The complete source proof and the
[residual-Jacobian calculation](research_conway_residual_jacobian_gaussian_determinant.md)
give the following facts. The minimum \(x_*\) is unique, is the global
minimum on the whole coordinate space, and satisfies
\[
 \|(x_*)_v\|\le\frac{33}{256},\qquad
 e:=E(x_*)\le\sigma^4,\qquad
 I\preceq D_{\mathbb R}^2E(x)\preceq3I\quad(x\in\mathcal D).
 \tag{2}
\]
Let \(H=D_{\mathbb R}^2E(x_*)\) and
\[
 g=\sqrt{\det_{\mathbb R}(H/2)},\qquad
 \gamma=\frac{197}{196}.
\]
The positive square root is understood. The earlier determinant
theorem gives
\[
 \sqrt{1-2^{-22}}\le g\le\gamma.
 \tag{3}
\]
Its Hilbert--Schmidt hypothesis is retained here; this is not an
unproved determinant assertion for a different physical metric.

For a real inverse temperature \(\tau>0\), define the positive
normalized integral, using real Lebesgue measure on \(\mathbb C^D\),
\[
 Z(\tau)=\left(\frac{\tau}{\pi}\right)^D
                \int_{\mathbb C^D}e^{-\tau E(x)}\,dx.
 \tag{4}
\]
Ordering children before parents makes \(DG\) triangular with diagonal
blocks \(-I\). The map \(G\) is a polynomial automorphism, with
real Jacobian one: its inverse is the finite upward recursion
\(x_v=\Phi_v((x_c)_c)-r_v\). In particular,
\[
 \int_{\mathbb C^D}e^{-E(x)}\,dx
 \le\int_{\mathbb C^D}e^{-\|G(x)\|^2}\,dx=\pi^D.
 \tag{5}
\]
The integral in (4) is therefore finite when \(\tau\ge1\).

## 2. An explicit finite-level estimate

Suppose \(\tau\ge2\), and set
\[
 r^2=\frac{8(D+1)\log\tau}{\tau}\le\frac14,\qquad
 \epsilon=\tau^{-D-2},\qquad
 \delta=\tau\left(\frac9{128}r^3+\frac1{1024}r^4\right).
 \tag{6}
\]
The symbol \(r\) here is a positive real radius in the entire packet
direct sum. It is unrelated to the recursion residual \(G(x)\).

**Theorem.** For the original objective (1),
\[
 \boxed{\quad
 e^{-\delta}(1-\epsilon)
 \le g\,e^{\tau e}Z(\tau)
 \le e^\delta+\gamma e^{\sigma^4}\epsilon .
 \quad}
 \tag{7}
\]
Consequently,
\[
 \left|\log Z(\tau)+\tau e+\log g\right|
                  \le\delta+4\epsilon .
 \tag{8}
\]
All quantities refer to the same objective and its original budgets.

**Proof.** Put \(T=DG(x_*)\). Since \(G\) is quadratic, its Taylor
formula is exact:
\[
 G(x_*+h)=G(x_*)+Th+\mathcal Q(h),\qquad
 \|\mathcal Q(h)\|\le\frac1{32}\|h\|^2,\qquad
 \|T\|\le\frac98.
 \tag{9}
\]
Only product vertices contribute to \(\mathcal Q\).
At one such vertex its value is \(\Phi_v(h_L,h_R)\).
The disjointness of sibling pairs bounds the direct-sum norm by
\(\sigma\|h\|^2/2\), giving (9).

The linear term in \(E\) vanishes at the interior minimum.
Its quadratic term includes
\(2\operatorname{Re}\langle G(x_*),\mathcal Q(h)\rangle\);
that term belongs to \(H\), and must not be discarded.
The remaining terms are precisely
\[
 E(x_*+h)=e+\tfrac12H[h,h]
       +2\operatorname{Re}\langle Th,\mathcal Q(h)\rangle
       +\|\mathcal Q(h)\|^2.
 \tag{10}
\]
Thus on the radius-\(r\) ball the absolute value of the last two
terms, multiplied by \(\tau\), is at most \(\delta\).
This ball is contained in \(\mathcal D\), since
\(r\le1/2\) and \(33/256+1/2<1\).

Consider the probability density
\[
 d\mu(h)=g\left(\frac{\tau}{\pi}\right)^D
                   e^{-\tau H[h,h]/2}\,dh .
 \tag{11}
\]
Diagonalizing the real positive matrix \(H/2\succeq I/2\) and
integrating each one-dimensional Gaussian gives
\[
 \mathbb E_\mu e^{\tau\|h\|^2/4}\le2^D .
 \tag{12}
\]
Indeed each of the \(2D\) real coordinates contributes a square-root
factor at most \(\sqrt2\). Markov's inequality, which follows by
integrating the pointwise indicator bound, now yields
\[
 \mu\{\|h\|\ge r\}
 \le2^De^{-\tau r^2/4}
 =2^D\tau^{-2(D+1)}
 \le\epsilon .
 \tag{13}
\]
The contribution of the radius-\(r\) ball to the middle quantity
in (7) is therefore between
\(e^{-\delta}(1-\epsilon)\) and \(e^\delta\).

It remains to bound the original integral outside that ball.
For \(x\in\mathcal D\), segment integration of the lower Hessian
bound gives \(E(x)\ge e+\|x-x_*\|^2/2\).
For \(x\notin\mathcal D\), choose a vertex outside its packet ball
whose children are inside theirs. Its normalized output has norm
at most \(\sigma\), so
\[
 E(x)>(1-\sigma)^2=\frac{225}{256}.
\]
Since \(e\le\sigma^4\) and \(r^2/2\le1/8\), this also exceeds
\(e+r^2/2\). Consequently that same energy gap holds on the
entire complement of the radius-\(r\) ball.

Using (5), its contribution to \(e^{\tau e}Z(\tau)\) is at most
\[
 \tau^D
   \exp\left\{e-\frac{\tau-1}{2}r^2\right\}
 \le e^{\sigma^4}\tau^{-D-2}.
 \tag{14}
\]
The last inequality uses \((\tau-1)/\tau\ge1/2\) in (6).
Multiplication by \(g\le\gamma\) proves (7).

Finally \(\epsilon\le1/8\) and
\(\gamma e^{\sigma^4}<4\). Taking logarithms of (7), using
\(-\log(1-\epsilon)\le2\epsilon\) and
\(\log(1+u)\le u\) for \(u\ge0\), proves (8).
This completes the proof.

## 3. Simultaneous quantum level and temperature

Fix the literal expression, hence \(s\). Take \(\tau_N=N^4\).
For all sufficiently large \(N\), the radius condition in (6)
holds. Its error satisfies
\[
 \delta_N
 \le\frac{9\sqrt2}{8}
       \frac{((Ns+1)\log\tau_N)^{3/2}}{\sqrt{\tau_N}}
      +\frac1{16}
       \frac{((Ns+1)\log\tau_N)^2}{\tau_N}
 =O_s\left(\frac{(\log N)^{3/2}}{\sqrt N}\right).
 \tag{15}
\]
In particular, with the same \(e_N\) and \(g_N\) as in (2)--(3),
\[
 \boxed{\qquad
 Z_N(N^4)=\frac{e^{-N^4e_N}}{g_N}\,(1+o(1)).
 \qquad}
 \tag{16}
\]
The error tends to zero as \(N\) and \(\tau_N\) grow together.
More generally (7) applies to any temperature sequence satisfying
its radius condition, with a relative error tending to zero whenever
\((D+1)^3(\log\tau)^3/\tau\to0\).

If \(B_N\) is the unchanged product of all source budgets, the
original comparison remains
\[
 B_N^2e_N\le |K_N|^2\le\gamma B_N^2e_N.
 \tag{17}
\]
Thus (16) gives a controlled positive integral for this particular
minimum. It does not give its value from the geometry.
For example, (8) estimates \(e_N\) with an absolute error
\((\delta_N+4\epsilon_N)/N^4\) after the determinant is retained.
Such an error need not be small relative to \(e_N\).
If \(e_N\) is exponentially small, the determinant term and this
absolute error cannot be omitted when extracting its rate.
No nonzero geometric coefficient, arbitrary-short-filling lower
bound, or finite-exception volume theorem follows from (16).

## Complete sources and coverage

Both complete texts were read at the matching versions below.
The finite-level tail bounds and the simultaneous estimate are
proved in Sections 2--3.

| Source | SHA-256 |
|---|---|
| [Normalized source and its exact budgets](research_convex_normalized_conway_source.md) | 6b89b4c6a67ef7a32cc41a5966c650f32de65d284ae7b70d94a71bddba21df3c |
| [Residual automorphism and Gaussian determinant](research_conway_residual_jacobian_gaussian_determinant.md) | db22b86a97302926fed77385f82ff2284109e288ec3d03dd99538d3671c926b2 |

The full uniform-physical-quartic note was read for coverage at
39895b430535f565d30133b46ef57f67589207bc83f40597ffe96e2ce79bbda8.
It uses different budgets and is not assigned the determinant bound
(3) here. The previous Gaussian note proves its Laplace limit only
at each fixed quantum level; (7) supplies the missing uniform error.
No general novelty is claimed for Laplace's method, Gaussian tails,
or Taylor's formula.

Only written mathematics and text/hash operations were used.
No mathematical program, numerical experiment, build, git action,
or earlier-final edit was performed.
