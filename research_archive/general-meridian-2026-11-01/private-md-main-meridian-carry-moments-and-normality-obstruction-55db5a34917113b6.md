# Bounded carries, signed moments, and the missing normal-family estimate

31 October 2026. Private continuation only. The input is the exact
filter in `/private/tmp/md-main-meridian-finite-source-and-regular-filter-inventory.md`,
together with the existing regular-period and scaled-profile notes.
No repository or public file is changed.

This report proves a finite signed-moment sufficient condition for
local boundedness of the actual regular microscopic profile. It also
shows that bounded carry width, the complete scalar rate, the actual
root operator and affine source, all color data, and all Mellin
quantum jets do not alone imply that boundedness. The counterexample
is a comparison family, not a second actual knot invariant: it does
not preserve the literal main-meridian finite-cut quantum-normal lift.

## 1. The all-integer filter and the carry decomposition

Fix a knot and a braid presentation. Let $q_N=e^{\pi i/N}$,
$Q_N=q_N^2$, $Y=M^2$, and let $f_N(Y)$ be its actual reduced ADO
Laurent polynomial. Write $K_N=f_N(1)$. For the knot class under
consideration, the proved scalar theorem gives

\[
 N^{-1}\log|K_N|\longrightarrow v>0.
 \tag{1}
\]

In particular $K_N\ne0$ for all sufficiently large $N$. All following
normalized statements refer to those levels.

Let $I_N$ interpolate at the nontrivial $N$th roots into degree
at most $N-2$, and put

\[
 S_N(Y)=\frac{Y^N-1}{Y-1},\qquad
 P_N=I_Nf_N,\qquad
 R_N(Y)=\frac{f_N(Y)-P_N(Y)}{S_N(Y)}.
 \tag{2}
\]

This is the original ordinary-color regularization. To check its
monomial rule, divide an arbitrary integer exponent as
$\ell=kN+t$, $0\le t<N$, and write $U=Y^N$. On the interpolation
points $Y^\ell$ equals $Y^t$. The interpolant is $Y^t$ if
$t\le N-2$, and is $Y^{N-1}-S_N$ if $t=N-1$. Therefore

\[
 \frac{Y^\ell-I_N(Y^\ell)}{S_N(Y)}
   =Y^t(Y-1)G_k(U)+\mathbf1_{t=N-1},\qquad
 G_k(U)=\frac{U^k-1}{U-1}.
 \tag{3}
\]

For negative $k$, the exact Laurent formula is
$G_k=-\sum_{j=k}^{-1}U^j$. Thus, for example,
$\mathcal D_N(Y^{-1})=Y^{-1}$ and
$\mathcal D_N(Y^{-N})=-Y^{-N}(Y-1)$. No sampled zero is divided
in this argument.

Write the finite carry decomposition uniquely as

\[
 f_N(Y)=\sum_{k\in\mathcal K}Y^{kN}p_{k,N}(Y),\qquad
 \deg p_{k,N}<N,
 \tag{4}
\]

padding unused carries with zero. The exact cut-source degree bound
allows one fixed finite set $\mathcal K\subset\mathbb Z$ for all
$N$. If the braid has $b$ strands and $L$ crossings, its exponents
obey

\[
 -\frac{(N-1)(L+b-1)}2\le\ell
        \le\frac{(N-1)(L-b+1)}2.
 \tag{5}
\]

This remains true before cancellations in the finite q-binomial
expanded cut state. It does not bound the absolute values of its
signed coefficients relative to $K_N$.

At every root point, (4) has the same values as
$p_{\Sigma,N}=\sum_kp_{k,N}$, whose degree is below $N$.
Interpolating those values gives the exact identities

\[
 \sum_kp_{k,N}(Y)=P_N(Y)+R_N(1)S_N(Y),
 \tag{6}
\]

\[
 \boxed{\quad
 R_N(Y)=R_N(1)+(Y-1)
                \sum_kG_k(Y^N)p_{k,N}(Y).
 \quad}
 \tag{7}
\]

For (6), the difference from $P_N$ is a constant times $S_N$;
its leading coefficient is the sum of the $Y^{N-1}$ carry
coefficients, which is $R_N(1)$ by (3). Subtract (6) from (4),
use $U^k-1=(U-1)G_k(U)$, and divide by $S_N$ to obtain (7).
These formulas retain all negative and positive carries.

## 2. A finite set of quantitative signed-moment estimates suffices

Use the microscopic coordinate $Y=e^{z/N}$ and the actual centered
regular profile

\[
 \rho_N(z)=e^{\alpha_Nz}\frac{NR_N(e^{z/N})}{K_N},
 \qquad \alpha_N=\frac{N-1}{2N}.
 \tag{8}
\]

Define $a_{k,N}(z)=p_{k,N}(e^{z/N})/K_N$ and
$c_N=NR_N(1)/K_N$. If $s=|\mathcal K|$, define the signed carry
moments

\[
 M_{j,N}(z)=\sum_{k\in\mathcal K}k^j a_{k,N}(z),
 \qquad 0\le j<s.
 \tag{9}
\]

They are central-carry moments, not derivatives in the quantum
parameter and not absolute coefficient moments. Their definition
uses the unique Euclidean carry representatives in (4).

The zeroth moment is already controlled. Set
$\pi_N(z)=P_N(e^{z/N})/K_N$ and
$H_N(z)=\sinh(z/2)/(N\sinh(z/(2N)))$, with its entire removable
values. Equation (6) gives

\[
 M_{0,N}(z)=\pi_N(z)+c_Ne^{\alpha_Nz}H_N(z).
 \tag{10}
\]

The ordinary-color bounds and (1) imply $\pi_N\to0$ locally
uniformly with every fixed derivative and $c_N\to1$. Thus
$M_{0,N}$ is locally uniformly bounded and converges to
$(e^z-1)/z$, with value $1$ at zero.

**Signed-moment criterion.** If the remaining $s-1$ functions
$M_{j,N}$, $1\le j<s$, are locally uniformly bounded on a fixed
complex disk, then so is $\rho_N$ there. Only the number of these
estimates, not their truth, follows from the finite carry width.

For the proof, the fixed matrix $V_{j,k}=k^j$ is an invertible
Vandermonde matrix. Hence the $a_{k,N}$ are fixed linear
combinations of the moments, with coefficients independent of
$N$. Equation (7) reads

\[
 \rho_N(z)=e^{\alpha_Nz}\left[
 c_N+N(e^{z/N}-1)
             \sum_kG_k(e^z)a_{k,N}(z)\right].
 \tag{11}
\]

On $|z|\le R$, the finitely many functions $G_k(e^z)$ are bounded
uniformly, including negative $k$ and $e^z=1$, and
$N|e^{z/N}-1|\le R e^{R/2}$ for $N\ge2$. This proves the
criterion with an explicit constant depending only on $R$ and
$V^{-1}$. Cauchy's inequality then bounds every fixed derivative
on a smaller disk.

If the moments converge locally uniformly, the same fixed inverse
gives limits $a_k$, and (11) gives the actual limit formula

\[
 \rho(z)=e^{z/2}\left[1+z\sum_kG_k(e^z)a_k(z)\right],
 \qquad \sum_ka_k(z)=\frac{e^z-1}{z}.
 \tag{12}
\]

Weyl symmetry makes any actual resulting limit even, as in the
existing scaled-profile theorem. Neither boundedness nor
convergence of the nonzero carry moments has been established by
the scalar volume theorem.

A still weaker exact target is the single signed carry combination
$\sum_kG_k(e^z)a_{k,N}(z)$. Its local boundedness is equivalent
to that of $\rho_N$: (11) proves one direction, and division on
a fixed surrounding circle followed by the maximum principle
proves the other, since $N(e^{z/N}-1)/z$ is uniformly a unit on
each fixed disk for large $N$. The moment criterion is stronger
but splits this target into a fixed finite number of explicitly
defined signed estimates. Values of those moments only at $z=0$
are not the asserted disk estimates.

## 3. Algebraic uniqueness does not bound these moments

The existing central-freedom construction can be sharpened into
an explicit failure of local boundedness while retaining all
color data and their Mellin quantum jets. Let $a_N$ be any scalar
and define the comparison family

\[
 h_N(U)=1+a_N(U+U^{-1}-2),\qquad
 \widetilde f_N(Y)=h_N(Y^N)f_N(Y).
 \tag{13}
\]

The multiplier has $h_N(1)=1$ and is reciprocal in $U$. It is
never the zero Laurent polynomial. Since every root shift fixes
$U$, it commutes with every specified root difference operator.
Thus $\widetilde f_N$ and $f_N$ have the same entire all-level
annihilator ideal, meaning the fixed Ore operators evaluated at
the roots $q_N$, not a supplied off-root finite-cut lift. The reverse
inclusion follows as well: if an
operator kills $\widetilde f_N$, its product with the nonzero
$h_N$ shows that it kills $f_N$ as a rational function at that
level. No operator is reconstructed from altered scalar values.

Every ordinary and complete orbit value is unchanged. Therefore
the fixed-color functions $C_r(q)$, their generic recurrence,
their finite-start Mellin source, and all their quantum jets are
unchanged. The actual interpolant $P_N$ is unchanged. The new
regular remainder is exactly

\[
 \widetilde R_N=h_NR_N+(h_N-1)p_N,
 \qquad p_N=P_N/S_N.
 \tag{14}
\]

This is Laurent polynomial, because $(h_N-1)/(U-1)$ is Laurent
polynomial. If $A_NR_N=b_N$ and $A_Np_N=-b_N$ are the original
rootwise affine equations, then
$A_N\widetilde R_N=h_Nb_N-(h_N-1)b_N=b_N$ exactly.
The ordinary source, including all its coefficients, is retained.

Since $h_N(U)-1$ vanishes to order two at $U=1$, (13) even
preserves the first meridian jet of $f_N$ at every root orbit
point. In particular it preserves $R_N$ at every one of those
points, the complete derivative of $R_N$, and the entire marked
ramified normal fibre $(a_0,b_0)$ of $(Y-1)f_N$. These observations
do not extend to its whole central profile or to the same
off-root main-meridian quantum-normal lift.

To compute the profile change, put
$g_N(z)=f_N(e^{z/N})/K_N$. The exact scaled identity is
$g_N=H_N\rho_N+\pi_N$. Here $g_N(0)=1$,
$H_N(0)=1$, and $H_N'(0)=0$. Equation (13) gives
$\widetilde g_N(z)=[1+a_N(e^z+e^{-z}-2)]g_N(z)$, while
$\pi_N$ is unchanged. Differentiating twice at zero yields

\[
 \boxed{\quad
 \widetilde\rho_N''(0)=\rho_N''(0)+2a_N.
 \quad}
 \tag{15}
\]

The equal complete values and first derivatives ensure that no
other term survives in this difference. Equivalently, divide
$\widetilde g_N-g_N$ by the same unit $H_N$ near zero.

Choose

\[
 a_N=N-\tfrac12\rho_N''(0).
 \tag{16}
\]

Then $\widetilde\rho_N''(0)=2N$. Cauchy's derivative estimate
proves that the modified profiles cannot be locally uniformly
bounded on any disk centered at zero. For actual cyclotomic
coefficients these $a_N$ are algebraic scalars; no transcendental
growth factor is needed for the example. Finitely many small
levels can be left unchanged.

The carry width in (13) grows by only two: multiplication by
$U+U^{-1}-2$ shifts the original carries by $-1,0,1$.
Thus a fixed finite carry bound does not prevent the example.
Even the coarse explicit degree enclosure (5) cannot by itself
exclude it. If desired, choose a fixed braid presentation with
two inserted cancelling crossing pairs. Its crossing count rises
by four, so each side of (5) acquires $2(N-1)$ of slack, at
least $N$ for every $N\ge2$. The comparison polynomial (13)
then fits that same presentation's enclosure. This changes no
knot, color value, or invariant; it only shows the limitation of
the enclosure as a proposed uniqueness/conditioning hypothesis.

The example is not claimed to be the actual finite-cut state of
that presentation. Its coefficients do not preserve the literal
crossing weights or the supplied whole main-meridian preoperator
and normal source. Those are precisely the data a successful
analytic transport must still use. The example refutes an
inference from the weaker listed algebraic data, not a theorem
about the fully specified knot family.

## 4. Why the existing quantum-jet theorem does not repair the estimate

The bounded-jet Mellin theorem fixes the rational function
$Z_N(X)$ from the actual color recurrence, its prefix, pole
lattice, and a bounded number of quantum jet levels. The families
in (13) have exactly the same $C_r(q)$, so they produce the same
$Z_N$ and pass all of those tests. They are not competing Mellin
solutions. They differ in the unsampled central meridian
direction, and (15) makes that difference quantitatively visible.

This agrees with the earlier polarization calculation: rational
main-meridian functions vary $Y^N$ with $T^N=1$, whereas the
rational Mellin realization varies $X^N$ with $S_X^N=1$.
Their finite Fourier correspondence retains the orbit and residue
numerator, not the whole main-meridian normal profile.

The source-corrected main quantum-normal theorem can prohibit
nonconstant central multipliers when its selected symbol is
nonzero and both sections lift through the same whole preoperator.
That theorem uses different information from the color/Mellin
jets just discussed. Our comparison family does not assert such
a lift. Even a uniqueness theorem for a fully specified lift
would still require quantitative conditioning to turn an
approximate or estimated source into uniform bounds for (9).

The finite-carry formulation therefore leaves a concrete analytic
target: bound the actual signed functions $M_{j,N}$ on a fixed
microscopic disk, or directly bound the single combination in
(11), with constants relative to $K_N$. Termwise polynomial
filter bounds or an absolute cut-state sum do not give this
relative control. No such estimate is inferred here.

## 5. A quantitative normal-connection criterion

The source-corrected connection does give a useful conditional
route, provided its actual marked lattice is controlled uniformly.
Here is a precise elementary version. For all sufficiently large
$N$, suppose that on a fixed microscopic disk $|z|<R$ the actual
source-normal section has coordinates $v_N(z)$ in a holomorphic
frame of rank at most a fixed $r$. Require that these are frames
of the supplied meridian source problem, with its original
normalization, and that the connection equation and the scalar
observation take the form

\[
 v_N'(z)=A_N(z)v_N(z),\qquad
 \rho_N(z)=\ell_N(z)v_N(z)+e_N(z).
 \tag{17}
\]

Assume on that disk, in fixed compatible norms,

\[
 \|A_N\|\le C,\qquad \|\ell_N\|\le C,\qquad
 \|e_N\|\le C,\qquad \|v_N(0)\|\le C.
 \tag{18}
\]

Then the profiles are locally uniformly bounded, with
$\|\rho_N(z)\|\le C^2 e^{C|z|}+C$. Indeed integrate the
holomorphic linear equation along the radial segment from zero
to $z$ and apply the elementary integral Gronwall inequality.
The bound is independent of $N$ and the actual rank. Cauchy's
inequality gives all fixed scalar derivative bounds on smaller
disks. This proves normality, not uniqueness of a subsequential
limit; convergence of $A_N$, the observation and the normalized
initial vector would also give convergence by the same integral
equation.

For the source-corrected construction, an invertible
kernel-to-cokernel symbol in uniformly controlled lattice frames
converts its first-order equation into (17). The coordinate
$U=e^z$ absorbs the $U\partial_U$ derivative. One must bound
the inverse symbol, the remaining connection/source matrices,
the scalar observation and the normalized initial vector; all of
these enter (18). An arbitrary singular change of frame can
destroy these bounds, which is why the actual marked lattice
is part of the criterion. A single nonzero selected symbol is
enough for the central-uniqueness argument but is not, by itself,
the stated matrix inverse estimate. The Mellin observable
cannot be substituted for this meridian lattice without the
unproved source-retaining comparison.

Thus (18) is one concrete operator-side sufficient condition,
while (9) supplies a direct finite-source condition. Neither is
an automatic consequence of algebraic uniqueness, bounded
quantum-jet order, or the scalar volume limit.
