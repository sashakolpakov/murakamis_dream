# The ordinary one-cut section is not generically zero on the figure-eight geometric root component

Independent audit, 27 October 2026. The ordinary quantum dimension
of an individual cyclic color is zero, but this does **not** force
the pivotal one-cut functional of the closed-braid Hom line to
vanish. For the figure-eight root-holonomy component, generic
nonvanishing holds at **every** level \(N\ge2\). There are also
literal full-quantum nonzero tests at complete irreducible points,
for \(N=2,3,4\), in both Riley embeddings.

This concerns the full root-center object
[constructed here](closed_braid_period_line.md), not an identification
of its root-central geometric point with the semiclassical geometric
block of the original nilpotent state. It gives no volume estimate
and no general-knot nonvanishing theorem.

## 1. Zero quantum dimension does not decide the one-cut section

In a regular color \(K_{aa}=xQ^{-a}\), and
\[
 \operatorname{Tr}(g)=
 x^{1-N}\sum_{a=0}^{N-1}Q^{a(N-1)}=0,
 \qquad g=K^{1-N}.
\]
For a knot Hom-line frame \(J\), the partial pivotal trace is
\(\operatorname{ptr}(J)=cI\). The full trace equation only says
\(\operatorname{Tr}(g)c=0\), which is \(0=0\). It cannot imply \(c=0\).
The identity tensor, whose partial trace does vanish, is not a
model for every braid Hom-line frame.

Vanishing is independent of a nonzero scalar rescaling of \(J\).
It is also independent of a change of splitting-module bases:
conjugate every local module and pivot, conjugate \(J\) by the
tensor basis change, and the cut conjugates by the first basis
change. Thus zero/nonzero evaluation is an intrinsic question on
the admissible splitting cover, not a determinant-root normalization.

## 2. A direct algebraic Riley component, including the attachment

Use the classical action word
\((\sigma_1\sigma_2^{-1})^2\). Put
\[
 A=\begin{pmatrix}z&1\\0&z^{-1}\end{pmatrix},
 \quad B=\begin{pmatrix}z&0\\u&z^{-1}\end{pmatrix},
 \quad C=A^{-1}BAB^{-1}A.
\]
The first fixed-braid equation is built into this expression
for \(C\). The second is \(CA=BC\); preservation of the ordered
product then gives the third. Direct multiplication yields
\[
 CA-BC=
 \begin{pmatrix}0&P/z\\-uzP&-uP\end{pmatrix},
 \qquad
 \boxed{P=u^2+(z^2+z^{-2}-3)(u-1).}                         \tag{2.1}
\]

At \(z=1\), the equation is \(u^2-u+1=0\), giving the two
complete irreducible figure-eight Riley representations.
For the root center, retain the selected actual Casimir branch
by putting
\[
 z=M^N,\qquad \Omega=-M-M^{-1}.
\]
This is compatible with the central Chebyshev relation and
\(\Omega(1)=-2\). It is not an assumption equating a root
center with a principal symbol.

The curve \(P(u,M^N)=0\) is irreducible over \(\mathbb C(M)\)
for every \(N\). Its discriminant is
\[
 \frac{(M^{4N}-3M^{2N}+1)(M^{4N}+M^{2N}+1)}{M^{4N}}.
\]
Each numerator factor has only simple nonzero roots: write
\(y=M^{2N}\), and its two roots are distinct and nonzero.
The two factors have no common root, since their difference
is \(4M^{2N}\). The discriminant therefore has \(8N\) simple
zeros and is not a square in \(\mathbb C(M)\). This proves
irreducibility of the quadratic in \(u\).

Let \(\varphi=(1+\sqrt5)/2>1\). At \(u=0,z=\varphi\),
\(z^2+z^{-2}=3\), so (2.1) holds. The representation is upper
triangular and nonabelian: \(B\) is diagonal but does not
commute with the nonzero upper entry of \(A\), since
\(\varphi\ne\varphi^{-1}\). It is an actual nonabelian
reducible Alexander attachment point on the same irreducible
Riley curve as the complete geometric points.

The upper-triangular chart has central \(F_i^N=0\), all
central crossing divisors equal to one, and a common
\(K\)-root \(x=q_N^{N-1}M_*\), where
\[
 M_*=\varphi^{1/N}>1.
\]
The semicyclic and balanced coherent crossing constructions
give invertible frames there, regular through their zero
section. Thus the Hom line and its evaluation are defined
at this attachment point.

## 3. A uniform positive anchor proves generic nonvanishing

The exact whole-cut source-independence theorem, proved by
the nonnegative wrap-degree argument in
[balanced coherent braiding](balanced_verma_coherent_braiding.md),
identifies the selected cut on this \(F^N=0\) family with
the actual reduced figure-eight value \(F_N(M_*)\), up to
the nonzero chosen Hom-frame unit. A wrap contributes
\(+N\) to residue degree; the one-cut range cannot absorb
it, so this is an equality of whole cut matrices.

The independently proved
[whole figure-eight identity](figure_eight_whole_source_identity.md)
is
\[
 F_N(Y)=
 \sum_{n=0}^{N-1}
 \prod_{r=1}^n\bigl(Y+Y^{-1}-Q_N^r-Q_N^{-r}\bigr),
 \qquad Y=M^2.
\]
At \(Y=M_*^2>1\), every factor is
\[
 Y+Y^{-1}-2\cos(2\pi r/N)
 \ge Y+Y^{-1}-2>0.
\]
Hence
\[
 \boxed{F_N(M_*)>0\qquad\text{for every }N\ge2.}              \tag{3.1}
\]

A section of the dual of an invertible line on an irreducible
component cannot be identically zero if it is nonzero at one
regular point of that component. Trivialize the line near
that point: the section is an ordinary function with a
nonzero value, and thus a nonzero rational function.
Applying this to (3.1) gives:

**All-level conclusion.** On the framed Riley component
containing the complete geometric representations, with the
selected Casimir branch and its admissible source cover,
\(\operatorname{ev}_{\beta,N}\) is not identically zero for
any \(N\ge2\). It is nonzero on a dense open set.

The statement is intrinsic under splitting-basis changes.
The root-cover phases change a chosen frame by a unit;
they do not turn a nonzero section into the zero section.
At charts where one chain presentation degenerates, an
isomorphic splitting chart is required, rather than
interpreting its singular basis as a vanishing period.

This does not prove that the section is nonzero at every
complete point, or exclude a zero divisor elsewhere.

## 4. Exact full-quantum tests at complete irreducible points

The script
[audit_geometric_root_holonomy_cut.py](../experiments/audit_geometric_root_holonomy_cut.py)
constructs the literal global quantum automorphism at the
complete Riley tuple. It does not replace its matrix
intertwiner by the classical or semiclassical braid map.

It performs the following independent steps:

1. Start from the two parabolic matrices at a root
   \(u^2-u+1=0\), whose distinct invariant lines prove
   irreducibility over the algebraic closure.
2. Apply an explicit conjugation, the prescribed
   \(\delta=(-1)^{N-1}\) meridian sign, and the prefix
   Gauss inverse to obtain the root-center parameters.
3. Choose the actual splitting modules with \(\Omega=-2\).
   Evaluate the whole checked rational quantum
   automorphism in operator-word order, including its
   contravariant center convention.
4. Construct an invertible global matrix-unit intertwiner.
   Check every factor \(E,F,K\) equation and its
   commutation with the actual diagonal coproduct.
5. Take the original pivotal partial trace \(g=K^{1-N}\).
   Check that the whole cut matrix is scalar.

The resulting nonzero exact reductions are:

| \(N\) | prime | Riley root | cut scalar in the chosen frame |
|---:|---:|---:|---:|
| 2 | 109 | 46 | 25 |
| 2 | 109 | 64 | 15 |
| 3 | 103 | 47 | 96 |
| 3 | 103 | 57 | 23 |
| 4 | 193 | 85 | 180 |
| 4 | 193 | 109 | 168 |

These are certificates of nonzero characteristic-zero
values, not floating-point evidence. All defining
denominators, roots, projectors and frame determinants
are units at the displayed reductions. The cyclotomic,
Riley, and \(K\)-root equations are etale there.
Hensel lifting therefore gives a compatible algebraic
characteristic-zero point; a nonzero residue cannot
come from a zero characteristic-zero section.
The two Riley choices give the geometric and conjugate
complete branches, with the prescribed complex root
embedding chosen after lifting.

The scalar values depend on the chosen Hom-line frame.
Only their zero/nonzero status is asserted intrinsically.
No determinant-normalization phase was discarded to
test that status.

## 5. What remains for a geometric-source comparison

The generic ordinary one-cut functional on this
irreducible root-holonomy component is genuine and
does not vanish for a universal quantum-dimension
reason. A modified/derived source is therefore not
forced merely by such a generic vanishing claim.

At a point where a particular evaluated section does
vanish, its first nonzero normal coefficient, divided
source, or another marked relative pairing may still
be needed; generic nonvanishing gives no uniform
lower bound across levels or control of that order.

The original Kashaev root augmentation has all
central meridians equal to \(I\). The geometric root
points here have noncentral parabolic meridians.
They are different interior central data even when
the peripheral scalar is \(M=1\). Nothing above
identifies their periods, their source lattices, or
their growth. The missing geometric-source and
regulator comparison remains a separate theorem.
