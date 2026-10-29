# The retained terminal phase is an extra Cartan coupon, with exact Ward sources

29 October 2026. The positive terminal packet has an exact phase integral,
but its phase is NOT the knot's existing meridian-color parameter. It
inserts a specified Cartan coupon on one physical wire. Original interval
Ward equations acquire explicit sources. A terminal ordinary cap projects
back to the complete Hopf multiplicity module, leaving a nontrivial,
explicit operator-valued coupon there. Neither that projection nor
Parseval makes the coupon an original Hurwitz crossing or a transparent
frame change.

Thus the sharp terminal-energy theorem remains a coherent estimate of
this extra coupling. The original scalar at phase one and its Cauchy
bound are unchanged. No topological identification with a drilled link
or with an existing peripheral variable is made by analogy.

## 1. The exact phase family of the original terminal packet

Use the original notation of
[the terminal positive Gram](actual_terminal_packet_positive_gram.md):
N>=2, d=N-1, Q=exp(2pi i/N), x=-exp(-pi i/N), and

    D w=I_w|d>, c=ell_12 tensor <d|,
    U_phys=I tensor R_+^2, U_red=R_23^2,
    T_n=c U_phys Pi_(2,n) D.

All common Cartan, ordinary-cap, framing and peripheral factors are
literal original ones. Put C_t=t^(J_2), J_2|a,b,c>=b|a,b,c>, t!=0.
Then, as a ROW IDENTITY on every complete multiplicity input,

    F_t=c U_phys C_t D=sum_(n=0)^d t^n T_n,
    F_1=ell U_red.                                        (1)

For every original prefix B,

    sum_n |T_n(Bp)|^2
       =(1/(2pi)) integral_0^(2pi)|F_(exp(i theta))(Bp)|^2 dtheta. (2)

The unchanged original scalar is chi_N F_1(Bp). Its given factor
chi_N remains outside (2). The family off t=1 uses the fixed input
and output d cut in the definition above. Scalarity of the original
uninserted knot does not identify other cut prescriptions off t=1.
In particular (1) is the specified packet deformation of a valid
original-scalar presentation. It is NOT asserted equal to inserting
C_t into an unreduced even plat and then replacing its unrestricted
marked row by the same lowest cut. That different off-phase observable
must retain its literal marked matrix functional. The exact terminal
Cauchy estimate needs only the prescribed (1) and the original t=1
sum, so it makes no such replacement.

## 2. Literal quantum Ward identities with t retained

On the physical middle head, including both nilpotent endpoints,

    C_t F_2 C_t^(-1)=t F_2,
    C_t Ecal_2 C_t^(-1)=t^(-1)Ecal_2,
    [C_t,K_i]=[C_t,H_i]=0, all i.                         (3)

In particular every single-head Casimir and its central K^N stay
fixed. The actual meridian family x=-M/q instead changes K by M
and its Casimir to -(M+M^(-1)). Thus (3) is an independent relative
Cartan conjugation on a FIXED-color module, not that meridian family.

Write the literal three-head coproducts as

    Ftot=F_1+K_1^(-1)F_2+K_1^(-1)K_2^(-1)F_3,
    Etot=Ecal_1 K_2K_3+Ecal_2 K_3+Ecal_3,
    At=K_1^(-1)F_2, Bt=Ecal_2 K_3.

They obey the ALL-EXTERIOR matrix identities

    [Ftot,C_t]=(1-t)At C_t,
    [Etot,C_t]=(1-t^(-1))Bt C_t,
    [Ktot,C_t]=0,
    [Omega_tot,C_t]
       =(1-t^(-1))Ftot Bt C_t+(1-t)At C_t Etot.            (4)

There is no omitted boundary arrow or small-error term. At larger
width the same formulas replace At by
K_1^(-1)...K_(r-1)^(-1)F_r and Bt by Ecal_r K_(r+1)...K_b.

The defect is macroscopic on an ACTUAL original source. For w=p,
D p=p_12 tensor |d>, Ftot Dp=0. For |t|=1 equation (4) gives

    ||Ftot C_t Dp||/||Dp||=sqrt(2)|1-t|, EVERY N>=2.        (5)

Indeed F_2 sends the u-th cup term to a distinct state with coefficient
1-Q^(-u). Original cup terms have modulus N, the K-prefix and C_t
are unitary, and sum_(u=0)^d |1-Q^u|^2=2N. Both squared source
norms in (5) retain their exact N^3 factor. Thus an order-one unit
phase does not preserve the old lowest-source Ward by an O(1/N) error.

The exact interval-cap identities DO persist after conjugating ALL
their operators and their cap/cup by C_t. If iota_p is an original
cup insertion, then iota_(p,t)=C_t iota_p satisfies the conjugated
interval identities with Omega^(t)=C_t Omega C_t^(-1). Without
that simultaneous change the source terms (4) remain. Keeping the
rest of the original word unchanged is precisely the relative seam.

## 3. Projection back to the complete module does not delete the coupon

One must not conclude from (4) that the final amplitude has left the
total character forever. The terminal ordinary cap is a Hopf map;
the following exact projection accounts for this.

Set

    F_d=(Q;Q)_d=N,
    xi_d=product_(a=1)^d(Q^(-a)-1)=(-1)^d N.

Let R_high extract the components |u,d-u,0> of a highest degree-d
vector. On physical degree 2d define

    P_low=Ftot^d Etot^d/(F_d xi_d),
    M_t=xi_d^(-1) R_high Etot^d C_t D.                     (6)

Then P_low is an idempotent onto the LOWEST degree-2d slice of the
COMPLETE total-Casimir-minus-two isotypic component. It has not been
declared orthogonal in the physical norm. To prove the statement,
Etot^d of any degree-2d vector is highest of degree d because
Etot^N=0. The complete highest-vector theorem identifies it with
H_L(w). Also Etot^d D w=xi_d H_L(w) and
Ftot^d H_L(w)=F_d D w. Therefore P_low D=D and

    P_low C_t D=D M_t, M_1=I.                             (7)

The original terminal row has c U_phys P_low=c U_phys on that
degree slice. This can be checked without a spectral assumption:
ordinary-cap naturality replaces Ftot and Etot by the remaining
single-head F and E, while <d|F^d=F_d<0| and
<0|E^d=xi_d<d|. Consequently the precise ALL-INPUT identity is

    F_t=ell U_red M_t.                                   (8)

Expanding M_t=sum_n t^n M_n gives sum_n M_n=I and
T_n=ell U_red M_n. All N original multiplicities remain; no period
or unknown amplitude was used in this completion.

The resulting M_t is generally neither scalar nor unitary and its
coefficients M_n need not be positive or projectors. Already at N=2,
in the original degree-one physical multiplicity basis,

    M_t=[[t,0],[i(t-1),2-t]].                             (9)

This follows from the original E/F/H_L/D matrices in (6), not a
chosen interpolation. M_0^2!=M_0, and at t=-1 the operator has
eigenvalue three. Thus physical unitarity of C_t does not give a
contractive effective coupon after the nonorthogonal Hopf projection.
The complete total character has been restored in (8), but the
original operator factorization has acquired the additional M_t.
No specific semiclassical canonical graph for M_t is inferred from
the finite-level example (9) alone.

## 4. What the doubled phase average matches

On the recorded head, Parseval inserts the exact doubled projector

    D_clock=sum_n Pi_n tensor bar(Pi_n)
      =(1/(2pi)) integral C_(exp(i theta))
                         tensor bar(C_(exp(i theta))) dtheta. (10)

It matches the integer recorded colors in the two copies. It commutes
with their Cartan clocks. It does NOT commute with the independent
raising/lowering Ward operators. For example,
(F_2 tensor I)D_clock|0,0>=(1-Q)|1,0>, whereas
D_clock(F_2 tensor I)|0,0>=0. The same nonzero example works at
every N>=2, with physical endpoints retained.

Thus (10) is a Cartan matching condition, not a full inverse-meridian
matrix equation. It does not by itself reestablish the faithful cap
interval certificate for a transparent middle wire. Effective projection
(8) instead retains its entire nontrivial operator M_t on both copies.

Classically, in an unbased Gauss frame the seam sends

    (k,e,f)->(k,t^(-1)e,t f),
    G->h_t G h_t^(-1), h_t=diag(t^(-1/2),t^(1/2)).         (11)

The square-root sign has no effect on this conjugation. Based meridians
to its right also change through their actual L_- prefixes; they may
not be held fixed while ignoring that change. This is a relative
Cartan-frame transition. It is not generally a peripheral longitude,
either: h_t need not commute with the physical meridian G.

## 5. Precise geometric implication

The original scalar at t=1 and the positive terminal Cauchy Gram are
fully source-exact. At a retained nontrivial phase the equations are
the TWISTED equations (4), or equivalently the completed coupon (8).
The phase has unchanged color/central powers and so cannot simply be
renamed the existing meridian parameter. No theorem here identifies
it with a drilled-component holonomy; that would need its own explicit
topological/source construction.

To apply the original-knot representation-volume bound to all critical
contributions of (2), one still needs to prove that this additional
seam's complete stationary equations make it transparent, or bound the
full M_t coupling with the correct calibrated action. Color equality
in (10), or total-Casimir recovery in (8), does not prove that statement.
The exact figure-eight energy identity in the terminal-Gram note is
unchanged; it is a coherent special calculation of this same family.

[Audit](../experiments/audit_actual_terminal_phase_coupon_ward.py):
literal coproduct Ward operators, full lowest/Hermite multiplicity
maps, every input column of (8), all packet coefficients, the exact
N=2 coupon, and the macroscopic original-source norm in (5).

Fresh replay: PASS six all-input physical Ward/terminal-completion levels,
the exact symbolic N=2 coupon, and eight source-norm levels through N=129.
Compilation passes. No closed-knot geometric estimate is inferred.
