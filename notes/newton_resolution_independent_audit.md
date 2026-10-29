# Independent audit of the geometric Newton resolution and normal scales

Audit, 27 October 2026, of
[the Newton resolution note](newton_resolution_and_regulator_cut.md),
especially Sections 3 and 5. The strict-transform calculation and its
etaleness conclusion are correct with the marked Weyl-stability
hypothesis explained below. No actual-symbol or selected-period
assertion follows from them.

## 1. The logarithmic branch and its involution

Write Y=exp(y), L=-exp(lambda), keeping the complete sign L=-1.
Assume the selected geometric normalization germ is smooth, etale
over y, and fixed by the simultaneous eigenflag-swap involution.
Then its local ring is k[[y]], the involution sends y to -y and
lambda to -lambda. Consequently lambda(y) is odd:

    lambda=tau y+c_3 y^3+... .                       (1.1)

Etaleness over y alone does not imply oddness. For example
lambda=tau y+b_2y^2 is etale over y and has any prescribed
nonreal cusp derivative, but is not Weyl stable when b_2!=0.
Thus the eigenflag assertion is an essential part of the proof.

For the marked complete hyperbolic place, that assertion has a
direct geometric justification. Generically swap the two peripheral
eigenflags while keeping the representation. At the complete
nontrivial parabolic meridian, both flags specialize to its unique
eigenline. Develop the vertex flags and take the cross-ratios in
the specified positive triangulation. At the complete point all
the cross-ratio denominators are units. The swapped decoration
therefore specializes to the same nondegenerate complete shapes.
Equivalently, the rational involution extends over the valuation
ring of the normalized curve and has the same closed shape point.
Smoothness of this gluing germ means there is only one normalization
place at that point. The involution fixes that place. Its action
on the recorded peripheral eigenvalues is precisely inversion.

This argument retains the shape place and the peripheral lift.
Invariance of an unmarked A-polynomial by itself would not exclude
exchanging distinct normalization places over its singular point.

## 2. Exact limits and the transverse parameter

The chart formulas become the following exact identities of germs:

    u=-sinh((y+lambda)/2)/sinh((y-lambda)/2),
    e=[cosh(y)-cosh(lambda)]/[2sinh(y)^2].          (2.1)

The common zeros cancel, since Im(tau)>0 implies tau!=+1,-1.
Both germs are even, hence functions of w=2cosh(y)-2. Their limits
are

    u_0=(tau+1)/(tau-1), e_0=(1-tau^2)/4,
    e_0=-u_0/(u_0-1)^2!=0.                       (2.2)

For tau=a+ib, b>0,

    Im(u_0)=-2b/[(a-1)^2+b^2]<0.

The invariant local ring is k[[y^2]]=k[[w]]. The exact algebraic
identity r=e(x-2) therefore gives

    r=e(w)w, dr/dw at 0=e_0!=0.                  (2.3)

It follows that the strict transform is a smooth algebraic germ,
is transverse to r=0, and is etale over the algebraic coordinate r.
The usual unique lifting over nilpotent thickenings follows at
the retained marked place. This uses no nonzero du/dw assumption.

One can see the last point even for a constant u projection. Fix
u=u_0, put e_0=1/(2-u_0-u_0^(-1)), and set

    e(w)=e_0/(1+e_0 w),
    r(w)=e_0 w/(1+e_0 w).                         (2.4)

This is still a transverse strict-transform branch. Thus division
by du/dw would incorrectly discard valid branches of the chart.
For reference the general first coefficient is

    du/dw at 0=(tau^3-tau-12c_3)/[6(tau-1)^2],

which can vanish without affecting (2.3).

The normalization matters: tau here is dlog(-L)/dlog Y. If the
earlier meridian coordinate is M and Y=M^2, this tau is one half
of dlog(-L)/dlog M. An inverse longitude convention also reverses
its imaginary sign. The note's formulas are correct in its stated
Y,L and boundary-orientation convention.

## 3. The N-squared adapter is trace-to-trace

For C_N(Y+Y^(-1))=Y^N+Y^(-N), define

    w=x-2, U_c=Y^N,
    W=U_c+U_c^(-1)-2=C_N(x)-2.

Then, exactly,

    C_N(x)-2=(x-2)H_N(x), H_N(2)=N^2,
    W=N^2w+N^2(N^2-1)w^2/12+... .               (3.1)

The projector H_N(X)/N^2 on the abstract source fiber is precisely
the simple X=2 projector in
[the source/monodromy chain map](source_lattice_monodromy_chainmap.md).
The multiplicities at the other roots are retained, so the assertion
is about the full possibly nonsemisimple source fiber.

There are two different normal scales here. W is the Weyl-invariant
central trace normal, whereas U_c-1 is the ordinary central first
normal uniformizer:

    W=(U_c-1)^2/U_c,
    U_c-1=N y+O(y^2), w=y^2+O(y^4).

Thus N^2 is the trace-to-trace adapter. It is not a linear
identification of the first Bockstein normal U_c-1 with x-2.
The physical cut still has its linear factor N:

    f=(U_c-1)b -> cut(f)=-N b(1).

For the canonical projector generator the divided-normal value
is -1/N, making its cut exactly one. This agrees with (3.1) and
does not replace the first-normal row by a trace evaluation.

## 4. Scope

The calculation supplies a regular algebraic target at the marked
geometric place, a transverse cut equation and an exact retained
normal normalization. It does not prove that the actual quantum
Newton coefficient object has that geometric component or that
the original selected source couples to its regulator period.

[Exact independent audit](../experiments/audit_newton_resolution_independent.py).
[Results](../experiments/newton_resolution_independent_results.json).
