# Actual sewing shifts are divided-Ward images of the wrap source

28 October 2026. The unit shifts in the exact cyclic sewing have
an explicit relation to the ORIGINAL integral divided Hopf adjoint.
The relation holds on the actual balanced head, including an exact
whole-q source profile. The large scalar powers cancel between the
two ends of a transfer. Thus these shifts need not be assigned an
auxiliary unipotent action.

This does not yet give a geometric centralizer chain map. There is
a first explicit obstruction to the simplest proposed extension:
independent head adjoints are not the full mixed coproduct adjoint.
Their difference has a nonzero ORIGINAL crossing-cap pairing.
The internal geometric interval cannot be inferred by omitting it.

## 1. The literal integral head and its two wrap coupons

Fix N>=2 and put `m=N-1`, `L=N(N-1)/2`, `rho=q-q^-1`.
Use the actual integral color of highest weight m, with basis v_j,

    E^(a)v_j=[m-j+a choose a]_q v_(j-a),
    F^(a)v_j=[j+a choose a]_q v_(j+a),
    K v_j=q^(m-2j)v_j.                           (1)

Terms outside the head are zero. Symmetric Gaussian coefficients
are their Laurent-polynomial values, not quotients evaluated at a
root. Let `B_+=|m><0|`, `B_-=|0><m|`. These are the literal
missing cyclic-wrap matrix units. Write `J_+,J_-` for the unit
truncated raising/lowering shifts and `J v_j=j v_j`.

Use the FULL integral Hopf adjoints

    A_(E^(n))(C)=sum_(k=0)^n (-1)^k q^(-k(n-1))
                         E^(n-k) C E^(k) K^-n,
    A_(F^(n))(C)=sum_(k=0)^n (-1)^k q^(k(n-1))
                         F^(n-k)K^-k C K^k F^(k). (2)

The mixed terms in (2) remain even when E^(N),F^(N) individually
vanish on the N-dimensional head. These are linear adjoint images;
no assertion that a single A_h is a square-zero differential is made.

## 2. Exact root identities in the ORIGINAL balanced basis

At `q=exp(pi*i/N)` one has `[m choose k]_q=1` for every k.
Indeed each numerator factor `[N-s]_q` equals `[s]_q`, with
all factors below N nonzero. Direct substitution in (2) gives

    A_(E^(N))(B_+)=(-1)^m J_- q^J,
    A_(F^(N))(B_-)=-q^-1 J_+ q^-J                (3)

in the integral basis. For example only the k-th term contributes
to entry `(k-1,k)` of the first identity. Its coefficient is
`(-1)^k q^(-km) q^(-N(m-2k))=(-1)^m q^k`.
For the second identity, entry `(j+1,j)` comes from `k=m-j`
and has coefficient `-q^(-j-1)`.

The original balanced crossing basis is the diagonal transport

    D_j=(-rho)^j q^(j(j+1)/2).                   (4)

It gives exactly the original raising coefficients `1-Q^(j+1)`
and balanced `Ecal=rho^2 E` coefficients `Q^-j-1`, with
`Q=q^2`. Transport the actual adjoint and the wrap coupons by
this same D, keeping their scalars. Equations (3)-(4) imply

    A^bal_(E^(N))(B_+)=-rho^(-N) q^-L J_-,
    A^bal_(F^(N))(B_-)=(-1)^m rho^N q^L J_+.     (5)

Hence on the actual two-head sewing edge,

    J_+ tensor J_- =(-1)^N
          A^bal_(F^(N))(B_-) tensor A^bal_(E^(N))(B_+). (6)

The rho^N and quadratic phase factors cancel EXACTLY. The same
statement with exchanged heads gives the other transfer. The
marked x^-1 coefficient in each actual transfer remains attached.
Neither endpoint wrap is reset or replaced by a new vacuum.

Thus an actual divided-current description of every local sewing
shift exists, at every N, before Gaussian contraction. It uses the
mixed Hopf adjoint, rather than an ordinary commutator with the
vanishing divided matrix.

## 3. The whole normal profile is explicit

The root formulas cannot simply be differentiated as constants.
Keep q generic and the same integral head and balanced frame. Put

    M_col=-q^N,
    G_j(q)=M_col^j [m choose j]_q,
    C_E(q)=(-rho)^(-N)q^(-Nm-L),
    C_F(q)=(-1)^m(-rho)^N q^(L+1-m^2).

Then the exact WHOLE-q identities are

    A^bal_(E^(N))(B_+)=C_E(q) J_- diag(G_j(q)),
    A^bal_(F^(N))(B_-)=C_F(q) J_+ diag(G_j(q)).   (7)

To verify the first, its integral `(k-1,k)` coefficient is
`(-1)^k q^(k(N+1)-Nm)[m choose k]_q`. The balanced-frame
ratio and the wrap scalar in (4) change this into
`C_E M_col^k[m choose k]_q`. For the second, put k=m-j
in (2); its integral coefficient is
`(-1)^(m-j)q^(-(m-j)m)[m choose j]_q`. The same frame
calculation gives the displayed C_F G_j.

At the root `G_j=1` and `C_E C_F=(-1)^N`. Off the root the
diagonal profile is nonconstant and may have source divisors.
It is tied to the already computed actual color-source profile:

    G_j=M_col^(2j) V_j,
    V_j=[m choose j]_q/M_col^j.                  (8)

Thus the [whole-head Gamma/source comparison](full_head_gamma_source_transport.md)
can transport this precise profile, with its extra character
retained. Equation (7) itself does not invert G_j at a zero.
Fractional source and dual lattices, all normal derivatives,
and the original peripheral line remain necessary.

The actual moment carry at these endpoints is also explicit.
Let `S=J_++B_-` be the cyclic raising completion. For every
polynomial p (indeed every function on the displayed finite
arguments), entrywise multiplication proves

    p(J)S-S p(J+1)=[p(0)-p(N)]B_-,
    p(J)S^-1-S^-1 p(J-1)=[p(m)-p(-1)]B_+.       (8a)

In particular `[J,S]=S-NB_-` and
`[J,S^-1]=-S^-1+NB_+`. Before taking moments, the whole
position-clock identity is

    z^J S z^-J=z S+(z^(1-N)-z)B_-,
    z^J S^-1 z^-J=z^-1 S^-1+(z^(N-1)-z^-1)B_+. (8b)

Euler derivatives in z recover every polynomial/logarithmic
moment with its actual endpoint. The factors z^N are retained
before specialization. For the two-head cyclic transfer A,

    [J_1+J_2,A]
        =Na[-B_-,1 tensor S_2^-1+S_1 tensor B_+,2]. (8c)

The two corner contributions cancel where both wrap edges
overlap. The nilpotent transfer has zero total-index commutator.
Thus its sewing sources have exactly the N-step moment carry
required to repair the cyclic completion. Equations (7)-(8c)
retain that carry; they do not turn it into an ordinary
derivation after cyclic specialization.

## 4. The first global mismatch has an actual nonzero cap row

Equation (6) contains INDEPENDENT adjoints on the two heads.
The original crossing intertwines the actual coproduct, whose
divided formulas have all mixed terms. Those are different
operations. The difference is already visible at N=2 without
an asymptotic argument.

Take `q=i`, `Q=-1`, `M=1`, `x=i`. In the original balanced basis,

    E=(1/2)E_01, F=2E_10, K=diag(i,-i),
    Delta E^(2)=(1/4)E_(00,11),
    Delta F^(2)=4E_(11,00).

Let `C=B_- tensor B_+`. Direct use of (2) with the full
coproduct matrices gives

    A^tot_(F^(2)E^(2))(C)
       =[[-i,0,0,0],
         [0,-i,1,0],
         [0,1,i,0],
         [0,0,0,i]].                            (9)

The independent product in (6) is `J_+ tensor J_-`, whose
only nonzero entry is `(row2,column1)=1`. Denote their
difference by D_mix. It is not a suppressed scalar or a
zero source current. Keep the original stripped crossing

    R_0=[[1,0,0,0],[0,0,-i,0],
                         [0,-i,2,0],[0,0,0,1]],

and its original normalized average first cut with closed
pivots `(-i,i)`. Exactly,

    Phi(D_mix R_0)=1/2,
    Phi(R_0 D_mix)=-1/2.                         (10)

The actual common Cartan factor kappa multiplies these by
kappa and is retained; restoring the other external factors
does not make them zero. Thus the proposed replacement of
the independent sewing image by a diagonal divided Ward
generator drops an actual nonzero endpoint contribution.

This rules out that replacement, not every corrected current
construction. A valid tensor/chain fusion must carry D_mix
and its counterparts, rather than use independent adjoint
identities as if they already had coproduct naturality.

## 5. The geometric endpoint condition is now specific

There is also a precise target on the ORIGINAL whole word,
not only on a separate source cone. The already proved
[actual Borel Ward calculation](actual_borel_ward_cut_contraction.md)
gives the complete principal conjugation fields

    (ad_Ktot-I)/H -> A(h/2),
    ad_Ecal,tot/H -> A f_sl,
    ad_Ftot/H -> A e_sl,

where `H=Log Q`. On the original inverse-eigenflag framing
chart the compensated cut-Borel fields are
`xi_1=2(r-1)partial_r+2s partial_s` and
`xi_2=(2r-1)partial_r+2s partial_s`. Define the literal
finite operator, with the specified LEFT multiplication,

    S_cut=-q K_1-1,
    W_cut=ad_Ftot-2(ad_Ktot-I)-ad_Ecal,tot,
    V_N(C)=S_cut W_cut(C).                      (11a)

Its cut symbol is `S_cut -> A_cut^-1-1=s`, so
`V_N/H -> s(xi_2-xi_1)=s partial_r=V_J`.
It vanishes exactly on the unweighted actual braid word.
The target classical ODE consequently has endpoint `r->r+s`
at time one. This gives the principal generator; it is not
a proof that an arbitrary finite exponential of V_N equals
the retained quantum meridian endpoint.

The target co-source row is explicit as well. For
`Phi_A(C)=Tr(A C)` set `B=A S_cut`, in that order. Then

    Phi_A(V_N(C))=Tr[W_cut^vee(B) C],
    W_cut^vee(B)=B Ftot-Ktot Ftot B Ktot^-1
              -2(Ktot^-1 B Ktot-B)
              -(Ktot^-1 B Ecal,tot-Ecal,tot Ktot^-1 B). (11b)

Each term follows by cyclicity of the trace, so the original
cut row and pivot need not be declared invariant. The whole
weighted Ward formula transports (11a)-(11b) with the actual
lower-moment Green currents: a moment polynomial p leaves
its specified forward difference `Delta_t p`, not a zero
endpoint. The normal clock/pivot adapters in the divided
Ward theorem remain attached. These target data already
exist; (6) does not by itself supply their source map.

The actual paired Frobenius source already supplies a precise
target generator. In the marked variables of
[the unprojectivized source torsor](actual_unprojectivized_frobenius_borel_torsor.md),
let `s=C alpha^2`, `r=(1+m_src)/2+D alpha^2`. The actual
divided-source generator `e-h-f` has field `2 partial_msrc`;
it fixes alpha. Hence its source-dependent multiple

    s(e-h-f) -> s partial_r=V_J.                (11c)

At fixed alpha its actual standard-vector group is
`I+b s [[-1,1],[-1,1]]`. Its square-zero matrix gives an
exact additive group law, and the paired dual parameter
changes by `m_src -> m_src+2bs`. At b=1 the frame changes
by `r -> r+s`, precisely the complete marked meridian
endpoint. Thus the desired endpoint is not an unspecified
abstract additive action.

Equation (11c) is a theorem on that actual paired source
family. Equations (6)-(8) identify the literal sewing
currents and their whole normal profiles. The missing map
must fuse the INDEPENDENT images in (6) into the FULL
ordinary/divided coproduct current, carry the correction
detected in (10) and all its Green-moment rows, and then
identify its transverse Gaussian image with (11a)-(11c).

The generic principal density `c_beta Omega_cut` and its
nonzero logarithmic residue do not perform that fusion.
No nonzero selected geometric image, equality of the
relative coordinates, or volume lower bound is claimed
from the two separate endpoint constructions.

[Exact audit](../experiments/audit_sewing_wrap_divided_ward.py).
It checks root and generic-q identities at levels 2 through
12, the retained paired transfer signs, and (9)-(10) in
characteristic zero. The displayed calculations prove the
all-level identities independently of those tests.
