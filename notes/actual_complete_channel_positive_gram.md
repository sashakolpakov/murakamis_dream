# Positive complete-channel Grams with the original source

29 October 2026. The complete source-generated N-dimensional module
has an explicit positive Gram, independent of the braid word and its
unknown value. All Casimir value AND derivative channels are retained.
The original incoming cup and outgoing cap have polynomial norms in
this metric. Their exact weighted norms below provide an honest
Cauchy inequality for the original reduced scalar.

This independently checks the full source formulas in
[the complete multiplicity theorem](actual_complete_source_multiplicity_module.md#4a-a-complete-positive-hermite-metric-with-both-original-sources-polynomial).
It also identifies the natural positive CD-weighted metric, distinct
from the simpler unweighted channel metric. They are polynomially
equivalent, so neither changes the exponential target. The unresolved
step is an upper estimate on the COHERENT channel energy, not a missing
boundary normalization.

## 1. Physical, right and channel coordinates

Use N>=2, d=N-1, q=exp(pi*i/N), Q=q^2, x=q^d. Let w be the physical
degree-d two-head vector representing the COMPLETE actual three-head
Hopf intertwiner I_w. The original source module has actual recoupling
J, original pair cup p, and ordinary cap ell, with EXACT identities

    Jp=Nx^(-d)e_d, ell J^(-1)=(x^d/N)e_0^T.          (1)

The module contains every intermediate Casimir Jordan channel.
An original signed word W acts on it as W_mult. Its genuine reduced
open-strand scalar, with its assigned external line chi_N, is

    K_N=chi_N ell W_mult p.                          (2)

Equation (2) is the already proved whole-source opening of the marked
cut: the exterior is the original Hopf braid, its remaining V map is
scalar, and the actual cut functional has value one on I_V. It is NOT
a local substitution of an ordinary cap for the unrestricted marked
row in an arbitrary exterior. The full marked operator is retained
when an exterior is not a Hopf intertwiner.

Let V=V_d be the canonical COMPLETE Casimir/Hermite frame from
[the all-channel theorem](actual_complete_casimir_hermite_packet.md).
The three coordinate systems are

    physical w, right y=Jw, channels z=V^(-1)y.

Put F=V^(-1)J. For ANY explicitly assigned positive channel matrix D,

    G_D=F^* D F, u=Fp, b=ell F^(-1)=ell J^(-1)V,
    W_ch=F W_mult F^(-1).                            (3)

G_D is positive definite of full rank N. It depends on the specified
actual module and D, not on W or K_N. Exactly

    K_N=chi_N b W_ch u,
    ||p||_(G_D)^2=u^*D u,
    ||ell||_(G_D^(-1))^2=b D^(-1)b^*.                 (4)

The two choices considered here are D=I and the positive CD measure
`D_CD=directsum |sigma_j| I_(multiplicity j)`. The bilinear CD matrix
itself is not being called positive. The complete original Cartan,
framing, modified dimension and peripheral line remain in W and
chi_N, exactly as assigned before the change of coordinates.

## 2. Exact cancellation in the complete source

At a double node c=c_j let `Q_j(z)=P_N(z)/(z-c)^2`,
`P_N=T_N+2`, and let nu_j be the original crossing eigenvalue.
The canonical frame has endpoints

    (f_d(c),f_d'(c))=x^d(nu_j,r_N'(c)),
    K_j=sigma_j[[0,1],[1,eta_j]],
    eta_j=r_N'(c)/nu_j+Q_j'(c)/Q_j(c).

Applying its EXACT inverse to (1) gives

    u_double=(-N nu_j sigma_j^(-1) Q_j'(c)/Q_j(c),
                                     N nu_j sigma_j^(-1)),
    b_double=(x^d/N,0).                              (5)

The potentially large crossing derivative cancels in the first
component. It has not been dropped: its cancellation uses the full
value/derivative inverse, not an independent semisimple evaluation.
At a simple node `u=N nu_j/sigma_j`, `b=x^d/N`.

There is an exact elementary simplification. The Chebyshev polynomial
defined by its recurrence obeys

    (4-z^2)P_N''-zP_N'+N^2(P_N-2)=0.

It follows either by differentiating `T_N(2cos t)=2cos Nt`, or by
induction in that recurrence. At every double root,

    Q_j(c)=N^2/(4-c^2), Q_j'(c)/Q_j(c)=c/(4-c^2),
    sigma_j=(-1)^d x^d nu_j/(4-c^2).                  (6)

Thus (5) is simply

    u_double=N(-1)^d x^(-d)(-c,4-c^2),
    b_double=(x^d/N,0).                              (7)

At the odd-level simple node c=-2,

    sigma=x^d nu, u=Nx^(-d), b=x^d/N.                (8)

All phases, parity and N factors are fixed. Neither original source
has an exponential hidden normalization in these FULL coordinates.

## 3. Unweighted channel metric: the simpler Cauchy prefactor

For D=I, let S_N=||u||_2^2 and T_N=||b||_2^2. Then exactly

    T_N=ceil(N/2)/N^2,
    S_N=N^2[sum_double(c_j^2+(4-c_j^2)^2)+1_(N odd)]. (9)

The notation T_N here denotes a source norm, not the Chebyshev
polynomial of Section2. Explicitly,

    S_N=N^2(4N-1), N odd,
    S_N=4N^3, N even and N>=6,
    S_4=192, S_2=64.

These are the source formulas proved in the multiplicity note. They
also follow directly by summing second and fourth powers of
`2cos((2j+1)pi/N)` and pairing the repeated nodes. In particular

    S_N T_N<=4N^2, EVERY N>=2.                       (10)

With the explicitly known unit source `u_0=u/sqrt(S_N)` define
`E_I(W)=||W_ch u_0||_2^2`. Genuine Cauchy--Schwarz gives

    |K_N|^2<=|chi_N|^2 S_N T_N E_I(W)
             <=4|chi_N|^2 N^2 E_I(W).               (11)

There is no contraction to K_N in the definition of this Gram:
F is the whole N-channel frame, u_0 has the explicit components
(7)--(8), and W_ch is the full original matrix word with every
mixed channel, phase and derivative retained.

A useful balanced scalar normalization is

    G_bal=F^*F/N,
    E_bal(W)=||W_mult p||_(G_bal)^2
                             =||W_ch u||_2^2/N.     (11a)

Then the EXACT original outgoing dual norm is
`||ell||_(G_bal^(-1))^2=ceil(N/2)/N<=1`, while the incoming
norm squared is `S_N/N=O(N^2)`. In particular

    |K_N|^2<=|chi_N|^2 [ceil(N/2)/N] E_bal(W).       (11b)

This version needs no additional polynomial Cauchy loss: it uses
the original unnormalized incoming cup. It is the same positive
Gram up to its specified scalar, not a different source.

## 4. Positive CD measure: exact weighted source norms

For D=D_CD, each double block has weight `(4-c_j^2)^(-1)`;
the odd simple block has weight one. Let

    A_N=u^*D_CD u,
    B_N=b D_CD^(-1)b^*.

Equations (7)--(8) give the exact finite formulas

    A_N=N^2[sum_double((4-c_j^2)+c_j^2/(4-c_j^2))
                                                   +1_(N odd)],
    B_N=N^(-2)[sum_double(4-c_j^2)+1_(N odd)].        (12)

In closed form,

    A_N=N^4/4+N^3/2, B_N=1/N, N even>=4,
    A_N=N^2(N^2+3N+8)/6, B_N=(N+1)/N^2, N odd,
    A_2=16, B_2=1.                                  (13)

For a direct proof put theta_j=(2j+1)pi/N, so
`4-c_j^2=4sin^2 theta_j`. The sum of reciprocal sine squares over
odd indices is `N^2/4` at even N and `(N^2-1)/6` at odd N before
the factor 1/4. These follow by subtracting even from all root
reciprocal-square sums, or pairing the odd and even indices when N
is odd. Also `c^2/(4-c^2)=4/(4-c^2)-1`. The first sine-square sum
is a finite geometric sum; N=2 is its stated resonance. This proves
(13) at composite and even levels without a modular half inverse.

In particular `A_N B_N<=2N^3` for every N>=2. With
`u_CD=u/sqrt(A_N)` and `E_CD(W)=||W_ch u_CD||_(D_CD)^2`,

    |K_N|^2<=|chi_N|^2 A_N B_N E_CD(W)
             <=2|chi_N|^2 N^3 E_CD(W).               (14)

This is a different natural positive metric from D=I; its source
normalizers must not be mixed with (9). Both metrics retain the
same complete channel source and original scalar.
For the similarly balanced metric `F^*D_CD F/N`, the original
outgoing dual norm squared is `N B_N<=2`; its incoming norm
squared is `A_N/N=O(N^3)`. Its corresponding unnormalized-cup
energy obeys the same bound as (11b), with coefficient `N B_N`.

## 5. One remaining coherent-energy assertion

The two channel metrics are polynomially equivalent:

    I/4<=D_CD<=max(1,N^2/16) I.                      (15)

The corresponding normalized-source energies E_I,E_CD therefore
have the same exponential rate, whenever that rate or limsup is
considered. No exponential conditioning is hidden by changing
between these two explicitly related channel measures. The physical
maps V and J themselves need not have polynomial norms.

The right-frame generators are the FULL Hermite block matrix
`D_braid=kappa r_N(Jordan(A))` and its complete conjugate
`C D_braid C^(-1)`, where `C=V^(-1)JV`. Derivative rows remain.
A single repeated-generator power costs polynomially, but C can
carry exponential energy and phase cancellation.

For this fixed positive Gram, the sufficient energy statement would be

    limsup_N (pi/N)log E_I(W)<=Vol(K),                (16)

or the stronger specified positive-geometric-partition comparison
`E_I(W)<=exp(o(N)) Z_geo,N`. Equation (11) would then give the
sharp original upper bound. It is not implied by positivity, the
unit spectral values, a Krein conservation law, or polynomial
boundary norms.
Equivalently one may use E_bal of (11a): it differs from E_I by
the explicit polynomial initial factor S_N/N.

The subsequent [exact original energy calculation](actual_figure_eight_complete_channel_energy.md)
shows that (16) is FALSE for this fixed candidate Gram already on
the true figure-eight word `[2,-1,2,2]`. The odd-level simple
channel has the exact coefficient proved in
[the finite quadratic transform](actual_half_color_quadratic_source_transform.md),
forcing `liminf_odd (pi/N)log E_bal>=v_8>Vol(4_1)`.
The source/Cauchy theorems above remain exact; this particular
positive norm retains more exponential energy than the final period.
Both D=I and the polynomially equivalent CD metric have this problem.

A [specified terminal packet Gram](actual_terminal_packet_positive_gram.md)
provides a different source-preserving metric on the SAME complete
module and recovers the sharp figure-eight energy. Its kernel is
positively completed, not discarded. A general sharp prefix bound
for that terminal construction is still unproved.

This theorem solves the complete boundary-norm problem on the actual
three-head Hom module (hence the original four-plat source), not the
global coherent q-Racah growth problem. At larger bridge width the
actual complete multiplicity reduction is known, but a compatible
complete-channel positive metric still has to be constructed.

[Audit](../experiments/audit_actual_complete_channel_positive_gram.py):
original coproduct-built complete source module and endpoint identities,
full Hermite inverse and parity, both positive metrics/source norms,
and original signed open-strand periods with the prescribed source.
