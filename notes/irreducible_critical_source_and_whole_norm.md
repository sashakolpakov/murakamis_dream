# Irreducible critical sources force nonzero conjugate coefficients

Research theorem, 27 October 2026. A fixed whole algebraic critical
source can provide more than uniqueness of a proposed comparison:
Galois descent can force its geometric coefficient to be nonzero.
The required source density is recovered from finitely many exact
moments. A fixed algebraic presentation also gives polynomial bounds
on every coefficient along the actual cyclotomic source arc, even
though the degrees of the specialized cyclotomic fields grow.

These results supply a finite target for an action-normalized selected
period comparison. They do not construct that comparison from the
actual quantum state. In particular, algebraicity of Rivin's critical
shapes alone does not prove the hypotheses below or the volume norm.

## 1. A descended source cannot kill one embedding of a field

Let F be a characteristic-zero field and let A/F be a finite field
extension of degree d. Let P be a rank-one A-line, with a source
\(\psi\in P\) and an F-linear co-source \(\lambda:P\to F\).
There is a unique A-linear map \(\eta:P\to A\) such that

\[
                 \lambda=\operatorname{Tr}_{A/F}\circ\eta.
                                                               \tag{1.1}
\]

Indeed choose a generator p of P. The trace pairing on A is
nondegenerate, so \(x\mapsto\lambda(px)\) is uniquely
\(x\mapsto\operatorname{Tr}(bx)\) for some b. Put \(\eta(px)=bx\).
To prove nondegeneracy directly, choose a primitive element theta
with distinct conjugates \(\theta_i\). The trace Gram matrix in
\(1,\theta,\ldots,\theta^{d-1}\) is \(V^tV\), where
\(V_{ij}=\theta_i^j\). Its determinant is the nonzero squared
Vandermonde product.

Put \(a=\eta(\psi)\). After splitting A over an algebraic closure,
the source coefficient at its i-th primitive idempotent is exactly

\[
                   \lambda(e_i\psi)=\sigma_i(a).       \tag{1.2}
\]

Thus if \(\psi\ne0\) and \(\lambda\ne0\), every coefficient in
(1.2) is nonzero. The field assumption matters: multiplication by
two nonzero elements cannot give zero. A particularly simple exact
certificate is

\[
                         \lambda(\psi)=1,             \tag{1.3}
\]

since \(\operatorname{Tr}(a)=1\) forces \(a\ne0\).
Changing the generator of P changes b and the coordinate of psi
inversely, and leaves a unchanged. A Gaussian determinant line or
its marked algebraic density can therefore be retained as P; no
arbitrary scalar trivialization is required. Multiplication by a
fixed nonzero algebraic Jacobian or density preserves nonvanishing.

For an A-module P of higher finite rank, (1.1) still holds by an
A-basis. The certificate (1.3) still implies every coefficient of
the paired element \(a=\eta(\psi)\) is nonzero. Merely assuming that
psi and lambda are individually nonzero is sufficient only in rank
one, where their product cannot vanish.

This proves a useful replacement for an independently assumed
nonzero geometric weight. It requires the ACTUAL source and co-source
to descend to this irreducible algebra. A nonzero pairing elsewhere
in a larger critical algebra does not prove (1.3) on its geometric
component.

## 2. The source density is an exact finite moment calculation

Write \(A=F[\theta]\), with a specified irreducible separable
polynomial p of degree d. Suppose the actual proposed source descent
supplies the finite moments

\[
 m_j=\lambda(\theta^j\psi),\quad 0\le j<d,\qquad
 G_{ij}=\operatorname{Tr}_{A/F}(\theta^{i+j}).
\]

Then the density \(a=\sum_{i=0}^{d-1}a_i\theta^i\) is determined by

\[
                         G(a_i)_i=(m_j)_j.             \tag{2.1}
\]

The same nonzero Vandermonde determinant makes G invertible. Thus a
whole period comparison need not guess its co-source density: these
d exact moments construct its only possible density. In particular
\(a\ne0\) if and only if the moment vector is nonzero, and \(m_0=1\)
is a direct certificate.

If a proposed critical observable Theta acts on a finite F-space V,
has irreducible characteristic polynomial of degree \(\dim_FV=d\),
and the source psi is nonzero, then \(V=A\psi\). Indeed A is a field
of dimension d and the map \(A\to V\), \(x\mapsto x\psi\), is
injective. It is therefore an isomorphism. In this situation (2.1)
uses actual moments \(\lambda(\Theta^j\psi)\). Any operator commuting
with Theta is multiplication by an element of A, and the selected
scalar is its trace against a. The same statement holds after a
specified period-ring extension, for an action operator in that
commutant.

To apply this to the knot, one must construct Theta or the critical
line on an ACTUAL source quotient and prove the moment descent.
The gluing critical field by itself is not such an operator. Neither
an abstract isomorphism of Borel groups nor the existence of a local
Gaussian block supplies these finite moments.

## 3. Exact normalized traces give another nonvanishing certificate

Irreducibility can be replaced by a stronger trace realization.
Let A be any finite etale F-algebra, faithfully represented on V,
and let \(\lambda(x)=\operatorname{Tr}_V(x)/\dim_FV\), with source
the identity. After splitting A, each primitive idempotent e_i is
a nonzero projection. Thus

\[
              \lambda(e_i)=\frac{\operatorname{rank}e_i}{\dim_FV}
                            \ne0.                    \tag{3.1}
\]

No positivity, self-adjointness, or irreducibility is needed: an
idempotent has eigenvalues zero and one, and its trace is its rank.
Equivalently, for \(A=\prod K_j\), a faithful A-module has positive
integer multiplicities \(r_j\), and its trace density on K_j is
\(r_j/\dim_FV\).

Even if \(\dim V_N\le C N^b\) grows, the weights in (3.1) lie
between \(C^{-1}N^{-b}\) and one. They cannot exponentially suppress
a geometric sector. Multiplying by a fixed algebraic Gaussian
density which is a UNIT on the selected etale algebra preserves
this conclusion by Section 4. Nondegeneracy must hold on each
selected component; a nonzero density on only one factor of a
product would not suffice.

The actual compact cut is a normalized matrix trace, but this does
not by itself establish (3.1) for a geometric critical sector.
One needs an exact trace-compatible critical summand of the actual
transfer or relative period object. Embedding an unrelated critical
algebra into a color matrix algebra is insufficient. In particular,
the already closed one-cut knot matrix is scalar; projecting that
matrix repeats the SAME scalar and does not decompose its phases.

## 4. A fixed whole presentation gives polynomial bounds on the root arc

Use the root SOURCE slice, after fixing its actual finite phases and
power coordinates \(Q^N=1\), \(M=1\), \(M^N=1\). On this slice put

\[
 F=k(t,Q),\quad k\subset\mathbb C,\qquad (t,Q)=\gamma(1/N)
              =(1/N,\exp(c/N)),\quad c=2\pi i.         \tag{4.1}
\]

Fix the displayed embedding of k in the complex numbers. The following
statement concerns this slice, not the larger space
in which \(Q^N\) is an independent quantum-normal coordinate.
Any fixed residue class of levels needed for a marked finite phase
can be used. All constants below are uniform along that class.

**Polynomial bound theorem.** Let a be a nonzero element of a fixed
finite field extension A/F. For every conjugate value a_(i,N) of
its specialization on (4.1), all sufficiently large N satisfy

\[
                    C^{-1}N^{-B}\le |a_{(i,N)}|
                                           \le C N^B. \tag{4.2}
\]

The constants depend on the fixed whole algebraic presentation,
not on N or the chosen conjugate. No bounded degree of the specialized
absolute cyclotomic fields, height assumption, or coherent choice of
one analytic branch is needed.

Here is an elementary proof. For any nonzero polynomial

\[
 R(t,Q)=\sum_j p_j(t)Q^{n_j},\qquad n_j\text{ distinct},
\]

the pullback \(R(t,e^{ct})=\sum_jp_j(t)e^{cn_jt}\) is nonzero.
To see linear independence, isolate one exponential by applying
\(\prod_{k\ne j}(\partial_t-cn_k)^{\deg p_k+1}\). On its polynomial
factor the remaining operators are \(\partial_t+c(n_j-n_k)\),
each invertible on a bounded polynomial space, so a nonzero p_j
cannot be killed. If
\(m=\sum_j(\deg p_j+1)\), the entire sum solves the constant
coefficient equation
\(\prod_j(\partial_t-cn_j)^{\deg p_j+1}f=0\) of order m.
Its coefficient recursion shows that a zero of order m would force
all Taylor coefficients to vanish. Therefore

\[
               \operatorname{ord}_{t=0}R(t,e^{ct})\le m-1.
                                                               \tag{4.3}
\]

This also proves Zariski density of the arc (4.1) on this two-variable
source slice. After clearing Laurent powers it applies to every
nonzero rational numerator or denominator on that slice.

Choose a polynomial relation for a over F, clear denominators and
write it as \(\sum_{j=0}^dR_j(t,Q)a^j=0\), with both \(R_0\) and
\(R_d\) nonzero. Such a relation exists with nonzero constant term
because a is nonzero in a field. On the arc every nonzero coefficient
has a finite order at zero by (4.3). Hence for small positive t,
\(|R_d|\ge c_1t^{\nu_d}\), \(|R_0|\ge c_1t^{\nu_0}\), while all
coefficients are bounded above. The elementary Cauchy root bound
applied to this polynomial gives \(|a_i|\le C t^{-\nu_d}\).
Applied to its reciprocal polynomial it gives
\(|a_i|\ge C^{-1}t^{\nu_0}\). This proves (4.2), uniformly over all
its roots. Formula (4.3) gives explicit exponents from the fixed
coefficient supports.

Apply this to the source density a in Section 1. Irreducible descent
and the retained nonzero normalization force ALL geometric conjugate
coefficients to be eventually nonzero and subexponential. This does
not assume their nonvanishing separately.

## 5. Height hypotheses: what suffices and what does not

There is also a simple arithmetic criterion, independent of degree.
If a nonzero algebraic number alpha satisfies some integer polynomial
whose coefficient maximum is H, then

\[
                       (1+H)^{-1}\le|\alpha|\le1+H.    \tag{5.1}
\]

Remove zero constant powers first. The leading and constant integer
coefficients then have absolute value at least one. For \(|z|>1+H\),
the sum of the lower terms is smaller than the leading term by the
geometric-series estimate \(H/(|z|-1)<1\); this proves the upper
bound. Reverse the polynomial for the lower bound. Consequently
\(\log H_N=o(N)\) forces \(\log|\alpha_N|=o(N)\), with NO condition
on the polynomial degrees. This strengthens the sufficient
degree-and-height estimate in the
[earlier global function audit](global_period_rigidity_function_audit.md).

H here is the naive coefficient height of an absolute integer
annihilating polynomial, not the absolute logarithmic Weil height.
Bounded Weil height without a degree bound is insufficient. For
N>=2, the polynomial

\[
                    z^N-2^Nz^{N-1}-2                \tag{5.2}
\]

is irreducible by the elementary Eisenstein argument at two: reducing
a hypothetical monic integer factorization modulo two gives powers
of z, so both constant terms would be even and their product would
be divisible by four. It has one real root alpha_N in
\((2^N,2^N+1)\). Every root with modulus at least one lies in
\(|z-2^N|\le2\), since \(z^{N-1}(z-2^N)=2\). On that disk,
\(z\mapsto2^N+2z^{-(N-1)}\) is a strict contraction, so it has at
most one root there. Thus every other conjugate has modulus less
than one. The Weil height is \(\log\alpha_N/N\), bounded and tending
to log two, while \(N^{-1}\log|\alpha_N|\to\log2\ne0\).

Bounded defining height of the TORSOR alone says even less: a fixed
\(\mathbb G_m\) torsor contains the points \(2^N\). The whole section
or its selected-point height must be controlled. The fixed algebraic
section theorem in Section 4 is one way to obtain control which does
not require estimating absolute cyclotomic polynomial heights.

## 6. Two sharp limitations of irreducibility and normalization

First, a split algebra can kill the geometric point. For
\(A=F\times F\), source \((1,1)\), and co-source
\(\lambda(x,y)=y\), the normalization is one but the first primitive
coefficient is zero. The same failure can occur if a co-source is
allowed coefficients in a splitting field rather than descending
to F. Thus levelwise algebraicity over \(\mathbb Q(\zeta_N)\) is not
the whole descent assumption in Section 1. A fixed shape field can
intersect these cyclotomic fields and split after such a base change.
The theorem requires one whole descended co-source before these
specializations, or the faithful trace realization of Section 3.

Second, even field descent and normalization do not bound a merely
levelwise source. In \(A=\mathbb Q(\sqrt2)\), take

\[
                  a_N=(1+2^N\sqrt2)/2,
                  \operatorname{Tr}(a_N)=1.           \tag{6.1}
\]

Both coefficients are nonzero but have exponential size. Multiplying
a geometric exponential by either changes its rate by log two.
The fixed quadratic field, its discriminant, and the normalization
remain unchanged. The selected point has exponentially growing
naive height; (6.1) is not a fixed algebraic function of \((t,Q)\)
on (4.1). This separates finite-type geometry from bounded complexity
of its selected section.

## 7. The resulting action-normalized period criterion

Suppose an ACTUAL scalar period has been represented, with its
source/cut preserved, in a finite global period space as

\[
 P_N=\sum_{i=1}^{d} a_{(i,N)}G_{(i,N)}.                \tag{7.1}
\]

Assume its source density is the fixed whole element of Sections
1--4, or its coefficients have the faithful trace weights of Section
3 times a fixed algebraic density which is a unit on every selected
component. Suppose a specified
geometric index g has

\[
 \frac1N\log|G_{(g,N)}|\longrightarrow s_g,\qquad
 |G_{(i,N)}|\le\exp(N(s_g-\delta))\quad(i\ne g)
                                                               \tag{7.2}
\]

for some positive delta and all sufficiently large N. The polynomial
bounds and nonvanishing already proved imply

\[
                         \frac1N\log|P_N|\longrightarrow s_g.
                                                               \tag{7.3}
\]

Indeed the total of the other finitely many terms divided by the
geometric term tends to zero exponentially, up to polynomial factors.
This proves both the upper and lower rate, including cancellation
control. It does not assume nonvanishing of the geometric coefficient
as an extra hypothesis.

If (7.1) is instead a proposed leading-block formula with a remainder,
the TOTAL remainder requires a smaller-rate bound as well. Strict
Rivin concavity on the positive real angle domain does not bound all
other complex critical sectors or supply that global estimate.

For the knot, the marked regulator gives \(s_g=\operatorname{Vol}/(2\pi)\)
on the geometric period. The unresolved input is the source-preserving
global period-line realization (7.1), together with (7.2), not another
Taylor coefficient at the unique algebraic optimizer. The moment
formula (2.1) and trace criterion (3.1) are exact, finite algebraic
certificates for the missing source part of such a realization.

This is separate from
[actual Mellin root reconstruction](mellin_cyclotomic_jet_uniqueness.md):
that theorem fixes the whole root function once the actual bounded
quantum source jets and pole lattice are supplied. It does not yet
construct the action-normalized critical trace (7.1). Nor does the
present result replace the ACTUAL generally transcendental selected
Mellin section by an algebraic function; the
[adequate-knot transcendence theorem](adequate_mellin_transcendence.md)
already excludes that replacement.

The complementary [whole-unit weight theorem](whole_torsor_unit_weights_and_irregular_type.md)
shows why finite type of the torsor CONNECTION is weaker than the
bounded algebraic coefficient hypothesis in Section 4: a growing
character of one fixed regular algebraic unit can carry a nonzero
normal action. Its marked connection and character must be retained,
even when the unit has classical value one.

[Exact diagnostics](../experiments/audit_irreducible_critical_source.py).
[Results](../experiments/irreducible_critical_source_results.json).
[Independent proof audit](doubled_phase_and_critical_source_independent_audit.md).

[Independent proof audit](doubled_phase_and_critical_source_independent_audit.md).

The subsequent [actual pointed-commutant theorem](actual_pointed_commutant_and_critical_observable.md)
rules out obtaining this irreducible critical observable as a whole
horizontal endomorphism of the original pointed Mellin lattice. The
[dual-clock theorem](dual_clock_normal_cut_source.md) also shows that
raw framing moments have infinite Hilbert-matrix rank; they are not
the isolated transverse critical algebra. A finite list of proposed
moments constructs a density only AFTER the critical polynomial
action or quotient has been supplied and verified. These tests do
not infer critical descent from a finite moment fit.
