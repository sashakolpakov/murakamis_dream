# A tame Hermite frame for the original source channel

29 October 2026. The colliding c_0 Casimir channel containing the
original cup has an explicit generalized vector with harmonic-sum
coefficients. Its source-adapted Hermite frame has UNIFORMLY bounded
physical condition number after a common N^(3/2) scale. In that frame
the original marked and
ordinary caps are exactly the two coordinate rows, and the full
crossing is a unit scalar times a Jordan matrix with uniformly bounded
off-diagonal coefficient.

This proves an actual source-controlled Hermite Gram for the selected
T=N-1 channel, including its derivative direction. It does not estimate
recoupling from this channel into all other channels on overlapping
pairs. No full-channel q-Racah norm or sharp knot bound follows yet.

## 1. The original physical source and Casimir

Fix `q=exp(pi*i/N)`, `Q=q^2`, `d=N-1`, `rho=q-q^(-1)`,
`x=q^d=-q^(-1)`, `N>=2`. On balanced heads use exactly

    mathsfF|a>=(1-Q^(a+1))|a+1>,
    Ecal|a>=(Q^(-a)-1)|a-1>,
    K|a>=xQ^(-a)|a>,
    F_tot=mathsfF_1+K_1^(-1)mathsfF_2,
    E_tot=Ecal_1 K_2+Ecal_2,
    Omega=F_tot E_tot+qK_tot+q^(-1)K_tot^(-1).

Missing endpoint arrows are zero. Work on the physical integer-degree
d subspace with basis `|u,d-u>`, `0<=u<=d`. Let `c_*=q+q^(-1)`.
The original cup, ordinary pivotal cap and marked row restrict here to

    p_u=N x^(u-d), ell_u=x^(-u)Q^(-u)/N,
    m_u=x^(d-u)/N^2.                               (1)

The unrestricted marked row is not replaced by this restricted row
on other degrees; every vector constructed below has degree d.
These are the fixed actual turns, with no invented scalar frame.

Define finite harmonic sums

    H_0=0, H_u=sum_(j=1)^u 1/(1-Q^j),
    g_u=x^(u-d)=p_u/N,
    v_u=-g_u H_u/rho.                              (2)

Then the exact Jordan equations are

    (Omega-c_*)g=0, (Omega-c_*)v=g.                 (3)

In particular g,v are independent, and their span is the actual
size-two c_* block inside integer degree d. This block, rather than
the entire 2N-dimensional c_* generalized eigenspace across degrees,
is the source channel treated in this note.

## 2. Derivation from generic q with actual cup duality retained

Use a variable z near q and the ordinary highest-weight representation
of highest weight d=N-1. Put `Q_z=z^2`, `x(z)=z^d`,
`F_a(z)=product_(j=1)^a(1-z^(2j))`. Keep the standard highest-weight
endpoint, including `mathsfF|d>=0`. All factorials with `a<N` are
nonzero near q.

The top-channel descendant and spin-zero invariant cup may be
normalized as

    g_u(z)=x(z)^(u-d),
    h_u(z)=g_u(z) R_u(z),
    R_u(z)=(-1)^u z^[-u(u+1)] F_u(z)F_(d-u)(z)/F_d(z).
                                                               (4)

Indeed `g(z)=F_tot(z)^d|0,0>/F_d(z)`. The finite coproduct binomial
proves its displayed components. The E equation for an invariant
degree-d vector gives the successive ratio

    h_(u+1)/h_u=-z^[d-2u-2]
                         (1-z^(2u+2))/(1-z^(2d-2u)),

which is (4); direct F and K equations give `F_tot h=0`, `K_tot h=h`.
Thus h is the ACTUAL self-duality cup up to the stated analytic unit
normalization. Its paired evaluation is transported reciprocally.
One does not extend the root-only expression `K^(1-N)` as a generic-q
pivot or assume a root cyclic endpoint away from q.

The exact Casimir eigenvalues are

    Omega(z)g(z)=c_top(z)g(z),
    Omega(z)h(z)=c_triv(z)h(z),
    c_top(z)=z^(2N-1)+z^(-2N+1),
    c_triv(z)=z+z^(-1).                             (5)

These follow from the defining coproduct: the top highest vector has
K-root `z^(2d)`, while h is invariant. They can also be checked
directly from the entries above. Root complementation gives
`R_u(q)=1`, so `h(q)=g(q)`. Meanwhile

    D_logz(c_triv-c_top)|q=2N rho,
    D_logz R_u|q=-2N H_u.                           (6)

For the second equation, differentiate (4) and pair its last u
factorial terms with indices `N-j`. Their sum reduces to
`-2N sum_(j<=u)(1-Q^j)^(-1)`; the quadratic integer terms cancel.
All derivatives are at fixed N and the actual root, at either parity.

Consequently

    lim_(z->q) [h(z)-g(z)]/[c_triv(z)-c_top(z)]=v.   (7)

Applying (5) before the limit proves (3). This is a normalized divided
difference of actual Clebsch channels, with the original cup kept.
It does not use the fixed-q common-meridian splitting at a dual cap;
that cap's exact dual-color product keeps its Casimir nodes collided.

An analytic rescaling of h or g, equal to one at q, can add a multiple
of g to v. The source-adapted vector in Section3 removes precisely
that ambiguity. Thus the final Hermite frame does not depend on the
unphysical first derivative of an eigenvector normalization.

## 3. Exact original co-sources and the canonical Hermite lift

The finite sums in (1)--(2) give

    ell g=0, m g=1/N,
    gamma_N:=ell v=q x^(-d)/(N rho^2)
                   =(-1)^N/(N rho^2),
    mu_N:=m v=-(sum_(u=0)^d H_u)/(N^2 rho).          (8)

In particular gamma_N is NONZERO at every level. To check its value,
interchange the two finite sums:

    sum_(u=0)^d Q^(-u)H_u
      =sum_(j=1)^d [sum_(u=j)^d Q^(-u)]/(1-Q^j)
      =-1/(1-Q^(-1)).

Also `q x^(-d)=(-1)^N`, by `x=q^d` and the actual half-period q.
This accounts for the full parity sign.

Define the SOURCE-ADAPTED generalized vector

    t_N=(v-mu_N p)/gamma_N.                         (9)

Then all original source pairings are exactly

    m p=1, m t_N=0, ell p=0, ell t_N=1,
    (Omega-c_*)t_N=theta_N p,
    theta_N=1/(N gamma_N)=(-1)^N rho^2.              (10)

Thus the two original co-sources, not newly chosen dual rows, are
the inverse frame on this actual Jordan channel. In particular
`(Omega-c_*)|span(p,t_N)=theta_N p ell`, agreeing with the retained
rank-one nilpotent source. No ordinary quantum dimension is divided
out. The generalized direction and the marked co-source remain.

The replacement `v->v+lambda g` changes `mu_N` by `lambda/N`, so
the numerator in (9) is unchanged. This proves the normalization
independence asserted after (7).

## 4. Fourier--Plancherel gives uniform physical conditioning

For `1<=j<N`,

    |1-Q^j|>=4min(j,N-j)/N, |rho|>=4/N.

Hence, with `Harm_N=1+log N`,

    max_u |H_u| <=(N/2)Harm_N,
    ||v||_2 <=(N^(5/2)/8)Harm_N,
    |mu_N| <=(N/8)Harm_N,
    |gamma_N|^(-1)=N|rho|^2<=4N.

These estimates already give polynomial frame bounds without a
spectral projector. A stronger exact Fourier calculation removes
their condition growth.

On degree d the original marked row is `m=p^*/N^3`, so (10) gives
`p^*t_N=0`. If `Hbar=(1/N)sum_u H_u`, (9) becomes

    (t_N)_u=(-1)^(N+1)N rho g_u(H_u-Hbar).           (11)

Use the unnormalized cyclic Fourier transform
`Hhat_k=sum_(u=0)^d H_u Q^(-ku)`. Pairing j with N-j gives
`H_d=d/2`. The cyclic difference of H therefore has value `-d/2`
at zero and `(1-Q^u)^(-1)` at `u=1,...,d`. Its Fourier transform
is EXACTLY `-k`, for `1<=k<=d`: successive transforms differ by
`sum_(j=1)^d Q^(-kj)=-1`, starting at zero for k=0. Consequently

    Hhat_k=-k/(1-Q^(-k)), 1<=k<=d,
    ||t_N||_2^2=N|rho|^2 sum_(k=1)^d k^2/|1-Q^k|^2. (12)

This is ordinary finite Plancherel on the FULL physical N-window;
no Fourier channel is omitted or independently dephased.

The elementary root identity is

    sum_(k=1)^d |1-Q^k|^(-2)=(N^2-1)/12.

For a direct proof differentiate `P(z)=(z^N-1)/(z-1)` twice at
one. The first reciprocal sum is d/2 and the sum of squared
reciprocals is `d(5-N)/12`; their difference is the displayed
absolute sum. Pairing k and N-k then gives

    N^2(N^2-1)/48
       <=sum_(k=1)^d k^2/|1-Q^k|^2
       <=N^2(N^2-1)/24.

Since `4/N<=|rho|<=2pi/N`, it follows that

    N^3/4<=||t_N||_2^2<=pi^2 N^3/6,
    p^*t_N=0, ||p||_2^2=N^3.                       (13)

For the two physical columns `V=[p,t_N]` this proves

    sigma_min(V)>=N^(3/2)/2,
    sigma_max(V)<=pi N^(3/2)/sqrt(6),
    kappa(V)<=2, uniformly EVERY N>=2.              (14)

For the last bound use the known first column norm N^(3/2), not
just the two extreme singular-value bounds: the other column's
relative norm lies in `[1/2,pi/sqrt(6)]`, and `pi/sqrt(6)<2`.
The condition number is therefore at most two; N=2 attains two.

The exact inverse on its range is still the two original rows m,ell
by (10). The ordinary row on the full physical degree-d space has
a larger norm because it also sees other channel directions; its
restriction here is precisely the coordinate dual of t_N. No inverse
of a possibly ill-conditioned whole Casimir projector was used.

## 5. An actual positive Hermite Gram and crossing bound

On `S_N=span(p,t_N)` define the positive inner product

    ||w||_(Herm)^2=|m w|^2+|ell w|^2.                (15)

It makes p,t_N orthonormal. It has rank two on S_N, not rank one,
and retains BOTH the value and derivative channels. Both original
co-sources have dual norm one. Equation (14) compares this Gram
uniformly with N^(-3) times the physical metric. This is an explicit
source-controlled Hermite Gram, not
a metric defined from an unknown knot scalar or terminal word.

Keep the original crossing's common Cartan scalar kappa. The
independently derived Casimir polynomial has

    r(c_*)=1, r'(c_*)=-d/(2rho).

Therefore in the p,t_N frame the EXACT original signed crossing is

    R_+=kappa [[1,tau_N],[0,1]],
    R_-=kappa^(-1) [[1,-tau_N],[0,1]],
    tau_N=(-1)^(N+1)d rho/2, |tau_N|<=pi.            (16)

Thus, for every signed integer l,

    ||R_+^l||_(Herm)<=1+pi|l|                        (17)

at the original complete root, since `|kappa|=1`. The original full
Cartan, pivot, framing and modified-dimension line have not been
renormalized; (16) is a basis expression for that same operator.
The PHYSICAL operator norm on this SAME invariant source channel
is consequently at most `2(1+pi|l|)`, uniformly in N.

The Gram (15) is asserted on the SELECTED TWO-DIMENSIONAL invariant
channel only. Adjacent crossings may take it into other intermediate
Casimir channels. Extending it through the full q-Racah transform,
with the source, is the remaining problem. Declaring the rest of
the physical tensor space orthogonal would not control that leakage,
and no such full-channel estimate is claimed here.

[Audit](../experiments/audit_actual_tame_c0_hermite_source_frame.py):
literal original E/F Casimir and signed R, all original source rows,
generic-q cup/descendant divided difference, parity and frame singular
values at both odd and even levels.
