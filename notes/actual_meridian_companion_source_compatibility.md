# The actual meridian period and the companion source are different pointed objects

Actual-state compatibility audit, 27 October 2026. The polynomial
companion unfolding is a valid source-frame theorem. It is currently
AUXILIARY to the selected meridian/regulator comparison: the actual
rational meridian state does not satisfy its highest-clock pointing.
Canonical ordinary-color subtraction does produce an actual highest
residual, but its unnormalized pairing is precisely the unknown K_N.
The existing regular-period theorem supplies the finite affine source
extension retaining that datum. These facts do not advance gates C--E
of [the critical-path audit](critical_path_to_original_volume_conjecture.md).

## 1. The actual orbit and a universal failure of the highest-clock equation

Fix q=q_N, Q=q^2 primitive of order N, y=M^2, U=y^N. The actual
reduced state is the NONZERO Laurent polynomial f(y)=F_N(y), with

    f(1)=K_N, f(Q^j)=C_j(q), 1<=j<N, C_1=1.

These are the original quotient-color identities, not an independently
chosen rational solution. On E=C(y) over K=C(U), sigma(y)=Qy.
After the marked splitting cover alpha^N=U, identify functions with
their values at y=alpha Q^j. Multiplication by y/alpha is
B=diag(Q^j); sigma inverse is the cyclic shift P e_j=e_(j+1).

The actual state vector is f_j=f(alpha Q^j). At U=1,alpha=1,

    [(B-I)f]_1=(Q-1)C_1=Q-1 !=0.                (1.1)

Thus the actual state fails Xv=v for EVERY knot and N>=2 in the
complete-clock normalization. This is not just a possible failure
for a manufactured state. Its complete evaluation row is e_0^t,
which obeys e_0^t P=e_(N-1)^t, not ell P=ell. The invariant
row is the all-ones row; its value is instead

    sum_j f_j=K_N+sum_(j=1)^(N-1)C_j(q).          (1.2)

For the actual orbit these two co-sources cannot be silently
identified. Normalizing the invariant row to its value on f
would introduce an unknown scalar, rather than reconstruct it.

## 2. A root rational ratio supplies only a cyclotomic line

The actual ratio a_N(y)=f(Qy)/f(y) is rational and has exact norm

    product_(j=0)^(N-1) a_N(Q^j y)=1.             (2.1)

The horizontal operator a_N inverse sigma is conjugate to sigma
by multiplication by f. Its N-th power is I and, on restriction
of scalars to K, its characteristic polynomial is z^N-1. Its
actual horizontal vector f has orbit dimension ONE under this
operator, so it is not the cyclic source required in the rank-N
companion theorem. Using the base shift sigma instead does not
repair the highest-clock failure (1.1).

More generally, for a supplied actual order-r homogeneous operator,
the rational solution defines a surjective difference-module pairing

    pi_f: M_P -> (E,sigma),
    pi_f(T^j e)=sigma^j f,
    0 -> ker pi_f -> M_P -> (E,sigma) ->0.       (2.2)

Its kernel has E-rank r-1. On the last quotient monodromy is I;
therefore the actual central characteristic polynomial has a factor
W-1, but the remaining module and extension data have been discarded
if only this quotient is retained. This proves neither its equality
with the geometric A-curve nor the multiplicity/semisimplicity of
the ENTIRE 1-sector. Its generalized multiplicity is between one
and r and is not determined by the rational solution. Extraneous
annihilator left factors can change it; no general actual minimal
rank assertion is made here.

The ratio does retain the value when its ACTUAL pointing is carried:

    K_N=[product_(j=1)^(N-1) a_N(Q^j alpha)]_(alpha=1), (2.3)

since it telescopes to f(alpha)/f(Q alpha) and f(Q)=1. Canceled
whole germs are required at any zero/pole. Constructing a_N from f
does not provide an independent uniform quantum-A construction of
that ratio: it already uses the selected state being studied.

Multiplication by f can fail to be an integral unit above U=1
when one of its orbit values is zero. The Laurent state is primitive
there because its anchor is one, but its multiplication determinant
Norm(f) need not be a unit. Thus the generic Hilbert-90 gauge in
(2.1) is not an automatic regular pointed-lattice comparison.

## 3. An actual highest residual exists after canonical subtraction

Use the EXISTING actual regular-period theorem and its notation:

    S_N(y)=1+y+...+y^(N-1),
    P_N degree<=N-2, P_N(Q^j)=C_j(q), 1<=j<N,
    R_N=(F_N-P_N)/S_N, p_N=P_N/S_N.

Define the known zero-complete interpolation and actual remainder

    c_N=P_N-[P_N(1)/N]S_N,
    H_N=R_N+P_N(1)/N.

These definitions give WHOLE Laurent identities

    F_N=c_N+S_N H_N,
    c_N(1)=0, c_N(Q^j)=C_j(q),
    K_N=N H_N(1).                               (3.1)

In the central fiber the residual is exactly

    Fbar_N-cbar_N=K_N e_0,
    e_0=S_N(y)/N modulo y^N-1.                  (3.2)

Consequently it satisfies the highest CLOCK equation, but its
original invariant-row pairing is K_N, not one. A nonzero unit
normalization making it the companion source e_0 would divide by
the target. If K_N vanished it would not even be a cyclic source.
This is an exact source compatibility statement, not a new state
or a choice of a favorable residual.

Let the supplied actual operator have order r. The fixed gauge
and denominator clearing from
[the regular-period theorem](regularized_kashaev_period.md), Section 4,
give an order-r A with

    A R_N=b_N, b_N=-A p_N.

Therefore the SAME actual construction gives

    A H_N=B_N,
    B_N=b_N+[P_N(1)/N]A(1).                     (3.3)

This is a restatement/compatibility consequence of that existing
theorem, not a new generic rational inhomogeneous factor. B_N is
known from ordinary colors, has fixed Laurent support and polynomial
coefficient bounds. Its rootwise augmented companion has rank r+1
with distinguished LAST source coordinate one. The original period
is the first-coordinate evaluation N H_N(1). The source-one quotient
is not the actual scalar period itself.

This extension is ROOTWISE. It does not establish one rational
source in indeterminate q or bound its transverse q-jets. The
original all-level/finite-pointing and Mellin reconstruction results
retain those coherence requirements separately. No equality between
their source objects and a geometric regulator extension follows
from (3.3). If a different actual generic affine factor is supplied,
it may have smaller rank; no universal minimal source rank is claimed.

## 4. The full peripheral line keeps its sign, pole and first normal

The actual full state is

    N_N(M)=epsilon_N M^(N-1)F_N(y)/S_N(y).

Its N-step meridian character is (-1)^(N-1). It is a parity line
on the M-cover at even N; replacing it by a rational function in y
without this character would change the object. Its root shift
ratio equals kappa sigma(y-1)/(y-1) times a_N, with kappa=-q^-1.
The corresponding WHOLE q-normal adapter is the full g_N, not just
that root restriction, as proved in
[the peripheral-shift audit](full_peripheral_shift_root_and_normal_audit.md).

The central regular frame is

    (U-1)N_N=epsilon_N M^(N-1)(y-1)F_N.          (4.1)

At the anchor M=-q this has the nonzero marked residue
epsilon_N(-1)^N(q-q^-1). At M=1 it vanishes; its first U-normal
coefficient along y=U^(1/N),M=U^(1/(2N)) is epsilon_N K_N/N.
Thus that zero must be kept until differentiation. A normalized
companion eigenvector at the root alone loses this selected normal
functional. Equations (3.1) and (4.1) preserve the whole original
S_N and central norm factors rather than substitute 1/N early.

## 5. A genuine meridian prototype, with its rank qualification

[The whole figure-eight identity](figure_eight_whole_source_identity.md)
proves the original state satisfies the explicit second-order
inhomogeneous meridian equation

    (c_- T^-1+c_0+c_+ T)F_N
                      =D(y)(3-U-U^-1),           (5.1)

with the EXACT source and coefficients in
[the normal-period calculation](peripheral_normal_period.md), Section 9.
Here c_0 has unique smallest y-order zero, coefficient Q; c_-,c_+
have order two. A rational homogeneous solution cannot exist,
because all its shifts have the same valuation and the least
term would be unique. The proved cyclic descent then gives
det(I-H_hom)!=0 over C(U). Its actual homogenized rank-three
source module consequently has SIMPLE central eigenvalue one:
its monodromy is [[H_hom,s],[0,1]].

This is GENERIC central nonresonance, not regular invertibility
at the complete special fiber U=1. The normal-period construction
explicitly retains its enlarged special kernel and first normal.
The full source 3-U-U^-1 has not been canceled or replaced by one.
This exact prototype illustrates an actual meridian/source module;
it is not supplied merely by the clock/companion frame theorem.

## 6. Impact on the original proof goal

The companion shell is not yet on the selected regulator path.
An actual map must intertwine the EXISTING meridian insertion and
word, carry the original co-source and all norm/normal factors,
kill actual zero-source currents in the selected quotient, and send
the uninserted selected class to a proved NONZERO geometric class.
No such general map is constructed by the source-shell classification.

The established actual reconstruction and regularized affine source
remain exact. Gate C, the nonzero selected geometric image, is still
open; the source coefficient bound at D and global logarithmic
estimate at E are also unchanged. No completion percentage or claim
that these are routine normalization steps follows from this audit.

[Exact actual-orbit/source checks](../experiments/audit_actual_meridian_companion_compatibility.py)
and [saved results](../experiments/actual_meridian_companion_compatibility_results.json).
