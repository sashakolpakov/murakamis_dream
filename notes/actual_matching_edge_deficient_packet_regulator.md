# The deficient packet retains the diagram regulator and its source character

30 October 2026. The absolute reflected
anchor of the deficient packet introduces no new Bloch–Wigner regulator
constant. The fully normalized original circle coefficient has an exact
degree-reflection identity. Its endpoint Bloch symbol is invariant under
the corresponding rational involution, with absolute normalization fixed
on the real chart. The physical turn nevertheless contributes an explicit
integer-linear character. It is one on the original lattice, and cannot
be discarded in a continued stationary action.

Consequently the existing endpoint-volume theorem applies to the
source-marked full critical action after this character is retained.
This does not assign the hyperbolic volume to a bare polynomial-kernel
value, or prove that the original degree cycle contributes there.

## 1. An exact reflection of the normalized circle coefficient

Put d=N-1, q=exp(pi i/N), 0<=a<=floor(d/2),
beta_a=s_(2a)/s_a^2, and let k_a be the original fold multiplicity.
Use the actual monic determinant R_a(z;c) and define

    V_a(h)=product_(j=a+1)^(d-a) 2sin(pi(h+j)/N),
    c_t=-cos(pi(t+1)/N), h=d-t.

After the removable ordinary-column denominators are canceled, the
ORIGINAL circle-channel coefficient has the entire continuation

    C_a(t;r,s)=k_a beta_a^2 V_a(h) q^[d(r+s-t)]
                 *R_a(q^(t-2r);c_t) R_a(q^(t-2s);c_t).       (1)

Here t,r,s may be complex, while N,a remain integers. To verify the
normalization, start with the actual complete-circle coefficient

    k_a N P_a(h) x^-t nu_a^-1 fhat_a(t,r) fhat_a(t,s),
    x=q^d, nu_a=(-1)^a q^[a(a+1)],
    P_a(h)=N^-1 product_(j=1)^(d-a)2sin(pi(h+j)/N)
                    *product_(j=1)^a2sin(pi(h+j)/N).

The exact ordinary normalization is

    fhat_a(t,r)=beta_a q^[dr+(a^2-da)/2]
                  R_a(q^(t-2r);c_t)/S_a(t),
    S_a(t)=product_(j=0)^(a-1)2sin(pi(t-j)/N).

Thus N P_a/S_a^2=V_a, and the remaining channel unit is
(-1)^a q^[-a(d+1)]=1. This proves (1), first away from the
apparent poles and then by its removable continuation. The retained
half twist multiplies both sides by the same original
kappa^epsilon nu_a^epsilon, and does not change any comparison below.

Set

    t_H=N-t-2, r_H=r+N-t-1, s_H=s+N-t-1.

Then, EXACTLY as entire finite functions,

    C_a(t;r,s)=C_a(t_H;r_H,s_H).                            (2)

Indeed c_(t_H)=-c_t and q^(t_H-2r_H)=-q^(t-2r).
The monic recurrence gives R_a(-z;-c)=(-1)^a R_a(z;c).
Reindexing j by N-j in the residual product gives
V_a(d-t_H)=(-1)^(d-2a)V_a(d-t), while the monomial in (1)
changes by q^(dN)=(-1)^d. These signs cancel. This proves (2)
with scalar ONE, not an unspecified function of the degree or channel.

The [joint deficient packet](actual_q_hahn_joint_deficient_degree_packet.md)
uses precisely this reflection for its two absolute anchors. At the
negative-real determinant anchor the reflected columns lie in the
already selected ordinary packet. The offset -2 and all factors above
are retained. Formula (2) then continues the same normalized coefficient
to the large complex arguments of the geometric frame. No independent
normalization is chosen there.

## 2. The reflected endpoint symbol has exactly the same regulator

Work at the complete channel endpoint xi=1/2. Use the symbol from the
[endpoint regulator theorem](actual_augmented_plat_endpoint_regulator.md):

    B(T,U,Z)=-[U]-[T/U]+2[Z]+2[-1/Z]+[U/Z]+[-TZ/U].          (3)

The rational endpoint-root chart is

    U=T(a-1)^2/(Ta^2+1), Z=(a-1)/(a+1).

The degree reflection sends T to T_H=1/T and U to U_H=U/T.
Its SAME magnetic multiplier determines

    a_H=(2Ta-T+1)/((T-1)a+2),
    Z_H=(T+1)(a-1)/(3Ta-T-a+3).                            (4)

These identities follow by substitution in the original inverse
momentum formula. Direct substitution also gives
U_H=T_H(a_H-1)^2/(T_H a_H^2+1). The map (T,a)->(1/T,a_H)
is a rational involution. This is the degree reflection of (2),
not a replacement for the separate physical high-degree adapter.

There is an exact rational exterior-square identity

    delta B(T_H,U_H,Z_H)=delta B(T,U,Z),
    delta[z]=z wedge (1-z).                                  (5)

Here is a short factor certificate. Put

    A=2Ta-T+1, B0=(T-1)a+2, F=Ta^2+1.

Expanding (3) gives

    delta B = T wedge (T+1)+A wedge T-A wedge F
       +2A wedge (a-1)+B0 wedge F-2B0 wedge (a-1)
       +F wedge a+2a wedge (a-1).

Under (4) the corresponding factors become

    T_H=1/T, a_H=A/B0, a_H-1=(T+1)(a-1)/B0,
    A_H=(T+1)^2 a/(T B0), B0_H=(T+1)^2/(T B0),
    F_H=(T+1)^2 F/(T B0^2).

Bilinearity and antisymmetry now give (5), retaining every positive
rational constant; only the torsion sign is removed in the rational
exterior square. The focused audit expands the two symbols separately.

The regular complex chart is connected, and contains generic real
points. All maps in (3),(4) have real coefficients. Therefore the
differential formula for the Bloch–Wigner dilogarithm makes the
regulator difference constant, and the generic real point makes it zero:

    D B(T_H,U_H,Z_H)=D B(T,U,Z).                              (6)

This is an ABSOLUTE regulator comparison; equality of magnetic
momenta alone would not prove it.

The sine normalization has not disappeared from this argument. A
single normalized column has symbol

    B(T,U,Z)+[T]-[-T].

The exact reflection factor S_a(t_H)/S_a(t), at xi=1/2, contributes

    -[T_H]+[-T_H]+[T]-[-T].

It therefore converts the reflected column normalization to the
original one. The complete inverse measure has symbol
-2[T]+2[-T], canceling the two column additions. Its remaining
symbol is exactly the sum of the two terms (3). Thus (6) accounts
for both columns AND the original measure, including the residual
sine product in (1). There is no uncomputed additive regulator
constant from the absolute reflected anchors.

## 3. The exact physical turn supplies a Poisson character

Let u<=v be the target rows, h=v-u, l=t_target-v, and put

    t=d-h, r=t-u=d-v, s=l.

The literal inverse turn and nested physical cups give the original
W_a pi_a entry from the polynomial entry with multiplier

    beta_a^-1 q^[(d+2)u+d l+2N h].                            (7)

This is the actual cup convention pV(j)=N q^(-d^2+dj) and turn
s(j)=(-1)^d q^(d-2j). Substituting the entire polynomial kernel
and h0_a=k_a N beta_a gives the EXACT continued identity

    h0_a (W_a pi_a)_continued(t;r,s)
          =exp(-2pi i r) C_a(t;r,s).                         (8)

Equivalently the character is exp(2pi i v), since r=d-v.
It is one on every physical integer entry. Off the grid it is a
genuine exponential, and adds -2pi i r/N to the action normalized
by N (where r itself is the unscaled index).
For the other physical degree chamber use the already proved
exact high-block index translation. The displayed r is then its
normalized low coordinate; its complete integer affine expression
in the physical indices must be pulled back along with the character.
The high adapter adds no independent coefficient scalar.

The compiler also records the choice of the degree logarithm:
x^-t=q^(-dt), whereas the equal INTEGER expression (-1)^t q^t
with the positive product logarithm differs off the grid by
exp(-2pi i t). In scaled coordinates tau=t/N, using the marked
inverse logarithm of nu_a, the literal coefficient action is
Theta_epsilon-2pi i tau; (8) supplies the additional -2pi i r/N.
Changing the logarithm of a fixed integer channel unit adds its
explicit imaginary constant; the channel is real and held at the
endpoint, so such a constant contributes no regulator. Neither
degree nor magnetic characters may be silently removed.

These are exact reindexings of EXISTING source sectors. In the
[shared Fourier compiler](actual_matching_graph_shared_cycle_fourier_compiler.md),
the actual wire has r=epsilon x_c+B_c with B_c an integer affine
function of the retained matching labels. Since X_c=Q^x_c,
the factor in (8) is X_c^(-N epsilon) exp(-2pi i B_c).
At each original matching state the latter factor is one, and

    [X_c^b]_N X_c^(-N epsilon)L_c=[X_c^b]_N L_c.

Thus the integer winding is reindexed and the marked charge b=1
is UNCHANGED. The same fact on the original product-cotangent
cycle is equality of all lattice residues. On a continued degree
cycle the affine B_c character must also remain. This is not a
guessed correction fitted to the hyperbolic volume.

The subsequently proved [specified generic boundary lift](actual_matching_edge_generic_deficient_operator_lift.md)
has root value exp(-2pi i v) K_ent. Its own character therefore
cancels exp(2pi i v) from the actual physical turn, restoring
C_a exactly. Thus (8) describes the bare canceled-root continuation;
it is not an additional uncanceled magnetic character of the restored
specified generic lift. The two off-grid continuations remain distinct,
and the original degree logarithm and global source marks remain retained.
This consequence uses the proved generic lift, not variation of q in
the canceled root formula.

## 4. Exactly when the existing volume theorem applies

Equations (2),(6) show that the actual deficient packet carries the
same endpoint regulator as the original crossing-circle diagram,
for either physical adapter and every retained half twist. The
exact typed turn changes only the explicitly recorded monomial
characters, not its Bloch symbol. Summing these symbols at the
complete geometric representation therefore gives the ACTUAL
augmented-link volume by the degree-one diagram theorem.

To identify this regulator with a numerical critical action one
must still use the full marked stationary equations. With all
the characters above retained, the existing identity is

    Im G-sum D(B)=rho dot Im(gradient G), G=2pi i phi.

It applies to the reflected expression too: its normalized
dilogarithms, sine primitives, and exact monomials have the same
real-quadratic/imaginary-linear form, with real constant in G.
At FULL correctly marked stationarity the right side vanishes;
the held endpoint channel has zero real logarithm. Hence

    2pi Re phi=Vol(actual augmented link).

This is the volume of the source-marked critical candidate, not
the rate of the bare p_a(J) entry or of an absolute envelope.
The required winding reindexing fixes action bookkeeping; it does
not prove a nonzero coefficient of that critical point in the
original degree period. Generic operator boundary lifts, global
cycle transport and competing-source estimates remain separate.

Focused verification: [exact symbol and source normalization audit](../experiments/audit_actual_matching_edge_deficient_packet_regulator.py)
and [saved results](../experiments/actual_matching_edge_deficient_packet_regulator_results.json).
It checks the rational involution and full wedge difference, original
Newton numerators in both parity families, literal nested cups and turn,
the unchanged cyclic mark, and the absolute regulator calibration.

Independent source review: section 1 and the reflected absolute anchors
PASS. The reader rederived the original column normalization, residual
product sign, q^(dN) sign, and their exact cancellation, including both
finite index offsets. No generic moving-q lift is inferred from them.

Independent full analytical review and fresh audit: PASS. The reader
checked the exact reflection, rational regulator involution, absolute
real calibration, both physical adapters, and the original marked-charge
reindexing. A fresh redirected audit reproduced eight rational checks,
the full wedge identity, three exponent identities, 24 comparisons each
of the reflection, measure normalization and literal turn, 48 cyclic
charge checks, and three regulator calibrations. This review makes no
claim about a contributing global degree cycle.

Primary-agent full analytical review: PASS. The reader checked the
exact normalized reflection and scalar one, the exterior-square identity
and real calibration, the literal turn character, its full affine
pullback and marked-charge reindexing, and the limitation to full marked
stationarity. No cycle coefficient or unproved generic lift is included.

Scoped update: the final paragraph of section 3 records the exact
character cancellation of the independently reviewed generic-lift theorem.
It changes no residue-cycle or global-contribution claim above.
