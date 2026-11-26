# Spatial quotients as exact dual-endpoint contour sources

Private written proof, 16 November 2026.

The auxiliary ordinary quotients in projected recovery admit an exact
endpoint-parameter contour representation after all subsequent turns
and shared multiplications. The representation introduces products
of dual coupons \(TK_N(z,\cdot)\), with a polynomial contour cost.
Roots near the negative endpoint require the negative dual family.
That family has an actual exponentially growing image under \(T\),
so it cannot be bounded individually at the positive family's
zero first-turn rate. No growth of the coherent quotient contour
sum is inferred.

## 1. The full-quotient identity

Retain
\[
 N\ge2,\quad D=N-1,\quad \eta=(-1)^D,\quad
 P_N(C)=2T_N(C/2)+2,\quad
 \mathcal A_N=\mathbb C[C]/(P_N),
\]
\[
 c_j=2\cos((2j+1)\pi/N),\quad
 S_j=\prod_{\ell=1}^j2\sin(\ell\pi/N),\qquad
 e_j(C)=S_j^{-2}\prod_{a<j}(c_a-C),
\]
\[
 K_N(w,C)=\sum_{j=0}^{D}e_j(w)e_j(C),\qquad
 Te_j=e_{D-j},\qquad
 \phi_N(e_i e_j)=\mathbf1_{i+j=D}.
 \tag{1}
\]
The ordinary dual coupon is exactly
\[
 \delta_z(C)=TK_N(z,C)
       =\frac{P_N(C)-P_N(z)}{\eta N^2(C-z)} .
 \tag{2}
\]
The quotient on the right is an ordinary polynomial in both
variables, including on their diagonal.

Let \(P(C)\) be a specified ordinary polynomial, possibly with
joint external parameters. Define its ordinary divided quotient
\[
                Q_z(C)=\frac{P(C)-P(z)}{C-z}.
 \tag{3}
\]
Then the ordinary identity
\[
 \delta_z(C)\{P(C)-P(z)\}
       =\frac{P_N(C)-P_N(z)}{\eta N^2}Q_z(C)
 \tag{4}
\]
gives in the original full algebra
\[
 \boxed{\quad
 \delta_z\{P-P(z)\}
                =-\frac{P_N(z)}{\eta N^2}Q_z .
 \quad}                                                   \tag{5}
\]
No inverse of \(C-z\), \(P_N(C)\), or a physical nilpotent is
used in this identity. The ordinary \(P_N(C)Q_z\) residual has
zero values and first normals at every double physical root,
and zero value at the odd simple root.

The representative in (3) matters. For the projected-recovery
quotients, \(P\) is the specified canonical representative before
ordinary division. Replacing it by an arbitrary \(P_N\) multiple
before division would generally change the quotient's physical
jets at a divisor root. No such replacement is made here.

Let \(\Gamma\) be a positively oriented parameter contour
surrounding \(a\), with \(P_N(z)\ne0\) on \(\Gamma\).
Cauchy's formula for the polynomial \(Q_z\) and (5) give
\[
 \boxed{\quad
 Q_a=-\frac{\eta N^2}{2\pi i}
       \oint_\Gamma
       \frac{\delta_z P-P(z)\delta_z}
                    {P_N(z)(z-a)}\,dz
       \quad\hbox{in }\mathcal A_N .
 \quad}                                                   \tag{6}
\]
The complete numerator in (6) is divisible by \(P_N(z)\)
as an \(\mathcal A_N\)-valued polynomial, by (5). Thus all
apparent parameter poles at physical colors are removable,
including the double ones. The contour may enclose other
zeros of \(P_N\); the integrand as a whole has only the
Cauchy pole at \(a\).

There is also the useful ordinary identity
\[
 \frac{\delta_w(C)-\delta_w(a)}{C-a}
             =\frac{\delta_w(C)-\delta_a(C)}{w-a}.
 \tag{7}
\]
Both sides are the symmetric second divided difference of
\(P_N/(\eta N^2)\). This closes ordinary divided differences
within the dual family, not within the original \(K\) family.
In particular \(T(\prod K_{w_i})\) cannot be replaced by
\(\prod\delta_{w_i}\).

## 2. The identity after the actual later operations

Let \(\mathscr L_N\) be any fixed linear map on \(\mathcal A_N\),
with values in a finite-dimensional output space or in a space
of remaining joint spectator functions. It may include any fixed
sequence of original \(T,V_n,U_\tau\), multiplication by the actual
shared external coupons, canonical reduction in the originally
traced variable, and original closing traces. Its coefficients
and external data are independent of the new contour variable \(z\).

Applying it to (6) gives exactly
\[
 \boxed{\quad
 \mathscr L_NQ_a=-\frac{\eta N^2}{2\pi i}
       \oint_\Gamma
       \frac{\mathscr L_N(\delta_zP)
                      -P(z)\mathscr L_N(\delta_z)}
                    {P_N(z)(z-a)}\,dz .
 \quad}                                                   \tag{8}
\]
This is a formula after the later turns, not an estimate before
them. In the projected-recovery application, take
\(\mathscr L_N=\mathfrak F\), including its inner turn, whole
received tensor, even/odd descent, and outer turn. Apply (8)
componentwise to the specified canonical input coordinates.
The output can be the entire collar packet with both physical
values and first normals.

All identities hold jointly in uncontracted outside variables.
Their derivatives preserve the ordinary product rule and the
original first normals. The endpoint parameters in (8) remain
ordinary integration variables; they are not quotiented.

## 3. Both microscopic endpoint contours and their cost

The divisor roots in the recovery construction belong to a
fixed finite collection
\[
                  a_N=\varepsilon(q^k+q^{-k}),\qquad
                  q=e^{\pi i/N},\quad \varepsilon=\pm1 ,
 \tag{9}
\]
where \(k\) is fixed. They are \(O(N^{-2})\) from \(2\varepsilon\).
Choose parameter circles
\[
             \Gamma_{\varepsilon,N}:
                  z=2\varepsilon+\lambda/N^2,\quad |\lambda|=R .
 \tag{10}
\]
The fixed \(R\) can be chosen to enclose every scaled root of
the relevant sign and to satisfy \(R\notin\{\pi^2m^2:m\ge0\}\).

Uniformly on compact \(\lambda\)-sets,
\[
 \begin{split}
 P_N(2+\lambda/N^2)&\longrightarrow
                         2+2\cosh\sqrt{\lambda},\\
 P_N(-2+\lambda/N^2)&\longrightarrow
                         2+2(-1)^N\cos\sqrt{\lambda}.
 \end{split}                                             \tag{11}
\]
The square-root expressions are entire functions of \(\lambda\).
For the first formula use
\(T_N(1+\lambda/(2N^2))
 =\cosh(N\operatorname{arccosh}(1+\lambda/(2N^2)))\)
on a local branch, and extend analytically over a finite compact
cover; at zero the same conclusion follows from its power series.
The second follows from the parity of \(T_N\).
The possible limiting zeros have modulus \(\pi^2m^2\).
Thus the stated choice of \(R\) works on both parity classes.

For all large \(N\), on the chosen circles,
\[
 |P_N(z)|\ge c,\qquad |z-a_N|\ge cN^{-2},
 \qquad |dz|=N^{-2}|d\lambda|.
 \tag{12}
\]
Consequently (8), in any norm on its actual output, implies
\[
 \|\mathscr L_NQ_{a_N}\|
 \le C N^2\sup_{z\in\Gamma_{\varepsilon,N}}
       \left\{\|\mathscr L_N(\delta_zP)\|
                         +|P(z)|\,\|\mathscr L_N\delta_z\|\right\}.
 \tag{13}
\]
No bound on the operator norm of \(\mathscr L_N\) was used.

For reference, the dual coupons themselves have uniformly
bounded real norm on either fixed microscopic parameter disk:
\[
       \sup_{C\in[-2,2]}|\delta_z(C)|\le C_R,\qquad
                       |z-2\varepsilon|\le R/N^2 .
 \tag{14}
\]
Indeed put the disk and \([-2,2]\) in a Bernstein ellipse
of parameter \(e^{B_R/N}\). Its convexity contains every segment
from \(z\) to a real \(C\). The identity
\(P_N'=N U_{N-1}(C/2)\), and the finite geometric-sum formula
for \(U_{N-1}\), give \(|P_N'|\le C_RN^2\) there.
Integrate that derivative along the segment in (2).
The same reasoning bounds \(\delta_z(z')\) when \(z,z'\) lie
in the same endpoint disk. At opposite endpoints their
distance is bounded below, and (2),(11) give an \(O(N^{-2})\)
bound. All these statements include coincident parameters by
their ordinary removable interpretation.

If \(\deg P\le cN\) and \(\|P\|_{[-2,2]}\le B_N\), its
Chebyshev coefficient bound gives
\[
                    \sup_{\Gamma_{\pm,N}}|P(z)|\le C N B_N .
 \tag{15}
\]
For the original inner coordinates \(B_N\) is polynomial,
by the full endpoint-product bound, fixed full shifts,
even/odd descent, and exact Hermite folding. Fixed normal
derivatives in (14),(15) add only polynomial powers of \(N\).
These are pre-turn bounds on scalar coefficients, not
post-turn bounds on the families in (13).

## 4. Repeated polynomial division

Ordinary division by a monic fixed-degree polynomial
\[
                         d_N(C)=\prod_{\ell=1}^s(C-a_{\ell,N})
 \tag{16}
\]
can be performed by the successive ordinary operators
\(D_aP=(P-P(a))/(C-a)\). Their composition is the ordinary
quotient by \(d_N\); the subtracted Newton interpolation
polynomial has degree less than \(s\). Repeated roots use
the same removable divided differences.

To iterate (6), use the canonical section at each intermediate
step. This is necessary: an ordinary divided difference is not
an operator on arbitrary representatives modulo \(P_N\).
The actual successive ordinary quotients already have degree
at most \(D\), so this convention gives exactly the desired
division of an original canonical input.

At each integral step one either multiplies the current class
by a new \(\delta_z\), or evaluates its canonical representative
at \(z\) and leaves one new dual factor. The latter scalar is
exactly its original Frobenius evaluation
\[
                 [\operatorname{can}F](z)=\phi_N(\delta_zF).
 \tag{17a}
\]
It is not in general the evaluation of the unreduced ordinary
product. In particular it must not be replaced by a product
of the separate factor values.

After \(\ell\) fixed steps, the result is a finite sum of
iterated contour integrals whose transformed inputs are of the forms
\[
       \mathscr L_N\left(P\prod_{\nu=1}^{\ell}\delta_{z_\nu}\right),
       \qquad
       \mathscr L_N\left(\prod_{\nu=1}^{t}\delta_{z_\nu}\right),
                               \quad 1\le t\le\ell .
 \tag{17}
\]
Canonical products in (17) are understood inside the original
linear map. The second class has scalar coefficients built from
the actual reset traces
\[
       \phi_N\left(P\prod_\nu\delta_{z_\nu}\right),
            \qquad
       \phi_N\left(\prod_\nu\delta_{z_\nu}\right).
 \tag{17b}
\]
The original \(P\) occurs in at most one such trace in each
term. Their signs, contour weights, full normals, and shared
variables are those of the iterated formula. No reset trace
has been factorized into separate physical values.

For an ordinary polynomial \(f\) of degree at most \(cN\),
the exact Hermite Fourier folding and the leading-coefficient
formula for \(\phi_N\) give
\[
                    |\phi_N(f)|\le C_cN^3\|f\|_{[-2,2]}.
 \tag{17c}
\]
Indeed its Fourier coefficient sum is at most
\((2cN+1)\|f\|\), only a fixed number of alias blocks occur
in the canonical remainder, and
\(\phi_N(f)=\eta N^2[C^D]\operatorname{can}f\).
This argument preserves the full normals before estimating.

Equations (12),(14),(17c) now give a polynomial prefactor
for the actual families (17). A coarse explicit bound is
\(C_\ell N^{5\ell}\) times the largest first-family norm
plus \(C_\ell N^{5\ell}B_N\) times the largest second-family
norm. There are at most \(\ell\) reset traces in a term.
The contours retain the endpoint sign of each divisor root.
This applies to every auxiliary quotient collar in projected
recovery, after its whole original map \(\mathfrak F\).

Thus an upper exponential rate uniform for these mixed original/
dual product families transfers to the quotient collars at
that same rate. The previously proved bound for original
\(K\)-products alone does not establish the required premise.

## 5. A post-turn obstruction for the negative dual family

There is an exact all-level distinction between the signs.
By the real mean-value formula and
\(\|P_N'\|_{[-2,2]}=N^2\),
\[
                            \|\delta_{-2}\|_{[-2,2]}\le1 .
 \tag{18}
\]
Nevertheless
\[
                       T\delta_{-2}=K_N(-2,\cdot),
 \qquad K_N(-2,-2)=\sum_{j=0}^{D}e_j(-2)^2 .
 \tag{19}
\]
All summands in the second expression are nonnegative.
For \(j_N=\lfloor N/4\rfloor\),
\[
 e_{j_N}(-2)
   =\prod_{h=0}^{j_N-1}
       \frac{\cos^2((h+\tfrac12)\pi/N)}
            {\sin^2((h+1)\pi/N)} .
 \tag{20}
\]
The cosine logarithm is smooth on this range. For the sine
logarithm, comparison of the monotone Riemann sum with its
integral leaves \(O(\log N)\) error at zero; equivalently
one may first subtract \(\log x\) and use the elementary
factorial integral bounds. Therefore
\[
 \lim_{N\to\infty}\frac1N\log e_{j_N}(-2)^2
       =4\int_0^{1/4}\log\cot(\pi x)\,dx
       =\frac{4G}{\pi}>0 ,
 \tag{21}
\]
where \(G=\int_0^{\pi/4}\log\cot t\,dt\) is Catalan's constant.
In particular
\[
 \liminf_{N\to\infty}\frac1N
                   \log\|T\delta_{-2}\|_{[-2,2]}
                                \ge\frac{4G}{\pi}.
 \tag{22}
\]
The chosen index is below every odd-level zero, so the same
argument covers both parities. It is an actual original turn
evaluated at the literal real output color \(-2\), not an
indicial mode or a synthetic spectator.

In contrast, \(T\delta_2=K_N(2,\cdot)\) has polynomial real
norm by the endpoint-product theorem. Thus even bounded raw
real norm of the dual coupons cannot justify treating both
signs as the same zero-rate source family after \(T\).

Equation (22) does not prove growth of a quotient in (8):
the difference there and its contour integration may cancel
this channel. Nor does it establish participation in a final
geometric coefficient or an obstruction to the volume goal.
It rules out an individual negative-coupon estimate used
without that coherent cancellation.

There is an actual calibration where that limitation matters.
If every original endpoint is a fixed physical mark
\(w_i=c_{b_i}\), with the \(b_i\) independent of \(N\), then
\(K_N(c_{b_i},C)\) has degree \(b_i\) and polynomially bounded
coefficients. Their product, and its ordinary quotient by any
fixed number of the factors (9), have fixed degree and polynomial
coefficients. Applying \(T\) gives a fixed linear combination
of terminal Newton polynomials \(e_{D-j}\), whose real norms
are polynomial by the endpoint source. Thus the actual first
\(T\)-image of these quotient products is polynomial for either
sign of the divisor roots. This does not extend the estimate to
generic microscopic parameters: fixed physical marks do not
supply a uniform analytic uniqueness or interpolation bound.

## 6. Coverage and direct sources

The Frobenius reproducer and polynomial microscopic endpoint
bounds are existing inputs. The additional statement here is
the exact post-turn contour reduction of spatial quotients,
including repeated divisions and both endpoint signs, together
with the actual negative-family warning (22).
A targeted search of the dualizing-residue, two-sided quotient,
Casimir-resolvent, endpoint-turn, and projected-recovery notes
found no previous version of this assembly.

The following complete direct sources were read at unchanged
pins, with their used implications and hashes checked:

* [Ordinary dual kernel and exact turns](research_full_endpoint_unit_turn_identities.md),
  SHA256 e2f69aaff28080b9dd9e11365ce18d68a9d738667917204714556681c50789e8.
* [Projected recovery and its actual auxiliary collars](research_multikernel_parameter_leading_projected_recovery.md),
  SHA256 04ff3a2fe980009d527214407b20709b9c962a5935314cf2666619f03447034d.
* [Polynomial full endpoint products and Hermite folding](research_endpoint_two_half_plane_relative_source.md),
  SHA256 985fa3331379c3877734f28773d314b667ee87fa63314a5ef4513a3fe128d194.

Only written mathematics and source-text/hash reads were used.
No mathematical program, numerical experiment, test, build, or
compilation was run. Adopted notes and public manuscripts are unchanged.
