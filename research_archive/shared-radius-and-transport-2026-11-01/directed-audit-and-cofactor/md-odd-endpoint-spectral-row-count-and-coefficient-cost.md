# Odd endpoint perturbations: exact row count and a uniform coefficient cost

This is a finite-source estimate for the original central cofactor.
It is separate from the even parity question. It proves a uniform
small-spectral-neighborhood coefficient bound, but does not transfer
signed negative-axis cancellation from the endpoint to that
neighborhood.

## 1. The actual odd cofactor

Let \(N=2m+1\ge3\), \(d=N-1\), \(\theta=\pi/N\), and
\(\sigma=-2-u\). Put

\[
a_r=2+2\cos((2r+1)\theta),\qquad s_r=2\sin(r\theta).
\tag{1}
\]

The exact cleared lower cofactors are those of
`actual_cross_cofactor_factorization.md`, Sections 1–2:

\[
\begin{aligned}
R_0(b;u)&=1,\\
R_j(b;u)&=b^j\prod_{r<j}(a_r+u)
 +s_j^2(x+y)R_{j-1}(b;u)
 +s_js_{j-1}(a_{j-1}+u)xyR_{j-2}(b;u),\\
G_b(u)&=R_m(b;u),\qquad D_b(u)=R_{m-1}(b;u),\\
P_C(u)&=G_b(u)G_c(u)+u s_m^2xyD_b(u)D_c(u).
\end{aligned}
\tag{2}
\]

Here \(s_{m+1}=s_m\) has been used. All the factors in (2) belong to
the original level, and \(P_C\) has the original degree \(d\) in
the face variables. Its final term is the central-skipping path; it
must remain when \(u\ne0\).

For a polynomial in the face variables, \(|P|_{\mathrm{coef}}\) means
replace each complex coefficient by its modulus. A coefficientwise
inequality compares every coefficient separately.

## 2. Exact finite estimate

For \(\epsilon\ge0\), define

\[
\alpha=\operatorname{arsinh}(\sqrt\epsilon/2),\qquad
K_N(\epsilon)=
\begin{cases}
\dfrac{\sinh(N\alpha)}{N\sinh\alpha},&\epsilon>0,\\
1,&\epsilon=0.
\end{cases}
\tag{3}
\]

Then for every complex \(u\) with \(|u|\le\epsilon\),

\[
|P_C(u)|_{\mathrm{coef}}
\le_{\mathrm{coef}}
\left(1+\frac\epsilon{2s_m^2}\right)K_N(\epsilon)^2 P_C(0).
\tag{4}
\]

In particular, since \(s_m^2\ge3\),

\[
|P_C(u)|_{\mathrm{coef}}
\le_{\mathrm{coef}}
(1+\epsilon/6)e^{N\sqrt\epsilon}P_C(0).
\tag{5}
\]

**Proof.** Each monomial path in \(G_b\) or \(D_b\) contains a
subset of the unused diagonal factors \(a_r+u\), with \(r<m\),
each at most once. All remaining path factors are nonnegative face
polynomials independent of \(u\). Therefore

\[
|G_b(u)|_{\mathrm{coef}}\le G_b(\epsilon)
\le_{\mathrm{coef}}\prod_{r=0}^{m-1}
\left(1+\frac\epsilon{a_r}\right)G_b(0).
\tag{6}
\]

The same reasoning applies to \(D_b\). There is no singular central
row in this product: the row \(a_m=0\) is absent from every visited
central cofactor, and the skipping contribution is the explicit last
term of (2).

The lower diagonal list is exactly
\(a_r=4\sin^2((m-r)\pi/N)\). The elementary root-of-unity product
therefore gives

\[
\prod_{r=0}^{m-1}\left(1+\frac\epsilon{a_r}\right)
=\prod_{\ell=1}^m\left(1+
\frac\epsilon{4\sin^2(\ell\pi/N)}\right)
=K_N(\epsilon).
\tag{7}
\]

To check the scalar, set \(z=e^{2\alpha}\). The product over all
\(N\) roots of unity of
\((z-\zeta)(z-\zeta^{-1})/z\) is
\(4\sinh^2(N\alpha)\). Remove the \(\zeta=1\) factor
\(4\sinh^2\alpha=\epsilon\), pair the remaining conjugate roots,
and take the positive square root. At \(\epsilon=0\) the unnormalized
half-product is \(N\), giving exactly (7).

The expansion of every expression in (2) in the variables
\(u,x,b,c,y\) has nonnegative coefficients. Thus modulus replacement
is bounded by evaluation at \(u=\epsilon\). Moreover the recurrence
at the terminal row gives
\(G_b(\epsilon)\ge_{\mathrm{coef}}s_m^2(x+y)D_b(\epsilon)\).
Since \((x+y)^2\ge_{\mathrm{coef}}2xy\),

\[
\epsilon s_m^2xyD_b(\epsilon)D_c(\epsilon)
\le_{\mathrm{coef}}
\frac\epsilon{2s_m^2}G_b(\epsilon)G_c(\epsilon).
\tag{8}
\]

Equations (6)–(8) prove (4). Finally
\(\sinh(N\alpha)/\sinh\alpha\) is the sum of \(N\) exponentials
with exponents \((N-1-2k)\alpha\), so
\(K_N\le e^{(N-1)\alpha}\le e^{N\sqrt\epsilon/2}\). This proves
(5).

Products and the original nonnegative face coefficient extraction
preserve (4). Thus for a fixed exterior with \(r\) central coupons,
all original face targets retained, its binary polynomial obeys

\[
|P_N(\boldsymbol u;A,C)|_{\mathrm{coef}}
\le_{\mathrm{coef}}
\prod_{e=1}^{r}\left[
\left(1+\frac{\epsilon_e}{2s_m^2}\right)
K_N(\epsilon_e)^2\right]P_N(\boldsymbol0;A,C)
\tag{9}
\]

whenever \(|u_e|\le\epsilon_e\). No face demand is shifted in this
statement. It is valid even if some protected face variables are set
to zero before extraction.

## 3. Number of negative rows

For real \(\sigma=-2+\epsilon\), or \(u=-\epsilon\), with
\(0\le\epsilon<4\), the number of strictly negative lower diagonal
rows is exactly

\[
\#\left\{1\le\ell\le m:
\ell<\frac N\pi\arcsin(\sqrt\epsilon/2)\right\}.
\tag{10}
\]

There can also be one zero row if the endpoint is an integer. In
particular this number is at most
\(N\arcsin(\sqrt\epsilon/2)/\pi=O(N\sqrt\epsilon)\).

This count is literal and includes the original half-index. However,
it does not by itself yield a stable-minor expansion. The cofactor
away from its physical node is a row-replacement determinant of the
upper triangular Casimir block, as in
`actual_cross_cofactor_interior_packet.md`, Section 1. That matrix is
not the positive Hermitian q-Hahn pencil. The positive Hermitian
identification in that source is proved only at the actual spectral
node. In addition, every positive diagonal row also changes when
\(u\) changes; only the count of rows that change sign is small.

## 4. What is still missing for a coherent bound

The exponential cost in (5) tends to zero per level as the fixed
spectral radius tends to zero. This is stronger than continuity at
each fixed \(N\), and it retains the odd central-skipping term and
the original targets. It is nevertheless a **coefficient modulus**
estimate. Evaluating at a negative boundary fugacity after (9) gives
an absolute coefficient sum, not the signed endpoint polynomial.

In particular, (9) does not imply
\(|P_N(\boldsymbol u;-t,1)|\le e^{o_\epsilon(N)}
|P_N(\boldsymbol0;-t,1)|\), nor the analogous supremum bound. The
general counterexample in
`research_even_cross_stability_obstruction.md`, Section 4, shows why
even exponentially sharp positive coefficient comparison cannot
justify that inference. A stable-minor representation with controlled
degrees and original target shifts, or a direct coherent estimate,
is still needed to extend the odd common-axis cancellation theorem
through a fixed spectator spectral neighborhood.

The source dependencies and their hashes are recorded in the
companion private even-cofactor obstruction note. This statement uses
only their finite path identities; no local packet or asymptotic
stability assertion is imported.
