# The original Green generating relation on a signed straddling chart

Workspace research draft, 31 October 2026. Not approved for publication.
This proves a LOCAL regular action and ordered-character identity,
including the omitted-half scalar. It does not construct the global
marked signed pattern or its relative regulator.

## 1. Strict chart and the actual stationary integral

Let x,y,b,c>0, A=x+y, P=xy, 0<delta<1/2, and write

    z=sin²(pi delta), k=cos(pi delta), D=A²-4Pz>0,
    T_b=sqrt(bA+P+b²z),
    T_c^-=sqrt(c²z-cA+P).

Assume c>L_end=(A+sqrt D)/(2z). The original lower interval has
stationary endpoints

    sin²(pi mu)=k²b²/[(b+x)(b+y)],
    sin²(pi nu)=k²c²/[(c-x)(c-y)],
    0<mu<1/2-delta<nu<1/2.                                  (1)

All signs and endpoint intervals are part of the chart. It is localized
at the displayed nonzero factors and at the ordinary Gauss units used
below. No squaring is used to choose the post-pole root.

Let alpha=4[k²-sin²(pi t)] and let Lambda be the positive cleared root
in the original cofactor action. The actual absolute stationary value,
retaining both unused intervals, is

    G=mu log b+(1-nu)log c+integral_mu^nu log(Lambda/|alpha|)dt
     =Q_b+log c-J_c,                                         (2)

where Q_b is the calibrated pre-pole triangle action and

    J_c=nu log c+integral_0^nu log|alpha|dt
                       +integral_nu^(1/2) log Lambda dt.

The equality follows from integral_0^(1/2)log|alpha|=0, after keeping
the actual outside products; it is the reviewed LEFT identity.

## 2. Exact analytic continuation to the signed clock

Use the physical output clock c_tilde=-c. Choose

    Log c_tilde=log c-pi i,
    T_(c_tilde)=-T_c^-,
    Log alpha=log|alpha|+pi i after t_c=1/2-delta.

Before t_c its logarithm is real. The analytic stationary primitive
of the ORIGINAL source triangle, continued with these logarithms,
is exactly

    Q_(c_tilde)
      =nu Log c_tilde+integral_0^nu Log alpha dt
                            +integral_nu^(1/2) Log Lambda dt
      =J_c-pi i t_c.                                        (3)

The two imaginary terms are -pi i nu and +pi i(nu-t_c);
their sum fixes the constant in (3). The contour is the continuation
past the logarithmic alpha zero on its specified side, rather than
an undefined principal-log integral. Locally all endpoints are away
from that zero, so (3) gives an analytic germ. Its row equation is
Log c_tilde+Log alpha(nu)-Log Lambda(nu)=0 exactly.

The lower Green action on these SAME signed physical clocks is

    S_G=Q_b-Q_(c_tilde)+Log c_tilde
       =G-pi i(1/2+delta).                                  (4)

In particular its head derivatives equal those of G evaluated with
the signed clock. Its spectral derivative is

    partial_delta S_G=log(H_c/E_b)-pi i,
    E_b=A+2bz+2sqrt(z)T_b,
    H_c=2cz-A+2sqrt(z)T_c^-.                                 (5)

This agrees with the exact analytic branch
E_(c_tilde)=-H_c, Log E_(c_tilde)=log H_c-pi i.

## 3. Both retained finite scalar modes

In the strict straddling chamber the exact unused suffix sign is
(-1)^(m-1-j). Evaluating its c monomial at the physical clock -c
contributes (-1)^(d-j). At even N their product is (-1)^m;
this cancels the (-1)^m in

    A_rest=(-1)^m[exp(pi i N delta)+exp(-pi i N delta)].

Thus, apart from the already recorded overall source sign, the two
actual principal modes at these signed clocks are

    S_-=G-pi i delta=S_G+pi i/2,
    S_+=G+pi i delta=S_G+pi i/2+2pi i delta.                  (6)

At odd N the retained scalar is
4(-1)^m sin(pi delta)sin(N pi delta). The same sign computation
leaves two modes with the same actions (6), with explicit nonzero
scalar multiples of sin(pi delta) on the strict chart. The principal
actions are unchanged; no sine endpoint is included.

Both differences from (4) are independent of all face/head variables.
Their real parts are zero on the real chart. The two spectral logarithms
differ by2pi i, as expected from the two actual modes; neither mode
may be deleted merely because its modulus has zero rate.

## 4. All head derivatives and the whole ordered product

Here is a direct algebraic check beyond matching a scalar trace.
For a generic possibly signed middle q, use a root

    T²=qA+P+q²(1-k²), d_D²=(x-y)²+4xy k²=D.

Set the exponentiated middle and outer forces to

    p(q)=(T-iqk)/(T+iqk),
    E_y(q)=[y(x-y)+q(x+y(2k²-1))+2iykT]/[(y+q)d_D].          (7)

These are the exponential logarithmic derivatives of the same
triangle primitive. At b use T=T_b; at c_tilde use T=-T_c^-.
Equation (4), with the ORIGINAL physical adapter H/(b c_tilde)^(d/2),
gives

    p_in=p(b), p_out=p(c_tilde),
    g_out/g_in=E_y(b)/E_y(c_tilde).                           (8)

No magnetic reciprocal is changed from the proved physical convention.
Put gamma=g_in E_y(b)=g_out E_y(c_tilde).

For one endpoint, the original Gauss heads with
X1=-x/q, X2=-q/y, S1=-g p, S2=g have total coordinates

    K_tot=y/x,
    E_tot=[y(q+x)/(xp)-(y+q)]/(qg),
    F_tot=g[-p(q+x)+x(y+q)/y]/q.

Substitution of (7) gives EXACTLY

    E_tot=-d_D/(x gamma), F_tot=d_D gamma/y,
    P=B A=
       [[y/x, -d_D/(x gamma)],
        [d_D gamma/x, sigma-y/x]],
    sigma=-2+4z.                                            (9)

For a finite symbolic check, clear the displayed denominators and
reduce by T²=qA+P+q²(1-k²) and d_D²=(x-y)²+4xy k². The numerators
of xg E_tot E_y+d_D and yF_tot/g-d_D E_y both reduce to zero.
Thus BOTH physical legs preserve the same ENTIRE ordered product.

The existing actual ordered-character formula now identifies the
primitive projective centralizer eigenratio. The Green output uses
the reciprocal triangle root D/E_(c_tilde), so

    R0=E_b/E_(c_tilde)=-E_b/H_c,
    C=I+(R0-1)/(J-J^(-1))(P-J^(-1)I),
    J=-exp(-2pi i delta).                                   (10)

This is the original three-contact ordering, not an independently
chosen matrix with the right trace. Its determinant is R0; the
original determinant-one/auxiliary lift is chosen only after that
projective map has been fixed. Formula (10) agrees with the actual
ordered-character identity R0=e_in e_out/D for its lower output
root. It transports both raw trace-minus-two heads.

At a free critical point of the real absolute G,

    H_c=E_b,  (c-b)z=A,  R0=-1.                              (11)

Hence the untwisted actual auxiliary meridian has squared eigenvalue
-1 and trace0 on this local regular chart. The retained-half-twist
fixed-word interpretation is stated separately in
[the conditional peripheral-gap note](research_signed_spectral_peripheral_gap.md).

## 5. Global conditions that are still not proved

These local signed clock choices must come from ONE face assignment
on the original source. The exact obstruction is the incidence-cycle
test in [the sign-cocycle note](research_spectral_face_sign_cocycle.md).
A true complex saddle may instead require general complex clocks;
independent local sign flips do not define it.

When the common clock assignment and all original head stationarity
equations are genuinely supplied on a regular chart, (9)--(10) are
the local ordered maps used by the original Morse reconstruction.
They do not by themselves prove that every absolute shared maximum
has such an assignment. Nor do they supply the forced marked-line
flags: the formula (9) divides by x,y, so a protected outer face
requires its own literal boundary adapter. No limit is claimed to
recover those flags solely from a scalar quadratic.

Finally the real equality of local actions in (4),(6) is not yet
the absolute GLOBAL relative-volume identity. One must sew the
actual original fundamental chain with its unchanged marked
decoration. The old failure of local Gauss-reference invariance
remains relevant. No source period, spectral-cycle contribution or
general upper bound is asserted by this local lemma.
