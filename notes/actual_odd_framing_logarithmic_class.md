# The marked logarithmic class of the source-preserving odd form

30 October 2026. The underlying odd framing
form is the pullback of an explicit integral logarithmic class.
Keeping q0 gives a stronger two-integer noncancellation criterion.
Neither calculation assigns those integers to the original quantum
cycle or removes its coherent base weight.

## 1. The actual marked functions

Use the fixed original cut and the ACTUAL routed first head of
[the source-preserving odd-period theorem](actual_source_preserving_odd_framing_period.md).
The recorded route and its inverse remain in the source. In its
complete parabolic frame write

    F(r,s)=[[r,1-r],[s,-s]], A=(1+s)^-1,
    mu_e=I+c[[b,-b^2],[1,-b]], c!=0,
    R=r-sb, p_e=(R-1)/R,
    k-1=(c/s)R(1-R), q0=exp(pi i/N), N>=2.             (1)

Here mu_e is the actual Hurwitz-transformed meridian, not the
unrouted edge meridian. The constant c is nonzero exactly when
this routed first-head position detects the residual framing.
The underlying original marked density is

    Omega_src=(c_D/s)dr wedge dLog A,
    c_D!=0, independent of r,s.                       (2)

Work on its regular framed locus where s!=0,-1 and R!=0,1,
with any additional source divisors also removed. Define the units

    f=1-A=s/(1+s), g_0=R, g_1=R-1,
    Psi=(f,k-1): framed locus -> (C*)^2.               (3)

These are algebraic functions of the ACTUAL marked physical clocks
and relative wave momentum. For example R=1/(1-p_e). They do not
depend on logarithm branches or on reparametrizing the same framed
point. They do depend on the chosen cut, route and orientations;
changing those data is an actual source adapter, not an invariance
assertion about (3).

The principal odd form computed from the literal two bands is

    (p_e^-1-p_e)Omega_src
       =c_D ds wedge d(k-1)/[(1+s)s(k-1)]
       =c_D dlog f wedge dlog(k-1).                    (4)

Thus (4) is precisely the pullback of dlog z1 wedge dlog z2
through Psi, with its original nonzero scalar and orientation.
This is a logarithmic class on the FRAMING orbit. It is not a
Bloch regulator, and it must not be substituted for the separately
proved Bloch-regulator value of the actual three-manifold.

## 2. Closed-cycle pairing, proved directly

Let Gamma be a compact closed oriented two-cycle in the displayed
regular locus, or a finite sum of smooth such cycles. For two
nonvanishing functions u,v there, write

    dlog u=dlog|u|+i alpha_u,

where alpha_u is the globally defined closed argument one-form.
Every term of dlog u wedge dlog v containing a modulus derivative
is exact: log|u| and log|v| are single-valued real functions, and
the argument one-forms are closed. Its closed-cycle integral is
therefore -integral_Gamma alpha_u wedge alpha_v.

The map (u/|u|,v/|v|):Gamma->S1 x S1 has an integer degree n.
One elementary description is the signed number of inverse images
of a regular point after subdividing the cycle. Local change of
variables and cancellation along paired subdivision edges give

    integral_Gamma alpha_u wedge alpha_v=(2pi)^2 n.

Consequently

    integral_Gamma dlog u wedge dlog v=(2pi i)^2 n.     (5)

The same argument extends additively to integral cycles. In
particular the period of (4) is (2pi i)^2 c_D deg(arg Psi).
This proves the normalization without selecting a geometric cycle
or citing a cohomological comparison theorem.

For an unramified finite cover of degree d over such a cycle, its
FULL transferred cycle pairs with the pulled-back form as d times
the original period. This follows by summing the local sheets in
the integral. A zero pairing therefore stays zero under transfer.
One selected lift instead requires its actual descent and multiplicity;
the covering map alone does not select an original nonzero period.
This statement concerns the specified transported source cycle, not
an assertion about character polynomials of arbitrary manifold covers.

## 3. The retained q0 detects two integer classes

Keep the actual finite quantum coefficient in the UNDERLYING
rational symbol form, and put

    Omega_q=(p_e^-1-q0 p_e)Omega_src,
    lambda=(r/s)dlog A.

Since d lambda=Omega_src/c_D and dR=dr-b ds, direct substitution
of p_e gives the exact identity

    Omega_q=(1-q0)c_D d lambda
            +c_D dlog f wedge [dlog g_1+q0 dlog g_0].  (6)

No primitive is dropped on a relative chain. On a CLOSED Gamma,
however, the first term integrates to zero. Define the two integers

    n_j=(2pi i)^-2 integral_Gamma dlog f wedge dlog g_j.

Then

    integral_Gamma Omega_q=(2pi i)^2 c_D(n_1+q0 n_0).   (7)

The argument of q0 lies strictly between zero and pi. Thus (7)
vanishes if and only if n_0=n_1=0. More quantitatively, for a
nonzero integer pair,

    |n_1+q0 n_0|>=sin(pi/N)>=2/N.                     (8)

If n_0!=0 use its imaginary part; otherwise |n_1|>=1. The last
bound follows from concavity of sine on [0,pi/2]. This covers both
parities and all N>=2. No restriction on the relative sizes or
signs of the two integers is needed.

At q0=1 the two classes combine: because
k-1=-c g_0 g_1/s and dlog f wedge dlog s=0,
deg(arg Psi)=n_0+n_1. The finite-q criterion is strictly sharper:
opposite nonzero integers may have zero classical total degree,
while (7) is still nonzero with only polynomial loss. This remains
a criterion for the stated rational SYMBOL form, not an assertion
that a finite quantum packet has already been replaced by it.

## 4. The original source still requires relative transport

The odd-period theorem proves the unchanged scalar exactly as
Tr(e_t C0(T1-q0T_-1))/kappa_N(t). The original scalar density (2)
contains a marked row 1/N; this new source has the additional base
weight N beta_a(t)/kappa_N(t), with its original finite head sum.
It cannot be absorbed into c_D as A varies. A legitimate first-cut
Gaussian retains its own nonzero factor; an arbitrary replacement
by a closed two-cycle with constant weight is not licensed by (5).

Likewise the explicit nonzero finite sample of the fiber residue
in that theorem is only a sample of the underlying form. It does
not show that the actual quantum period has degree (n_0,n_1).

There is a useful CONDITIONAL sampling corollary. Suppose a specified
closed cycle on EVERY canonical first-head fiber has the SAME integer
winding pair (m_0,m_1) about R=0,1. Its underlying fiber period is
2pi i c_D(m_1+q0 m_0)/s_a, where
A_a=q0 Q0^a and s_a=A_a^-1-1. Keeping the original coherent sample
and its normalization gives exactly

    2pi i c_D(m_1+q0 m_0) G_N(t)/kappa_N(t),
    G_N(t)=sum_a beta_a(t)/s_a.                        (8a)

For real t, Re G_N=-1/2; on any fixed interior real t compact,
|kappa_N|<=C/N. Thus a nonzero common pair gives a lower bound
c|c_D| in (8a), even if m_1=-m_0!=0. This is algebra of the
SPECIFIED underlying cycles; their realization by the quantum source
is not proved. A restricted window is not covered without an explicit
bound for its weighted remainder: a small binomial tail alone does
not bound unspecified winding integers on the discarded fibers.

Uniform matching is also separate: at r=N rho, the actual
q-retained symbol has size N^-1, and separate O(N^-1) errors in
the two quantum bands do not determine their normalized difference.

For a relative chain, (6) retains the boundary term
(1-q0)c_D integral_(boundary Gamma) lambda. Its argument integrals
need not be integers. Every source-divisor tube, the primitive
cotangent measure, the finite-head carries and the retained
Poisson characters must be transported with that chain. The
[H-period theorem](actual_root_channel_H_period_transport.md)
gives explicit corrections for the two normal insertions; it does
not provide the missing geometric pushforward or its ends.

There is no known identification of those integers with the
original physical head cycle. If Psi and g_0,g_1 extend as
nonvanishing functions over a particular small head polydisk,
its local torus has zero degree by contraction within that disk.
This observation has that EXPLICIT regular-extension hypothesis;
it says nothing about integer nodes where source or geometric
divisors degenerate. An N-head carry fixes the physical clocks,
so it does not by itself assign degree one. Nonzero winding can
only be asserted after the actual pushforward and its relative
end/divisor terms have been computed.

Thus the new checkable criterion is precise: for an explicitly
constructed CLOSED underlying framed cycle, a nonzero pair
(n_0,n_1) prevents cancellation in (7). For the original invariant
one must additionally justify its weighted quantum realization.

## 5. Class-wide geometric and long-twist quantifiers

Fix k>=2 and a finite ordered 2k-plat skeleton D, with every
crossing in a designated two-strand box, actual cups/caps, cut,
primitive crossing-disk markings, and fixed half twists
epsilon_i in {0,+1,-1}. Combine adjacent powers of the same
generator before treating their full twists as independent. The
outside terminal matching together with the parity restoration
must be one cycle. This finite test ensures that all exponents
epsilon_i-2p_i give knots; full twists do not change connectivity.
Here k is a presentation width, not a claim of minimal bridge number.

For geometry alone, the least restrictive proved sufficient input
is an [actual positive marked gluing certificate](general_marked_positive_gluing_certificate.md):
the correct labeled manifold quotient, torus links, positive shapes,
complex edge equations and complete primitive peripheral equations.
It proves the complete metric and volume of the actual marked exterior.

The current common boundary-chart route uses the STRONGER labeled
right-angled certificate of the [matching-graph theorem](general_augmented_plat_matching_geometry.md).
Its ideal vertices and supporting Lorentz normals have the original
medial incidence, strict nonincident inequalities, and orthogonal
adjacent face normals. The actual white-reflection prefixes and
signed shaded pairings are retained. These are finite algebraic
equalities/strict inequalities on supplied exact data. The certificate
constructs a positive marked triangulation; the reverse implication
has not been proved. There is no restriction to a Conway tree or to
one fixed width, but existence of such data for EVERY essential
hyperbolic augmented plat is not asserted.

No EXTRA noncommuting-route hypothesis is needed in that class.
At an actual complete box Tr A=Tr B=Tr BA=-2, so its punctures
cannot all preserve the reference cusp flag. The literal Hurwitz
routes and induction in the odd-period theorem therefore supply a
fixed routed first head with c!=0. Its exact source-preserving odd
observable, nonzero kappa_N, and the nontrivial forms (4),(6) are
now proved at arbitrary fixed width. This removes the old need to
POSTULATE an orientation-sensitive observable representing the same
scalar. It removes none of the original global-cycle or mixed-color
asymptotic hypotheses.

The [geometric filling corollary](general_augmented_plat_long_filling_quantifiers.md)
already supplies T_geom(D) for all independently long signed
fillings, and all partial subsets, under the positive marked
certificate. The full conjecture remains: for every fixed essential
hyperbolic augmented D as above, there exists T(D) such that for
EVERY FIXED integer vector p with all |p_i|>T(D),

    lim_(N->infinity) (2pi/N)log|K_N(K_D(p))|
                       =Vol(S3 minus K_D(p)).           (9)

The broad conjecture assumes hyperbolicity of the actual augmented
exterior; it is not restricted to diagrams already carrying our
right-angled certificate. The present boundary construction applies
to the certified subclass and does not prove that certificate exists
for every diagram in the conjecture.

Both level parities and composite levels are included. Signs and
relative slope magnitudes are unrestricted. The slopes are fixed
BEFORE N tends to infinity; thresholds may depend on the entire D,
not just k. No uniform statement for p=p(N) follows.

The existing [source-to-filling theorem](general_original_source_long_filling_transfer.md)
proves (9) CONDITIONALLY on the original uniform complex external-color
packet, its nonzero contracted amplitude, full alias/normal/color
gap, and actual marked geometric action selection. A unit amplitude,
or a controlled coordinate monomial times a unit, gives every long
tuple. A merely nonzero germ permits an exceptional analytic divisor,
as the [source-divisor theorem](general_long_filling_source_divisor.md)
states. The internal Casimir deficits N-1-2a_i controlled by the
boundary envelope are not the external filling-color defects N-j_i.
The new logarithmic integer criterion isolates a concrete part of
the needed cycle calculation; it is not a replacement for that packet
or its global complementary-color estimate.

This elementary note has no separate numerical audit. Its identities
follow by the displayed changes of variables, Stokes argument and
integer-degree calculation; the finite source and routed geometry
are audited in the cited odd-period theorem.

The logarithmic-class calculation supplies neither the geometric winding nor a mixed-color packet.

The logarithmic criterion remains separate from the actual weighted quantum cycle and the three-manifold regulator.