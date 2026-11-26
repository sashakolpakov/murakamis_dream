# The undamped whole Frobenius Gaussian source period

Private written proof, 18 November 2026.

For a knot braid the whole paired Frobenius Gaussian integral
converges absolutely at zero grading. This does not make its
undamped infinite operator trace class. Rather, the original
rational graded trace is realized by a convergent combined
integral, with all finite residue coefficients and first meridian
jets retained. The decay comes from the absence of a fixed vector
in the quotient of a one-cycle strand permutation.

The complete directs are B, the damped analytic period, and F,
the original reduced Frobenius source comparison. The new
quadratic estimate and the continuation argument are proved below.
The continuous variables here are auxiliary Frobenius variables,
not geometric shapes.

## 1. The actual whole kernel

Keep the notation of B:
\[
 N\ge2,\quad r=m-1,\quad k=k_0e^u,\quad
 k_0=(-1)^{N+1},\quad u=N\log M.
 \tag{1}
\]
The fixed reduced braid word has \(L\ge1\) factors and knot
closure. At \(u=0\), all its degree-one Frobenius matrices
\(\Gamma_\ell^0\) are unitary in B's common positive metric.
Their ordered product
\(\Gamma_\beta^0=\Gamma_L^0\cdots\Gamma_1^0\) is the quotient
of the \(m\)-cycle permutation by its invariant line. Hence
\[
 \operatorname{spec}\Gamma_\beta^0
   =\{e^{2\pi ij/m}:1\le j<m\},\qquad
 \sigma_{\min}(I-\Gamma_\beta^0)
                         =\delta_m:=2\sin(\pi/m)>0.
 \tag{2}
\]
Both parity choices have the same statement.

For residues \(a,b\in\{0,\ldots,N-1\}^r\), the exact local
block is
\[
 (\widetilde A_\ell)_{ba}
       =M_{P_{\ell,ba}}\operatorname{Sym}\Gamma_\ell(k).
 \tag{3}
\]
B proves that \(P_{\ell,ba}\) is homogeneous of degree
\((|a|-|b|)/N\in\{0,\ldots,r-1\}\) when nonzero.
It retains every original scalar and carry coefficient.

In B's orthonormal linear coordinates the undamped kernel is
\[
 \mathcal K^0_{\ell,ba}(Z,\overline W;u)
    =P_{\ell,ba}(Z;u)
                      \exp(Z^t\Gamma_\ell(k_0e^u)\overline W).
 \tag{4}
\]
For a fixed finite Cartan mark \(f(K_0)\), let
\[
 \begin{split}
 \mathcal G_f(u)=
 \sum_{a_0,\ldots,a_{L-1}}
 f(x_0^rQ^{-|a_0|})
 \int\prod_{\ell=1}^L
  \mathcal K^0_{\ell,a_\ell a_{\ell-1}}
                       (Z_\ell,\overline Z_{\ell-1};u)
                  \prod_{\ell=0}^{L-1}d\mu(Z_\ell),\\
 a_L=a_0,\quad Z_L=Z_0,\qquad
 d\mu(Z)=\pi^{-r}e^{-|Z|^2}d^{2r}Z,\quad x_0=-q^{-1}.
 \end{split}
 \tag{5}
\]
The finite residue sum remains part of this expression.
We first prove convergence; no infinite operator trace is
used to define (5).

## 2. A uniform quadratic gap from the knot permutation

Put \(y_\ell=\overline Z_\ell\), with cyclic indices, and
\[
             v_\ell=y_\ell-\Gamma_\ell^0y_{\ell-1},
             \qquad E=\sum_{\ell=1}^L\|v_\ell\|^2.
 \tag{6}
\]
Since every \(\Gamma_\ell^0\) is unitary, the real part of
the full Gaussian exponent at \(u=0\) is exactly
\[
 -\sum_{\ell=0}^{L-1}\|y_\ell\|^2+
   \sum_{\ell=1}^L\operatorname{Re}
              \langle y_\ell,\Gamma_\ell^0y_{\ell-1}\rangle
                            =-\frac12E .
 \tag{7}
\]
Here \(Z_\ell^t\Gamma_\ell^0\overline Z_{\ell-1}
=\langle y_\ell,\Gamma_\ell^0y_{\ell-1}\rangle\).
Thus the conjugation and operator order are the actual ones
in B's kernel.

Telescoping the recurrence in (6) gives
\[
 (I-\Gamma_\beta^0)y_0
       =\sum_{\ell=1}^L
                \Gamma_L^0\cdots\Gamma_{\ell+1}^0v_\ell.
 \tag{8}
\]
Equations (2) and (8) imply
\(\|y_0\|\le\sqrt L\,E^{1/2}/\delta_m\).
For each other index the partial recurrence gives
\[
 \|y_\ell\|\le
            \sqrt L(1+\delta_m^{-1})E^{1/2}.
 \tag{9}
\]
Consequently
\[
 -\frac12E\le -g_\beta\sum_{\ell=0}^{L-1}\|y_\ell\|^2,
 \qquad
 g_\beta=\frac1{2L^2(1+\delta_m^{-1})^2}>0.
 \tag{10}
\]
The constant is independent of \(N\) and its parity.
This is a whole-word estimate. Individual local factors
have no such strict undamped estimate.

The knot hypothesis is exactly what removes these flat
directions. If the closure has \(c\) components, its strand
permutation has \(c\) cycles; the quotient by the common
invariant line has fixed space of dimension \(c-1\).
The recurrence in (6) identifies the kernel of \(E\) with
that fixed space. Thus the same computation gives exactly
\(c-1\) complex flat directions in the link case, and none
for a knot.

For complex \(u\) near zero, B's fixed-dimensional matrices
satisfy
\(\|\Gamma_\ell(k_0e^u)-\Gamma_\ell^0\|\le C_\beta|u|\).
The change in the real quadratic form is at most
\[
 C_\beta|u|\sum_\ell\|y_\ell\|\|y_{\ell-1}\|
                     \le C_\beta|u|\sum_\ell\|y_\ell\|^2.
 \tag{11}
\]
Choose a fixed \(\eta>0\) so that \(C_\beta\eta\le g_\beta/2\).
Then throughout \(|u|\le\eta\) the exponent is bounded above
by \(-g_\beta\sum\|Z_\ell\|^2/2\).
All remaining factors in (5) are polynomials. The integral
is therefore absolutely convergent and holomorphic in \(u\)
on a fixed smaller disk, uniformly in the Gaussian ends.

For every fixed order, meridian differentiation is legitimate
under the integral: it adds polynomial factors in \(Z\), and
\(\partial_M=(N/M)\partial_u\). Cauchy estimates give \(N^j\)
times the same finite-source coefficient bounds for the
\(j\)-th meridian normal on a smaller scaled collar.
No moving-\(q\) derivative is asserted.

For completeness, at \(u=0\) retain B's distributed grading
\(\rho=e^{-s/L}\), \(s\ge0\). The exact real quadratic form is
\[
              -(1-\rho)\sum_\ell\|y_\ell\|^2-\rho E/2.
 \tag{12}
\]
It is negative definite for every \(s\ge0\). On a bounded
interval in \(s\), (10) gives one positive decay constant.
Small complex \(u,s\) also preserve (10) by continuity of
the finite-dimensional quadratic matrix.

## 3. Equality with the prescribed rational trace

Let \(\mathcal G_f(u,s)\) be the integral (5) with B's exact
damped local kernels, including their residue factors.
The preceding estimate proves that this is holomorphic
on some fixed bidisk about \((u,s)=(0,0)\).
Its definition includes all the original finite residue
coefficients; no independent compact quantum dilogarithm
has been specialized.

For real \(s>0\) and \(|u|\le cs\), B identifies this actual
integral with
\[
 \mathcal G_f(u,s)=
       \frac{t_f(e^{u/N};e^{-s/N})}
                    {d_\beta(k_0e^u;e^{-s})}.
 \tag{13}
\]
The denominator at the origin is \(m\), so the rational
right side is holomorphic on a fixed smaller bidisk.
The two holomorphic functions agree on that entire bidisk.
One elementary justification is to expand their difference
in \(u\): for every small real \(s>0\) all its \(u\)-Taylor
coefficients vanish by B's identity. Each coefficient is a
holomorphic function of \(s\), so it vanishes identically.
Then uniqueness of the \(u\)-Taylor expansion proves the claim.

Setting \(s=0\) gives the promised actual period:
\[
 \boxed{\qquad
 \mathcal G_f(N\log M)
      =\frac{t_f(M;1)}{d_\beta(x(M)^N;1)}
      =\widetilde t_f(M;1).
 \qquad}
 \tag{14}
\]
The last term denotes F's specified rational graded trace.
Equation (14) realizes it by an absolutely convergent whole
Gaussian integral on \(|N\log M|<\eta\).
Dominated \(s\downarrow0\), including any fixed meridian jet,
is now valid for this combined integral.

It does not follow that
\(\widetilde B_\beta\) is trace class without grading.
For example its Frobenius symmetric-power action at
completeness has unit-modulus eigenvalues in every degree.
Equation (14) is an integral realization of a prescribed
regularized trace, not an ordinary trace of that operator
or an ungrouped sum of its original monomial diagonal entries.

## 4. The exact first-meridian-jet closing row

Use the actual pair mark \(P_{\mathfrak o}K_0^{\pm1}\) and
write \(G_{\mathfrak o,\pm}(M)=\mathcal G_{P_{\mathfrak o}K_0^{\pm1}}
(N\log M)\). F's original source comparison and (14) give
\[
 \Phi_{\mathfrak o}
 =m\left[
 \frac{G_{\mathfrak o,+}(1)+G_{\mathfrak o,-}(1)}
                                             {2\varepsilon}
 +\frac{G_{\mathfrak o,+}'(1)-G_{\mathfrak o,-}'(1)}
                                             {2\varepsilon m}
 \right],
 \qquad \varepsilon=(-1)^{(N+1)(m-1)}.
 \tag{15}
\]
The derivatives here differentiate the complete integrand
(4)--(5), including its Frobenius matrices, common scalars
and every meridian-dependent residue coefficient. They are
convergent integrals by Section 2. Summing the pair formula
gives the whole original reduced source, with its external
normalization lines unchanged.

The determinant derivative has not been suppressed locally.
F first proves
\[
 t_{\mathfrak o,\pm}=d_\beta\,G_{\mathfrak o,\pm},\qquad
 G_{\mathfrak o,+}(1)-G_{\mathfrak o,-}(1)=0.
 \tag{16}
\]
Only this actual paired residue identity cancels the term
\(d_\beta'(1)(G_{\mathfrak o,+}-G_{\mathfrak o,-})/
(2\varepsilon m)\) in the original source row.
At positive grade the corresponding residue need not vanish,
and B retains it. On a separately selected geometric
component no such cancellation has been established.

For a closed residue cycle in (5), each nonzero local
polynomial has nonnegative degree (5) of B, and their
degrees telescope to zero. They are therefore all degree
zero on that cycle. This explains the determinant factor,
but does not authorize discarding carries in a general
inserted current, an open kernel or a changed boundary
functional. Equations (3)--(5) retain those data.

## 5. Contour scope

The same strict estimate permits bounded translations of
the paired cycle in the independent \(Z,W\) variables,
now at zero grading as well. Translation changes the
quadratic exponent only by linear and constant terms.
The ends are bounded by
\(\operatorname{poly}(|Z|)\exp(-g_\beta|Z|^2/2+C|Z|)\).
Stokes on truncated cylinders therefore gives the exact
translated period, with its original polynomial source.

This is a genuine convergent auxiliary source period.
Its finite residue-head kernels remain; if they are given
their own coherent presentation, their finite reproducing
polynomials remain too. The positive Frobenius metric does
not make the quantum residue matrices positive or unitary.
The continuous variables have not been identified with
geometric shapes or with a contributing thimble.

The decay proof and the continuation to \(s=0\) hold for
each original \(N\), on a uniformly scaled meridian collar.
They do not interchange a large-\(N\) asymptotic with an
Abel limit or give a relative lower bound for the scalar
period. No geometric contribution or global noncancellation
is inferred.

## Complete proof-source pins

* B: notes/research_damped_frobenius_gaussian_source_period.md,
  SHA256 b82e72ebbf9c4b846b6a62350d6c8ad724db6af67cf409d999ba57c9fd56244c.
* F: notes/research_reduced_frobenius_trace_and_cap_transport.md,
  SHA256 647539c72374cecd69a4decc6531684852f8f3d34c889972103abd24db9bd3a8.

Both complete matching directs were read nontruncated in the
active author sequence. All new estimates and the holomorphic
continuation argument are written above. Only written mathematics
and text/hash operations are used.
