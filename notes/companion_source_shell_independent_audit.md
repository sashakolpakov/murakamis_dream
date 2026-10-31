# Independent audit of the whole pointed companion source

27 October 2026. The classification and polynomial comparison in
[the pointed source theorem](pointed_companion_source_and_polynomial_hilbert90.md)
hold over the stated commutative coefficient rings, including
nonreduced bases. They require no quantum-gap division or imported
multiplicative-quiver classification. The full actual word and
selected regulator norm remain additional data.

## 1. Exact scheme classification in the source orbit basis

The cyclic source basis e_j=Y^jv fixes v=e_0 and makes Y the
companion with last column t_i. Its determinant is
(-1)^(N-1)t_0. The identities ell v=1 and ell Y=ell give
ell=(1,...,1) and sum_i t_i=1, without division. The multiplicative
moment equation is equivalent to requiring that XY-QYX have image
in the source line, with its row then uniquely determined by the
two invertible matrices.

Let Xv=v. In a nonzero-index row, for column j<N-1 the companion
equation is

    X_(i,j+1)=Q[X_(i-1,j)+t_i X_(N-1,j)].

Induction on j gives X_(N-1,j)=0 there and

    X_(i,j)=Q^i x_(j-i) for i<=j, and zero for i>j.

Only x_0=1 and the still undetermined zeroth-row coefficients
occur. In the last column put m=N-i. Dividing by the UNIT Q^i
gives exactly

    x_m=(1-Q^m)t_(N-m)
                 +sum_(l=1)^(m-1)t_(N-m+l)x_l.

This recursively determines every x_m and proves the converse
at the same time: all nonzero-index moment rows vanish. Thus
det X=Q^(N(N-1)/2), and its inverse requires only powers of Q.
Y inverse requires t_0 inverse, exactly the indicated principal
open. The row w is unique. Its determinant character is

    wv=Q^-N-1,

by det(I+v w)=1+w v, which follows directly from determinant
multilinearity and also holds over rings with nilpotents.

Every inverse map and classification step is over the stated
coordinate ring, so this is an isomorphism of schemes, not merely
a classification of field-valued points. The source chart is the
principal open 1-sum_(i>0)t_i!=0 in affine (N-1)-space. With a
chosen free ambient basis the representation chart is GL_N times
that open: the source orbit basis gives the unique gauge, and
its stabilizer is trivial.

## 2. The polynomial coboundary and its retained co-source

Let chi(z)=z^N-sum t_i z^i and h(z)=z^N chi(1/z). Since
sum t_i=1, ordinary monic division gives

    chi=(z-1)chi_red, h=(1-z)h_red,
    h_red=z^(N-1)chi_red(1/z), h_red(0)=1.

The recurrence is precisely

    h(z)x(z)=h(Qz) modulo z^N,

where x(z)=sum_(m<N)x_m z^m. On the finite lowering shift L,
L^N=0 and B L B^-1=Q^-1 L. Thus

    G=h(L), G B=B h(QL)=X G.

G is upper unipotent and its inverse is the finite nilpotent
geometric series. This proves X=G B G^-1 over the WHOLE ring.
No factors 1-Q^m or 1-Q^N are inverted, canceled or evaluated.
The formula remains valid at Q=1; at that value it is a canonical
choice from chi, not a uniqueness assertion for every clock
conjugator.

Since L v=0, Gv=G inverse v=v. Since ell(I-L)=e_0^t,

    ell G=e_0^t h_red(L).

Hence the source pairing identity

    ell C v=[e_0^t h_red(L)] [G inverse C G] v

has the printed orientation. Trivializing the clock has not made
the co-source constant. The new Y, actual crossing/cap/current
matrices and source must ALL be conjugated. Parameter-dependent
connections also carry the forced gauge term G inverse dG.
No fixed original peripheral/dimension line is normalized away.

## 3. Whole mixed moments recover the retained polynomial

For 0<=j<N, Y^jv=e_j, so the mixed moments are exactly

    m_j=ell X Y^jv=sum_(l=0)^j Q^(j-l)x_l,
    m_0=1, x_j=m_j-Q m_(j-1).

The second identity is ordinary telescoping. On the head-unit
localization, the already proved recurrence then recovers
t_(N-m) successively, by dividing only by 1-Q^m. Thus these
N-1 mixed source/clock moments determine the WHOLE polynomial,
not merely a normal Taylor approximation. Ordered in the reverse
tail variables (t_(N-1),...,t_1), their polynomial Jacobian is
lower triangular with diagonal 1-Q^m. Its determinant is

    product_(m=1)^(N-1)(1-Q^m)=N at primitive Q_N.

The last equality follows by evaluating
(z^N-1)/(z-1)=product_(m=1)^(N-1)(z-Q_N^m) at z=1.
It is an exact root unit, not a bound for the global inverse map.
At other Q, including Q=1, those moment coordinates can be
singular although the companion chart and G remain regular.

Pure Y moments do NOT recover this data: ell Y^jv=1 for all
integer j, by the normalized output equation and invertibility
of Y. On the actual section the mixed moments are Q^j, so the
reconstruction gives the original cyclotomic chi=z^N-1. This
does not identify chi with a knot A-polynomial or compute an
actual closed-word scalar.

## 4. The actual section and the remaining period

On the source orbit chart, Y^N=I implies Y^Nv=v. Expanding
this single equation in its basis forces t_0=1 and t_i=0 for
i>0. Conversely those equations make Y the cyclic shift.
This is valid over every supplied commutative base, not only
at a root or in characteristic zero. Then

    chi=z^N-1, h=1-z^N, G=I,
    h_red=1+z+...+z^(N-1),
    w=(Q^-N-1)e_0^t.

Thus the original finite source is a regular SECTION of the
unfolding, while its two finite endpoint deletions remain the
actual operators from the previous boundary theorem. This is
not a change of the actual knot state to a deformed companion.

The theorem determines a whole algebraic source chart and an
exact comparison for any GIVEN full word. It does not determine
that word's scalar closed period, identify chi_red with A_K,
select a global geometric cycle, or give a growing-N norm bound
for G. Its retained co-source polynomial is precisely why clock
conjugacy alone is insufficient.

[The exact independent script](../experiments/audit_companion_source_shell.py)
and [saved results](../experiments/companion_source_shell_results.json)
pass symbolic N=2,...,7 checks of every lower moment row,
characteristic/pointing factor, determinant, polynomial coboundary,
co-source, mixed-moment inverse/Jacobian and original section.
Twelve additional primitive/generic
finite-field fibers check the FULL multiplicative moment row and
its determinant character, not only the linearized relation.
