# The genuine adjacent observable algebra and its macroscopic source filtration

29 October 2026. Two ACTUAL adjacent interval Casimirs already generate
the full matrix algebra on the complete three-head source multiplicity.
This narrows the older arbitrary-coupon quotient obstruction to a small
physical moment-map algebra. Its proof is constructive and retains the
original nilpotent normal source.

The associated filtration is equally important: bounded-degree source
tests see zero until an integer traversal of length N-1. A single
original crossing has precisely that macroscopic observable degree.
Thus full matrix generation does not disprove a filtered or microlocal
geometric reduction, and low-degree source-null identities do not by
themselves control its norm.

## 1. Original matrices, sources and charts

Let N>=2, d=N-1, q=exp(pi*i/N), Q=q^2, x=q^d, rho=q-q^(-1).
On the COMPLETE original W=(V tensor V)_(degree d), use e_j=|j,d-j>.
The actual interval Casimirs A=Omega12 and B=Omega23, in the left
highest chart, are

\[
 A_{j,j}=q+q^{-1}-q(1-Q^j)^2-q^{-1}(1-Q^{j+1})^2,
 \qquad A_{j-1,j}=A_{j,j-1}=-(1-Q^j)^2,                       \tag{1}
\]
\[
 Be_j=c_je_j+b_je_{j-1},\qquad
 c_j=q^{2j+1}+q^{-2j-1},\quad b_j=Q^j+Q^{-j}-2.              \tag{2}
\]

All off-diagonal coefficients in (1) are nonzero. Put c*=q+q^(-1).
The original cup and ordinary cap are

\[
 p_j=Nx^{j-d},\qquad \ell_j=x^{-j}Q^{-j}/N=x^j/N.
\]

The complete anti-Pascal chart J satisfies the exact source identities

\[
 JB=AJ,\quad JAJ^{-1}=B^{\mathsf T},\quad
 Jp=Nx^{-d}e_d,\quad \ell J^{-1}=(x^d/N)e_0^{\mathsf T}.      \tag{3}
\]

These are the original coproduct and actual cap identities from
[the complete source theorem](actual_complete_source_multiplicity_module.md),
not a semisimple replacement. In particular all N multiplicities,
both members of every colliding Casimir pair, and even levels remain.

## 2. A tame nilpotent source operator generates all channels

The monic characteristic polynomial of A is

\[
 \mathcal P_N(z)=\prod_{j=0}^d(z-c_j)=2T_N(z/2)+2.
\]

Its roots have multiplicity two, except the simple root -2 when N
is odd. At N=2 it is z^2, so the following construction also applies.
The irreducible Jacobi matrix A has cyclic endpoint vectors; hence
its minimal polynomial is this full degree-N polynomial.

Set Q0(z)=P_N(z)/(z-c*)^2. Define the explicit degree-d observable

\[
 \Xi_0(A)=\frac{(A-c*)Q_0(A)}{Q_0(c*)}.
\]

Then

\[
 \boxed{\displaystyle
 \Xi_0(A)=\theta p\ell,\qquad
 \theta=(-1)^N\rho^2\ne0.}                                  \tag{4}
\]

Here is a proof not assuming a Jordan basis. At all other Casimir
nodes the polynomial has the full required vanishing multiplicity.
At c* it has value 0 and derivative 1. The eigenspace of an
irreducible Jacobi matrix is one-dimensional, so its range is the
original eigenline Cp and its row is the original eigenrow Cell.
The coefficient is fixed by its (0,d) entry. Lower matrix powers
cannot connect d to 0, and

\[
 (A^d)_{0,d}=\prod_{j=1}^d[-(1-Q^j)^2]=(-1)^dN^2.
\]

The elementary Chebyshev differential equation at the double zero
gives Q0(c*)=N^2/(4-c*^2)=-N^2/rho^2. Since p0 ell_d=1,
the coefficient in (4) is theta. This proves its normalization,
including the exceptional N=2 case.

In the original positive physical norm,

\[
 \|\Xi_0(A)\|_{\mathrm{op}}=N|\rho|^2\leq4\pi^2/N.                \tag{5}
\]

Indeed ||p||^2=N^3 and ||ell||^2=1/N. This rank-one normal source
is polynomially controlled; it is not an exponentially conditioned
projector. It is nonzero even though it is square-zero, because
ell p=0.

For 0<=r,s<=d,

\[
 B^r\Xi_0(A)B^s=\theta(B^rp)(\ell B^s).                     \tag{6}
\]

By (3), the columns B^r p are a basis: their J images are a nonzero
constant times A^r e_d, which are triangular endpoint Krylov columns.
The rows ell B^s are also a basis, since their products with J^(-1)
are a nonzero constant times e0^T A^s. Therefore the N^2 operators
in (6) are a basis of End(W). In particular

\[
 \boxed{\displaystyle \mathbb C\langle A,B\rangle
                              =\operatorname{Mat}_N(\mathbb C).} \tag{7}
\]

No arbitrary Borel-relative matrix coupon is needed for (7): A and B
are the two actual adjacent interval observables.

## 3. Consequence for an exact positive or invariant quotient

Suppose a linear quotient q0:W->H is compatible with these two
observables: q0 A=A' q0 and q0 B=B' q0. Its kernel is invariant under
(7), and is therefore either 0 or all of W. If it preserves the
original source and its inserted observable values it cannot be the
zero quotient, since

\[
 \ell B^d p=(-1)^dN^2\ne0.                                  \tag{8}
\]

Thus it is injective. Equivalently, a positive semidefinite packet
Gram whose nullspace is invariant under BOTH actual observables
cannot remove a source channel: its nullspace is 0 or it kills
the entire original source representation.

A multiplicative quotient imposing a nonzero relation on this actual
observable algebra is likewise impossible while retaining all source
insertions. In particular setting the rank-one normal (4) to zero
generates the whole matrix ideal by (6). This is a restriction on
an EXACT observable-compatible quotient, not a no-go theorem for a
nonmultiplicative Ward pushforward, a current-complex reduction, or
a geometric comparison after taking semiclassical asymptotics.
Nor does it preclude a faithful embedding of W into a larger positive
angle space satisfying additional edge constraints. Such an embedding
need not be a smaller quotient of this observable representation.

The same statement applies to a reflected double IF both copies of
the actual observable algebra are retained independently: (7) then
gives the full matrix algebra on W tensor conjugate(W). It is not
asserted for a construction that retains only synchronous diagonal
braid action and no independent copy observables.

## 4. The exact source filtration: degree N-1 is essential

Define

\[
 \mathcal F_m=\operatorname{span}\{p,Bp,\ldots,B^mp\},
 \qquad0\leq m\leq d.
\]

The endpoint Jacobi calculation and (3) give EXACTLY

\[
 J\mathcal F_m=\operatorname{span}\{e_{d-m},\ldots,e_d\},
 \quad\dim\mathcal F_m=m+1,
 \quad A\mathcal F_m\subset\mathcal F_m,
 \quad B\mathcal F_m\subset\mathcal F_{m+1}.                 \tag{9}
\]

The A statement uses JAJ^(-1)=B^T, which is LOWER bidiagonal, and
therefore preserves the displayed terminal coordinate subspace.
Also

\[
 \ell|_{\mathcal F_{d-1}}=0,\qquad
 \ell B^m p=0\ (m<d),\qquad
 \ell B^d p=(-1)^dN^2.                                    \tag{10}
\]

More generally EVERY mixed word with fewer than d occurrences of B
has zero original pairing ell w(A,B)p, independently of the number
of A factors. In the J chart each B can lower the integer index by
at most one, each A preserves or raises it, and the source travels
from d to 0. Thus there is no cyclic shortcut.

At the first detected degree the complete associated-graded source
is explicit. For any nonnegative integers a0,...,ad,

\[
 \boxed{\displaystyle
 \ell A^{a_0}B A^{a_1}B\cdots B A^{a_d}p
       =(-1)^dN^2\prod_{j=0}^d c_j^{a_j}.}                  \tag{11}
\]

With exactly d lowering opportunities, every B must use its lowering
Jacobi entry and every A its diagonal entry. This proves (11) as a
unique finite path, with all original source constants cancelling
as (Nx^(-d))(x^d/N)=1. In particular, for N>=3 and 1<=r<=d-1,

\[
 \ell B^{d-r}(A-c*)B^rp
                =(-1)^dN^2(c_r-c*)\ne0.                    \tag{12}
\]

The local cup relation (A-c*)p=0 therefore cannot be reimposed
after an arbitrary legitimate exterior. Its first detectable
exterior has macroscopic observable degree, not bounded degree.
For the selected normal (4), the exact factorization (6) implies
that an exterior on BOTH sides needs at least d B occurrences on
each side before the original scalar can detect it.

Its retained response is nevertheless explicitly local, rather than
an unspecified lost normal direction. For ANY allowed exteriors U,V,

\[
 \ell U\Xi_0(A)Vp=\theta(\ell Up)(\ell Vp).                 \tag{12a}
\]

This is the actual cup--cap rank-one surgery (4), with its known
normalization; it does not define a metric from an unknown closed
period. The individual factors still require their own estimates.
With r such normals the exact correction is
\(\ell U_0\Xi_0U_1\cdots\Xi_0U_rp
=\theta^r\prod_{j=0}^r(\ell U_jp)\).
All factors are in the SAME original cap/cup normalization; converting
them to separately normalized knot periods retains their individual
known external lines. No inequality between their volumes is implied.

## 5. A fixed braid already reaches the macroscopic degree

This degree distinction is not permission to ignore it for fixed
knot diagrams. The actual adjacent crossing is
R23=kappa r_N(B), a polynomial of degree<N. Its coefficient at B^d
has EXACT modulus N^(-2):

\[
 \boxed{\displaystyle
 [B^d]R_{23}=\frac{\kappa(-1)^d x^{-d}}{N^2}.}                \tag{13}
\]

To prove it directly from the original crossing, highest-chart
extraction forces one finite transfer and gives
(R23 p)_j=kappa p_j F_(d-j). Therefore

\[
 \ell R_{23}p=\kappa x^{-d}
       \sum_{k=0}^d Q^{k+1}F_k=\kappa x^{-d}.                \tag{14}
\]

The last sum telescopes, Q^(k+1)F_k=F_k-F_(k+1), with F_N=0.
All lower polynomial degrees pair to zero by (10), proving (13).
In particular the original crossing really has degree d, at every
level, and its first detected source coefficient is polynomially
large rather than exponentially suppressed.

A fixed number of actual crossings can therefore expose the normal
even though low-degree observable tests cannot. From (12a),(14),

\[
 \ell R_{23}\Xi_0(A)R_{23}p
         =\theta\kappa^2x^{-2d}=\theta x^{-d}\ne0,            \tag{14a}
\]

of exact modulus |rho|^2. This is a polynomial-sized normal current
between TWO original crossings. It must not be set to zero in an
exact source identity, but it is compatible with a filtered
construction that explicitly retains and estimates polynomial
normal counterterms. These statements concern the specified
complete source sector; no rank-one formula is asserted on an
unrestricted larger multiplicity space without its actual charge
projector.

For any polynomial f of degree<d, (14) also gives the elementary
operator-norm separation

\[
 \|R_{23}-f(B)\|_{\mathrm{op}}\geq1/N,                            \tag{15}
\]

since the original source has dual product ||ell|| ||p||=N.
This does not preclude a polynomial-error approximation at a
specified order or an exponentially normalized upper comparison.
It does show that fixed-degree truncation does not preserve even
the first nonzero original source value automatically.

The viable filtered alternative must therefore state how its
fixed-degree Ward equations act on these degree-N crossing packets,
including the retained normal source and the norm of the resulting
counterterms. Low-degree tests against the bare cup are identically
zero, so they cannot alone certify a nonzero geometric component or
a polynomial-cost positive reduction. No sharp global energy estimate
or obstruction to a properly controlled microlocal quotient follows
from (7) alone.

## 6. Original braid algebra at prime levels

For completeness there is an actual-word strengthening along every
prime level. At an odd prime N, the nodal eigenvalues
nu_j=(-1)^j q^[j(j+1)] coincide only at the paired indices j+l=d.
Indeed equality implies N divides (j-l)(j+l+1); for distinct indices
primality forces j+l+1=N. At every double Casimir node r_N' is
nonzero. Finite Hermite interpolation therefore recovers A as a
polynomial in R12, and B as the same polynomial in R23. Hence

\[
 \mathbb C\langle R_{12},R_{23}\rangle=\operatorname{Mat}_N
                    \quad\text{for every prime }N.          \tag{16}
\]

N=2 has a single double node and nonzero derivative, so it also
satisfies (16). For composite levels additional braid-phase
coincidences can occur; (16) is not asserted there. The all-level
observable statement (7) has no such restriction. The interpolation
degrees and inverse norms in (16) are not claimed uniform or tame.

[Audit](../experiments/audit_actual_adjacent_observable_source_filtration.py)
reconstructs the original coproduct Casimir and physical highest
intertwiner, checks the normal operator and full Krylov bases,
all-level filtrations and source values, and the literal full-Cartan
crossing coefficient. It does not infer a geometric norm from algebra
dimension or from a finite numerical rank fit.

The finite audit checks twelve literal coproduct/source modules at
N=2,...,12,14, every rank-one observable generator and strict
source flag, the retained normal between two actual crossings,
and actual-braid recovery at the tested prime levels.