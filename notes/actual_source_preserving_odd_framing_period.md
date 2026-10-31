# A source-preserving odd framing period

30 October 2026. A specified difference
of the two nearest physical bands, with its exact quantum coefficient,
has the SAME normalized value as the original complete invariant.
Its normalization is nonzero at every level and costs only O(N) on
an interior real coherent cut. In the actual routed physical chart
the underlying odd form has an explicit nonzero logarithmic residue;
the actual coherent base weight remains part of the source.

This closes the old distinction between the unchanged scalar and an
inserted odd observable. It does not determine the original relative
cycle's winding, justify a quantum boundary-scale limit from separate
local packets, or supply the missing mixed-color global estimate.

## 1. The literal source and its normalization

Fix N>=2, d=N-1, q0=exp(pi i/N). Use the original regular generic
channel, with epsilon the genuine quantum parameter,

    C_e(X)=P_V[A U^-1(X tensor I)U B], C_e(I)=z(e)I.       (1)

Here A:W->V and B:V->W may have different actual Morse widths,
U is the recorded braid carrying the chosen W head to FIRST position,
and P_V closes the other physical heads with g_e=(-1)^d K_e.
All original cups, caps, complete-circle scalars and peripheral lines
are retained. These are exactly the hypotheses of the
[braided source theorem](actual_braided_two_cut_source_adapter.md).
The statement applies at arbitrary fixed width and to the specified
regular complete-source sector sum. It does not make a bare root
mark a generic intertwiner.

Let T_n=sum_(r-s=n)E_rs be the UNWRAPPED physical band, and set

    beta_a(t)=binom(d,a)t^a(1-t)^(d-a), e_t=beta(t)1^T,
    O_N=T_1-q0 T_-1,
    kappa_N(t)=1-q0-t^d+q0(1-t)^d.                       (2)

The [actual divided-descendant theorem](actual_explicit_root_channel_normal_adapter.md)
proves C_0(T_n)=z_0 T_n, including both n=+1 and n=-1.
Moreover Tr(e_t T_1)=1-beta_d and Tr(e_t T_-1)=1-beta_0.
Consequently the exact original scalar is

    Tr[e_t C_0(O_N)]/kappa_N(t)=z_0,                    (3)

wherever kappa_N!=0. No second pivotal closure or new state is inserted
in (3). The numerator is the original coherent FIRST-cut row applied
to two actual neighboring bands of (1).

For real 0<=t<=1 it is nonzero at EVERY N. Indeed put
A0=1-t^d, B0=1-(1-t)^d and theta=pi/N. Then A0,B0>=0,
A0+B0>=1, and exactly

    |kappa_N|^2=(A0-B0)^2 cos^2(theta/2)
                         +(A0+B0)^2 sin^2(theta/2)
                  >=sin^2(theta/2)>=N^-2.              (4)

There is no odd/even exception. On any fixed t in [delta,1-delta],

    kappa_N=(1-q0)[1+O_delta(N(1-delta)^(N-1))],
    kappa_N=-pi i/N+O_delta(N^-2).                      (5)

Thus its inverse has size O(N), without an exponential cost.
For complex coherent t, keep the explicit kappa_N and its actual
zeros; (4) is not a claim on arbitrary complex t.

The exact finite period in (3) is

    kappa_N^-1 [sum_(0<=a,l<d) beta_a
                       C_0(E_(l+1,l))_(a+1,a)
       -q0 sum_(1<=a,l<=d) beta_a
                       C_0(E_(l-1,l))_(a-1,a)].         (6)

These are TWO different physical support sets, with the original
internal head sums and their own finite endpoint rows. Neither is
wrapped cyclically or identified with the other's support cycle.
Their common primitive charged chart and meromorphic local currents
are supplied by the [common-band theorem](actual_matching_graph_common_band_ward_current.md).
If the cut is already the first physical slot, U=I is permitted.
For a different selected edge, its actual U and U^-1 remain in (6).

## 2. Genuine quantum normals and the indispensable q coefficient

The ordinary closed source is F_e=D_N(e)z(e), with
D_N=(-1)^d[N]_(q0 exp(epsilon)), D_N(0)=0 and D_N'(0)=nu_N.
For example retain the literal regular lift
O_e=T_1-q0 exp(epsilon)T_-1 and
kappa_e=Tr(e_t O_e). Equation (3) implies exactly

    Z_e=Tr[e_t C_e(O_e)]/kappa_e,
    D_N(e)[Z_e-z(e)]=O(epsilon^2),
    [epsilon]D_N Z_e/nu_N=z_0.                          (7)

Every original exterior scalar is the same on both sides. This is
a whole-source FIRST-trace-normal identity. It does not assert
Z_e=z(e), equality of higher quantum normals, or permission to
differentiate (3) as a generic identity. The audit retains nonzero
individual normal defects of that false replacement.

There is also a specified eigenkernel lift. With h_s(q) the ACTUAL
normalized generic descendants in the adapter theorem, put

    O_e^h=(T_1-q T_-1)diag(h_s(q)), q=q0 exp(epsilon).

Both its bands lie in the same generic descendant family, so
C_e(O_e^h)=lambda(e)O_e^h exactly and lambda(0)=z_0.
Using its own actual coherent normalization in (7) therefore gives
the same first trace normal. This option changes the generic boundary
germ; no ordinary coupon or bare mark is silently substituted.

The finite q0 in (2) is essential, not a disposable phase. Exactly

    O_N=(1+q0)/2 (T_1-T_-1)
                         +(1-q0)/2 (T_1+T_-1).          (8)

Without it, the coherent normalization would be
(1-t)^d-t^d, which is exponentially small in the interior and zero
at t=1/2. The actual O(1/N) normalization comes from the retained
quantum coefficient. Endpoint terms in (2) also remain exact.

## 3. The actual routed momentum and its logarithmic form

This section concerns the proved regular geometric chart of the
certified complete source. Its local nonzero amplitude and framing
form are those of the [source Ward density theorem](actual_augmented_plat_framing_density_source_ward.md).
No geometric assertion for an arbitrary algebraic channel is inferred.

Write A'=A U^-1 and B'=U B. The inserted head is literally the
FIRST physical slot at this new level, so its lower-prefix adapter
is the identity. Its meridian is the ACTUAL Hurwitz-transformed
meridian, not the old unbraided selected-wire matrix. Inserting
E_(l+1,l) changes the first exposed output by +1 and the A'-side
input by +1. The original boundary generating form gives
+Log p_cut-Log p_e. The coherent row used here has p_cut=1.
Thus the two actual local principal ratios are

    T_1 : p_e^-1,                 T_-1 : p_e.            (9)

This is the same bounded-band source calculation as
[the physical port theorem, Section 6](actual_two_cut_framing_port_reconstruction.md),
now with the route and its physical prefix explicitly fixed.

For completeness a suitable noncommuting first-slot route exists
in the certified complete-circle source. Choose a slice entering an
actual circle box. Its two main meridians A,B have
Tr A=Tr B=Tr BA=-2. They cannot both fix reference infinity: two
upper triangular trace-minus-two parabolics have product trace +2.
The positive route R_1...R_j makes its new first meridian
V_j^-1 mu_j V_j, V_j=mu_(j-1)...mu_1, by the actual Hurwitz rule.
If every routed candidate fixed infinity, induction would make every
original mu_j upper triangular, a contradiction. Thus some recorded
route has nonzero lower-left entry. This uses the original reference,
main component and complete-circle geometry, not a free reframing.

In the same trace-two parabolic normalization as the port theorem,
write that routed meridian and the cut frame as

    mu_e=I+c[[b,-b^2],[1,-b]], c!=0,
    F(r,s)=[[r,1-r],[s,-s]], s!=0,
    R=r-sb, A_cut=(1+s)^-1.

Directly conjugating by F gives

    p_e=(R-1)/R,             k-1=(c/s)R(1-R).            (10)

On its regular chart R!=0,1 and k-1!=0, the underlying original
marked scalar density is

    Omega_src=(c_D/s) dr wedge dLog A_cut, c_D!=0.        (11)

The factor c_D is independent of the framing point; the original
marked source and transverse Gaussian normalization is in it. The
full channel Gaussian, when included under its proved hypotheses,
changes it by its retained nonzero factor, not an assigned unit.

That original marked row has entries 1/N, whereas (6) uses beta_a(t).
Thus the literal new source retains the base weight

    B_(N,t)(a)=N beta_a(t)/kappa_N(t).                  (11a)

It multiplies the corresponding two band densities. It is not globally
absorbed into the framing-constant c_D: beta_a has its own coherent
action as the first cut varies. At a legitimate first-cut localization
one instead retains its ACTUAL nonzero local Gaussian factor. The
following rational-form calculations concern (11) times the odd symbol;
the full coherent source additionally keeps (11a), or that localized
factor, and its original first-cut cycle.

The q-retained combination of the two classical ratios is exactly

    p_e^-1-q0 p_e=(1-q0)+1/(R-1)+q0/R.                  (12)

At fixed s its product with the residual one-form c_D dr/s has
primitive

    (c_D/s)[(1-q0)r+Log(R-1)+q0 Log R].                  (13)

Its residues at R=1, R=0 and r=infinity are respectively
c_D/s, q0 c_D/s and -(1+q0)c_D/s. On a FIXED first-cut fiber the
coherent base weight is independent of r, so it multiplies all three
residues unchanged; after a proved first-cut Gaussian the retained
factor does the same. These are local meromorphic-form residues.
They do not assert that the original period surrounds any of those
divisors with a nonzero relative coefficient.

There is an exact noncancellation check for a SPECIFIED sample of this
underlying residue. Use the canonical half-index clocks

    A_a=q0 Q0^a, s_a=A_a^-1-1, Q0=q0^2, 0<=a<=d,
    G_N(t)=sum_a beta_a(t)/s_a.                         (13a)

None of the s_a is zero. Since |A_a|=1 and A_a!=1,
Re[A_a/(1-A_a)]=-1/2. Thus for every real 0<=t<=1,

    Re G_N(t)=-1/2, |G_N(t)|>=1/2.

At t=1/2 the exact pairing a with d-a has A_(d-a)=A_a^-1
and equal beta weights, so G_N(1/2)=-1/2 exactly at both parities.
Retaining the base co-source and its original 1/N averaging explicitly,
the sampled fiber residue is

    (1/N)sum_a [N beta_a(t)/kappa_N(t)]
                     *[-(1+q0)c_D/s_a]
            =-(1+q0)c_D G_N(t)/kappa_N(t)!=0.           (13b)

This is a finite algebraic sample of the UNDERLYING meromorphic form.
It is not an identification with the actual quantum period's residue,
its first-cut pushforward, or a uniform packet outside a fixed chart.

At fixed framing point q0 tends to one. Put s2=k-1. Equations
(10)--(11) give the leading odd form exactly as

    (p_e^-1-p_e)Omega_src
                =c_D ds wedge ds2/[(1+s)s s2].          (14)

The UNDERLYING form (14) has double logarithmic residue c_D!=0
at s=s2=0, in the displayed order. This is not automatically the
full coherent-weighted residue there: (11a) varies with the base
clock, and an interior coherent localization is a different operation.
Equivalently the physical two-position deck exchanges
p_e and p_e^-1; its odd density times this odd observable is the
nonzero deck-EVEN form (14). This is a statement about the specified
leading form. A formal two-sheet trace cancels an odd-density part
only when the actual two-sheet pushforward with its orientations is
being taken; it is not automatically the original global cycle.

## 4. What this replacement does and does not settle

Equation (3) closes the source-preservation gap left in Section 7 of
the older port theorem: the q-weighted odd observable is now an EXACT
normalized source for the unchanged scalar. It does not replace the
relative cycle by a field trace or determine its winding. The original
two support cycles, their marked orientations and every endpoint term
in (6) are still required in that comparison.

There is a separate uniformity issue at the resonant boundary.
For r=N rho, with rho bounded away from zero and s,b bounded,
the RATIONAL expression (12) has

    p_e^-1-q0 p_e=(2/rho-pi i)/N+O(N^-2),
    (p_e^-1-q0 p_e)/kappa_N -> 1+2i/(pi rho)             (15)

for an interior real coherent t. Here both parts of (8) have the
SAME order. Separate O(1/N) errors in the two actual quantum band
packets can alter the normalized limit (15). Consequently (15) is
classical-symbol data, not a proved uniform quantum boundary-period
kernel. A source-level joint expansion with sufficient cancellation
control remains necessary there.

Finally this complete-source identity supplies neither a nonzero
mixed-color packet nor a global contributing-cycle theorem for long
fillings. Its exact finite algebra is uniform in fixed width; its
geometric residue has the stated certified complete-source scope.

## Validation

The [focused original-source audit](../experiments/audit_actual_source_preserving_odd_framing_period.py)
and its [results](../experiments/actual_source_preserving_odd_framing_period_results.json)
check 22 actual original/routed sources, including rectangular cuts:
200 root odd entries, 188 literal band terms, 22 whole first normals
and 400 generic eigenkernel jet entries. Twenty literal boundary
normal defects are nonzero, confirming the stated distinction.
Independent symbolic calculations check all four physical Gauss
entries, the q decomposition and primitive, three one-form residues,
the oriented doublelog form and residue, and the two CLASSICAL
boundary limits. At 80 digits, 315 all-level/both-parity normalization
checks reproduce (4), with maximum identity error 2.11e-81. The
expanded audit also checks the exact inverse-clock residue identity,
315 specified coherent residue samples and 63 symmetric t=1/2
samples; the largest real-part error is 2.02e-77. These samples
retain the stated underlying-form scope.

The statement concerns the genuine first trace normal and the underlying forms in (13a,b), with the coherent base weight retained.

The half-index sampling corollary has only the stated limited domain.
