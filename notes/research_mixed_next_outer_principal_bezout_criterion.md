# A compact exceptional set for the paired principal characteristics

Private algebraic criterion, 8 November 2026. The paired principal
polynomials have a compact exceptional set of outgoing parameters.
That set is covered by finitely many real-analytic root branches and
finitely many additional points; in particular it has planar measure
zero and empty interior. Away from it, the classical polynomial
Bezout coefficients are uniformly bounded along the full physical
middle arc.

No actual knot reference is asserted to avoid the exceptional set.
This is not a finite difference-operator inverse, an estimate of
transformed forcings, or an outer cancellation theorem. No
mathematical numerical evaluation or frozen-source edit is used.

## 1. The source-specific principal pair

Use exactly the polynomials of
[the paired Newton characteristic theorem, equations (27), (30)--(33)](research_mixed_next_outer_paired_newton_characteristics.md):
\[
\begin{gathered}
\mathcal X=\{e^{2\pi i t}:1/2\le t\le5/6\},\\
\mathsf P(x,z)=x^5z^3\mathfrak b(x,z),\\
\mathsf Q(x,z,Z)
 =(x-1)z^2+(3x-2-x^2Z)z-(x-1)^2,\\
\mathsf R(x,Z)
       =\operatorname{Res}_z(\mathsf P(x,z),\mathsf Q(x,z,Z)).
\end{gathered}                                                     \tag{1}
\]
Here \(\mathfrak b\) is the original Newton period symbol,
and \(\mathsf Q=x^2z(\mathfrak j^{\mathrm t}-Z)\) uses the
signed outgoing transpose. Thus both the original factor
\((-q)^b\) and the reciprocal period shift have already been
accounted for. We do not substitute an unsigned conditional
characteristic.

The source theorem proves
\[
\begin{gathered}
\deg_z\mathsf P=11,\qquad
\operatorname{lc}_z\mathsf P=(x-1)^{16},\qquad
\mathsf P(x,0)=x^{10}(x-1)^6,\\
\deg_z\mathsf Q=2,\qquad
\deg_Z\mathsf R=11,\qquad
\operatorname{lc}_Z\mathsf R=x^{32}(x-1)^{22}
                         \qquad(x\in\mathcal X).
\end{gathered}                                                     \tag{2}
\]
In particular all these leading coefficients are nonzero on
the compact arc. The two characteristic polynomials have a
common root precisely when \(\mathsf R(x,Z)=0\); none of
their roots is zero there.

Define the exceptional outgoing set
\[
\boxed{\qquad
\Sigma=\{Z\in\mathbb C:\mathsf R(x,Z)=0
                                \text{ for some }x\in\mathcal X\}.
\qquad}                                                           \tag{3}
\]
Its definition concerns all roots of the principal equations.
It does not select a stationary sheet or a marked gluing branch.

## 2. Compactness and the real-analytic root branches

**Theorem 1.** The set \(\Sigma\) is compact. It is the union
of finitely many real-analytic images of open real intervals
and finitely many points. It has planar Lebesgue measure zero
and empty interior.

*Proof of compactness.* Write
\[
\mathsf R(x,Z)=\ell(x)Z^{11}
                    +\sum_{j=0}^{10}r_j(x)Z^j,\qquad
\ell(x)=x^{32}(x-1)^{22}.
\]
All coefficients are continuous on \(\mathcal X\), and
\(\ell\) is nonzero there. Consequently the number
\[
B_{\rm root}=1+\max_{x\in\mathcal X}
                         \sum_{j=0}^{10}|r_j(x)/\ell(x)|
                                                                    \tag{4}
\]
is finite. If \(|Z|>B_{\rm root}\), the leading term has modulus
strictly larger than the sum of the other terms, so
\(\mathsf R(x,Z)\ne0\) for every \(x\in\mathcal X\).
The incidence set
\[
\{(x,Z):x\in\mathcal X,\ |Z|\le B_{\rm root},\
                                      \mathsf R(x,Z)=0\}
                                                                    \tag{5}
\]
is closed and bounded, hence compact. Its projection onto
the second coordinate is exactly \(\Sigma\), proving
compactness.

*Proof of the branch statement.* Factor the monic polynomial
\(\mathsf R/\ell\) over the field \(\mathbb C(x)\):
\[
\frac{\mathsf R(x,Z)}{\ell(x)}
          =\prod_{\nu=1}^{s}F_\nu(x,Z)^{m_\nu},
\qquad
S(x,Z)=\prod_{\nu=1}^{s}F_\nu(x,Z),
                                                                    \tag{6}
\]
where the \(F_\nu\) are distinct monic irreducible polynomials
in \(Z\), with coefficients rational in \(x\).
Characteristic zero implies that the squarefree polynomial
\(S\) has nonzero discriminant in \(\mathbb C(x)\).

Exclude the zeros and poles of that discriminant and all poles
of the coefficients appearing in (6), together with the zeros
of any clearing factors used in its rational identities.
Each is a nonzero one-variable polynomial's zero set, so
only finitely many \(x\)-values are excluded. Outside them,
the specialization of (6) remains an identity, the factors
are monic of unchanged degree, and the specialized \(S\)
has simple roots. In particular its roots are exactly the
roots of the full \(\mathsf R\) there, with only their
multiplicities removed. This is why specialization of a
formal squarefree part is not used at an exceptional value.

Parametrize the arc by \(x(t)=e^{2\pi i t}\).
The excluded points, together with its two endpoints, divide
\([1/2,5/6]\) into finitely many open intervals.
On each such interval all roots of \(S(x(t),Z)\) are simple.
The holomorphic implicit-function theorem gives local
holomorphic root functions; their unique continuation along
the interval gives at most eleven real-analytic root
branches. Continuation cannot stop at an interior parameter:
the coefficients have no pole, every root is bounded by
(4), and the discriminant is nonzero there.
There is no monodromy ambiguity along an interval.

The roots over the finitely many excluded \(x\)-values and
the two arc endpoints are retained separately. Each such fiber is
finite, since the full polynomial \(\mathsf R(x,\cdot)\) still has degree
eleven by (2). This proves the stated finite union.

*Proof of measure zero.* Restrict any one of the analytic
branches to a compact subinterval of its open domain.
Its derivative is bounded, so its image is Lipschitz.
To see directly that such an image has planar measure zero,
partition the subinterval into \(n\) equal parts. Each image
part lies in a disk of radius at most a fixed constant
times \(n^{-1}\); the total area of the \(n\) disks tends
to zero as \(n\to\infty\).

Every open branch interval is a countable union of compact
subintervals. Its entire image therefore has planar measure
zero. The finite branch inventory and the additional finite
fibers preserve that conclusion. A set of planar measure
zero contains no open disk, so its interior is empty.
\(\square\)

Thus \(\mathbb C\setminus\Sigma\) is open and dense in the
ordinary Euclidean topology. No complex Zariski-open
conclusion is asserted. This statement is about the outgoing
parameter plane; it says nothing about the distribution of actual
knot references. An actual reference set could still meet, or lie in,
\(\Sigma\).

## 3. Uniform classical Bezout coefficients off the exceptional set

**Theorem 2.** Let \(\mathcal K\) be a nonempty compact subset of
\(\mathbb C\setminus\Sigma\). There are unique polynomials
\[
A(x,z,Z)=a_0(x,Z)+a_1(x,Z)z,\qquad
B(x,z,Z)=\sum_{j=0}^{10}b_j(x,Z)z^j
                                                                    \tag{7}
\]
such that
\[
\boxed{\qquad
A(x,z,Z)\mathsf P(x,z)
      +B(x,z,Z)\mathsf Q(x,z,Z)=1
       \quad(x\in\mathcal X,\ Z\in\mathcal K).
\qquad}                                                           \tag{8}
\]
Their coefficients are rational functions of \(x,Z\), holomorphic
on a fixed neighborhood of \(\mathcal X\times\mathcal K\),
and uniformly bounded there after shrinking that neighborhood.
Every fixed coefficient derivative has a uniform bound on
a smaller neighborhood.

*Proof.* The original resultant is continuous and nonzero
on the compact product, so
\[
\Delta_{\mathcal K}:=
\min_{\mathcal X\times\mathcal K}|\mathsf R(x,Z)|>0.
                                                                    \tag{9}
\]
Consider the linear coefficient map
\[
\mathbb C[z]_{\le1}\oplus\mathbb C[z]_{\le10}
          \longrightarrow\mathbb C[z]_{\le12},
\qquad (A,B)\longmapsto A\mathsf P+B\mathsf Q.
                                                                    \tag{10}
\]
Its domain and codomain each have dimension thirteen.
It is injective when the two polynomials are coprime:
if \(A\mathsf P=-B\mathsf Q\), then \(\mathsf P\) divides
\(B\), which has smaller degree, so \(B=A=0\).
It is therefore an isomorphism and determines (7)--(8)
uniquely.

In monomial coefficient bases its matrix is a Sylvester
matrix, with determinant equal to \(\mathsf R\) up to sign.
The adjugate formula makes its inverse rational and holomorphic
where that determinant is nonzero. Compactness and (9) give
a common complex neighborhood on which it remains nonzero.
For an explicit bound on the compact product, if \(M_S\ge1\)
bounds all matrix entries, then every coefficient in (7)
has modulus at most
\[
                         \frac{13!M_S^{12}}{\Delta_{\mathcal K}}.
                                                                    \tag{11}
\]
This follows by the cofactor expansion and a row-sum bound
for the inverse. The same argument on a slightly larger
compact neighborhood, followed by Cauchy's formula, gives
the fixed derivative bounds. \(\square\)

In terms of the actual principal Laurent symbols, (8) is
equivalently
\[
x^5z^3A(x,z,Z)\,\mathfrak b(x,z)
 +x^2zB(x,z,Z)\,
                     (\mathfrak j^{\mathrm t}(x,z)-Z)=1.
                                                                    \tag{12}
\]
No original sign or reciprocal shift is changed in this form.

## 4. Scope of the criterion

For a specified actual reference \(Z_*\), proving
\(Z_*\notin\Sigma\) would supply (9) and the classical
coefficient bounds along the complete physical middle arc.
That avoidance has not been proved here.

Even under avoidance, (12) concerns commuting principal
Laurent symbols. The original finite difference operators
have shifted, varying coefficients. Replacing their ordered
products by (12) requires a separate exact error analysis,
including all accumulated shifts and all finite endpoints.
The retained outgoing cutoff forcing and the original
even-level period forcing remain those in the paired-source
note. Their multiplication by any proposed elimination
operators also needs its own estimate.

Accordingly this criterion does not bound the eleven
remainder observations, the complete-color layer, or the
full transfer. It proves a source-specific algebraic
condition and its uniform classical consequence, without
assuming that the original marked reference satisfies it.
