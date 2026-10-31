# Actual open meridian transport has a source-preserving horizontal polarization

Research theorem, 27 October 2026. The actual open R-word has an
explicit endpoint half-character under M->qM. An M-dependent SECOND-
wire gauge removes that half-step and preserves the whole source
on arbitrary current tensors. A first-wire alternative has its
separate explicit Cartan Ward correction. This constructs a real
word-induced meridian/current connection, retaining the original
finite source, power characters, cyclic wrap and peripheral factor.

It does not yet turn the selected word class into the marked geometric
period. The remaining insertion/current equation is stated explicitly
in Section 7; no principal rational-density filter is substituted for
the actual period.

## 1. The exact endpoint character of an arbitrary open braid word

Use the original zero-framed knot braid on b strands, with writhe w.
The first cut is at strand zero. The second is an INTERNAL IDENTITY
wire at a specified braid level and strand slot ell, counted from zero.
Use the literal tensor convention

    T_(c,d;a,b0)=ptr_other[A E_(b0,d)^(ell) B].

Thus d is the position immediately BEFORE the removed identity and
b0 immediately AFTER it. Every original pivotal matrix remains in
ptr_other; opening this wire neither removes its old cap nor adds a
new pivot. Put nu=d-b0. Conservation gives c=a-nu for the uninserted
tensor. All four physical head bounds and internal finite supports
remain the original ones.

For one actual crossing with first input i and first output c_1,
the already proved finite coefficient identity is

    r_sign(qM)=x^(-sign) q^(c_1-i) r_sign(M)/tau_sign,
    x=-M/q, Y=M^2,
    tau_+=BC/x *(1-Y/A)/(1-YC/A),
    tau_-=x/A *(1-Y/B)/(1-YC/B).                  (1)

The ratios in (1) mean their CANCELLED WHOLE finite products, as
in the actual longitude-insertion theorem. No zero Pochhammer or
peripheral denominator is divided separately.

To telescope the half-character use the INTEGER position potential
J(a_vec)=-sum_i i a_i. At every checked crossing,

    J_out-J_in=c_1-i.

The final/initial closed strands have identical positions and the
first position has coefficient zero in J. The matrix-unit insertion
at the second cut changes J by -ell(b0-d)=ell nu. Therefore exactly

    sum_crossings(c_1-i)=-ell nu.                 (2)

No root square root or cyclic interpretation is used in this equality.

Write n=N-1, kappa_D=w-b+1, and retain the whole scalar

    gamma_N=q^(n kappa_D),
    L=gamma_N x^(-w) product_crossings tau_sign^-1. (3)

The original closed pivotal/framing lines give gamma_N, just as in
the closed calculation: each old closed pivot contributes q^(1-N),
and the residual zero-framing line contributes q^(w(N-1)). The
opening has not changed them. All common full Cartan scalars are
kept with their original twist cancellation. At a knot root only,
kappa_D is even and gamma_N=q^(-kappa_D). Off root keep
gamma_N=q^(-kappa_D)(q^N)^(kappa_D), with its mark.

For every raw finite open weight I the result is

    I(qM)=q^(-ell nu) L I(M).                    (4)

Let T^[L] mean the SAME finite tensor with that cancelled whole
insertion on every actual path. Put rho=q^(-ell) and
D_rho=diag(rho^j) on the SECOND cut. Then (4) is the literal
matrix identity

    T(qM)=(I tensor D_rho)T^[L](M)(I tensor D_rho^-1). (5)

For the full ADO period multiply L by the ACTUAL whole ratio

    g_N=d_N(qM)/d_N(M)
       =q^(N-1)(q^2M^2-1)/(M^2-1)
                       *(M^(2N)-1)/(q^(2N)M^(2N)-1). (6)

Its original phase cancels only by using the SAME phase lift on
both sides. The root reduction of (6), its complete norm-zero
lattice and all q-normal source terms are not suppressed.

## 2. The raw Fourier source and independent alias powers

Keep the full band kernel F(M,eta)=sum_nu f_nu(M)eta^nu, with
the first input fixed and original output row still summed.
Equation (4) reads

    F(qM,eta)=F^[L](M,rho eta).                  (7)

The actual co-source is its constant coefficient, so CT_eta is
unchanged by rho dilation, for WHOLE functions and every finite
tail. No physical-position sum is replaced by a Fourier evaluation.
For one uninserted first-input head a, the band interval
[a-(N-1),a] has length N; root averaging computes CT exactly.
For unwrapped currents keep an independent V_eta=eta^N:

    Av_(N,V_eta)F=sum_k f_(kN)V_eta^k,
    V_eta ->rho^N V_eta=(q^N)^(-ell)V_eta.        (8)

Thus an odd ell changes the physical root grid V_eta=1 to the
antiperiodic grid -1. The original head CT agrees on these grids,
but alias powers of a current do not. They retain the sign and
the whole (q^N)^(-ell) character before normal differentiation.

On the complete root head-band window, dilation by rho is a genuine
finite matrix on the Fourier-label array: conjugate diag(rho^nu)
by its finite Fourier evaluation matrix, using the ACTUAL unwrapped
representatives in that interval. It fixes the constant-mode source,
commutes with cyclic Fourier-label shifts, and is unitary when
|rho|=1. It is not obtained by silently identifying every tail
with its residue modulo N. In a whole generic-Q Vandermonde frame,
use the original full tensor and its last-row carry, not a root
permutation extended without corrections.

## 3. The second-wire horizontal gauge preserves the entire source functor

On the SECOND identity wire put

    D_2(M)=diag(M^(-ell b)),
    T_h=(I tensor D_2^-1)T(I tensor D_2).

Its coefficient factor is M^(ell(d-b))=M^(ell nu) for EVERY
tensor entry, including charged current tensors. It therefore
cancels (4) for the uninserted open word:

    I_h(qM)=L I_h(M),
    F_h(M,xi)=F(M,M^ell xi).                    (9a)

The second partial trace is invariant under this conjugation on
ALL matrices, not only diagonal or scalar reclosures:

    ptr_second T_h=ptr_second T.                (9b)

The first source, original caps, peripheral line and every source
current are unchanged. On other internal pieces transform their
ordered operators by the same basis map. This is a strict whole
source/current functor before normal jets. No Schur argument or
source replacement is used in (9b).

There is an equally explicit GLOBAL braid-frame construction.
On a level of b strands use G(M)=tensor_j M^(-j J_j), with
first strand j=0. For one crossing its coefficient in G^-1 R G
is M^(-(c_1-i))r. Thus (1) immediately loses its q^(c_1-i)
factor under M->qM. All adjacent level gauges cancel in a word;
the original closed diagonal pivots commute with them, and the
first source is untouched. Cutting this global gauge at the
second wire gives exactly D_2 above.

In the actual generic-Q Fourier frame this is a SCALED
Vandermonde isomorphism, not a root-only kernel substitution:

    W(M,Q)=V(Q)D_2(M)^-1,
    W_(j,b)=(M^ell Q^j)^b,
    W^-1=D_2 V^-1.

The node gaps are only M^ell(Q^i-Q^j), so no additional source
norm-zero divisor has been inverted. Equations (5) and (9a)
give the exact whole matrix meridian identity

    (I tensor W(qM))T(qM)(I tensor W(qM)^-1)
       =(I tensor W(M))T^[L](M)(I tensor W(M)^-1). (9c)

Indeed W(qM)D_rho=W(M). The raw first-output sum of the
diagonal j entries therefore has fixed exterior xi=Q^j under
the meridian step. Its remaining action is the ACTUAL insertion
L, not a scalar chosen from the geometric branch.

The forced normal connection on this whole frame is

    A_M=(D_M W)W^-1=ell V J V^-1,
    A_Q=(D_Q W)W^-1=(D_Q V)V^-1  (M fixed).

Thus D_M T^W=W(D_M T)W^-1+[A_M,T^W] on that wire; the
commutator has zero second partial trace entrywise. At a complex
root, ||A_M||<=ell(N-1) and the old bound for A_Q is unchanged.
On |M|=1, W/sqrt(N) is unitary. These are source-frame bounds,
not full crossing-word bounds. Along M(q), retain the chain-rule
connection and the marked M^N and q^N powers.

There is a precise ROOT-only cyclic current corollary. For a
charge-zero fixed-input packet put

    F_a[j,c]=Q_N^(j(a-c)), 0<=c,j<N,
    H_a(M)=F_a diag(M^(ell(a-c)))F_a^-1.

Then J_h=H_a J, Sigma H_a=Sigma, H_a 1=1. Every factor is
diagonal in the same finite Fourier basis, so H_a commutes with
the cyclic shift, its normalized difference and its centered
primitive. Its M-connection is

    A_a=ell F_a diag(a-c)F_a^-1,
    Sigma A_a=0, A_a1=0, ||A_a||<=ell(N-1).

For |M|=1 this is an ISOMETRY of the actual cyclic source/current
complex. In particular its distance to the zero-source current
space is unchanged. This finite-packet statement is not extended
to charged/unwrapped tails by forgetting their alias powers;
those use the strict whole tensor map and (8).

The packet connection A_a is NOT the full matrix A_M and is
not independent of the unwrapped input window. For 0<=a<N-1,
let Pi_(a+1) be the root Fourier projector on residue a+1. Then

    A_(a+1)-A_a=ell N Pi_(a+1),
    H_(a+1)H_a^-1=I+(M^(ell N)-1)Pi_(a+1).

This is the exact branch carry as that head window moves by
one. It is trivial in value at M=1 but not in its normal jet.
The full tensor functor retains it, rather than treating A_a
as a window-independent current connection.

## 4. Optional first-wire gauge and its exact Ward correction

On the FIRST wire define

    D(M)=diag(M^(ell a)),
    T_hor=(D(M)^-1 tensor I)T(D(M) tensor I).      (9)

For a charge-zero path its coefficient is M^(ell(a-c))=M^(ell nu).
Substituting (4) at qM cancels the factor q^(-ell nu). Hence

    I_hor(qM)=L I_hor(M),
    F_hor(M,xi)=F(M,M^ell xi),
    F_hor(qM,xi)=F_hor^[L](M,xi).               (10)

This is an alternative meridian-horizontal polarization, with no guessed
quiver transport. Its endpoint half-character has been absorbed
by a specified whole diagonal gauge, while L itself remains the
actual word insertion rather than its critical value.

The first-wire reclosure C=ptr_second T is diagonal for every whole
uninserted auxiliary word by total position conservation. Therefore

    ptr_second T_hor=D^-1 C D=C                  (11)

even OFF root. The selected uninserted state and full d_N line
are exactly unchanged. For a current tensor of total charge d,
c+nu=a+d; its factor is M^(ell nu)M^(-ell d). This extra source
character is retained, rather than extending (11) to nonscalar
charged matrices without their row correction.

There are two equivalent complete current presentations. Transport
all source data by the actual gauge: psi_hor=D^-1 psi and
ell_hor=ell D, with the corresponding transformed coupon. Then
the pairing is identical on EVERY matrix. If one keeps the
convenient original fixed-input/all-ones row instead, its exact
whole defect is the Cartan Ward row

    lambda_a(D^-1 C D)-lambda_a(C)
      =sum_(c!=a) [M^(ell(a-c))-1]/[Q^(a-c)-1]
                                      (D_K C)_(c,a),
    D_K C=K C K^-1-C.                           (12)

Only genuine head units are inverted. No color edge or 1-Q^N is
removed. Equation (12) handles all ordered/Green current tensors.
On homogeneous charge d its selected line factor is M^(-ell d).

The forced M-connection in the horizontal matrix frame is

    (D_M+ad_(ell J_head)) C_hor
                 =D^-1(D_M C)D, D_M=M partial_M. (13)

Its sign follows by differentiating D^-1 C D. The q-normal
connection is zero with M held independent; on an actual path
M(q) retain its chain-rule multiple of ell J_head. This does not
freeze the fixed-level power graph or any normal source character.

On the physical unit-meridian arc D(M) is unitary. The row in
(12), in the original balanced flat metric, satisfies

    ||beta_(a,ell)(M)||^2 <=(N^2-1)/3, |M|=1,
    beta_(a,ell)(1)=0,
    ||D_M^k beta_(a,ell)(1)||
                     <=ell^k N^(k+1)/sqrt(12), k>=1. (14)

Proof: numerator modulus is at most two and the denominator runs
once through all nontrivial N-th root gaps; their inverse-square
sum is (N^2-1)/12. For k derivatives use |a-c|<N. These are
polynomial bounds for the SOURCE GAUGE and its fixed normal jets,
not for the whole R-word, the external d_N pole or a complex
neighborhood of the physical arc.

## 5. The pointed cyclic polynomial and wrap cannot be dropped

The MAIN second-wire construction leaves the original first source
and its supplied chi polynomial untouched. On any wire carrying
a pointed cyclic source, an actual basis change transports its
source vector, co-source and spectral polynomial simultaneously.
For the optional first-wire gauge, the original first source is
highest input and the orbit output
row; in a cyclic frame its repair P=U+W has P^N=I. Equation (9)
gives EXACTLY

    P_hor=D^-1 P D
       =M^(-ell)[P+(M^(ell N)-1)W],
    P_hor^N=I, ell_hor P_hor=ell_hor.            (15)

The marked source vector and row transform as just specified.
Thus its characteristic polynomial and FORCED pointed factor
are retained: chi(z)=(z-1)chi_red(z). In the actual cyclic repair
chi=z^N-1. For an unfolded sourced companion the full conjugation
also preserves its supplied chi and transports its chi_red row.
Replacing (15) by bare M^(-ell)P would instead change the
characteristic polynomial and its source eigenvalue. Its wrap
character M^(ell N) is essential, including at a normal root.
None of this identifies chi_red with the knot A-polynomial.

## 6. Compatibility with the geometric pole, with the exact scope

The horizontal open phase adds ell Log M times the boundary
displacement t=Hnu. Its principal incidence is therefore

    xi=M^(-ell)p_e^-1, p_hor=M^ell p_e.          (16)

The critical displacement is still zero, so its marked geometric
action is unchanged. The nondegenerate Fourier block persists
on the same regular meridian germ. At COMPLETENESS the proved
Möbius framing coordinate and its pole lambda_e apply. Away
from it, only a supplied marked polar branch, if it persists,
can be said to rescale to lambda_hor=M^ell lambda_e(M). No
global generic-M Möbius or single-pole theorem is assumed.

For the rational principal coefficient T(p)=G p/(p-lambda)^2,
sampling p^N=S gives EXACTLY

    Av_(N,S)T=G N S lambda^(N-1)/(S-lambda^N)^2. (17)

Thus the antiperiodic source grid changes 1-lambda^N to
1+lambda^N with the corresponding numerator sign. In horizontal
coordinates the retained candidate norm is

    1-M^(ell N)lambda_e(M)^N.                   (18)

The differential Jacobian is essential: at fixed M, dr expressed
in p_hor=M^ell p gives G_hor=M^ell G as well as the rescaled
pole. Where both expressions are regular, the RATIO of the two
principal filters under this coordinate rescaling alone is

    M^(ell N)[(1-lambda_e^N)/
                    (1-M^(ell N)lambda_e^N)]^2. (19)

At M=1 its extra logarithmic derivative is
ell N(1+lambda_e^N)/(1-lambda_e^N), retaining the pole. Equation
(19) is a geometric filter comparison, NOT a proved adapter of
the actual selected quantum period. The exact main tensor gauge
(9a)--(9c)
preserves that period while its raw principal filter may be
singular. Its missing whole word numerator/current correction
must cancel or account for such poles; (17) alone cannot do it.

## 7. The remaining source-current equation is now explicit

On any regular proper-array chart let R_i=S_i I_hor/I_hor be
the actual internal ratios. Since the main identity (9a)--(9c)
is exact,

    sigma_M(R_i)/R_i=S_i(L)/L.                  (20)

For the finite Green insertion operator d_R,i=R_i S_i-I,
this gives the coefficientwise chain identity

    L d_(sigma R),i(f)=d_R,i(Lf).              (21)

The global meaning is the zero-extended array identity, retaining
all original endpoints and cancellation lattices. Together with
the semilinear shift of f, it is the actual word-induced meridian
connection on the insertion/current complex. After finite source
pushforward it is the exact period equation

    T_M P_N=source(L I_hor),                    (22)

with (6) in full normalization. Finite coefficient elimination
already supplies a nonzero actual scalar meridian operator.

What (20)--(22) do NOT prove is a geometric quotient of this
SELECTED class. On ordinary finite-array currents multiplication
by L leaves the exact residual

    sum_s L(s)(S_i-I)H(s)
       =sum_s [L(s-e_i)-L(s)]H(s).             (23)

Discarding it, or replacing L by its critical longitude inside
the sum, would change the current/source comparison. A solution
of gate C must transport (21), its MAIN whole source functor
(9b)--(9c), its supplied pointed spectral/co-source data and the
norm-pole corrections (18), then prove that the resulting
original class is nonzero on the marked geometric period. This
note removes a concrete endpoint twist and supplies tame actual
source transport, but does not assert that last global map.
The first-wire rows (12),(15) describe only the optional alternative.

[Exact local/path/source/normal audit](../experiments/audit_open_meridian_horizontal_transport.py)
and [saved results](../experiments/open_meridian_horizontal_transport_results.json).
The audit passes 2,680 literal local meridian shifts, 1,268 open
paths in 44 genuine signed-word/cut families, 20 generic/root
scaled-Vandermonde matrices with 9,096 full port-source units,
60 root cyclic-packet isometries, 56 exact window branch carries,
812 optional source Ward rows,
588 independent alias-power cases, 42 periodic/antiperiodic
principal filters and 72 checks of the proved unit-arc source
metric estimates. Generic q and root q cases are kept separate.
