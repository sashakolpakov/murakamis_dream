# The full three-crossing column and its factorial approximation

Research note, 3 November 2026.

The three-crossing column has a first-order equation with a nonzero
forcing term. Its actual endpoint fixes a nonzero scalar. On every
closed interval of upper-half colors, the remaining dependence on
the color is an explicit sine factorial, with an exponentially small
relative error after the scalar is fixed at one color. This is useful
when retaining the column through another turn. It does not, by
itself, estimate that subsequent coherent contraction.

## 1. Exact original equation and endpoint

Let \(N\ge2\), \(D=N-1\), and use
\[
 q=e^{\pi i/N},\quad Q=q^2,\quad
 \kappa=q^{D^2/2},\quad
 d_j=4\sin^2(\pi j/N),\quad
 S_j=\prod_{r=1}^j2\sin(\pi r/N),\quad S_0=1.
 \tag{1}
\]
Let \(M_N\) be the original crossing multiplication matrix in
the normalized Newton basis. Remove only its specified scalar:
\[
 \beta_j=\kappa^{-3}(M_N^3e_0)_j,
 \qquad h_j=q^{j(j+2)}S_j^2.
 \tag{2}
\]
The [primitive odd source equation](research_odd_primitive_scalar_recurrence.md),
Theorem 2, gives exactly
\[
 \beta_0=1,\qquad
 \beta_j=q^{2j+1}d_j\beta_{j-1}+(-1)^j q^{3j}
                           \quad(1\le j\le D).
 \tag{3}
\]
Equivalently,
\[
 \beta_j=h_j L_j,\qquad
 L_j=\sum_{l=0}^j\frac{(-1)^lq^{-l(l-1)}}{S_l^2}.
 \tag{4}
\]
Indeed \(h_j/h_{j-1}=q^{2j+1}d_j\); dividing (3) by
\(h_j\) gives the consecutive difference in (4).
All denominators are nonzero at every level under consideration.

The endpoint is supplied by the full original normal trace, not by
an arbitrary initial value for the classical recurrence. The
[Gaussian endpoint calculation](actual_twist_endpoint_gaussian_certificate.md),
Sections 1--3, gives
\[
 \beta_D=(-1)^N e^{i\pi/4-3\pi i/(4N)-\pi iN/12}
                         N^{3/2}+O(N^{1/2}).
 \tag{5}
\]
For clarity, the two factors in that calculation are
\[
 \begin{split}
 C_{N,3}&=(-1)^N e^{-i\pi/2-3\pi i/(4N)}
                          (-i\sqrt3/2)e^{i\pi/4},\\
 G_3(N)&=-2\sqrt3\,e^{-\pi iN/12}/3.
 \end{split}
\]
Their product is precisely the coefficient in (5).
The odd-power error there is \(O(N^{1/2})\), uniformly in the
level residue class. Since \(S_D=N\) and
\(h_D=(-1)^Nq^{-1}N^2\), we obtain
\[
 L_D=N^{-1/2}\omega_N+O(N^{-3/2}),\qquad
 \omega_N=\exp\!\left(i\pi\left[\frac14+
                        \frac1{4N}-\frac N{12}\right]\right),
 \qquad |\omega_N|=1.
 \tag{6}
\]
This retains both level parities.

There is also a useful operator form that keeps the forcing visible.
Let \(\mathsf C_N\) be the original Casimir multiplication matrix,
\((\mathsf C_Nv)_j=c_jv_j-d_jv_{j-1}\), where
\(c_j=qQ^j+q^{-1}Q^{-j}\), and let
\(\mathsf X_N=\operatorname{diag}(Q^j)\). Then
\[
 \begin{split}
  (\mathsf C_N-q\mathsf X_N)h&=q^{-1}e_0,\\
  (\mathsf C_N-q\mathsf X_N)M_N^3e_0
                           &=\kappa^2q^{-1}M_Ne_0.
 \end{split}
 \tag{6a}
\]
For \(j>0\), the first identity is the consecutive ratio of
\(h_j\); its row zero is \(c_0-q=q^{-1}\). The second follows
from (3) and the exact one-crossing column
\((M_Ne_0)_j=\kappa(-q)^j\). Thus the inhomogeneity is an
original one-crossing column, not an unspecified error term.

## 2. A factorial tail estimate

Write
\[
                    J(x)=\int_0^x\log(2\sin\pi t)\,dt.
 \tag{7}
\]
The integral is convergent at zero. The elementary sine-factorial
estimate, including its endpoints, is
\[
                  \log S_j=NJ(j/N)+O(\log N)
                         \quad(0\le j<N),
 \tag{8}
\]
uniformly in \(j\). Also \(J(1-x)=-J(x)\),
\(J(x)<0\) for \(0<x<1/2\), and \(J(x)>0\) for
\(1/2<x<1\). These facts follow by integrating
\(\log(2\sin\pi x)\), whose only interior zeros are
\(1/6,5/6\). A written uniform proof of (8) is Lemma 2 of
[the weighted Green estimate](research_elementary_weighted_green_transport.md).

**Lemma 1.** For each fixed \(0<\varepsilon<1/2\),
\[
 \sum_{m=0}^{\lfloor(1/2-\varepsilon)N\rfloor}S_m^2
                                  =1+O_\varepsilon(N^{-2}).
 \tag{9}
\]
Moreover
\[
                  \sum_{m=0}^{\lfloor N/2\rfloor}S_m^2=O(N).
 \tag{10}
\]

*Proof.* Choose \(0<\delta<\min(1/6,1/2-\varepsilon)\).
For \(1\le m\le\delta N\), each consecutive squared ratio is
at most \(\rho=4\sin^2(\pi\delta)<1\). The first term
\(S_1^2\) is \(O(N^{-2})\). Thus the sum over these positive
indices is \(O(N^{-2})\). On the remaining closed interval
\([\delta,1/2-\varepsilon]\), (8) and strict negativity of
\(J\) bound the entire sum exponentially. This proves (9).

For (10), split at \(\lfloor N/3\rfloor\). On the first
part the sequence \(S_m^2\) first decreases and then increases;
its maximum is at one of its endpoints. Equation (8) shows that
the last endpoint is at most one for large \(N\), so this part
is \(O(N)\). On the remaining part the consecutive ratios are
bounded below by a constant greater than one. Summing backward
from the last term is a geometric bound. That last term is
\(N\) for odd \(N\), and \(2N\) for even \(N\), by
\(S_jS_{D-j}=N\). This proves (10). \(\square\)

The same product identity turns (4) into an endpoint-safe bound:
\[
 |L_D-L_j|
     \le\sum_{l=j+1}^{D}S_l^{-2}
     =\frac1{N^2}\sum_{m=0}^{D-j-1}S_m^2.
 \tag{11}
\]
An empty sum is zero. Hence
\[
 \begin{array}{ll}
 |L_D-L_j|=O_\varepsilon(N^{-2}),
                 &j\ge(1/2+\varepsilon)N,\\
 |L_D-L_j|=O(N^{-1}),&j\ge N/2.
 \end{array}
 \tag{12}
\]
These are absolute bounds on the actual reciprocal forcing. No
cancellation among its summands has been assumed.

## 3. Uniform complex coefficients on the upper half

**Theorem 2.** For every fixed \(\varepsilon>0\), uniformly on
\((1/2+\varepsilon)N\le j\le D\),
\[
       \beta_j=N^{-1/2}\omega_N q^{j(j+2)}S_j^2
                                       (1+O_\varepsilon(N^{-1})).
 \tag{13}
\]
On the entire upper half \(N/2\le j\le D\), the same formula
holds with relative error \(O(N^{-1/2})\). In particular these
coefficients are nonzero for large \(N\).

More strongly, let \(I=[a,b]\) be any closed interval contained
in \((1/2,1)\), and fix \(x_0\in I\). Choose
\(j_0/N\in I\) nearest to \(x_0\), and define the exact scalar
\(A_N=L_{j_0}\). There is a constant \(c_I>0\) such that
\[
 \begin{split}
  &A_N=N^{-1/2}\omega_N(1+O_I(N^{-1})),\\
  &\beta_j=A_N q^{j(j+2)}S_j^2(1+O_I(e^{-c_I N}))
                                      \qquad(j/N\in I).
 \end{split}
 \tag{14}
\]

*Proof.* Combine (6) and (12) and then multiply by \(h_j\).
This gives (13) and its upper-half variant. For (14), subtract
the two partial sums in (4). Every index between \(j_0\) and
\(j\) lies in \(I\). As \(\min_I J>0\), (8) gives
\[
 |L_j-L_{j_0}|\le N^{C_I}e^{-2N\min_I J}.
\]
Division by \(|A_N|\asymp N^{-1/2}\) absorbs the polynomial
factor into a slightly smaller positive exponential constant.
This proves (14). \(\square\)

The relative error in (14) is a statement at the original discrete
colors. It does not assert a holomorphic interpolation estimate in
a complex strip. Such an estimate must retain the exact forcing
when the column is used in a subsequent contour calculation.

## 4. A full-column consequence

**Corollary 3.** In the ordinary Euclidean norm of the original
Newton coefficient space,
\[
 \left\|\kappa^{-3}M_N^3e_0-N^{-1/2}\omega_N h\right\|_2
                 =O(N^{-1})\,N^{-1/2}\|h\|_2.
 \tag{15}
\]
Consequently the original reflected odd source satisfies
\[
 \phi_N(R^{-3}T(R^3))
       =\frac1N\sum_{j=0}^{D}S_j^4\,(1+O(N^{-1})),
 \qquad
 \lim_{N\to\infty}\frac1N\log\phi_N(R^{-3}T(R^3))
                       =4J(5/6).
 \tag{16}
\]
These formulas also hold with both crossing signs reversed.
The reflected odd closure has two components; this corollary is
not a knot-volume statement.

*Proof.* Fix, for example, \(\varepsilon=1/12\). On
\(j\ge(1/2+\varepsilon)N\), (13) proves the desired relative
norm estimate. On the rest of the upper half, (12) bounds
\(|\beta_j|\) by a constant times \(N^{-1/2}S_j^2\).
The maximum of \(J\) on this omitted interval is strictly
less than its unique maximum at \(5/6\), so its norm is
exponentially smaller than \(N^{-1/2}\|h\|_2\).

On the lower half, through the last distinct physical node,
the [original low-color theorem](research_original_low_color_bound.md)
gives \(|\beta_j|=O(N)\), uniformly. This covers every
remaining index. The comparison vector there is polynomially
bounded as well: \(S_j^2\le2N\) for \(j\le N/2\), by the
same unimodality and endpoint values used in Lemma 1.
The total norm of both lower-half vectors is thus polynomial,
whereas (8) at \(j\) nearest \(5N/6\) gives
\(\|h\|_2\ge\exp(2NJ(5/6)+O(\log N))\).
This proves (15). Squaring the norm and using the exact original
reflected pairing proves the first formula in (16). Equation (8),
the unique maximum of \(J\), and the elementary finite-sum bound
prove its logarithmic limit. Conjugation gives the negative-power
case. \(\square\)

The estimates in this note concern the actual three-crossing
column. A further crossing operator can have exponentially large
norm, and a further boundary evaluation can have degree growing
with \(N\). Neither (15) nor fixed-degree Casimir limits justify
dropping the exact remainder under those operations.

## 5. Finite checks of the source identities

The [coefficient checker](../experiments/check_three_crossing_coefficient_profile.py)
computes the literal crossing matrix cubed by matrix-vector
multiplication and compares it with (3)--(4) and (6a). It also checks
the factorial reflection and tail identities at both level parities.
The [140-digit record](../repro/results/research-three-crossing-coefficient-profile-root.json)
and [180-digit replay](../repro/results/research-three-crossing-coefficient-profile-review.json)
each contain 653 original coefficient comparisons at ten levels.
Their finite endpoint, vector and constant-band errors are diagnostics;
the uniform asymptotic assertions are proved above.
