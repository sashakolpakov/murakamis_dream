# A quadratic minimum for the original closing functional

22 November 2026. This note simplifies the quadratic formulation of the
finite Burau source. Only the original complete-color closing is needed.
The resulting minimum approximates the squared modulus of the original
Kashaev invariant within a prescribed factor. Ordinary colors, their
growth bounds, and an all-color frame are not used in this comparison.

The statement is at each finite level. Estimating the minimum at the
hyperbolic-volume scale remains an open problem.

## 1. The specified finite source

Fix a braid word whose closure is a knot. Let \(k\ge1\) be its number
of crossing occurrences, \(b\) its number of strands, and \(w\) its
writhe. Keep the original reduced invariant and framing convention of
the [orthogonal marked row model](research_burau_orthogonal_marked_row_model.md).
At level \(N\ge2\), that model supplies explicit data
\[
 D=N^{2k},\qquad L=k(N-1)+1,\qquad Q=e^{2\pi i/N},
 \qquad \zeta=Q^{(b-1+w)/2},
\]
\[
 C\in\operatorname{End}(\mathbb C^D),\quad C^L=0,
 \qquad \|e\|=1,\quad \|H\|=N^k,
 \qquad K_N=\zeta e^*(I-C)^{-1}H.
 \tag{1}
\]
Here \(e\) is a real coordinate vector. The matrix \(C\) is exactly
the compressed ordered operator of that model. The column \(H\)
includes the phases of its prescribed terminal columns. These data
are defined without supplying the value of \(K_N\).

Put
\[
 T=C^*,\qquad A=I-T,\qquad
 G=\sum_{r=0}^{L-1}(T^*)^rT^r,\qquad
 h=N^{-k}H,\qquad b_0=N^k e.
 \tag{2}
\]
Thus \(G\succeq I\), \(h\) is a unit vector, and
\[
 s:=h^*A^{-1}b_0=\zeta\overline{K_N}.
 \tag{3}
\]
The symbol \(s\) is used in the proof; it is not an input to the
minimization below. For a positive Hermitian matrix \(M\), write
\(\|x\|_M^2=x^*Mx\). All inner products are the actual orthogonal
row-model inner products.

## 2. A single scalar penalty suffices

Choose any real \(\tau\ge1\), and set
\[
 M=\tau L G,\qquad
 J_\tau(x)=\|Ax-b_0\|_M^2+|h^*x|^2,
 \qquad \mu_\tau=\min_{x\in\mathbb C^D}J_\tau(x).
 \tag{4}
\]
This is an unconstrained real quadratic minimization. There is one
complex closing component, rather than \(N\) color components.

**Proposition 1.** Define the real number
\[
 \eta_\tau=h^*A^{-1}M^{-1}A^{-*}h,
 \qquad A^{-*}=(A^*)^{-1}.
 \tag{5}
\]
Then \(0<\eta_\tau\le1/\tau\), and
\[
 \mu_\tau=\frac{|K_N|^2}{1+\eta_\tau},\qquad
 \mu_\tau\le |K_N|^2\le(1+\tau^{-1})\mu_\tau.
 \tag{6}
\]
These statements hold at every level, including even and composite
levels, and when \(K_N=0\). In particular \(\mu_\tau=0\) if and
only if \(K_N=0\).

**Proof.** The finite inverse and Cauchy--Schwarz give, for every \(r\),
\[
 |h^*A^{-1}r|^2
 =\left|\sum_{j=0}^{L-1}h^*T^jr\right|^2
 \le L\sum_{j=0}^{L-1}\|T^jr\|^2
 =L\|r\|_G^2=\tau^{-1}\|r\|_M^2.
 \tag{7}
\]
This proves the upper bound in (5). Strict positivity follows from
invertibility of \(A\) and \(M\) and from \(h\ne0\).
Substitute \(r=Ax-b_0\) into (4). With \(a=h^*A^{-1}\), the
objective becomes
\[
 r^*Mr+|s+ar|^2.
\]
Its unique minimizer and value, obtained by completing the square, are
\[
 r_*=-\frac{M^{-1}a^*s}{1+\eta_\tau},\qquad
 x_*=A^{-1}(b_0+r_*),\qquad
 \mu_\tau=\frac{|s|^2}{1+\eta_\tau}.
 \tag{8}
\]
Equations (3) and (5) prove (6). Uniqueness also follows because
\(A^*MA\) is positive definite. \(\square\)

For example, the finite choice \(\tau=N\) gives
\[
 \mu_N\le |K_N|^2\le(1+N^{-1})\mu_N.
 \tag{9}
\]
No penalty limit is needed. The extra penalty coefficient \(NL\)
is polynomial in \(N\) for the fixed word. For any specified \(V>0\),
\[
 \frac{\pi}{N}\log\mu_N\longrightarrow V
 \quad\Longleftrightarrow\quad
 \frac{2\pi}{N}\log|K_N|\longrightarrow V.
 \tag{10}
\]
One can use \(\tau=1\) instead: the constant comparison factor two
already suffices for (10). Zeros agree by Proposition 1, so convergence
to a finite positive \(V\) forces eventual nonvanishing on either side.

The scalar closing at the minimizer also preserves the original phase:
\[
 h^*x_* =\frac{s}{1+\eta_\tau},\qquad
 K_N=\zeta(1+\eta_\tau)\overline{h^*x_*}.
 \tag{11}
\]
The correction in this formula is a positive real number. This does
not identify that phase with a geometric action; it records exactly
which complex observation the minimization retains.

## 3. Orthogonality in the affine residual space

There is a direct orthogonal explanation of (6). The affine residual
map and its linear part are
\[
 F(x)=\binom{M^{1/2}(Ax-b_0)}{h^*x},\qquad
 B=\binom{M^{1/2}A}{h^*}.
 \tag{12}
\]
The image of \(B\) has complex codimension one in
\(\mathbb C^D\oplus\mathbb C\). Its orthogonal complement is
spanned by
\[
 n=\binom{-M^{-1/2}A^{-*}h}{1},\qquad
 B^*n=0,\quad \|n\|^2=1+\eta_\tau,
 \quad n^*F(x)=s.
 \tag{13}
\]
The last identity holds for every trial field \(x\). Minimization
removes the component in the image of \(B\), leaving its normal
component of squared norm \(|s|^2/(1+\eta_\tau)\).
This is orthogonality after retaining the entire source and closing.
No projection is inserted between the ordered crossing operators.
Constructing \(n\) still involves the full adjoint inverse.

## 4. A lower bound from any trial field

The minimum is the solution of one positive definite linear system:
\[
 (A^*MA+hh^*)x_*=A^*Mb_0.
 \tag{14}
\]
Its conditioning in the specified metric gives a certificate that
does not require an exactly feasible adjoint solution. Define
\[
 g(x)=A^*M(Ax-b_0)+h(h^*x).
 \tag{15}
\]
This is the complex half-gradient of \(J_\tau\): its real differential
at a displacement \(v\) is \(2\operatorname{Re}(g(x)^*v)\).

**Proposition 2.** For every \(x\in\mathbb C^D\),
\[
 \max\{0,J_\tau(x)-L^2\|g(x)\|_{M^{-1}}^2\}
       \le |K_N|^2\le(1+\tau^{-1})J_\tau(x).
 \tag{16}
\]
The estimate requires no ordinary-color subtraction.

**Proof.** Nilpotence gives
\[
 T^*GT=G-I,\qquad
 \|T\|_G\le1,\qquad \|A\|_G\le2,
 \qquad \|A^{-1}\|_G\le L.
\]
The same operator-norm statements hold in the scalar multiple \(M\).
Since \(M\succeq\tau L I\), in coordinates \(z=M^{1/2}x\) the
complex quadratic Hessian is
\[
 \mathcal H=M^{-1/2}(A^*MA+hh^*)M^{-1/2},
 \qquad
 L^{-2}I\preceq\mathcal H
       \preceq(4+(\tau L)^{-1})I.
 \tag{17}
\]
Writing \(\widetilde g=M^{-1/2}g(x)\), exact quadratic completion
therefore yields
\[
 0\le J_\tau(x)-\mu_\tau
   =\widetilde g^*\mathcal H^{-1}\widetilde g
   \le L^2\|g(x)\|_{M^{-1}}^2.
 \tag{18}
\]
Combine this with (6) and \(\mu_\tau\le J_\tau(x)\).
\(\square\)

Thus a geometric trial field would suffice if its energy had the
required volume rate and, for some fixed \(0\le\theta<1\),
\[
 L^2\|g(x)\|_{M^{-1}}^2\le\theta J_\tau(x).
 \tag{19}
\]
Indeed (16) would sandwich \(|K_N|^2\) between constant multiples
of that energy. No family satisfying these two estimates for arbitrary
fixed short partial fillings has been constructed here.

The exact dual has only one complex scalar at the closing. For any
\(u\in\mathbb C^D\) and \(y\in\mathbb C\) satisfying \(A^*u=hy\),
\[
 d(u,y)=2\operatorname{Re}(u^*b_0)-u^*M^{-1}u-|y|^2
       \le\mu_\tau\le |K_N|^2.
 \tag{20}
\]
Subtracting this expression from \(J_\tau(x)\) gives exactly
\[
 \|Ax-b_0+M^{-1}u\|_M^2+|h^*x-y|^2.
\]
For completeness, eliminating the constraint gives
\[
 u=A^{-*}hy,\qquad
 d=2\operatorname{Re}(\bar y s)-(1+\eta_\tau)|y|^2.
 \tag{21}
\]
Its maximum is \(\mu_\tau\), attained at
\(y=s/(1+\eta_\tau)\). Equation (21) is a proof of attainment,
not a way to obtain \(s\) from geometric data.

## 5. What has been simplified

For this direct source comparison the proof needs only the complete
marked row model. It no longer needs the other colors, a common-color
gauge, or a frame inverse. The earlier all-color formulation still has
an advantage: the trivial color gives a positive polynomial floor at
every level. The present minimum can vanish, exactly when \(K_N\)
vanishes.

The remaining large space has dimension \(N^{2k}\). Its coordinates
form a tensor product over crossings, rather than a direct sum of one
small packet per vertex. No local Conway-tree elimination or small
separator decomposition follows from (14). Moreover the history
matrix \(G\), and its input energy, can grow exponentially. The
condition bound (17) is in \(M\) coordinates and makes no Euclidean
conditioning claim.

All comparison factors introduced in (6) can be made arbitrarily close
to one with a polynomial penalty. Consequently those factors cannot
be the missing exponential loss. The unresolved question is the
geometric growth of the specified affine residual distance itself,
or a trial field satisfying (19) with the correct energy rate. Neither
a new short-filling case nor the finite-exception theorem follows from
the simplification alone.

The sole entire direct proof source is the
[orthogonal marked row model](research_burau_orthogonal_marked_row_model.md),
read at SHA-256
`faade30be18b475de010b68cef3a5c5438e727fb17c599f38b97578ad369e4be`.
It supplies exactly (1) and the prescribed inner products and source
columns. The finite inverse estimate, minimizer, phase, orthogonal
normal, conditioning and certificates are proved above. The earlier
[scalar closing response](research_conway_scalar_cap_response.md) was
read in full for comparison. It concerns a nonlinear quartic Conway
energy; the present residual is affine. No claim of novelty is made
for quadratic least squares or its elementary penalty and dual formulas.

Only written mathematics and text operations were used. The frozen
manuscripts and public documentation were not changed.
