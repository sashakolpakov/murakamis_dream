# The actual resonant framed moment point is smooth over the quantum parameter

Research proof, 27 October 2026. The framed multiplicative moment
scheme is smooth at the actual primitive-root head, including its
quantum normal direction. Its cyclic-vector quotient has relative
dimension 2N over Q. The ACTUAL ordered source section is a transverse
cut by 2N equations, not an extra singularity of this ambient scheme.
The proof gives an explicit Jacobian inverse and a literal quotient
chart; no general quiver-variety smoothness theorem is used.

This is a finite-head geometric theorem. It does not determine the
scalar of an actual closed word, compare that word to a geometric
regulator, or identify the distinct divisor 1-lambda^N of the
geometric Fourier-framing pole.

## 1. Scheme and the actual resonant point

Fix N at least two over C. Let X,Y be invertible N by N matrices,
v a column, w a row and Q an invertible scalar. Set

\[
 G=Q^{-1}XYX^{-1}Y^{-1}-I-vw.
\]

Let M_N be the finite-type scheme cut out by ALL N squared entries
of G. At a primitive Q_N put

\[
 X=B=\operatorname{diag}(1,Q_N,\ldots,Q_N^{N-1}),\quad
 Y=P,\quad v=e_0,\quad w=0,
\]

where P e_j=e_(j+1 modulo N). This is exactly the actual resonant
head and its scaled moment covector in
[the actual rank-one moment/source construction](actual_rank_one_multiplicative_moment_and_orbit_source.md).
In particular BP=Q_N PB, so G=0. The root rank drop of vw is
part of the specified point, not removed by inverting its normal.

Taking determinants gives the automatic scheme-theoretic equation

\[
                         1+wv=Q^{-N}.                    \tag{1}
\]

Indeed det(I+vw)=1+wv, and det(Q inverse XYX inverse Y inverse)
is Q inverse N. Their difference belongs to the ideal of the
matrix entries of G. Equation (1) is not an additional independent
moment equation, including on nonreduced bases.

## 2. Exact Jacobian and a right inverse at the actual point

Use left tangent coordinates delta X=aB, delta Y=bP and
epsilon=delta Q/Q_N. At the indicated point, direct differentiation
of the four factors gives

\[
 dG=(I-\operatorname{Ad}P)a+(\operatorname{Ad}B-I)b
                           -e_0\,\delta w-\epsilon I.      \tag{2}
\]

There is no delta v term because w=0. The factor Q has been
retained; replacing the commutator by an unscaled one would change
the last term and the equation. The two adjoint actions commute
at the root because BP differs from PB by the scalar Q_N.

Here is an explicit relative right inverse, with epsilon fixed
to zero. For any target H in Mat_N, put

\[
 t=\operatorname{Tr}H,\quad T=H-tE_{00},\quad
 \delta w=-t e_0^t,\quad \delta v=0,
\]
\[
 a=\operatorname{diag}(a_0,\ldots,a_{N-1}),\quad a_0=0,
 \quad a_i=\sum_{k=1}^i T_{kk}\ (i>0),
\]
\[
 b_{ij}=\frac{T_{ij}}{Q_N^{i-j}-1}\ (i\ne j),\qquad
 b_{ii}=0.                                                  \tag{3}
\]

All denominators are nonzero. The diagonal identity
a_i-a_(i-1 modulo N)=T_ii follows because Tr T=0. Hence
(I-Ad P)a equals diag T, while (Ad B-I)b is its off-diagonal
part. Adding -e_0 delta w yields H, proving surjectivity of
the relative Jacobian onto ALL Mat_N, not only sl_N.

There is also a literal unit minor. Choose the tangent directions
delta w_0, a_i for i=1,...,N-1, and b_ij for i not j. Their
diagonal block has determinant -1; their off-diagonal block has
determinant product_(i not j)(Q_N^(i-j)-1). Thus an N squared
Jacobian minor is a unit. These left tangent coordinates differ
from ordinary matrix-entry coordinates by invertible linear
changes, so this is also a unit minor in an ordinary local chart.

Consequently M_N is smooth over the Q-line at this point, of
relative dimension N squared plus 2N. For completeness, this
conclusion can be obtained directly without a smoothness import:
on the open set where that minor is a unit, every square-zero
error in G is removed uniquely in the chosen N squared coordinate
directions by its inverse Jacobian. The other coordinates and Q
are free. Repeating this for successive nilpotent ideals gives
the formal local lifting property; the displayed polynomial/
Laurent finite presentation and unit minor give its usual smooth
algebraic chart. No inversion of 1-Q^N occurs.

In the flat positive root matrix norm, this particular right
inverse can be bounded by 2 N^(3/2). Indeed the off-diagonal
inverse gap is at most N/4, the trace row has norm sqrt N,
and the diagonal prefix sum has norm at most N. The diagonal
trace correction has norm sqrt N: its output is
(-sum_(i>0)H_ii,H_11,...,H_(N-1,N-1)). Combining these estimates
in the orthogonal product norm gives the displayed bound. This is only
a bound on the explicit local Jacobian inverse, not a global
neighborhood, word norm or selected-period estimate.

## 3. The Q-normal direction and the root determinant law

The actual whole curve gives an explicit tangent lift of epsilon=1:

\[
 a=J_{head}=\operatorname{diag}(0,1,\ldots,N-1),\quad
 b=0,\quad \delta v=0,\quad \delta w=-N e_0^t.              \tag{4}
\]

In fact (I-Ad P)J_head=I-NE_00, and substituting (4) into
(2) gives zero. This is the derivative of the exact whole family
X=diag(Q^j),Y=P,v=e_0,w=(Q inverse N minus one)e_0^t.
Its divided defect, endpoint walls and actual co-source orbit
are the ones already retained in the boundary theorem.

Tracing (2) on a tangent vector to M_N gives
delta w v=-N epsilon. This agrees exactly with differentiating
(1). The zero root covector does not obstruct lifting the quantum
normal. Locally delta=1-Q^N is another base coordinate because
its derivative is -N Q_N inverse times delta Q. Thus the same
smoothness gives actual local flatness over that normal parameter.
It does not identify it with another geometrical pole normal.

## 4. A literal cyclic-vector quotient, with the correct dimensions

On the open set where

\[
             H_v=[v,Yv,\ldots,Y^{N-1}v]
\]

is invertible, use it as the basis. In that basis v=e_0 and Y
is the companion matrix with first N-1 columns e_1,...,e_(N-1)
and last column tau=(tau_0,...,tau_(N-1)), with tau_0 invertible.
The remaining coordinates are the N squared entries of X, N
companion coefficients and N entries of w, besides Q, subject
to the N squared moment equations.

This is an explicit quotient, not a GIT assumption: every cyclic
point is uniquely a pair of its matrix H_v and these companion-
slice data. The cyclic chart is therefore GL_N times the slice,
and simultaneous conjugation is left multiplication on the GL_N
factor. Its stabilizer is trivial over all commutative base rings:
an automorphism fixing Y and v fixes the entire cyclic basis.

At the root the orbit matrix H_v is I. Any tangent right inverse
from (3) can be put into the slice by the infinitesimal gauge
minus delta H_v, without changing dG. Explicitly the j-th column
of delta H_v is

\[
 P^j\delta v+\sum_{k=0}^{j-1}P^k(\delta Y)P^{j-1-k}v.
\]

Thus the sliced relative Jacobian is also surjective. The quotient
is smooth over Q, of RELATIVE dimension 2N. Each fixed-Q fiber
has dimension 2N; including the Q direction gives total dimension
2N+1. Vector pointing removes the scalar stabilizer as well.
No source covector of the actual Whittaker type is presumed on
every ambient point merely from this construction.

## 5. The actual ordered source section is a transverse cut

Inside the companion slice impose the additional ACTUAL equations

\[
                         Xv=v,\qquad Y^N=I.               \tag{5}
\]

Since v is cyclic, the second equation is equivalent exactly to
the N equations tau=e_0: applying it to v fixes the last companion
column, and conversely that column makes Y=P. The first supplies
the N equations X e_0=e_0.

The constrained scheme is exactly the actual source section over
the Q-base. Indeed with Y=P, the moment equation says that the
image of XP-QPX lies in the zeroth line. The lower-row recurrence
and the fixed first column force X=diag(Q^j), as in
[the aligned cyclic-frame proof](flat_cyclic_source_frame_and_scalar_period.md),
without division by delta. The remaining first row then gives
w=(Q inverse N minus one)e_0^t. This argument works over arbitrary
commutative bases and therefore rules out hidden nilpotent thickening.

These 2N constraints are transverse at the actual root. To see this
directly, a fixed-Q tangent in their common kernel has delta Y=0
and delta X e_0=0. The lower rows of the linearized moment relation
give the same cyclic recurrence for delta X; its first column is
zero, so every entry is zero. The top row forces delta w=0.
The ambient sliced tangent has dimension 2N by Section 4. Hence
the differentials of these 2N constraint functions form an
isomorphism onto C^(2N). They are relative local coordinates.

The actual Whittaker co-source is now canonical ell=ones transpose.
It has ell v=1 and ell Y=ell, and its required orbit and both
endpoint deletions are still retained; smoothness does not set
their derivatives to zero. In particular this source section is
not all of the smooth ambient 2N-dimensional moment fiber.

There is a natural intermediate sourced locus. Adjoin a row ell
with ell v=1, ell Y=ell, and impose Xv=v, but do NOT impose Y^N=I.
In the cyclic companion frame the row is forced to be ones and
the remaining equation is sum_i tau_i=1. These N+1 conditions
are independent combinations of the transverse coordinates above,
so this locus is smooth of relative dimension N-1 near the root.
Imposing the remaining N-1 companion conditions gives the actual
ordered section. This is a local assertion here; its explicit
global recurrence classification can be proved separately.

The subsequent [pointed companion theorem](pointed_companion_source_and_polynomial_hilbert90.md)
now proves precisely that GLOBAL classification: the sourced
cyclic chart is a principal open affine (N-1)-space over Q, with
polynomial matrices, a canonical clock gauge and an explicit
residual-polynomial co-source. Its proof needs no root-gap
division and works over arbitrary commutative coefficient rings.

## 6. What this softens, and what it does not fix

The resonant rank drop at the ACTUAL point is not a singularity
of the source-vector-framed moment scheme. There is a smooth whole
Q-normal deformation space, an explicit free quotient chart and a
transverse actual source section. This supplies a precise algebraic
setting in which comparisons can be made BEFORE quantum jets.

The actual meridian parameter M and its kappa and norm factors can
be retained as additional base coordinates and endpoint data. The
argument does not identify them with the Q-normal or erase their
source ratios. Likewise it does not identify delta with the
independent intrinsic pole norm 1-lambda^N.

Identifying these finite frames or their smooth moment spaces
does not compare the selected scalar evaluations of a full actual
crossing word. A closed scalar cI remains a separate word section.
No regulator action, selected endpoint pairing or volume growth
has been deduced from smoothness or from this finite quotient alone.

## 7. Reproducible exact audit

[The independent script](../experiments/audit_actual_resonant_moment_smoothness.py)
and [its output](../experiments/actual_resonant_moment_smoothness_results.json)
check (2)-(4), an explicit Jacobian right inverse on every matrix
unit, the actual Q-normal tangent, the companion-slice ranks and
both sourced transversality dimensions over primitive-root fields.
These are exact linearization tests supporting the direct proof,
not an imported generic-parameter moduli theorem.
