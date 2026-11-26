# Nonvanishing of every single-edge pointed projection

Private research note, 17 November 2026.

For a genuine interior edge with positive angle sum \(2\pi\) and a
primitive edge row, every compatible single-edge projector is nonzero
on the original tensor of pointed tetrahedron generators. This holds
at every level, including even and composite levels. It does not prove
nonvanishing after imposing several edge equations simultaneously.

## 1. Statement with the original incidence and pointing

Consider a finite collection of oriented tetrahedra with their faces
paired in distinct occurrences. Every paired face map identifies its
three edge occurrences. Fix a global interior edge \(e\). In tetrahedron
\(j\), let \((a_j,b_j,c_j)\) count the occurrences of \(e\) in the three
opposite-edge pairs. Thus

\[
 a_j,b_j,c_j\in\{0,1,2\}.
\tag{1}
\]

Assume each tetrahedron has a nondegenerate positively oriented shape.
Let its three positive dihedral angles be
\(\alpha_j,\beta_j,\gamma_j\), with sum \(\pi\), assigned to those
opposite pairs. The actual edge-angle equation is

\[
 \sum_j(a_j\alpha_j+b_j\beta_j+c_j\gamma_j)=2\pi.
\tag{2}
\]

Use exactly the pointed root modules and Weyl convention of the direct
source. In particular, in each local clock frame,

\[
 X_jY_j=R_jY_jX_j,\quad
 (X_j+Y_j-1)p_j=0,\quad (p_j)_0=1,
\tag{3}
\]

where \(R_j\) has order \(N\ge2\). The source's root cover and all
orientation and ordering units are retained. The global edge exponent
in its \((A_j,B_j)=(X_j,Y_j^{-1})\) convention is

\[
 \beta(e)_j=\epsilon_j(a_j-c_j,b_j-c_j).
\tag{4}
\]

Assume \(\beta(e)\) is a nonzero primitive vector in the integral
tetrahedron lattice. Let \(W_e\) be its actual Weyl monomial, with any
specified edge-ordering unit included. Choose a compatible central root
\(c_e\), so that \(U_e=c_e^{-1}W_e\) satisfies \(U_e^N=1\). No root or
character is chosen by testing the generator for nonvanishing.

**Theorem.** For every prescribed \(\chi\in\mu_N\),

\[
 \Pi_{e,\chi}=\frac1N\sum_{h=0}^{N-1}\chi^{-h}U_e^h,
 \qquad
 \Pi_{e,\chi}\bigotimes_jp_j\ne0.
\tag{5}
\]

In particular this applies to each nonzero edge row in a one-ideal-vertex
knot triangulation covered by the direct source: deleting any one edge
row gives an integral basis of the primitive edge lattice, so each
individual row is primitive when that lattice has positive rank. The
rank-zero case has no nontrivial edge equation to impose.

## 2. Local spectral support

For a local monomial normalized to have \(N\)-th power one, define its
support on \(p_j\) as the set of characters whose spectral projectors
do not kill \(p_j\). Scalar root changes translate this subset of
\(\mathbb Z/N\); they do not change its size.

There are only three kinds of integral incidence factors in (1), up to
scalar units, inversion, and the exact pointed \(S_3\) changes of the
direct source. The classification is before specialization; an axis
square itself becomes central at level two.

1. If all three counts are equal, the factor is central and has one
   supported character.
2. If exactly two counts are equal, the factor is a shape-axis power
   \(Z^d\), with \(|d|=1\) or \(2\).
3. If all three counts are distinct, they are a permutation of
   \((2,0,1)\); the factor is in the pointed orbit of \(XY\).

To verify this classification, subtract the common minimum count,
using \(Z_0Z_1Z_2\) equal to its recorded scalar. Two equal counts
leave a power of one triad variable, possibly inverted. Three distinct
counts leave a permutation of \((0,1,2)\). The source's exact cyclic
and reflection adapters permute those triad positions, change \(R\)
to \(R^{-1}\) when required, and carry the original pointing. Thus
they preserve the spectral-support assertions below; they are not
arbitrary changes of vacuum.

For a shape axis, \(p_j\) has a nonzero component at every eigenvalue.
For \(X_j\) this is its explicit clock recurrence; the other axes follow
by those pointed adapters. Therefore the support size of an axis power
is

\[
 \frac{N}{\gcd(N,d)}.
\tag{6}
\]

Components at distinct axis eigenvalues lie in a direct sum, so their
merging into one eigenspace of \(Z^d\) cannot cancel. In particular
power one has full support, and power two has at least \(N/2\) support.

**Mixed-factor lemma.** The support of \(p\) for a normalized \(XY\)
has size at least

\[
 N-\lfloor N/3\rfloor=\lceil2N/3\rceil>N/2.
\tag{7}
\]

**Proof.** Write \(U\) for the normalized monomial. Its eigenvalues are
simple: its \(N\)-th power is one, and the invertible operator \(X\)
moves any eigenspace through a cycle of all \(N\) eigenvalues. Since
the local space has dimension \(N\), all eigenspaces are one-dimensional.
The relations

\[
 UX=R^{-1}XU,\qquad UY=RYU
\tag{8}
\]

show that, in a cyclic eigenbasis, (3) takes the form

\[
 p_k=A_kp_{k+1}+B_kp_{k-1},\qquad A_kB_k\ne0.
\tag{9}
\]

For \(N\ge3\), two consecutive zero coordinates force all coordinates
to vanish by (9), which is impossible. Zeros at distance two also force
the intermediate coordinate to vanish, and hence are impossible.
Thus distinct zeros have cyclic spacing at least three, so there are
at most \(\lfloor N/3\rfloor\) zeros. At \(N=2\), if one coordinate
were zero, the equation at the other coordinate would make that one
zero too. This gives (7) at every level. \(\square\)

No positivity or angle inequality was needed for this local lemma.

## 3. The actual edge excludes the sole support exception

If the edge has a power-one axis factor, it already has a factor of
full support. Suppose it has none. Primitivity of (4) then forces at
least one mixed factor: otherwise every local exponent is either zero
or twice an integral axis vector, making the whole row divisible by two.

If there are two mixed factors, their support sizes sum to more than
\(N\). The same is true for one mixed factor and one nonzero
power-two axis incidence, by (6)--(7). Consequently the only configuration
not yet covered by these alternatives is

\[
 \text{one mixed tetrahedron, all other incidence factors central.}
\tag{10}
\]

We now rule out (10) using genuine angle and face incidence data. The
mixed tetrahedron contributes an angle

\[
 \vartheta=\pi+\theta_2-\theta_0\in(0,2\pi),
\tag{11}
\]

where \(\theta_2,\theta_0\) are the positive angles in its count-two
and count-zero pairs. A central incidence \((d,d,d)\) contributes
\(d\pi\), with \(d=0,1,2\). Equation (2) therefore forces precisely
one further tetrahedron with incidence \((1,1,1)\), no tetrahedron
with incidence \((2,2,2)\), and \(\vartheta=\pi\). All remaining
tetrahedra have incidence \((0,0,0)\).

Count, in each triangular face occurrence, how many of its three edge
occurrences belong to \(e\). A mixed pattern \((2,0,1)\) marks a
three-edge path in the tetrahedron. Its four face counts are

\[
 \{1,1,2,2\}.
\tag{12}
\]

A pattern \((1,1,1)\) selects one edge from each opposite pair.
Those three edges form either a vertex star or a face triangle, giving
respectively

\[
 \{0,2,2,2\}\quad\hbox{or}\quad\{3,1,1,1\}.
\tag{13}
\]

Every \((0,0,0)\) tetrahedron contributes four zero-count faces.
In the star case the total number of count-two faces in the entire
triangulation is \(2+3=5\); in the triangle case the total number of
count-one faces is \(2+3=5\). Both are impossible. Paired faces have
the same count, so the number of faces of each count must be even.
This parity argument includes faces paired within a tetrahedron and
all tetrahedra having no occurrence of \(e\). Thus (10) cannot occur.

## 4. Tensor support and the prescribed character

Choose an \(N\)-th-power-one normalization of each local factor. Their
tensor product differs from \(U_e\) by a scalar in \(\mu_N\); this
retains all the specified root and Weyl units. Let \(S_j\) be their
nonempty local supports, written additively in \(\mathbb Z/N\).
The tensor pointing has a direct decomposition into the products of
local eigenspaces. Its nonzero summands have exactly the labels
\(\prod_jS_j\). Even when different tuples have the same global edge
character, they belong to different summands of this finer direct sum
and cannot cancel. Hence the global support is the translate of

\[
 S_1+\cdots+S_T.
\tag{14}
\]

For arbitrary subsets \(S,T\subset\mathbb Z/N\), the elementary bound
\(|S|+|T|>N\) implies \(S+T=\mathbb Z/N\): for every \(k\), the
sets \(S\) and \(k-T\) intersect. This uses no prime-level hypothesis.
Section 3 guarantees either a full local support, two mixed factors,
or a mixed factor and a power-two axis factor. Equations (6)--(7) make
(14) the full group in every case. Translation by the retained scalar
does not change that conclusion. This proves (5) for every prescribed
compatible character, rather than selecting a favorable lift.

## 5. Scope for several edge equations

The theorem uses a genuine angle sum and face pairing to strengthen
the local support information. It proves every single-edge marginal
of the original tensor is nonzero. It gives no assertion that

\[
 \left(\prod_{e\in\mathcal B}\Pi_{e,\chi_e}\right)
       \bigotimes_jp_j\ne0
\tag{15}
\]

for an entire independent edge basis \(\mathcal B\). After the first
projection the vector is generally no longer a pure tensor. Moreover
local factors of different commuting global edge operators need not
commute inside an individual tetrahedron. The direct tensor support
argument of Section 4 therefore cannot simply be iterated. Complete
single-edge supports do not determine joint support.

The theorem also does not identify the reduced tensor with the actual
relative quantum source, give a lower bound uniform in the level, or
prove a selected scalar or regulator asymptotic. These remain distinct
from the exact nonvanishing established in (5).

## Direct source and author audit

The direct source is
[Pointed tetrahedron modules and all-level edge reduction](pointed_tetrahedron_gluing.md),
SHA256
`ba91c4be463e38add42b2f8ebc53c3cd3a7e96e97ac4247330dc325e7f6b3a7c`.
Its complete text was freshly read in this author sequence and the pin
renewed. Sections 1--2 give the exact pointed adapters and local kernel;
Sections 3--5 give the incidence, integral primitivity, and retained
Weyl characters; Section 6 supplies the original tensor pointing.
The local support, face-parity, and single-edge conclusion above are
proved by written algebra and incidence counting, without computation.
