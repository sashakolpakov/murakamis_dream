# Complex neighborhoods of the complete horizontal source bounds

Research proof, 5 November 2026. The conditional kernels and the full
finite integrands are Laurent polynomials whose degrees grow at most
linearly with the quantum level. This fact turns a uniform bound on a
real rectangle of logarithmic variables into a bound on a fixed complex
neighborhood, with any prescribed positive loss in the exponential rate.
Fixed derivatives have the same rate bound. The argument applies to
the complete finite functions, including their zeros.

The new conclusion is an upper estimate. It does not supply a leading
coefficient, prove that a critical point contributes, or establish the
remaining real-row comparisons. It removes a separate complex-domain
obligation once the corresponding real estimate is available.

## 1. A polynomial estimate on a small arc

For \(\rho>1\), let \(E_\rho\) be the closed ellipse with foci
\(-1,1\) and semiaxes
\[
 a_\rho=(\rho+\rho^{-1})/2,\qquad
 b_\rho=(\rho-\rho^{-1})/2.
 \tag{1}
\]
If a polynomial \(p\) of degree at most \(d\) satisfies
\(|p(t)|\le M\) on \([-1,1]\), then
\[
                  |p(t)|\le 2(d+1)M\rho^d
                      \qquad(t\in E_\rho).
 \tag{2}
\]
Here and below a zero supremum means that the polynomial vanishes
identically. For a proof of (2), expand \(p\) in the Chebyshev
polynomials \(T_j\). Cosine orthogonality gives a constant coefficient
of modulus at most \(M\), and every other coefficient has modulus
at most \(2M\). The identity
\[
 T_j((w+w^{-1})/2)=(w^j+w^{-j})/2
 \tag{3}
\]
gives \(|T_j|\le\rho^j\) on the boundary of \(E_\rho\),
and the maximum principle gives the same estimate inside. Summing
the at most \(d+1\) terms proves (2). These are the usual
Chebyshev identities; see [NIST DLMF, equation 18.5.1](https://dlmf.nist.gov/18.5.E1)
and its [orthogonality table](https://dlmf.nist.gov/18.3).
We use the elementary proof just given, rather than assuming a more
general continuation theorem.

For a polynomial in \(k\) variables with separate degrees at most
\(d_i\), iterated cosine orthogonality gives the product version
\[
 |p(\mathbf t)|\le
 2^k\prod_{i=1}^k(d_i+1)\,M\rho^{\sum_i d_i}
       \qquad(\mathbf t\in E_\rho^k),
 \tag{4}
\]
provided \(|p|\le M\) on \([-1,1]^k\). The coefficients may
be complex, and no sign assumption is used.

Now let
\[
 F(\mathbf z)=\sum_{|\nu_i|\le D_i}
                 c_{\boldsymbol\nu}e^{-2\pi i\boldsymbol\nu\cdot\mathbf z}
 \tag{5}
\]
be a Laurent polynomial in the exponentials. Fix real centers
\(c_i\), heights \(h_i\), and positive halfwidths
\(\alpha_i<1/4\). Put \(r_i=\tan(\pi\alpha_i)\).
The local change of variables
\[
 z_i=c_i+ih_i+\pi^{-1}\arctan t_i,
 \qquad
 e^{-2\pi i(z_i-c_i-ih_i)}=\frac{1-it_i}{1+it_i}
 \tag{6}
\]
converts
\[
             p(\mathbf t)=\prod_i(1+t_i^2)^{D_i}F(\mathbf z)
 \tag{7}
\]
into a polynomial of separate degrees at most \(2D_i\).
Indeed, the term of exponent \(\nu_i\) contributes
\((1-it_i)^{D_i+\nu_i}(1+it_i)^{D_i-\nu_i}\);
both exponents are nonnegative and their sum is \(2D_i\).
The constant \(e^{-2\pi i\nu_i(c_i+ih_i)}\) has no effect on
the degree calculation.

Suppose that \(|F|\le M\) on the real box
\(\prod_i[c_i-\alpha_i,c_i+\alpha_i]+i\mathbf h\).
On \(\prod_i[-r_i,r_i]\), (7) then gives
\(|p|\le M\prod_i(1+r_i^2)^{D_i}\).
For \(\mathbf t\in\prod_i r_iE_\rho\), assume
\(R_i=r_i a_\rho<1\). Since
\(|1+t_i^2|\ge1-R_i^2\), applying (4) after rescaling gives
\[
 |F(\mathbf z)|\le
 2^k\prod_i(2D_i+1)M
 \exp\left\{\sum_iD_i
   \left[\log\frac{1+r_i^2}{1-R_i^2}+2\log\rho\right]\right\}.
 \tag{8}
\]
The factor divided out in this calculation is the explicit,
nonvanishing factor in (7). No source polynomial or quantum
factorial is divided out. The branch of \(\arctan\) in (6) is
the one equal to zero at zero; it is holomorphic on \(|t_i|<1\).

The exponent in (8), divided by \(\sum_iD_i\), can be made
arbitrarily small: first make the real halfwidths small, and then
take \(\rho>1\) sufficiently close to one. Nevertheless each
ellipse contains its whole real interval strictly in its interior.
Thus its inverse image in the \(z_i\)-plane contains a complex
neighborhood of that entire interval, including its endpoints.

## 2. A continuous upper rate extends with an arbitrary tolerance

Let \(I=\prod_i[a_i,b_i]\) be a fixed nondegenerate real
rectangle. Let \(\lambda\) range over a compact parameter space
\(K\), and let \(\mathbf h(\lambda)\) be real. For each
\(N\ge2\) and \(\lambda\), suppose that
\(F_{N,\lambda}\) has the form (5), with
\[
                      D_{i,N}\le d_iN
 \tag{9}
\]
for constants \(d_i\) independent of \(\lambda,N\).
Let \(V(\lambda,\mathbf x)\) be continuous on \(K\times I\).
Assume that for every \(\tau>0\) there are constants
\(C_\tau,A_\tau\), uniform in \(\lambda\), such that
\[
 |F_{N,\lambda}(\mathbf x+i\mathbf h(\lambda))|
       \le C_\tau N^{A_\tau}
                    e^{N(V(\lambda,\mathbf x)+\tau)}
                \qquad(\mathbf x\in I).
 \tag{10}
\]
No holomorphic dependence on the label \(\lambda\) is assumed.

**Theorem 1.** For every \(\varepsilon>0\), there exist
\(\delta>0,C,A\), independent of \(N,\lambda,\mathbf x\),
such that
\[
 |F_{N,\lambda}(\mathbf z)|\le CN^A
                    e^{N(V(\lambda,\mathbf x)+\varepsilon)}
 \quad\text{if}\quad
 \mathbf x\in I,\quad
 \max_i|z_i-x_i-ih_i(\lambda)|\le2\delta.
 \tag{11}
\]
Every fixed multiindex \(\beta\) consequently satisfies
\[
 |\partial_{\mathbf z}^{\beta}F_{N,\lambda}(\mathbf z)|
 \le \beta!\delta^{-|\beta|}CN^A
                  e^{N(V(\lambda,\mathbf x)+\varepsilon)}
 \quad\text{if}\quad
 \max_i|z_i-x_i-ih_i(\lambda)|\le\delta.
 \tag{12}
\]
In particular the derivatives transverse to the original real
rectangle are controlled. The neighborhood may shrink as
\(\varepsilon\) decreases, but is fixed before \(N\to\infty\).

*Proof.* By uniform continuity of \(V\), cover \(I\) by finitely
many small closed boxes contained in \(I\), so that its oscillation
on each box is less than \(\varepsilon/4\), uniformly in
\(\lambda\). The boxes have positive side lengths; their union
includes the boundary of \(I\). Make their maximum halfwidth small
enough, and then choose one \(\rho>1\) close enough to one, that
the exponent in (8), using (9), is less than
\(N\varepsilon/4\) on every box. This choice is possible
because the bracket in (8) tends to zero with the halfwidths and
\(\rho-1\).

Use (10) with \(\tau=\varepsilon/4\) on each box. For any
\(\mathbf x\) in that box its supremum is at most
\(C_\tau N^{A_\tau}e^{N(V(\lambda,\mathbf x)+\varepsilon/2)}\).
Equation (8) bounds the corresponding complex neighborhood with
exponent at most \(V(\lambda,\mathbf x)+3\varepsilon/4\).
The extra factor \(2^k\prod_i(2D_{i,N}+1)\) is polynomial in
\(N\), with constants independent of \(\lambda\).

For each of the finitely many boxes, its entire real box is compactly
inside the product of the inverse ellipse images in (6). Choose
\(2\delta>0\) smaller than their minimum complex neighborhood
width. Translating by \(i\mathbf h(\lambda)\) does not change
this width. The preceding estimate proves (11), with spare rate
tolerance. Cauchy's formula on polydisks of radius \(\delta\)
then proves (12). No assertion about a derivative in \(\lambda\)
is made. \(\square\)

As a useful consequence, a strict real rate gap is retained in a
fixed complex neighborhood after any prescribed smaller loss. If a
holomorphic comparison action is also present, its uniform continuity
on a compact neighborhood permits comparison with its real part at
the displaced point, at the cost of another prescribed tolerance.
This does not produce a relative asymptotic expansion from an upper
bound.

## 3. Application to the complete conditional kernels

Use the original kernels and interpolation polynomial from the
[finite source formula](research_mixed_local_outer_contribution.md):
\[
 \begin{split}
 C_{\epsilon,N}(X,Y)&=\sum_{j=0}^{N-1}
     \frac{X^{-j}(rX;r)_j(rY;r)_j}{(r;r)_j^{2+\epsilon}},
       \qquad r=e^{-2\pi i/N},\\
 \deg d_N&\le N-1.
 \end{split}
 \tag{13}
\]
The \(X\)-exponents of \(C_{\epsilon,N}\) lie in
\([-(N-1),0]\); its \(Y\)-exponents lie in \([0,N-1]\).
This follows term by term from (13), regardless of the size of the
coefficients or the zeros of the finite sum.

For the physical allocation flags \(\eta,\epsilon\in\{0,1\}\),
form the holomorphic Laurent polynomial
\[
 P_N(X,Y)=C_{\epsilon,N}(X,Y)^2d_N(X)^\eta d_N(Y)^\epsilon.
 \tag{14}
\]
It has exponent bands
\[
 \begin{array}{c|c}
 X&[-2(N-1),\eta(N-1)]\\
 Y&[0,(2+\epsilon)(N-1)].
 \end{array}
 \tag{15}
\]
Thus (9) holds, for example with \(d_1=2,d_2=3\). Moreover
\[
 |P_N|^{1/2}=|C_{\epsilon,N}|\,|d_N(X)|^{\eta/2}
                                      |d_N(Y)|^{\epsilon/2}
 \tag{16}
\]
at every complex argument, including every zero. No square root of
a holomorphic function needs to be chosen.

The [asymmetric contour estimate](research_mixed_horizontal_asymmetric_contour.md),
with its [half-index extension](research_mixed_half_index_contour.md),
already gives the required real bound for (16), with the continuous
rate
\[
 V_Z(x,z)=\max\{B_Z(x,z),T_Z(x,z)\}.
 \tag{17}
\]
Here \(Z\) is the original fixed reference, \(B_Z\) is its
affine supporting plane with the established quadratic loss, and
\(T_Z\) is the complete real-tail rate. On the actual height
domain, the [right-tail comparison](research_mixed_right_tail_endpoint_bound.md)
reduces \(T_Z\) to the three indicated endpoint rows. For own
type four the [smaller-cutoff theorem](research_mixed_four_left_cut_extension.md)
and its [support comparison](research_mixed_four_left_cut_support.md)
remove the left row. None of these simplifications is needed for
the extension argument: the maximum over the compact full row
interval is continuous by the original zero-safe entropy estimates.

Square the bound for (16), and apply Theorem 1 to (14) with rate
\(2V_Z\). Taking moduli and square roots in the result proves
the same upper bound for (16) on a fixed complex neighborhood,
with any prescribed added rate tolerance. This is uniform on each
compact actual-reference family for which the cited real estimates
are uniform. The physical negative-height restrictions at type-four
references remain part of that starting hypothesis.

The derivative conclusion applies directly to the polynomial (14).
It must not be used to divide by \(d_N\), or to infer weighted
bounds for derivatives of \(C_{\epsilon,N}\) alone at zeros of
that weight.

## 4. Full products and the remaining real comparison

In a full finite source every Fourier factor has an integer exponent;
the two neighboring half allocations multiply to that factor. The
resulting integrand is itself a Laurent polynomial. For example,
at an ordinary coordinate of the cyclic source, its two incident
conditional kernels give exponents in \([-(N-1),N-1]\).
The factor \(d_N\), when present, adds at most \(N-1\),
and a selected extra frequency subtracts \(N\). Hence all exponents
lie within \([-2N,2N]\). A fixed open source has the same linear
degree property after retaining its original finite endpoint
polynomials; its constants may depend on the fixed word.

Whenever the complete horizontal bounds have been multiplied for
such an actual finite integrand, Theorem 1 applies to the product
directly. It then controls derivatives of that holomorphic product,
without introducing fractional factors or dividing by a zero. The
ordinary boundary variables require their own initial uniform
estimates, or their own explicitly verified degree-and-real-bound
hypotheses; they are not supplied by changing the conditional
variables in (13).

In particular, if the remaining real comparisons prove
\(T_Z\le B_Z\), the full horizontal supporting-plane upper
bound also holds nearby in the complex variables, with an arbitrarily
small exponential tolerance. This addresses the transverse-domain
qualification in the earlier contour theorem. Even without that
comparison, the already established maximum (17) has this extension.
The extension does not make the positive part of \(T_Z-B_Z\)
disappear, provide the missing ordinary boundary sign, or prove
noncancellation for a completed open word.

The method is a local polynomial growth estimate of Bernstein--Walsh
type. Related real-spectral-variable arguments already occur in the
[connected short-filling theorem](research_connected_short_filling_clusters.md#8-the-entire-remaining-boundary).
The point here is its direct application to the logarithmic Laurent
variables and the original finite Fourier allocations, with a full
proof of the neighborhood and degree requirements.
