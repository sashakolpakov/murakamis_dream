# The compact geometric homotopy has an exact wall and peripheral charge

Research proof, 27 October 2026. At fixed complete meridian the
physical compact source sphere and the exceptional source sphere
are not homologous in the Gauss open set. Their difference is one
explicit wall torus, with its orientation and period determined.
Varying the meridian supplies a global logarithmic orbit homotopy
avoiding that wall, at the cost of the opposite SL2 lift and an
explicit peripheral Cech period.

The actual full quantum source has a matching, completely specified
central-sign character. Along this meridian path every possible
modified-dimension pole has a residue equal to an original ordinary
color, with a polynomial total norm bound. This is an actual source
wall theorem. It does not turn the Kashaev point evaluation into a
meridian integral or continue the full geometric A-branch for free.

Use [the resolved framing source](springer_centralizer_boundary_source.md)
and the [exact exponential Cech/current construction](compact_exponential_cech_current_detour.md).
All source phases and the complete modified-dimension function remain
marked throughout.

## 1. A closed form detects the fixed-meridian obstruction

On the resolved threefold Y use north coordinates v,eta,a and south
coordinates

    V=1/v, eta'=-v^2 eta, a'=v-v^2a.

Put f=1-eta v=1+eta' V, and remove the Gauss divisor

    D_cut={f=0}.

The exceptional divisor is E={eta=0}=X. The following form is
globally regular and closed on Y minus D_cut:

    Xi=dLog f wedge dLog v
      =dv wedge d eta/f
      =dV wedge d eta'/f.                                  (1.1)

The last two expressions show that its apparent flag poles cancel.
It is pulled back from the resolved meridian surface and is closed
therefore also on the threefold.

Let c=2pi*i. Orient the actual compact source sphere by

    0<=T<=1, 0<=phi<2pi,
    v=sqrt(T/(1-T))exp(i phi),
    a=sqrt(T(1-T))exp(-i phi).

Its source form is

    Omega_0=dv wedge da=-i dT wedge dphi,
    omega_I=-Omega_0/c, integral_Gamma omega_I=1.           (1.2)

Let Gamma_E be this sphere at eta=0. Let Gamma_phys be its actual
physical-symbol section

    eta_phys=(1-exp(-cT))/v.                               (1.3)

The removable pole formulas at both endpoints make these genuine
compact cycles. By the exact physical Gauss identity,

    Xi|_(Gamma_E)=0,
    Xi|_(Gamma_phys)=c Omega_0,
    integral_(Gamma_phys)Xi=-c^2=4pi^2.                    (1.4)

Thus no homology, and in particular no homotopy, inside Y minus
D_cut can identify the two cycles. This conclusion does not assume
that the flag or centralizer coordinates stay fixed during a proposed
homotopy.

## 2. The necessary relative cycle is one explicitly oriented wall torus

The straight normal interpolation eta_lambda=lambda eta_phys is a
global compact three-chain before D_cut is deleted. Its Gauss factor is

    f_lambda=1-lambda+lambda exp(-cT).

It hits D_cut exactly at lambda=T=1/2, for every phi. The intersection
loop is

    C: v=exp(i phi), a=1/(2v), eta=1/v,

inside D_cut, which is globally C^*_(v) times A^1_(a). Near that loop,

    f_lambda=-2(lambda-1/2)+pi*i(T-1/2)+higher terms.        (2.1)

The normal real Jacobian is negative. Define Tube(C) with first the
counterclockwise f-circle and then the positive v-circle. Removing
a small neighborhood of the intersection from the three-chain gives
the exact relation

    [Gamma_phys]-[Gamma_E]=-[Tube(C)]
                  in H_2(Y minus D_cut).                   (2.2)

Indeed the inner boundary of the removed disk has the opposite
normal orientation, and (2.1) reverses that orientation once more.
This fixes the sign without a convention about an unspecified cap.

The wall residue and period are

    Res_(D_cut) Xi=dLog v,
    integral_(Tube(C))Xi=c^2=-4pi^2.                      (2.3)

Equation (2.3) independently checks (2.2). Since C winds once in the
C^* factor of D_cut, it has no cap inside D_cut. A source comparison
must retain this torus or an equivalent relative boundary co-source.

The actual principal Gaussian flag form from the resolved source has
the corresponding balanced residues:

    nu_cut=-(d eta/eta) wedge Omega_0/f,
    Res_E nu_cut=-Omega_0,
    Res_(D_cut) nu_cut=+Omega_0.                            (2.4)

For the geometric Gaussian multiply (2.4) by its recorded nonzero
torsion/phase coefficient c_beta and retain the original base-only
quantum line. To check the second residue, on v!=0 use

    nu_cut=df/[f(1-f)] wedge Omega_0.

On the wall Omega_0=d(v da); along the actual intersection loop
v da=-(1/2)dLog v, so its primitive also has the explicit period
-pi*i. The ordinary two-form residue and this lower boundary current
are different degrees of data and should not be identified.

## 3. The integer winding cannot be erased at fixed meridian

There is a simple relative interpretation of (1.4). A globally finite
eta section has f=1 at both flag poles. Since the sphere is simply
connected, choose Log f=0 at its north pole. Its value at the south
pole is 2pi*i times an integer, invariant in any continuous family
avoiding f=0. The exceptional sphere has integer zero; the physical
sphere has integer -1. This is the source degree obstruction.

The tempting logarithmic interpolation

    eta_lambda=(1-exp(-c lambda T))/v

avoids f=0 on the north chart but does not patch at the south pole:

    eta'_lambda=
      [exp(-c lambda)exp(c lambda T')-1]/V,
    T'=Va'=1-T.                                          (3.1)

For nonintegral lambda it has a nonzero V^(-1) coefficient.
Discarding that coefficient would remove precisely the global clutch
being tested. The exact finite-current regularization in the cited
Cech note keeps this defect; it is not a new quantum dressing.

## 4. Varying the meridian gives an explicit global orbit homotopy

Let m be the eigenvalue on the retained flag. The Grothendieck
meridian chart is

    mu(v,m,eta)=
      [[m-eta v, eta],
       [(m-m^(-1))v-eta v^2, m^(-1)+eta v]].               (4.1)

Its determinant is one, its trace is m+m^(-1), and [1:v] is its
m-eigenflag. Its second chart is the affine transition

    eta'=-v^2 eta+(m-m^(-1))v.                             (4.2)

At m=1 this is the Springer bundle. Away from m=+/-1 it is a
nontrivial affine cotangent torsor. The full Gauss entry

    f=m-eta v=m^(-1)+eta' V

is global. Its two polar flag values are m and m^(-1), rather than
both one.

Define the marked path, for 0<=lambda<=1,

    m_lambda=exp(pi*i lambda),
    f_lambda=exp[pi*i lambda(1-2T)],
    eta_lambda=m_lambda[1-exp(-c lambda T)]/v.              (4.3)

The south expression forced by (4.2) is

    eta'_lambda=m_lambda^(-1)
                         [exp(c lambda T')-1]/V.          (4.4)

Both are removable at the corresponding poles for every lambda.
All eigenvalues and f_lambda stay nonzero. At lambda=0 the family
is the exceptional sphere at the identity. At lambda=1 it is
-mu_phys, with m=-1 and eta=-eta_phys. Thus (4.3) is a globally
regular projective meridian-orbit homotopy avoiding the Gauss wall.
Its SL2 lift changes by the central sign, explicitly.

This sign change is necessary for a once-winding clock. Along a
meridian family choose Log m continuously. The pole conditions give
Log f(S)=-Log m modulo 2pi*i, while the physical relative clock
has Log(f/m)(S)=-2pi*i. Starting with the zero clock forces
2 Log m_end=2pi*i modulo the chosen path mark. A closed path ending
m=1 cannot accomplish this odd winding; ending m=-1 does.

The actual inverse-eigenvalue convention of the finite source is
M=m^(-1), so its path is M_lambda=exp(-pi*i lambda). Formulas
(4.3)--(4.4) agree with the bridge note's determinant-h matrix
after division by M_lambda. No sign is silently discarded.

## 5. The avoided wall reappears as a marked peripheral Cech period

On the total varying-meridian family the naive dLog f wedge dLog v
has meridian poles at the two polar flags. The regular local forms are

    Xi_N=(dLog f-dLog m) wedge dLog v,
    Xi_S=(dLog f+dLog m) wedge dLog v.                      (5.1)

Their difference is exactly

    Xi_S-Xi_N=2dLog m wedge dLog v
                    =d(2Log m dLog v).                   (5.2)

Thus the global object is the specified peripheral period torsor,
not a single absolute two-form with a forgotten patch. Along
m:1->-1 the marked Log m changes by pi*i. The Cech term in (5.2)
then has flag period c^2, the wall period of (2.3). Changing the
meridian transfers the charge; it does not delete it.

On a fixed lambda fiber the two local forms agree. Their actual
compact period is

    integral_Gamma Xi_lambda=-c^2 lambda
                              =-2c Log m_lambda.          (5.3)

For the physical h_N=c/N, its signed normalized curvature integral is

    (1/(2pi*i h_N)) integral_Gamma Xi_lambda=-N lambda.    (5.4)

The coherent source uses the Chern convention c_1=-F/(2pi*i).
For curvature F=Xi_lambda/h_N its positive Chern degree is therefore
N lambda, agreeing with the endpoint prequantum line O(N). The
minus sign in (5.4) belongs to the stated flux orientation, not to
a claim that the actual source has line O(-N).

At the endpoint the prequantum exponential of the full flux is
exp(-2pi*i N)=1. The integer clutch and its half-form/sign data
still remain. In particular the intermediate integral-degree
locations lambda=k/N are precisely the actual ordinary-color wall
locations in Section 6. This is an exact equality of locations and
signed curvature integrals; it is not an unproved identification
of generic quantum dressing with ordinary coherent SL2 action.

There is a stronger exact root identity, proved with all marks in
[the flux/peripheral-character theorem](gauss_wall_flux_and_actual_peripheral_character.md).
Our oriented period is I_phys(M)=+2c Log M for M=m^(-1). Its
explicit inverse I_inv=-I_phys gives

    chi_H=exp(-2c LogM/H),
    chi_(h_N)=M^(-2N),
    d_N=epsilon_N (M-M^(-1))chi_(h_N)^(1/2)/(1-chi_(h_N)).

The marked half-root is antiperiodic under the actual q half-step.
Thus the wall flux supplies the actual central character and full
polar adapter at the roots. This does not identify that logarithmic
H-lift with a particular off-root auxiliary source or its normal jets.

## 6. Every actual meridian wall charge is an ordinary color

Fix the original N-th-root state, and write its reciprocal reduced
Laurent function as F_N(Y), Y=M^2. Keep the full original factor

    epsilon_N=i^(N+3), n=N-1,
    d_N(M)=epsilon_N M^n/S_N(M^2),
    S_N(Y)=1+Y+...+Y^(N-1),
    P_N(M)=d_N(M)F_N(M^2).                                (6.1)

Along the actual meridian path M_lambda=exp(-pi*i lambda), the
only possible interior poles are simple and occur at

    lambda_k=k/N, M_k=exp(-pi*i k/N), 1<=k<N.             (6.2)

A pole is removable if the corresponding actual color vanishes.
The actual finite-color identity and reciprocity give

    F_N(M_k^2)=F_N(Q_N^(-k))=C_k(q_N).                   (6.3)

Direct differentiation of S_N gives the exact wall residue

    Res_(lambda_k)[P_N(M_lambda)d lambda]
      =epsilon_N (-1)^k sin(pi k/N) C_k(q_N)/(pi N).       (6.4)

Equivalently the canonical meridian one-form has

    Res_(M_k)[P_N(M)dLog M]
      =-i epsilon_N (-1)^k sin(pi k/N) C_k(q_N)/N.         (6.5)

Proof: at a nontrivial root Y_k,
S_N'(Y_k)=-N Y_k^(-1)/(1-Y_k). Also
M_k^(N-1)(1-M_k^2)=(-1)^k 2i sin(pi k/N). Substitution
into the ordinary simple-pole formula proves both equations.
They retain the original phase, parity and full source factor.

The independently established actual ordinary-color bound is

    |C_k(q_N)|<=D_N=O(N^(b-1)), 1<=k<N,

for a fixed b-strand knot braid. Hence

    sum_k |Res[P_N dLog M]|
       <=(D_N/N)cot(pi/(2N)) <2D_N/pi.                   (6.6)

The corresponding total closed-contour correction is at most
4D_N. For d lambda the bound is smaller by pi. These are
polynomial source-wall charges for every knot in this actual
presentation, not estimates imported from a geometric saddle.

More generally a transport kernel holomorphic at these walls
multiplies each residue by its literal value there. A bound for
that kernel is additional input. Singular kernels require their
actual derivative residues and cannot be covered by (6.6) alone.

Equations (6.4)--(6.6) are meridian-integral statements. They do
not express the Kashaev point evaluation as such an integral or
prove that an unknown geometric transport has polynomial wall
values. The universal charges themselves are now exact and bounded.
The [existing regular-period decomposition](regularized_kashaev_period.md)
already separates these ordinary-color principal parts from the
regular quotient carrying the complete value. Thus even all the
residues in (6.5), with their normalization fixed, do not determine
that regular part or its large-level norm.

### 6.1 The endpoint central sign is an actual source-line character

The original reduced state depends on M^2, so it is unchanged
by M->-M. Its full source satisfies exactly

    P_N(-M)=(-1)^(N-1)P_N(M),
    P_N(M^(-1))=P_N(M).                                  (6.7)

For the second identity use reciprocity and
S_N(Y^(-1))=Y^(-(N-1))S_N(Y). Thus the semisimple detour ends
at the same reduced complete Kashaev value, with a completely
specified full peripheral-line sign. In particular

    P_N(M)/M^(N-1)=epsilon_N F_N(Y)/S_N(Y)

descends as a rational function of Y. P_N itself descends in
the character line of the double cover M^2=Y. This is an exact
property of the actual finite source, independent of an assumed
classical coherent dressing. The matrix Weyl adapter carries
additional integral information; its norm is not replaced here
by this scalar calculation.

## 7. The unresolved full-knot continuation is sharply separated

The homotopy (4.3) is universal for the meridian orbit and compact
source. To lift it to the full geometric critical family one must
continue the marked A-curve branch and all crossing charts along
the chosen M path. Ramification, ideal places, vanishing chart
denominators and branch monodromy can occur. The local Rivin
algebraic place does not establish that global continuation.

A finite cover can record monodromy, and the normalization of an
algebraic A-curve supplies a proper compact curve. Neither fact
ensures that its lifted endpoint is the central twist of the
chosen geometric representation, keeps its finite source lattice
regular, or bounds a transport kernel at the walls. Such assertions
must be proved with their marked source; they do not follow from
the orbit homotopy alone.

Nor can a finite etale cover remove the fixed-meridian wall class.
Pull back Xi and sum the lifts of the two cycles. Their period
difference is the covering degree times -c^2, still nonzero in
characteristic zero. Equivalently pushforward of an upstairs
cobordism would contradict (1.4). A cover can retain a spin or
branch mark; it cannot turn this non-torsion cycle correction into
zero while preserving the selected cycle.

What is now explicit is the entire universal obstruction and its
possible detour: one Gauss wall torus at fixed meridian; one
peripheral Cech charge when varying it; one actual central-sign
line; and finitely many ordinary-color source residues with total
polynomial norm. These remain meaningful before quantum jets.
They do not identify the normal d at fixed N with h_N, or prove
the geometric selected phase or the volume norm.

The [exact audit](../experiments/audit_meridian_homotopy_wall_and_source_residues.py)
checks the chart clutch, both homotopies, wall orientation, curvature
degree, all parity signs and actual finite-source residues. The
[independent Gauss-wall/flux proof audit](gauss_wall_cycle_and_peripheral_flux.md)
also verifies the cycle sign, global clutch, peripheral convention
and actual source residue formulas.
