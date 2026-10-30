# The original crossing torus transports the actual meridians

31 October 2026. Independently reviewed and frozen. The full physical
phase of the [original crossing torus](actual_crossing_casimir_torus.md)
induces the actual signed Hurwitz transport, including its common
magnetic scale. Full regular critical points of the layered direct-power
source therefore map to representations of the actual filled diagram.
This is a forward morphism on the recorded localized chart, not an
isomorphism or a selected-cycle theorem. No global coefficient bound
is asserted. Use N>=3, d=N-1, q=exp(pi i/N) and the original
scalar lambda0=q^(d^2/2), with its recorded exponential lift.

Put A0=x+y, P0=xy, f(b)=(b+x)(b+y). Distinguish the frozen crossing
note's COEFFICIENT momentum r_H=exp(2pi i I) from the PHYSICAL momentum
p=r_H^-1. This inverse must be proved from the full physical adapter,
not chosen using the symmetric Casimir. We first do that calculation.

## Full physical phase, all derivatives and the original half powers

Write the physical input heads as (v,t-v) and output heads as (u,t-u),
all divided by N at principal order. The exact finite homogeneous
identity is R^epsilon_entry=N^-1 H_(R^epsilon)/(bc)^(d/2), with its
recorded log lifts; this is (7a) of the [homogeneous-source theorem](actual_homogeneous_casimir_face_source.md).
There is no new cap or pivot in this identity. Let Psi_H be the ACTUAL
homogeneous kernel phase (including lambda0^epsilon). At a regular
local critical point of its three simplex variables, the envelope
derivatives with respect to (Log x,Log b,Log c,Log y) are (K,I,T,L),
where K+I+T+L=1. All integer characters from its original signs remain
in the critical equations. The physical principal phase is therefore

    Theta=Psi_H-(Log b+Log c)/2.                      (0a)

Take a common face-scale gamma=Log y and the literal head clocks

    Log x=gamma+2pi i t,
    Log b=gamma+2pi i(t-v)+pi i,
    Log c=gamma+2pi i(t-u)+pi i,
    Log y=gamma.                                   (0b)

These are precisely X_in,1=-x/b, X_in,2=-b/y and the corresponding
output clocks -x/c,-c/y. Here b/c are PHYSICAL input/output middle clocks
after the exact Fourier adapter. The frozen crossing note's LEFT output
b / RIGHT input c instead describes its polynomial monomial operator;
these are dual uses of the kernel, not competing physical orientations.
The finite half-index and d/N offsets in the
exact identity are retained in the original amplitude; (0a,b) are
the explicitly stated PRINCIPAL symbol. Homogeneity cancels the common
gamma derivative exactly at this order. Differentiation gives

    Theta_v=-2pi i(I-1/2),
    Theta_u=-2pi i(T-1/2),
    Theta_t=2pi i(K+I+T-1)=-2pi i L,
    Theta_gamma=K+I+T+L-1=0.                        (0c)

For the ORIGINAL kernel convention, input raising-shift symbols
differentiate positively and output symbols negatively. Restoring a
nonzero common input scale g gives

    S_in=(g exp Theta_v,g),
    S_out=(g exp[-Theta_t-Theta_u],g exp[-Theta_t]). (0d)

Indeed its generating one-form is
Log(S1_in)dv+Log(S2_in)d(t-v)-Log(S1_out)du-Log(S2_out)d(t-u);
comparison of dv,du,dt yields exactly (0d).

Thus, independently of the crossing sign,

    p=exp(-2pi i I), p_out=exp(2pi i T),
    S_in=(-g p,g),
    S_out=(-g exp(2pi i L)p_out,g exp(2pi i L)).     (0e)

The outer derivative is ESSENTIAL: it fixes the common scale transport
and not just the first/second-head ratio. No arbitrary scale is assigned
after examining a trace. For epsilon=+/-1 set E_j=exp(2pi i epsilon j)
as in the [crossing-torus theorem](actual_crossing_casimir_torus.md), section2. Equations (0e) read

    p=E_I^(-epsilon), p_out=E_T^epsilon,
    g_out/g=E_L^epsilon.                           (0f)

Now (4) of that note supplies E_I=(P0-bc)/f(b),
E_T=(P0-bc)/f(c), E_L=-(b+y)(c+y)/(P0-bc). Therefore
positive physical chronology has (c,p_out)=F_-(b,p), and negative
chronology has F_+(b,p). Equivalently it is the coefficient graph
F_epsilon conjugated by p=1/r_H. This explicitly explains the inverse
and its full normalization; it is not inferred from (2) below.

## The actual meridian matrices

The resulting ACTUAL physical Gauss data are

    X1=-x/b, X2=-b/y, S1=-g p, S2=g.                    (1)

The sign in S1/S2=-p is compulsory by (0c--f). As a separate check,
the original Jacobi symbol
at X=X1,T=X1X2=x/y has

    a(X)=-f(b)/b^2,  d(X)=-2A0/b-2P0/b^2.

Thus a(X)(Y+Y^-1)+d(X), with the original magnetic Y=S1/S2=-p,
is exactly the source-torus invariant

    sigma=2+((p-1)^2/p)f(b)/b^2.                       (2)

For each leg define the original matrices

    K=-1/X, F=S(1-X), E=(X^-1-1)/S,
    G=[[K,E],[FK,FE+K^-1]], Lminus=[[1,0],[-KF,K]].

Then the ordered physical meridians are

    A=G1, B=Lminus1^-1 G2 Lminus1, P=B A.              (3)

They have determinant one and trace minus two. Direct multiplication
gives P11=y/x and Tr(P)=sigma; this is the ORIGINAL ordered pair
Casimir, not just an abstract first integral. These formulas are on
the same Gauss units as the original compiler; any additional scale
or total-F denominator needed below is explicitly localized.

## Actual signed Hurwitz moves

Positive physical chronology is

    (A,B) -> (A^-1 B A,A),

and negative chronology is its inverse (A,B)->(B,B A B^-1). The first
new physical clock is recovered from the new first meridian by
b_new=x*(A_new)11. After setting g=1 for display, multiplication gives

    positive: c=(P0-f(b)/p)/b,
      S1_new=b p/(-b+p x-x),
      S2_new=-(-b+p y-y)/b,
      p_new=-S1_new/S2_new=(P0-bc)/f(c);

    negative: c=(P0-p f(b))/b,
      S1_new=-(b p+p x-x)/b,
      S2_new=b p/(b p+p y-y),
      p_new=-S1_new/S2_new=f(c)/(P0-bc).              (4)

For general g multiply both new S values by g. Rebuilding the second
leg from X2_new=-c/y and these S values gives exactly the SECOND
Hurwitz meridian as well, so the WHOLE ordered matrix P is preserved.
This is stronger than trace matching. The displayed extra denominators
are already factors of the regular source chart after the corresponding
F_+ or F_- substitution; they must remain excluded.

Substitution of (0f) gives exactly the S values in (4), including
S2_new/g=E_L for positive chronology and E_L^-1 for negative chronology.
Consequently the matrices checked here come from ALL physical phase
derivatives, not only the Casimir. No crossing sign or original scalar
is changed by the coefficient-to-physical inversion.

## Fixed product, centralizer and the spectral sign

The full product has the actual form

    P=[[T^-1,E_tot],[F_tot/T,F_tot E_tot+T]], T=x/y.

On F_tot!=0, fixing sigma and T fixes E_tot once F_tot is fixed. As
(b,p) varies on one conic, choose the scale g so that F_tot has that
fixed value. The common magnetic scale is thereby restored, and the
conic is a rational chart of ACTUAL ordered trace-minus-two pairs with
that fixed P. Conversely the original regular Gauss inverse recovers
(b,p,g) from such a pair. This is a local birational statement, with
the same recorded open units; not every completed-conic point is an
allowed source point.

If J is the selected eigenvalue of P, then

    J+J^-1=sigma, lambda=-J or -J^-1.

On the chosen source spectral sheet lambda=-J. Hence physical positive
crossings multiply the norm coordinate by lambda^-1, while negative
crossings multiply by lambda. The central minus sign cannot be removed
for an odd power. In particular the square of positive Hurwitz is
simultaneous conjugation by P^-1:

    H_+^2(A,B)=(P^-1 A P,P^-1 B P),

and the torus multiplication is lambda^-2=J^-2, as required. The
opposite spectral sheet interchanges the reciprocal coordinate.

At sigma=2 and f(b)!=0, equation(2) is the double equation (p-1)^2=0.
Its reduced locus p=1 has the two meridians sharing their fixed line;
positive Hurwitz swaps this commuting pair. This explains why the
completed double line is not an additional regular source saddle.
At sigma=-2 the already derived additive coordinate advances by -2A0
under positive physical chronology, the inverse of the pullback advance.

All of this is rational matrix algebra on the source-defined classical
chart. The exact finite kernels still retain their original Hermite
data, scalar lambda0^n, punctures and original marked target. A global
representation follows only after the actual wire/cup constraints are
imposed; none of these identities assigns a coefficient to that branch.

## Full regular direct-power critical points and the filled group

Fix the ORIGINAL flat-plat index word and integer exponents
n_e=epsilon_e-2p_e. Expand each nonzero power into |n_e| literal signed
crossings, preserving the original cups, caps and unrestricted marked
cap. This is the same finite source by the
[exact direct-power composition](actual_direct_long_power_source.md), and
the same actual filled diagram by the specified crossing-disk marking.
The fixed half-twist permutation and cap pairings are required to give
one main component when calling this diagram a knot; otherwise the
statements refer to its actual filled link. No asymptotic interchange
in a growing power is involved:
the exponents and expanded diagram are fixed before N.

Consider the following PRECISE class of principal critical points.
Each layer has the three simplex critical equations of its actual
homogeneous coefficient phase, on the recorded open chart (all E_j and
E_j-1, physical Gauss clocks, prefix diagonals and used denominators are
units). The point is also critical in EVERY independent physical-head
direction of the expanded diagram, with original degree constraints,
cup/cap phases and the marked-cap character retained. Local branches and
integer logarithmic characters are fixed throughout. No boundary endpoint,
escaping flag, protected-zero limit or merely constrained tangential
stationarity is included in this statement.

Every such FULL regular critical point defines a representation of the
ACTUAL filled knot group, with noncentral boundary-parabolic main
meridians and the original Morse basepaths. Scheme-theoretically, let
D_reg be the product of all of the displayed layer units, all physical
clock and raising-symbol units, all original prefix diagonals, and the
K+1 factors used for the unique noncentral main flags. Use the LOCALIZED
critical scheme (O/I)[D_reg^-1], with the original fixed logarithmic
characters on each formal neighborhood. If polynomial equations were
cleared first, I:D_reg^infinity has the same restriction to this open
scheme but denotes its closure, not an equivalent assertion on D_reg=0.
The construction below is a regular morphism from this localized critical
scheme to the actual marked representation scheme modulo simultaneous
diagonal conjugation. It is valid over local Artin C-algebras as well:
the spanning-tree recursion and all matrix formulas divide only by the
recorded units. NO isomorphism, surjectivity or converse branch selection
is claimed here. Here is the entire forward construction.

1. Use the oriented event incidence matrix B of the expanded source.
   Centered physical variations lie in ker_Z B. Its integral cycle
   lattice is saturated. Magnetic criticality says that the product of
   local derivative multipliers around every cycle is one. On a spanning
   tree solve for vertex multipliers; each non-tree edge then satisfies
   the same equation by its fundamental cycle. This is the elementary
   construction of sections2--3 of the [actual critical-scheme
   theorem](actual_augmented_plat_critical_scheme.md), and uses no extra geometric assumption on the width or cycles.
   It supplies a SHARED raising symbol S on every actual physical wire.
   The one free common multiplier rescales all S and hence conjugates
   every meridian by the same projective diagonal matrix. Fixing one
   actual unit S=1 gives a concrete gauge slice; this is not a new cap
   or a second boundary functional.

2. At each crossing, (0a--f) and (3)--(4) make those shared symbols the
   full actual signed Hurwitz map, including the common scale. This is
   why trace conservation alone would not suffice. At a cup the actual
   principal phase is pi i(x1-1), at an ordinary cap pi i x1, and at the
   marked cap pi i x2. The complementary constraint x1+x2=1 at the
   marked cap is the permitted WHOLE-SOURCE consequence of exact degree
   conservation through all other tensors, not a local replacement of
   the unrestricted mark. All three phases yield X1 X2=1 and S1/S2=-1,
   hence the literal based inverse-pair relation P=I. Their different
   integral characters remain in the action.

3. At each horizontal slice use the same lower-triangular prefix
   factors Lminus as the original Morse presentation. Whole-product
   preservation at crossings and P=I at cups/caps leave the prefixes
   outside the event unchanged. Therefore each wire has the same based
   meridian at both ends. The local Hurwitz relations and inverse-pair
   closure relations are exactly the original diagram's Wirtinger/Morse
   relations. They give its group representation, with the recorded
   central signs converted to the actual meridian lift as in the same
   critical-scheme compiler, section5. For n_e=epsilon_e-2p_e that diagram is the
   stated crossing-circle filling, so no new peripheral filling equation
   must be guessed from the scalar Casimir.

The same proof works for a connected marked link diagram componentwise
on its peripheral subgroups; the intended fixed-parity plat gives one
main component. Its noncentral unipotent meridian has unipotent PSL2
centralizer, so its commuting longitude is boundary parabolic. Neither
faithfulness nor discreteness of this representation is inferred.

This conclusion does NOT identify every point of a CLEARED whole-box
characteristic with a representation. Such a point must lift to the
regular layered chart just specified. A critical point of a reduced
phase with some variables already set to protected zero need not satisfy
the full equations. Nor has an asymptotic for H_(R^n) on this entire
chart been proved by this algebraic statement. The original finite
coefficient may receive endpoint, singular or escaping contributions;
the regular representation correspondence does not bound or select them.
Identifying the actual original cycle and obtaining the required global
phase-preserving estimate remain the substantive missing steps.


## Verification and review

[The focused audit](../experiments/audit_actual_crossing_torus_meridian_transport.py)
checks the four full physical-phase derivatives, both signed input/output
momenta and common-scale transports, all entries of both actual Hurwitz
meridians and the preserved whole product, the double-crossing conjugation,
and the commuting endpoint. It also rejects the incorrect magnetic sign.
[Results](../experiments/actual_crossing_torus_meridian_transport_results.json)
record exact symbolic identities, not numerical evidence for cycle
selection or an asymptotic. The global assembly uses the separately proved
primitive incidence and literal Morse presentation, rather than a finite
collection of diagrams.

Root full analytical/audit-code review and fresh independent replay PASS.
Independent full analytical/code review and fresh redirected replay PASS,
including the corrected coefficient-to-physical inverse, all common-scale
derivatives and the forward localized full-critical morphism. Neither
review infers a converse, a boundary extension, or a contributing period.
