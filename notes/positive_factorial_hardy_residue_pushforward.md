# A unit-residue pushforward for the actual positive-factorial layers

28 October 2026. This proves a source-preserving contour step in the
[continuous Gaussian/cyclic period](actual_continuous_gaussian_cyclic_network.md).
An artificial Hardy reset immediately after a positive factorial can
be removed by its ordinary Cauchy residue, with coefficient exactly
one. The other contour component is killed by the actual polynomial
input condition. This holds throughout the whole original word,
including its fixed Gaussian variables and original source.

This is a contraction of specified auxiliary layers. It neither
identifies the remaining phase with a positive triangulation nor
computes its geometric intersection number.

## 1. The exact local contour decomposition

Put d=N-1 and retain the anchored literature function V_N of the
continuous-period note. A positive factorial followed by its identity
reset has the active kernel

    Fhat_N(z/w) K_+(b/z)
       =N(z/w)^d V_N(Qw/z)/(1-b/z).                  (1)

The z-integral, with its original dz/(2*pi*i*z) measure, is

    N w^(-d)/(2*pi*i) integral
                z^d V_N(a/z) dz/(z-b), a=Qw.        (2)

Suppose |a/b|<=delta<1/2, and choose an outer circle R>|b|
and the inner circle |z|=|b|/2. The whole annulus between them
lies in |a/z|<1, so the cyclic function has its same anchored
branch and has no norm divisor in the annulus. Its only pole
there is z=b. With both circles positively oriented,

    I_outer=Fhat_N(b/w)+I_inner.                     (3)

Every original factor N, w^(-d), and b^d is retained. The pole
coefficient is exactly +1: dz/[z(1-b/z)]=dz/(z-b).
There is no determinant, root scalar, or N multiplier from this
normal pushforward.

The inner term is not zero as a bare scalar kernel. Indeed the
outer contraction in (1) is the finite factorial polynomial in
b/w, while Fhat is its full Laurent completion. Treating (3) as
a pole-only equality before checking its incoming state would
lose that difference.

## 2. Why the remainder vanishes on the actual incoming states

For EVERY nonnegative polynomial f(w), not only the distinguished
cup, the positive-factorial scalar kernel acts by

    CT_w Fhat_N(z/w) f(w)
       =sum_(a=0)^d F_a f_a z^a,                    (4)

where f(w)=sum_(a>=0) f_a w^a and F_a=(Q;Q)_a. To prove (4),
expand V_N at zero. Its coefficients below N agree with the
original v_N, and the exact reflection is

    N Q^(d-a) [t^(d-a)]V_N(t)=F_a, 0<=a<=d.

Coefficient contraction requires the cyclic Taylor index h=d-a.
For a>d that index is negative and the contribution is zero.
No negative power of z is produced by a nonnegative input.

Thus, after the incoming Cauchy contractions, the z-dependence
in (2) is a polynomial g(z) of degree at most d. Its inner
contour is exactly

    (1/(2*pi*i)) integral_(|z|<|b|) g(z) dz/(z-b)=0. (5)

Consequently the inner component is an operator-zero remainder
on nonnegative polynomial inputs. This statement is stronger
than cancellation of one final scalar, but does not assert that
the bare inner chain vanishes in an unpointed twisted homology
group. A negative Laurent input need not satisfy (5).

In the actual completed word every preceding head is a
nonnegative polynomial. Hardy transfers and diagonal operators
have that property, and each fixed Gaussian dilation preserves
it. Therefore (5) applies at every selected layer. It can be
applied successively in word time, leaving the upstream output
polynomial at each step. The original monomial input, output,
peripheral line and framing are unchanged. The same argument
works for a finite sum of original finite-head sources.

Absolute convergence on the deformed cycles follows by the
same Gaussian majorant as before: on the inner circle the new
cyclic argument has modulus <=2delta<1 and |b/z|=2, so its
Hardy factor is bounded. Fubini permits the upstream contractions
used in (4)-(5). No Ward corner is reapplied at fixed Gaussian
variables.

## 3. All these residue steps have a common actual radius chamber

Use the original forward reset construction with rho=1/16, and
choose delta=1/16. At a positive factorial replace its old output
radius by

    R_F=2 r_F/(rho delta),                           (6)

where r_F is that active head's incoming radius. At the next
reset, the unadjusted active radius is then b=r_F/delta.

The actual strict crossing order ensures that any transfer
immediately following a positive factorial lowers that factorial's
active head:

    inverse fusion's F_2 -> U_+ (positive crossing),
    final fusion's F_1   -> U_-.

For a negative crossing the former successor is Gaussian instead.
A final fusion F_2 is followed by a diagonal factor of the next
block, or by the terminal source. Transfer radius adjustments
shrink only the numerator, that is, the RAISING head. They do
not shrink b in the two cases above. Thus every interior pair
in (1) simultaneously has |a/b|=delta. A terminal positive
factorial without a following reset is not removed by this lemma.

Every other forward inequality remains feasible. The factor in
(6) is a fixed word-independent constant. If desired, choose
the initial radii sufficiently small by a fixed constant depending
on the word length, so all later radii remain at most one. Their
logarithms still obey C_word+C sum|xi_j|, uniformly in N.
All roots in the residue term are inside their anchored disks.

This supplies an actual common contour, rather than a formal
choice of separate residues in incompatible radius chambers.

## 4. A quantitative normal bound, without using source cancellation

For |t|<=r<1 the exact cyclic logarithm gives

    |log V_N(t)| <= -(N/4)log(1-r).                  (7)

On the inner circle of Section 1, (7) implies the pointwise
relative estimate

    |I_inner/Fhat_N(b/w)| <= 2 exp(-N gamma),
    gamma=log 2+(1/4)log[(1-2delta)(1-delta)].        (8)

At delta=1/16, gamma>0.64. The residue value is nonzero on
these anchored disks, so the ratio is defined. The estimate
follows directly from |z|/|b|=1/2, the upper bound for
V_N(a/z), and its corresponding lower bound at a/b.

For a fixed number of pairs, their product differs pointwise
from the pole product by O_word(exp(-gamma N)). This alone
would not give a relative estimate for the whole selected
period, because the remaining integrations may cancel. Here
the exact equality instead follows from the stronger
operator-zero statement (5). No physical-metric condition
number or geometric lower bound is inferred from (8).

## 5. Why the residues are necessary in the unreduced presentation

Choose an interior positive-factorial output variable z in the
reset presentation, keeping all other variables fixed. It appears
only in the two factors (1). Define

    A_N(r)=r partial_r log V_N(r), r=Qw/z, H=b/z.

The EXACT logarithmic derivative of the full scalar density in
that variable is

    partial_logz log I=(N-1)-A_N(r)-H/(1-H).          (9)

There is no source monomial in this interior variable. From the
exact logarithmic series and min_(N not divides m)|Q^m-1|>=4/N,

    |A_N(r)| <= N rho/[4(1-rho)]=N/60,
                                               |r|<=1/16. (10)

If also |H|<=1/16, (9) has modulus at least
N-1-N/60-1/15>0 for every N>=2. The initial reset presentation
therefore has no holomorphic critical point in its common small
argument chamber whenever the word contains a crossing.

More precisely, at ANY exact critical point retaining |r|<=1/16,
equation (9) forces

    1-H=1/[N-A_N(r)],
    60/(61N) <= |1-H| <= 60/(59N).                   (11)

Thus these normal directions approach the Hardy pole at scale
1/N. This is a property of the unreduced presentation, not an
intrinsic obstruction to the period having a geometric saddle.
The unit-residue pushforward above removes those auxiliary
normal variables exactly. It explains why applying ordinary
smooth Morse theory or Rivin concavity to the unreduced initial
torus cannot by itself assign the selected geometric degree.
The remaining geometric transport still has to be proved after
the actual kernel constraints have been imposed.

## 6. Reproducible checks

`experiments/audit_positive_factorial_hardy_residue.py` checks the
finite/coefficient contraction, the nonzero negative Laurent tail,
the quantitative pole bound and stationary boundary-layer formula,
and the common radius construction in the actual signed gate order.
The all-level proofs are (3)-(11), not an extrapolation from tests.
