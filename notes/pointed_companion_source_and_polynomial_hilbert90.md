# A polynomial unfolding of the actual pointed cyclic source

Research theorem, 27 October 2026. There is an explicit whole
algebraic unfolding of the original cyclic boundary. Allow its
cyclic repair to acquire a characteristic polynomial, while keeping
the actual highest vector, normalized output row and aligned
rank-one multiplicative relation. The resulting sourced moduli
chart is a principal open subset of affine (N-1)-space over the
Q-line. Every matrix and the full co-source have polynomial
formulas. A unipotent conjugation, requiring no quantum-gap
division, trivializes the clock and retains the residual spectral
polynomial in the transformed co-source.

This is a source-specific chart of the existing framed
multiplicative-commutator problem. It is not a new definition of
the knot invariant, nor a proof that its residual polynomial is
the knot's geometric A-polynomial. That requires the actual
crossing-word and peripheral transport.

## 1. Keep the source and relax just the fixed cyclic polynomial

Let R be any commutative coefficient ring and Q a unit. Let E
be locally free of rank N, N at least two. Consider invertible
X,Y, a vector v, and rows w,ell satisfying

    Q inverse X Y X inverse Y inverse=I+v w,              (1)
    Xv=v,   ell v=1,   ell Y=ell.                         (2)

Require the actual source-orbit chart: v,Yv,...,Y^(N-1)v is a
basis. These hypotheses retain the normalized source v ell;
in particular its image is aligned with the moment vector v.
They relax the additional actual finite-head equation Y^N=I.
The row w in (1) is the moment covector; ell is the original
co-source and must not be replaced by w.

In this canonical basis write

    Y e_j=e_(j+1), 0<=j<N-1,
    Y e_(N-1)=sum_(i=0)^(N-1) t_i e_i.                    (3)

Then t_0 is a unit, ell=(1,...,1), and

    sum_i t_i=1.                                        (4)

Conversely choose arbitrary t_1,...,t_(N-1), set
t_0=1-sum_(i>0)t_i and invert t_0. Define x_0=1 and

    x_m=(1-Q^m)t_(N-m)
             +sum_(l=1)^(m-1)t_(N-m+l)x_l, 1<=m<N.       (5)

The UNIQUE possible clock is

    X_(i,j)=Q^i x_(j-i) if i<=j, and zero if i>j.          (6)

It is invertible: det X=Q^(N(N-1)/2). The unique row w is the
zeroth row of Q inverse X Y X inverse Y inverse minus I.
All other rows of that matrix vanish. Consequently (3)-(6)
are a complete construction and classification over R, including
bases with nilpotents. They do not require Q^N-1 or any 1-Q^j
to be invertible.

Here is the entry proof. Equations (2) and cyclicity first fix
the zeroth column of X and the row ell. Equation (1) is equivalent
to saying that XY-QYX has image in Rv. In its nonzero-index rows,
the first N-1 columns force (6) inductively: until the final
column the additional companion term contains X_(N-1,j)=0.
For i=N-m>0 the final-column equation, divided only by the
unit Q^i, is

    x_m=sum_(l=0)^(m-1)t_(N-m+l)x_l-Q^m t_(N-m),

which is exactly (5). Conversely that recurrence kills every
nonzero-index row. Invertibility of X,Y then gives (1) and w.
The final-column output equation ell Y=ell is precisely (4).

Thus the sourced quotient in this cyclic chart is EXACTLY

    Spec R[t_1,...,t_(N-1),
                         (1-sum_(i>0)t_i) inverse].        (7)

If a free basis of E is included in the data, the representation
chart is GL_N times (7). There are no residual stabilizers:
an automorphism fixing Y and v fixes its full cyclic basis.
In particular the sourced chart is smooth and flat over the
whole Q-unit base, of relative dimension N-1. This follows
from the displayed coordinate ring, not from a nonroot generic
smoothness theorem.

The surrounding [framed moment scheme](actual_resonant_framed_moment_smoothness.md)
also has a direct root Jacobian proof and a cyclic-vector quotient
of relative dimension 2N. The present formulas describe its full
sourced subchart globally, rather than merely near that root.

## 2. The pointed spectral factor and a polynomial Hilbert-90 gauge

The companion characteristic polynomial and its reversed form are

    chi(z)=z^N-sum_i t_i z^i,
    h(z)=z^N chi(1/z)
        =1-sum_(m=1)^N t_(N-m)z^m.                       (8)

Because chi(1)=0, there are monic and constant-one polynomials
chi_red and h_red, respectively, with

    chi(z)=(z-1)chi_red(z),
    h(z)=(1-z)h_red(z),
    h_red(z)=z^(N-1)chi_red(1/z).                         (9)

Let L be the actual finite lowering shift, L e_j=e_(j-1) for
j>0 and L e_0=0. Thus L^N=0. Put

    B=diag(1,Q,...,Q^(N-1)),   G=h(L).                    (10)

G is upper unipotent, with polynomial inverse: its nonconstant
part is nilpotent. Equations (5)-(6) imply the exact WHOLE identity

    X=G B G inverse.                                    (11)

To verify this without matrix inversion, let
x(z)=sum_(m=0)^(N-1)x_m z^m. Recurrence (5) is equivalent to

    h(z)x(z)=h(Qz) modulo z^N.

Thus X=B h(QL)h(L) inverse. Since B L B inverse=Q inverse L,
B h(QL)=h(L)B, which proves (11). This is an explicit finite
polynomial coboundary, rather than a comparison obtained after
truncating a quantum jet or choosing a singular eigenbasis.
In particular no factors 1-Q^j or 1-Q^N have been canceled.

The source is transported exactly as well:

    G inverse v=v,
    ell G=e_0^t h_red(L).                                (12)

Indeed Gv=v and ell(I-L)=e_0^t, while (9) holds at L. Therefore
the coefficients of the residual spectral factor remain in the
actual transformed co-source. For every whole operator C,

    ell C v=[e_0^t h_red(L)] [G inverse C G] v.            (13)

The new transport is G inverse Y G, and every crossing, cap and
inserted current has to be conjugated with it. Trivializing X
alone does not erase the co-source polynomial. If the original
period carries an external peripheral/dimension line, retain that
SAME line on both sides of (13), including its norm-zero ratios.

## 3. The actual finite head is a regular section, not a singular limit

The actual data are recovered by EQUALITY at

    t_0=1, t_i=0 for i>0,
    chi(z)=z^N-1,
    h(z)=1-z^N,
    h_red(z)=1+z+...+z^(N-1).                             (14)

Then G=I, X=B, Y=P is the original cyclic repair, and

    w=(Q^-N-1)e_0^t,
    ell=e_0^t sum_(j=0)^(N-1)L^j=(1,...,1).               (15)

This is exactly the original orbit co-source of
[the moment/source theorem](actual_rank_one_multiplicative_moment_and_orbit_source.md).
The finite head itself still uses its two explicit endpoint
deletions; unfolding P has not changed those actual matrices.

Conversely Y^N=I FORCES (14): applying it to v and using its
cyclic basis gives t_0=1 and t_i=0 for i>0. This works over every
commutative base, without a distinct-eigenvalue or characteristic
zero hypothesis. The fixed cyclic source is cut out by the
N-1 ordinary coordinate equations t_i=0 in the smooth chart (7).
It is a flat section over Q. The earlier aligned rigidity theorem
is precisely this section, with the defect projector retained.

The determinant of (1) supplies another retained character:

    1+w v=Q^-N.                                         (16)

At a primitive N-th root the matrix v w therefore has square
zero, even when w is nonzero elsewhere on the unfolded fiber.
The actual section has w=0 there, and its divided normal still
recovers e_0 e_0^t. Square-zero boundary monodromy does not imply
nilpotence of the full braid image; the previously proved
semisimple braid sector is unaffected.

## 4. Finitely many mixed source moments recover the polynomial

This chart has a concrete comparison test. The uninserted source
moments ell Y^j v are all one, so they cannot distinguish ANY
of the residual spectral polynomials. Keep the clock insertion
and define instead

    m_j=ell X Y^j v, 0<=j<N,   m_0=1.

The canonical columns give

    m_j=sum_(l=0)^j Q^(j-l)x_l,
    x_j=m_j-Qm_(j-1), 1<=j<N.                            (17)

If the usual finite-head units 1-Q^m, 1<=m<N, are inverted,
equation (5) then gives the UNIQUE recursive reconstruction

    t_(N-m)=[x_m-sum_(l=1)^(m-1)t_(N-m+l)x_l]/(1-Q^m).   (18)

Finally t_0=1-sum_(i>0)t_i. The mixed moment map is therefore
a polynomial coordinate change over this head localization,
with polynomial inverse there; it is not just a pointwise
injectivity assertion. The determinant of its Jacobian, in the
ordered variables t_(N-1),...,t_1, is exactly

    product_(m=1)^(N-1)(1-Q^m),                           (19)

because (5) is triangular in this order and (17) is unit
triangular. At a primitive N-th root (19) is N. These formulas
construct a finite algebraic test for a proposed source-transport
comparison and retain its whole normal derivatives.

They do not yield a uniform bound on the inverse matrix's
condition number; its other entries depend on the retained
polynomial. For the actual fixed finite repair P one simply has
m_j=Q^j and recovers chi=z^N-1. A different polynomial cannot be
assigned to that same transport by relabeling its spectral factor.
An actual quantum meridian transport would have to supply its own
mixed moments and satisfy the sourced equations before this test
could be applied to it.

## 5. What this gives to the A-torsor program

There is now a fully explicit algebraic sourced family, its
spectral polynomial with a FORCED pointed factor z-1, and a
whole comparison carrying the remaining polynomial into the
co-source. This supplies functions and a flat scheme before
quantum jets. It also makes precise why an unpointed spectral
equation and a bare diagonal clock omit selected-period data.

Nothing here identifies chi_red with A_K. The coefficients t_i
are arbitrary source-transport coordinates until an ACTUAL
crossing word or quantum meridian transport produces them.
No such new transport is substituted for the original P. The
identity (13) compares a given full operator exactly; it does
not determine its scalar period or give a growing-N norm bound.
An upper-unipotent gauge can have large condition number, so its
determinant one is not a subexponential estimate.

In particular [the actual Fourier cancellation theorem](actual_fourier_source_cancellation.md)
continues to apply. A nonzero formal block with the regulator
action can lie in the zero-source current sector. To prove the
volume conjecture the actual word class, source polynomial and
independent normal/norm divisors must be carried into the marked
regulator period. The present theorem is an exact algebraic source
unfolding and polynomial comparison; it does not prove that final
selected norm.

The underlying multiplicative-commutator terminology is covered by
[Chalykh--Fairon's one-loop quiver presentation](https://arxiv.org/pdf/1704.05814).
Only its defining equation is used; the classification and all
gauge/source formulas above follow from the entry proof.

[The exact audit](../experiments/audit_companion_source_shell.py)
and [saved results](../experiments/companion_source_shell_results.json)
check the universal formulas at six symbolic levels and twelve
full generic/primitive-root moment fibers. The
[independent proof audit](companion_source_shell_independent_audit.md)
checks the chart, periodic section, polynomial gauge and retained
co-source separately.

The [actual meridian compatibility audit](actual_meridian_companion_source_compatibility.md)
now proves a universal mismatch if one tries to use the invariant's
meridian orbit state directly as this normalized highest source.
Its canonical highest residual has pairing K_N. This chart remains
a comparison tool; a division by that unknown value cannot serve
as the requested geometric-period proof.
