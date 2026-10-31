# The actual local source phase generates ordered character transport

30 October 2026. The explicit augmented-plat phase has a direct algebraic
map to the original ordered pair character. This note proves that map,
including the full factorial normalization, its centralizer transport,
and its regular parabolic limit on the longitude cover. It is a local
critical-phase theorem, not a claimed full-source asymptotic or a new
choice of quantum invariant.

The remaining global issues are stated in section 6. In particular the
local calculation does not assign the source action an absolute manifold
regulator merely because its critical equations have the right character.

Subsequent comparison: the [regular geometric chart](actual_augmented_plat_regular_geometric_phase_chart.md)
supplies an unfolded complete geometric candidate, and the
[endpoint regulator theorem](actual_augmented_plat_endpoint_regulator.md)
fixes its absolute volume anchor under full marked stationarity.
Those additional results do not supply the physical cycle or global
source estimate left open in this local note.

## 1. Retain the complete normalized coupon phase

Use the low physical degree chamber of the
[actual compiler](actual_augmented_plat_phase_compiler.md). Let tau be
the scaled pair degree, u and v its output and input first magnetic
indices, xi the folded Casimir index, and alpha,beta the two internal
q-Hahn variables. Set

    J0(s)=integral_0^s Log(2 sin(pi w)) dw,
    B(s,r)=J0(s)-J0(r)-J0(s-r),
    E(tau,xi,u,alpha)=B(xi,alpha)+B(u,alpha)
                         +B(tau-u,xi-alpha)-B(tau,xi),
    Phi(tau,xi,u,alpha)=E(tau,xi,u,alpha)
                  +pi i [u-xi u+(tau+xi-1)alpha],
    H(tau,xi)=2J0(tau)-J0(tau-xi)-J0(tau+xi-1).

All logarithms have the compiler's actual factorial marks. The complete
coupon, with retained half twist epsilon in {0,+1,-1}, has leading phase

    Theta_epsilon=H+Phi(tau,xi,u,alpha)+Phi(tau,xi,v,beta)
                      +pi i[tau+(epsilon-1)(xi+xi^2)].       (1)

Its already recorded external kappa^epsilon is not removed or replaced;
its leading constant is a unit phase and has no derivative in these
variables. The finite offsets and normal-derived coefficients remain
those of the exact compiler. Equation (1) is their leading phase, not
an equality of finite quantum germs.

Write

    T=e^(2pi i tau), U=e^(2pi i u), V=e^(2pi i v),
    J=e^(2pi i xi), Z=e^(2pi i alpha), W=e^(2pi i beta).

On a regular logarithmic chart the two internal equations are exactly

    P(U,Z)=0, P(V,W)=0,
    P(X,Y)=T(J-Y)^2(X-Y)+(Y-1)^2(TY-XJ).                    (2)

Every formula below is localized only where its displayed denominators
are nonzero. In particular these equations have not licensed deleting
boundary strata. Their leading quadratic coefficients may be assumed
nonzero for the symbolic certificate; the rational identities themselves
hold wherever their displayed denominators are defined.

## 2. The actual Casimir equation, with its magnetic momentum

Direct differentiation of Phi gives

    Y(X,Z)=e^(Phi_u)=(1-X)(TZ-XJ)/[J(X-Z)(T-X)].            (3)

The principal symbol of the original symmetric Jacobi block is

    a(X)= (X-T)(1-X)/T,
    d(X)=2X(1+T-X)/T,
    Omega_cl=a(X)(y+y^-1)+d(X).

These follow directly from the physical tridiagonal entries, with
q->1 and q^(N-1)->-1. Equation (2) implies

    a(X)[Y(X,Z)+Y(X,Z)^-1]+d(X)=J+J^-1.                  (4)

This is an exact rational identity modulo P. For example its difference
from the right side equals

    -X(J-T)P(X,Z)/[JT(X-Z)(JX-TZ)].

Thus the critical phase yields the actual ordered pair trace, not just
an independently chosen quadratic with the same number of roots.

The inverse change is explicit:

    Z=XJ[y(T-X)+(1-X)]/[yJ(T-X)+T(1-X)].                  (5)

On its regular chart, the Jacobi equation (4) conversely implies (2).
The local root is therefore selected by the actual magnetic momentum y;
one does not choose a root by its numerical size.

## 3. Full normalization preserves the ordered product

Differentiating ALL terms of (1), including H and pi i tau, gives

    D=e^(Theta_tau)
      =JZW(T-J)(T-U)(T-V)/[(TJ-1)(TZ-UJ)(TW-VJ)].          (6)

Omitting the inverse-measure factorials or their phase would change (6).
Introduce an arbitrary nonzero common magnetic scale g. The actual
incoming and outgoing raising-shift symbols are

    (S1_in,S2_in)=(g Y(V,W),g),
    (S1_out,S2_out)=(g/[D Y(U,Z)],g/D).                   (7)

The signs in (7) follow from a kernel: right multiplication by a raising
shift differentiates its input positively, and left multiplication
differentiates its output negatively. Total-degree conservation supplies
the common scale g. No Hermitian conjugation has been inserted.

For a physical head define its original classical flag matrices by

    K=-1/X, F=S(1-X), E=(X^-1-1)/S,
    Lplus=[[K,E],[0,1]], Lminus=[[1,0],[-KF,K]],
    G=Lminus^-1 Lplus=[[K,E],[FK,FE+K^-1]].                (8)

They have determinant one and trace -2. Prefix conjugation gives the
ordered meridians A=G1 and B=Lminus1^-1 G2 Lminus1, exactly as in the
proved quantum character identity. Their product is

    P=B A=[[T^-1,E_tot],[F_tot/T,F_tot E_tot+T]],
    F_tot=F1+K1^-1 F2, E_tot=E1 K2+E2.                   (9)

Equations (2),(3),(6),(7) give

    F_tot,out=F_tot,in,
    K_tot,out=K_tot,in=T^-1,
    Tr P_in=Tr P_out=J+J^-1.                             (10)

For F_tot nonzero, (9) then gives E_tot,out=E_tot,in as well. Hence the
ENTIRE ordered matrix P is preserved. This is stronger than trace
matching. The identity continues wherever the full rational expressions
are defined; the present proof uses the stated regular F_tot chart.

For reproducibility set g=1 and write

    f=(1-V)Y(V,W)+T-V.

The first equality in (10) is the following explicit certificate:

    [(1-U)/Y(U,Z)+T-U]-D f
      = VZ(J-T)(T-U)P(V,W)
         /[(V-W)(JT-1)(JU-TZ)(JV-TW)].                   (11)

The scale g merely conjugates the common matrices and costs no source
normalization.

The HIGH-degree chamber has an equally literal adapter. If s is the
physical pair degree divided by N, put

    tau=2-s, u=a-s+1, v=c-s+1,

where a,c are its physical output/input first indices. These are the
leading versions of the exact compiler's d=N-1 index translation;
the finite offsets remain in its amplitude. The physical exponentials
are (U/T,U^-1) at the output and (V/T,V^-1) at the input. Chain-rule
differentiation of the SAME phase gives

    Y_out,high=Y(U,Z), Y_in,high=Y(V,W),
    D_high=1/[D Y(U,Z)Y(V,W)].                           (11a)

Use (7) with D_high and these PHYSICAL head exponentials. This is
the actual Chevalley-and-flip map (X,S)->(X^-1,-S^-1) on both low
heads, with the common scale consistently transported. It exchanges
the total F and E and inverts total K. Therefore the whole high
ordered product is preserved as well. There is no independent high
frame gauge or differentiation of a root-only identity involved.
The high coupon has the SAME channel derivative (12), and the four
centralizer identities (14) are also checked symbolically in these
physical high coordinates. Thus the local principal map covers BOTH
original degree chambers, while retaining their separate integer lifts.

## 4. The channel derivative is a centralizer eigenratio

Let R0=e^(partial_xi Theta_0). Direct differentiation yields

    R0=ZW(J-1)^4(TZ-UJ)(TW-VJ)
        /[JUV(J-Z)^2(J-W)^2(T-J)(TJ-1)].                 (12)

For J!=+/-1 define the matrix

    C=I+(R0-1)/(J-J^-1) (P-J^-1 I).                     (13)

Its eigenvalues on the P-eigenlines J and J^-1 are R0 and 1,
respectively, so det C=R0 and C commutes with P. Moreover

    A_out=C A_in C^-1,
    B_out=C B_in C^-1.                                 (14)

These are exact rational identities on (2). An entirely polynomial
certificate is obtained by putting

    Ctilde=(J-R0/J)I+(R0-1)P.

Clear only its displayed denominators in Ctilde A_in-A_out Ctilde.
Every one of the four resulting entries has zero remainder modulo the
two explicit quadratics P(U,Z),P(V,W). The accompanying executable
certificate performs this calculation over Q(T,U,V,J), not at sampled
roots or numerical shapes. Equations (8),(9) supply all matrices used.
The second identity of (14) follows from the first and preservation of P.

Thus R0 is the eigenratio of a genuine ordered-pair conjugator. It is
not merely a scalar Casimir value. To compare with determinant-one
peripheral lifts one must retain the selected square root of R0.

For the retained half twist, the FULL derivative is

    e^(partial_xi Theta_epsilon)=R0(-J)^epsilon.           (15)

The physical conjugator in (14) is independent of epsilon at fixed
magnetic/channel variables. Equation (15) removes the explicit half
twist from its peripheral marking. Indeed positive original Hurwitz
transport is (A,B)->(A^-1 B A,A); with P=BA it is simultaneous
conjugation by P^-1-I, whose eigenratio is -J^-1. Therefore internal
stationarity in the pure spectral phase, R0(-J)^epsilon=1, gives
exactly that recorded signed Hurwitz factor. It would be incorrect to
call R0 itself the unchanged auxiliary meridian for every epsilon.

For the entire core's cosine branch exp[+pi i N(1-2xi)chi], the
additional xi derivative is -2pi i chi. Hence its channel equation is

    R0(-J)^epsilon=e^(2pi i chi).                        (16)

The opposite Fourier branch inverts the right side. The external color
deficit chi is distinct from the internal channel xi.

The primitive collar is fixed by the original threading word, not by
centralization alone. Apply the positive Hurwitz rule chronologically
at [2,1,1,2] to the three meridians (A,B,C_aux), and put
K=P^-1 C_aux P. The exact three outputs are

    (K^-1 A K, K^-1 B K, K).

Closing the auxiliary sets K=C_aux. Thus the pure physical transport
is conjugation by C_aux^-1. The actual zero-self-linking disk longitude
is P=BA, with no meridian factor, as proved in the
[literal mixed-loop marking](actual_mixed_crossing_circle_preferred_longitude.md),
sections 4--5. Its argument uses the two underpasses and the absence
of an auxiliary self-crossing; it is independent of plat width.

On the chosen P eigenflag J=-ell, the primitive auxiliary meridian has
eigenvalue M_aux. Hence the pure transport eigenratio is M_aux^-2.
The retained main half twist adds the already computed factor
(-J)^(-epsilon) to the physical transport and adds no auxiliary
longitude detour. Consequently the exact marked relation is

    R0(-J)^epsilon=M_aux^-2=e^(-U_aux),
    M_aux=-q^(N-h) -> e^(-pi i chi), U_aux=-2pi i chi.    (16a)

This calibrates (16) and the primitive collar in the original source
convention. Opposite eigenflag choices are retained by the Fourier
sign, rather than replacing the projective multiplier by an unmarked
square root.

## 5. The endpoint retains additive transport, rather than losing it

At the geometric endpoint J=-1, both quadratics (2) have simple roots
on any chart where their discriminants are nonzero. Equation (12) obeys

    R0=1                                                 (17)

identically modulo those two endpoint quadratics. Thus complete internal
channel stationarity is automatic EXPONENTIALLY; a Poisson/logarithmic
sheet is still to be recorded. It does not force C to be identity.

Continue the two chosen roots analytically with J. The quotient in (13)
has a removable singularity and

    C=I+b(P+I), b=(1/2) dR0/dJ at J=-1.                  (18)

The derivative in (18) is along the chosen roots of (2), not a derivative
with Z,W incorrectly frozen. The matrix H=P+I is nonzero and H^2=0 at
an essential complete crossing disk. For common-trace parabolic A,B,
Tr(H A)=4. Consequently the same coefficient is recoverable without
any limit by

    b=Tr([H,A_in] A_out)/32.                             (19)

To verify (19), C A C^-1=A+b[H,A]-4b^2 H, while
Tr([H,A]^2)=32 and Tr([H,A]H)=0. The positive-certificate disk has
distinct puncture flags, so this is its regular additive centralizer,
not the central matrix P=-I.

On the selected longitude cover set J=-ell=-exp(V_long/2). Then

    d_(V_long) log R0 at completeness=-b,
    log[R0(-J)^epsilon]=log R0+epsilon V_long/2.           (20)

With the calibrated auxiliary source convention R=e^(-U_aux), (20)
is precisely the centered shear U_epsilon=U_0-epsilon V_long/2.
The factor of two and inverse eigenratio convention are both retained.

## 6. The peripheral differential on a selected stationary branch

There is a useful conditional consequence for the FULL assembled core
phase, rather than just one local coupon. Choose one of the two original
cosine signs sigma_i in {+1,-1} at each auxiliary region. Its added
leading phase is exactly

    sum_i sigma_i pi i (1-2xi_i) chi_i.                    (22)

The finite -1 in m_j=N-2j-1 changes the amplitude, not (22). Assume
there is a holomorphic stationary branch of the assembled phase in all
its internal variables on a specified logarithmic/Poisson sheet. This
is a hypothesis here, not inferred from the local character equations.
Call its critical action phi(chi), retaining the original source phases
and fixed internal Poisson characters. Envelope differentiation gives

    partial_i phi=sigma_i pi i(1-2xi_i).                  (23)

On the marked longitude branch centered at xi_i=1/2 put

    V_i=sigma_i 2 Log(-J_i)
       =sigma_i 4pi i(xi_i-1/2), U_i=-2pi i chi_i.

These are equalities on the specified CENTERED logarithmic sheet. An
integer change of a xi lift, or an additional recorded exterior color
character, changes the corresponding linear term of phi and the marked
peripheral logs together. Such terms must be kept; (24) is not a rule
for resetting them to zero.

Then (23) proves, without an unidentified proportionality constant,

    V_i=-2 partial_i phi,
    d(2pi i phi)=(1/2) sum_i V_i dU_i.                   (24)

The local channel equations are R_epsilon,i=e^(sigma_i 2pi i chi_i).
The actual collar comparison above identifies its selected multiplier
with R_epsilon,i^(-sigma_i)=e^(U_i), while the selected longitude
multiplier is J_i^(2sigma_i)=e^(V_i). An inverse choice of collar
orientation or eigenflag must be changed explicitly on BOTH sides.

Consequently the primitive differential is forced by the original
Fourier-color coupling ON ANY such correctly marked stationary branch.
It is not evidence that the branch exists globally, contributes to the
finite source, or has the required complex estimate. Moreover (24)
does not determine the additive value phi(0). Even after the marked
representation comparison, its complete-volume anchor still needs an
actual fundamental-chain or absolute period proof.

## 7. What can be sewn, and what is still missing

The original cup has exact affine degree a+b=N-1 and phase
x^(a-d); the ordinary cap has phase x^a, and the original marked cap
has phase x^b after the allowed WHOLE-SOURCE degree restriction.
Their principal equations all give

    X1 X2=1, S1/S2=-1, P=I.                             (25)

This is the actual inverse-meridian cap relation. It does not identify
the ordinary and marked amplitudes or discard their different normals.
Their leading phases pi i u and pi i(1-u) have derivatives differing
by an integral 2pi i character. Exponentiation hides precisely that
original marked Poisson/logarithmic datum; it must remain in the global
action and cannot be recovered from P=I alone.
Shared physical wires identify the same X and S symbols, so (10),(14),
and (25) are source-compatible local character equations at every width.

Conversely, on a regular magnetic Borel chart an ordered parabolic pair
with its actual P determines X,S, hence Y; equation (5) reconstructs
its internal q-Hahn root. The full normalization (6) then reconstructs
the outgoing scale. In this sense the local map covers the regular
ordered-pair centralizer relation, including its parabolic limit.

A global marked representation must still be compared with its source
degree-chamber choices and integer carries, and the original logarithmic/
Poisson sheets. The local primitive collar is fixed above; the rational map
alone does not prove that every positive complete gluing certificate
lands in one physical source chart or has the required global lift.
Nor does it supply existence of a nearby marked deformation merely
from a complete point.

Most importantly, the local generating phase and its correct character
relation do NOT fix its absolute Bloch/regulator class. Section 6 proves
the primitive differential on a correctly marked stationary branch;
its existence and its actual degree-one complete-volume anchor remain
necessary. Matching a character variety cannot fix an additive action
constant or a different period class. No absolute comparison, cycle
selection, nonzero amplitude, or global source gap is asserted here.

The advance is the explicit local source-to-character generating map,
with its full normalization and additive parabolic transport preserved.
It is a reusable algebraic input to those remaining comparisons.

Audit: [exact rational identities and parabolic normal checks](../experiments/audit_actual_augmented_plat_local_critical_character_map.py).

The local character map retains the stated global-branch, logarithmic-mark, absolute-period and source-estimate limitations.