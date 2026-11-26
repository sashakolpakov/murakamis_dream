# Recovery at degenerate parameters by holomorphic continuation

Private written proof, 16 November 2026.

A finite-window matrix can lose rank at a particular microscopic
parameter even when it has full rank for generic parameters. For
the actual source, this need not prevent a uniform upper estimate.
The source is a holomorphic family. Cauchy's formula transfers the
estimate from a small parameter circle where the matrix is well
conditioned to its center, even when the matrix is singular there.

The conclusion uses upper bounds for the supplied data on a complex
neighborhood. It does not create a missing boundary estimate, prove
generic rank, or transfer a lower bound to a special parameter.

## 1. The finite-window setting

Let \(D\subset\mathbb C^s\) be a connected open set of microscopic
parameters, with \(s\ge1\). For each physical level \(N\), let
\[
 X_N:D\longrightarrow\mathbb C^d,\qquad
 B_N:D\longrightarrow\mathbb C^b,\qquad
 F_N:D\longrightarrow\mathbb C^p
 \tag{1}
\]
be the actual holomorphic unknown, supplied-boundary and forcing
packets. The packet \(X_N\) includes every unknown shifted component
and physical first normal specified in the finite-window problem.
All remaining components in the chosen equations are in \(B_N\)
or \(F_N\). Repeated occurrences of the same component are identified.

Split the levels into a fixed finite number of residue classes
\(\sigma\), as in the rational-phase conditioning theorem. Suppose
the exact equations in each class are
\[
 \mathsf A_\sigma(h,\alpha)X_N(\alpha)
       =F_N(\alpha)-\mathsf L_\sigma(h,\alpha)B_N(\alpha),
 \qquad h=1/N,\quad N\in\sigma.
 \tag{2}
\]
We use polynomially cleared equations: on every relatively compact
parameter neighborhood there is an integer \(s_0\ge0\) such that
\(h^{s_0}\mathsf A_\sigma\) and
\(h^{s_0}\mathsf L_\sigma\) are holomorphic and locally bounded
near \(h=0\). A finite number of classes permits one common
power on each such neighborhood.

Assume that, for each class, some full-column minor of the
holomorphic matrix is not the zero germ as a function of
\((h,\alpha)\). On a connected coefficient neighborhood its
expansion therefore has the form
\[
 \det\widehat{\mathsf A}_{\sigma,0}(h,\alpha)
       =h^{\nu_\sigma}
          \{c_\sigma(\alpha)+h r_\sigma(h,\alpha)\},
 \qquad c_\sigma\not\equiv0.
 \tag{3}
\]
Here \(\widehat{\mathsf A}_\sigma=h^{s_0}\mathsf A_\sigma\),
and the subscript zero on the minor labels the selected rows,
not specialization in \(h\). All source equations remain exact.

For clarity, the theorem below may be applied on such a connected
coefficient neighborhood rather than on a larger \(D\). Its generic
minor assumption must hold on a neighborhood of the compact
parameter set to which it is applied. It is not inferred from
the classical principal matrix.

## 2. Circles avoiding the leading-coefficient zero sets

**Lemma 1.** Let \(c_1,\ldots,c_q\) be nonzero holomorphic functions
on connected \(D\), and let \(\alpha_0\in D\). There are a complex
direction \(v\in\mathbb C^s\), a radius \(r>0\), a neighborhood
\(U\) of \(\alpha_0\), and a constant \(\delta>0\) such that:

* all disks \(\alpha+zv\), \(|z|\le r\), \(\alpha\in\overline U\),
  lie in one compact subset of \(D\);
* on their boundary circles,
  \[
       |c_i(\alpha+r e^{i\theta}v)|\ge\delta
       \quad(\alpha\in\overline U,\ \theta\in[0,2\pi],\
                                                    1\le i\le q).
  \tag{4}
  \]

*Proof.* The product \(c=\prod_i c_i\) is a nonzero holomorphic
function. Its germ at \(\alpha_0\) is not zero, by the identity
theorem on the connected domain. In its Taylor expansion about
\(\alpha_0\), let \(P_k\) be the first nonzero homogeneous term.
Choose \(v\) with \(P_k(v)\ne0\). Then
\[
             c(\alpha_0+zv)=z^k(P_k(v)+O(z)).
\]
For sufficiently small \(r>0\), this has no zero on
\(|z|=r\), and its whole disk lies compactly in \(D\).
Each factor \(c_i\) is nonzero on that circle. Compactness gives
a positive minimum for every factor. Uniform continuity and
a smaller neighborhood \(U\) preserve these minima, and also
keep every translated disk inside a compact subset of \(D\).
Taking the smallest of the finitely many lower bounds gives
(4). \(\square\)

For any holomorphic vector function \(H\) on these disks,
the ordinary one-variable Cauchy formula gives exactly
\[
 H(\alpha)=\frac1{2\pi}
          \int_0^{2\pi}H(\alpha+r e^{i\theta}v)\,d\theta ,
 \qquad
 \|H(\alpha)\|\le
       \sup_\theta\|H(\alpha+r e^{i\theta}v)\|.
 \tag{5}
\]
Only the parameter is moved. Physical colors, levels, twist
powers, the chosen row window and the original closing conventions
are unchanged.

## 3. A uniform upper bound on compact parameter sets

**Theorem 2.** Under (1)--(3), for every compact
\(K\Subset D\) in a common coefficient neighborhood there exist
a compact \(K'\Subset D\), constants \(C>0\), \(k\ge0\),
and \(N_0\), such that
\[
 \sup_{\alpha\in K}\|X_N(\alpha)\|
       \le C N^k
          \sup_{\beta\in K'}
                  \bigl(\|F_N(\beta)\|+\|B_N(\beta)\|\bigr)
                    \qquad(N\ge N_0).
 \tag{6}
\]
The compact \(K'\) is fixed before \(N\) tends to infinity.
The bound holds even at parameters where every actual
full-column minor vanishes. It estimates the actual holomorphic
source; it is not a bounded pointwise inverse of a singular matrix.

*Proof.* Apply Lemma 1 to the finitely many functions
\(c_\sigma\) in (3). On the compact family of parameter circles
around any fixed \(\alpha_0\), all these functions have a
common positive lower bound. The remainder terms in (3) are
uniformly bounded there. For all sufficiently small positive
\(h\), the selected minor in each residue class consequently
has modulus at least \(\delta h^{\nu_\sigma}/2\).

The entries of its adjugate are bounded, since the matrix size
is fixed and the entries of \(\widehat{\mathsf A}_\sigma\) are
bounded. Thus the finite-window inverse estimate applies on
every boundary circle:
\[
 \|X_N(\alpha+r e^{i\theta}v)\|
   \le C_{\alpha_0}N^{k_{\alpha_0}}
        \bigl(\|F_N(\alpha+r e^{i\theta}v)\|
                 +\|B_N(\alpha+r e^{i\theta}v)\|\bigr).
 \tag{7}
\]
The powers used to clear \(h\), and the polynomial norm of
\(\mathsf L_\sigma\), are included in \(k_{\alpha_0}\).
All estimates are uniform on the circle family and across
the finitely many residue classes.

Apply (5) to the actual function \(X_N\). This proves (6)
on a neighborhood of \(\alpha_0\), with the right side taken
over that fixed compact family of circles. Cover \(K\) by
finitely many such neighborhoods. Their circle families have
compact union \(K'\Subset D\). Take the largest exponent,
constant and threshold among the finite choices. This proves
(6). The proof never inverts a matrix at a degenerate parameter.
\(\square\)

In particular, if the supplied packets have locally uniform
bounds on \(D\) with parameter-independent exponents
\[
 \|F_N(\alpha)\|\le e^{NA_F+o_K(N)},\qquad
 \|B_N(\alpha)\|\le e^{NA_B+o_K(N)}
                       \quad\text{on each }K\Subset D,
 \tag{8}
\]
then
\[
 \limsup_N \frac1N\log
          \left(1+\sup_{\alpha\in K}\|X_N(\alpha)\|\right)
                  \le \max(0,A_F,A_B).
 \tag{9}
\]
The zero in this display comes only from the explicit \(1+\).
Without it, the corresponding upper rate is at most
\(\max(A_F,A_B)\), with \(\log0=-\infty\).
Every fixed parameter derivative has the same upper exponent:
first apply (6) on a compact neighborhood of \(K\), then use
Cauchy's derivative estimate on smaller parameter polydisks.
Physical first normals are already part of \(X_N\).

The exponent in (8) must hold on the surrounding complex
neighborhood. A bound known only at one real parameter, or
only for a real family, does not supply (7).
If the rate depends on parameters, (6) retains its supremum
over \(K'\); it does not automatically give the rate at the
center.

## 4. Uniqueness of a holomorphic source family

**Corollary 3.** For each sufficiently large fixed level, there
is at most one holomorphic solution of (2) on connected \(D\)
with the prescribed holomorphic supplied data, under the generic
minor hypothesis above.

*Proof.* Fix the residue class of \(N\). Since \(c_\sigma\)
is not identically zero, choose a parameter where it is nonzero.
The expansion (3) shows that the selected minor, as a
holomorphic function of \(\alpha\) at this fixed sufficiently
small \(h\), is not identically zero. It is nonzero on a
nonempty open set. Two holomorphic solutions with the same
right side agree there by full column rank. Their difference
is a holomorphic vector function, so the identity theorem
makes it zero on connected \(D\). The finitely many classes
permit a common threshold. \(\square\)

This clarifies the distinction in the rank-loss theorem.
A singular matrix at one parameter can leave an algebraic
first-normal freedom at that parameter. If the entire source
is a holomorphic family determined at generic parameters,
that isolated freedom cannot be chosen independently.
Its value is fixed by the family. This does not apply when
all candidate minors vanish identically in parameters.

## 5. Application to the repeated-turn source and its limits

The actual repeated-turn source is holomorphic in the
microscopic parameters \(\alpha_i\): each
\(w_i=2\cosh(\alpha_i/N)\) is entire, the original kernel is
polynomial in \(w_i\), and finite multiplication, canonical
reduction and the original linear turns preserve this
dependence. The same is true of its physical values and
first normals. For this application use the original
polynomially cleared equations and a common coefficient
neighborhood as specified in section 1.

The rational-phase window theorem provides the finite
residue classes and meromorphic coefficient germs. Once
the required full-column minor is proved to be a nonzero
germ in \((h,\boldsymbol\alpha)\) in each class, Theorem 2
extends its polynomial-cost estimate across the leading
coefficient's parameter zeros for the actual source.
Consequently proving a nonzero minor at every parameter
separately is unnecessary for this upper-bound step.

Three qualifications remain substantive:

* Generic full rank for a suitable complete window has
  not been proved for every resonant product.
* Every supplied packet remains on the right of (6).
  A right boundary known only at a larger exponential
  rate still supplies that larger rate. Holomorphic
  continuation does not change the direction of transport.
* The conclusion is an upper estimate and uniqueness
  within a prescribed holomorphic family, not a lower
  coefficient statement. For example
  \(H_N(\alpha)=\alpha e^{NA}\) is holomorphic, has rate
  \(A\) at every fixed \(\alpha\ne0\), and vanishes at
  \(\alpha=0\). Generic nonvanishing does not exclude
  this behavior.

This result therefore removes parameter-specific inverse
difficulties from a conditional source estimate. It does
not prove that a fixed knot's geometric contribution
survives, or establish the finite-exception filling theorem.

## 6. Coverage and direct sources

The use of Cauchy's formula for fixed parameter derivatives
is already widespread in the research notes. The additional
statement here uses parameter circles to transfer a recovery
estimate across the zero set of the matrix's leading minor.
The circle construction and uniqueness argument are proved
above; no new theorem about abstract torsors is assumed.

Complete direct sources at their recorded pins:

* [Rational-phase window conditioning](research_resonant_physical_window_conditioning.md),
  SHA256 f1af212ec05ffdb79cc9b99ce03961622740d58622213e648918000e81e5fa07:
  exact unknown and supplied packets, finite residue classes,
  nonzero meromorphic minors and polynomial conditioning.
* [Exact rank loss and the remaining normal](research_simple_rank_loss_full_normal_transport.md),
  SHA256 307a26ca51fc9b0cc7bff689f52a873a49d7773406e67d243ec71021401e4694:
  pointwise first-normal freedom and the full stacked-row criterion.
* [Full-step repeated-turn source](research_full_step_repeated_turn_tensor_interface.md),
  SHA256 ef851eab40c8b2c44388a41d324e2fa41d4400f0f2118fe587405911e00e3398:
  original holomorphic parameter dependence and cleared exact rows.

Only written mathematics and source-text/hash reads were used.
No mathematical program, test, numerical experiment or compilation
was run. The frozen manuscripts and public documentation are unchanged.
