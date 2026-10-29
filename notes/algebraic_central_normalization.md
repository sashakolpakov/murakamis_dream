# Fixed algebraic central factors cannot change the volume rate

Research note, 25 October 2026. This is a normalization theorem for the
A-module torsor program. It retains the central variable before root
specialization and evaluates whole period germs. It does not assume
that an unknown comparison of the Kashaev and geometric periods is
algebraic, and does not prove the volume conjecture.

## 1. The specialization theorem

Fix nonzero c in C and an integer k>=1. At level N put

    t_N=1/N, q_N=exp(c/N), z=M^(kN).

Let R be an algebraic function over the fixed field C(q,t,M,z), on
any fixed finite algebraic cover. For each sufficiently large N,
choose a branch after the displayed substitutions. Assume its whole
germ at M=1 has a finite nonzero value r_N. A finite ramified germ
is allowed, provided its value at M=1 is defined.

**Theorem.** There are constants B,C>0, independent of N and of the
chosen branches, such that

    C^(-1)N^(-B) <= |r_N| <= C N^B.                  (1.1)

Consequently log|r_N|=O(log N), so multiplying an already specified
period by r_N does not change its exponential volume rate.

The assumption is a fixed finite algebraic presentation of the factor
across levels. Being algebraic separately at every N is insufficient.
The theorem also allows rational dependence on N itself, since N=1/t.

## 2. Proof by bounded central jets

Choose an algebraic relation, clear denominators, and write

    P(q,t,M,z,Y)=sum_(i=0)^d G_i(q,t,M,z)Y^i=0,

where each G_i has finite Laurent support in M,z and rational
coefficients in q,t. Introduce M=exp(y). After q=exp(ct), z=exp(ky/t),
each coefficient is a finite exponential sum

    G_i(t,y)=sum_(a,b) g_(i,a,b)(t) exp((a+kb/t)y).    (2.1)

The g coefficients are meromorphic germs at t=0. Its y-jets are

    J_(i,j)(t)=sum_(a,b) g_(i,a,b)(t)(a+kb/t)^j,      (2.2)

also meromorphic germs. The exponent functions a+kb/t are distinct
for all sufficiently small nonzero t after identical pairs are
combined. A Vandermonde matrix shows that a nonzero coefficient
with S monomials has some nonzero jet of order less than S.

There is no hidden identically zero relation caused by q=exp(ct):
a nonzero rational function in q,t cannot vanish identically on
that germ. After clearing denominators such a relation would be a
polynomial exponential sum sum_j p_j(t)exp(jct)=0. On a ray with
ct real and tending to positive infinity, the highest exponential
dominates all lower ones, contradicting a nonzero polynomial p_j.

Let m be the smallest jet index for which some J_(i,m) is a nonzero
meromorphic germ. All lower jets vanish identically. For sufficiently
small nonzero t the order m is stable, because a nonzero meromorphic
germ has no zeros accumulating at zero. Divide all coefficients in
the relation by y^m and evaluate the whole branch at y=0. It follows
that every r_N is a nonzero root of the same meromorphic polynomial

    Q(t_N,Y)=sum_i J_(i,m)(t_N)Y^i.                   (2.3)

The common factorial m! is irrelevant. The polynomial Q is nonzero.
Remove its power of Y so that its constant and leading coefficients
are nonzero meromorphic germs. Ratios of its coefficients have at
most a fixed power pole at t=0. The elementary root bound for a
monic polynomial gives |r_N|<=C N^B. Apply the same bound to its
reciprocal polynomial to obtain the lower bound. This proves (1.1)
uniformly for every nonzero branch value.

This proof never evaluates separate vanishing numerator and
denominator factors. The bounded jet m performs their common
algebraic cancellation before specialization.

## 3. The actual ADO normalization is an example

For the literature meridian family, write f=M-M^(-1), k=2 and
q_N=exp(pi*i/N). The reduced/full factor is

    d_N(M)=eta_N f(M) M^N/(M^(2N)-1), |eta_N|=1.

After retaining z=M^(2N), its quotient by eta_N is the fixed
algebraic function

    R(M,z)=f(M)*sqrt(z)/(z-1),                         (3.1)

with the root sqrt(z)=M^N specified. Its polynomial relation is

    Y^2(z-1)^2-f(M)^2 z=0.

After substitution, the lowest common y-jet is of order two and
gives

    4N^2 Y^2-4=0.

Thus Y=+/-1/N. The specified root germ selects +1/N and hence
d_N(1)=eta_N/N, exactly as independently proved from the state
definition. This is a fixed algebraic central factor despite its
level-dependent powers in M.

Likewise 1+M^N=1+sqrt(z) evaluates to 2 on the specified root.
It remains part of an exact comparison. The theorem says that such
a factor has no exponential effect after its whole nonzero germ
has been correctly specified; it does not authorize omitting it
from a move identity.

## 4. How this fits the two torsors

The finite cyclic norm-torsor comparison permits central scalar
factors. The formal A-curve connection retains the action and
meromorphic connection coefficients, but actual difference periods
can contain functions of the invariant

    z=exp(2pi*i*Log M/h).

At h=pi*i/N this is M^(2N). The exact ADO factor illustrates this
missing difference-constant datum; see
[the formal period construction](formal_a_curve_period_torsor.md).

If a genuine comparison between two selected quantum-period
realizations has a factor from a fixed finite algebraic central
cover, (1.1) controls that normalization uniformly. This strengthens
the earlier bound for a fixed meromorphic germ in q alone.

The qualification matters. The levelwise unit (z/2)^N evaluates to
2^(-N) at z=1. It has no fixed finite algebraic presentation of the
kind in the theorem; its exponential behavior is exactly excluded
by that hypothesis. Hilbert 90 at separate levels does not exclude it.

No fixed algebraic comparison between the actual Kashaev period and
a geometric quantum-period realization has been constructed here.
In particular the theorem is not applied to an assumed algebraic
ratio between the Kashaev invariant and the bare classical exponential
of volume. The full period comparison and its geometric norm are
still the outstanding theorem in
[the primary formulation](a_polynomial_torsor_status.md).

`experiments/audit_algebraic_central_normalization.py` checks bounded
central jets, canceled rational germs, the actual algebraic ADO factor,
and its root selection. The growth bound itself is the proof above.
