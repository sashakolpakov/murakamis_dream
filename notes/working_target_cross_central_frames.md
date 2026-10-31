# Working calculation: actual target frames with real anti-diagonal rows

30 October 2026. WORKING, not a global feasibility theorem. The local
rank-one equations below are exact. Their compatibility with the
common selected frame for the ENTIRE augmented link is unproved.
In particular the first local branch must not be used to claim that
the Green-kernel theorem applies at the complete global critical point.

## Local inverse-turn data

Use the ACTUAL inverse-turn pairs of
[the polynomial generating-action note](actual_matching_edge_polynomial_geometric_action.md).
For a target trace below -2, put

    J=-exp(-2 eta), eta>0, S=sinh eta,
    T=diag(J,J^-1),
    R=(1+iS)/(1-iS), D=diag(R,1).

The first incoming target meridian can be put, by a centralizer
conjugacy, in the form

    A_t=[[a,1],[kappa,d]],
    a=-2J/(J+1), d=-2/(J+1),
    kappa=-(J-1)^2/(J+1)^2.

The second is B_t=T A_t^-1. Both have trace -2 and determinant one.
The first outgoing target meridian is D A_t D^-1. This retains the
actual ordered target conjugator; it is not a freely chosen diagonal.

Choose a real total physical degree parameter tau in (1/2,1), and
write

    E=exp(-2pi i tau), e=exp(-pi i tau), c_tau=-cos(pi tau)>0,
    p=(E-J^-1)/(J-J^-1),
    h=1/(2S^2), K=h^2(c_tau^2+S^2).

For a rank-one trace-one projector

    Pi=[[p,q],[r,1-p]],

the target total diagonal is Tr(T Pi)=E. Define X=r/e and
Y=kappa q/e. Then the rank-one condition is exactly XY=K, and

    Tr(A_t Pi)/e=-2h c_tau+X+Y,
    Tr(D A_t D^-1 Pi)/e=-2h c_tau+R X+R^-1 Y.       (1)

## Two exact real anti-diagonal branches

Demand that the two expressions in (1) are respectively

    q_in=rho+i sqrt(1-rho^2),
    q_out=rho-i sqrt(1-rho^2), -1<rho<1.            (2)

They then have modulus one and are conjugates. Solve the two
linear equations (1) for X,Y. Direct substitution in XY=K gives

    [(1+S^2)rho+c_tau]^2=S^2+2,
    rho_+=[sqrt(S^2+2)-c_tau]/(1+S^2),
    rho_-=[-sqrt(S^2+2)-c_tau]/(1+S^2).             (3)

The projector is reconstructed by r=eX, q=eY/kappa. Consequently
these are ACTUAL common local frames for the ordered inverse-turn
pair, not independent choices of three magnetic variables.

The original physical-coordinate dictionary is U=-1/a_1 and
T_physical=1/a_2. With the marked argument in (2), its rows are

    nu_out=(tau-1)/2+acos(rho)/(2pi),
    nu_in=tau-nu_out.                             (4)

Thus strict physical cross-central support is equivalent to

    -1<rho<c_tau.

The stronger two finite-propagation windows at the folded row are

    0<nu_out<tau-1/2, 1/2<nu_in<tau,

and, together with physical support, are equivalent to

    -c_tau<rho<c_tau.                             (5)

For tau>3/4, one has c_tau>1/sqrt(2), and

    0<rho_+<c_tau

for EVERY eta>0: the upper inequality is exactly
c_tau>1/sqrt(S^2+2). Hence the plus branch supplies a local real
anti-diagonal frame satisfying (5), uniformly without a small-eta
restriction.

For the minus branch, (5) is equivalent to

    c_tau>sqrt(S^2+2)/S^2.

It can therefore be arranged with tau sufficiently close to one
precisely when S^2>2, equivalently the crossing-circle rectangle
ratio c=sech eta is below 1/sqrt(3). This is a sufficient local
frame statement, not a proof that the link's other disks allow it.

There is an EXACT finite-source discriminator beyond these local
frame equations. Since J is tridiagonal, p_a(J) has bandwidth at
most a. In the anti-diagonal coordinates (4), the scaled row distance
is

    nu_in-nu_out=1-acos(rho)/pi=1/2+asin(rho)/pi.   (5a)

The plus branch has rho_+>0, so its distance is strictly greater
than 1/2. For the folded row a/N->1/2, all sufficiently close
integer row pairs therefore have IDENTICALLY ZERO polynomial
matrix entry. This rules out that branch as a direct nonzero
real-row exceptional kernel, independently of its strip diagnostics.
The minus branch has distance below 1/2 and does not have this
support obstruction. This does not prove it is selected or nonzero
in the surrounding contraction. The finite-propagation identity
concerns action on a whole continuant vector; its safe output window
must not be confused with support of an individual input-output entry.

## The actual frame pullback cannot be omitted

The inverse pivotal turn changes the basepoint. If the original
first based meridian is A_out, the local lower-Borel formula gives

    Pi_target=A_out Pi_old / Tr(A_out Pi_old),
    Pi_old=A_out^-1 Pi_target / Tr(A_out^-1 Pi_target). (6)

To verify (6), in a physical frame the first lower matrix is
L_1=[[1,0],[-G_21,G_11]]. Its cyclic base change sends the projector
E_11 to L_1^-1 E_11 L_1=G E_11/G_11. Conjugating back gives (6).
The denominators in this calculation are nonzero at the strict
unit-diagonal local frames above.

The common shaded-exterior/selected-strip conditions must be tested
on Pi_old and its actual prefixes. They cannot be tested on Pi_target
as if the turn left the frame unchanged.

Diagnostic calculations in the canonical original A,B,C matrices,
with eta=.2,1,2 and tau=.8,.875,.99, put the PLUS-branch old image
and kernel flags outside the crossing disk's own selected strip.
For the MINUS branch at eta=1.2, arcosh(2),2, the tested flags lie
inside that one strip. These observations are NOT a proof of those
inequalities throughout either family. They give no information
about all the OTHER disk circles of an arbitrary matching graph.

Thus local real Green rows are achievable, but their simultaneous
compatibility with the already selected complementary boundary state
remains the precise missing geometric condition. No common-frame,
Green-branch, contour or full-source asymptotic theorem follows from
this working calculation.
