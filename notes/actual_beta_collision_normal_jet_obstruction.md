# The complete beta source has an exponentially large first normal jet

28 October 2026. This is an obstruction to a uniform normal-neighborhood
estimate AFTER integrating the original beta fiber. It is not an
excess-volume contribution to a knot period, and it does not contradict a
local exp(o(N)) bound in a shrinking collar where all the unintegrated
full-Psi arguments approach one.

## 1. Exact source and exact first derivative

Use precisely the original finite source in
[the trivalent source theorem](actual_trivalent_quantum_beta_source.md#1-the-source-and-its-exact-finite-polynomial):

    Q=exp(2*pi*i/N), d=N-1, F_k=product_(j=1)^k(1-Q^j),
    B_N(u,v)=sum_(a=0)^d product_(j=0)^(a-1)(u-Q^j v).

In the actual full-Psi fiber the arguments are u=Q^2 U, v=Q V,
and its source normalization is Q^(-d)/N. These exact tags and that
normalization are unchanged here. No residue-only beta replacement is
made.

Every nonempty Newton product contains u-v, so, identically in v,

    B_N(v,v)=1,
    partial_u B_N(v,v)=J_N(v):=sum_(k=0)^(N-2) F_k v^k,
    partial_v B_N(v,v)=-J_N(v).                         (1)

The second equality follows by differentiating the first factor of each
nonempty product; differentiating any other factor leaves u-v=0.
Consequently this is a derivative of the COMPLETE original source,
including the current responsible for B_N(v,v)=1. This is not the
derivative of its homogeneous balanced-residue term alone.

## 2. A fixed regular point with an exponential derivative

Set

    c_*=exp(-i*pi/3),
    I(s)=integral_0^s log(2 sin(pi*t)) dt,
    gamma=I(5/6)=-I(1/6)=v_3/(2*pi)>0.

Here v_3 is the volume of the regular ideal tetrahedron; equivalently
gamma=Im Li_2(exp(i*pi/3))/(2*pi)=0.161532973609725257....
For EVERY sequence of integer levels N tending to infinity, including
both parities and every residue class modulo six,

    J_N(c_*)=i N exp[N gamma-25*pi*i*N/72] (1+o(1)).    (2)

More generally, uniformly for theta in a fixed bounded real interval,

    J_N(c_* exp(i*theta/N))/J_N(c_*)
                      =exp(5*i*theta/6)+o(1).          (3)

Here and below c_* is a value of the actual tagged beta argument v. If
one instead parametrizes its untagged argument V, choose V=Q^(-1)c_*.
An O(1/N) root tag changes the nonzero prefactor through (3), not gamma.
If a particular full-Psi chart also excludes c^N=1, use instead
c_N=c_* exp(i*theta_0/N), for example theta_0=pi/7. Its N-th powers
range over a fixed finite set bounded away from one, and (3) gives the
same exponent with nonzero prefactor exp(5*i*theta_0/6). Thus the
obstruction is not an artifact of the levels for which c_*^N=1.

### Proof

For 0<=k<N there is an exact, continuously accumulated factorial phase:

    F_k=|F_k| exp[i*pi*k(k+1)/(2N)-i*pi*k/2].          (4)

On every compact subinterval of 0<s=k/N<1, Stirling and elementary
Euler--Maclaurin give the uniform estimate

    |F_k|=sqrt(2 N sin(pi*s)) exp[N I(s)](1+O(1/N)).   (5)

For clarity, subtract log(2*pi*t) from log(2 sin(pi*t)); the difference
is smooth through t=0. Stirling for k! and the endpoint half-sum for
that difference give exactly the prefactor sqrt(2 N sin(pi*s)). A
global, endpoint-uniform version sufficient for discarding tails is

    log |F_k|=N I(k/N)+O(log N), 0<=k<=N-1.           (6)

One direct proof of (6) subtracts log t+log(1-t). The remaining function
is smooth on [0,1], while the two singular sums are exactly

    log(k!)+log((N-1)!/(N-1-k)!)-2k log N.

Uniform Stirling bounds, also at k=0 and k=N-1, give the stated error.

The function I has its unique absolute maximum on [0,1] at s_*=5/6.
Indeed I'=log(2 sin(pi*s)), its only interior zeros are 1/6 and 5/6,
and I(0)=I(1)=0<I(5/6). Combining (4)--(5) gives the summand

    F_k c_*^k = sqrt(2 N sin(pi*s)) exp[N psi(s)]
                                    exp(i*pi*s/2)(1+O(1/N)),
    psi(s)=I(s)+i*(pi*s^2/2-5*pi*s/6).

At s_* we have

    psi'(s_*)=0,
    psi(s_*)=gamma-25*pi*i/72,
    psi''(s_*)=-pi*(sqrt(3)-i).

Equation (6) makes the sum outside any fixed neighborhood of s_*
exponentially smaller. Within that neighborhood, I(s)<=gamma-c(s-s_*)^2.
Set xi=(k-Ns_*)/sqrt N and use (5). The shifted lattice Gaussian
Riemann sums converge by this bound, with arbitrary fractional part
of Ns_*. Its integral is

    sqrt(2*pi/(-psi''(s_*)))=exp(i*pi/12).

The remaining amplitude is sqrt N exp(5*pi*i/12); the lattice density
is sqrt N. Their product with the Gaussian integral is iN, proving
(2). Inserting exp(i*theta*k/N) proves (3) by exactly the same dominated
Gaussian argument, uniformly on compact theta intervals. No external
quantum-dilogarithm asymptotics or knot invariant identification enters.

## 3. Consequences for normal neighborhoods

Already the order-one normal jet at the fixed regular point c_* has
exponential rate gamma. Thus a claim that EVERY order r=o(N) normal jet
costs exp(o(N)) relative to B_N(c,c)=1 is false, even for r=1.

In fact the sharp uniform first-jet exponent on the entire unit circle
is

    lim_(N->infinity) (1/N) log sup_(|c|=1)|J_N(c)|=gamma. (7)

The upper bound follows from (6) and the sum of |F_k|; (2) gives the
matching lower bound. Also, for ANY positive radius rho_N with
log rho_N=o(N), Cauchy's derivative estimate gives

    sup_(|delta|<=rho_N)|B_N(c_*+delta,c_*)|
                           >=rho_N |J_N(c_*)|
                            =exp[N gamma+o(N)].       (8)

This concerns a complex normal disk. It does not claim the same growth
on every specified real contour or at every point of that disk.

## 4. The actual three-star block cannot uniformly hide this slope

The exact actual figure-eight block in
[the six-circuit computation](actual_six_circuit_beta_collision.md)
has, after an invertible monomial coordinate change, the form

    W_N(U,V;a,b,c)=B_N(U,a) B_N(V,b) B_N(c,c U V).     (9)

The collision is U=V=1; c remains an independent nonzero parameter.
All the other original atoms, cap factors, and remaining integrations
are retained outside (9). Choose a,b with
P_N=B_N(1,a)B_N(1,b)!=0. This excludes only the explicit finite local
zero sets, and does not divide by an unknown knot period. Then

    W_N(1,1)=P_N,
    (partial_U W_N/P_N)(1,1)
                 =A_N-c J_N(c),
    A_N=partial_u B_N(1,a)/B_N(1,a).                 (10)

In particular no estimate on A_N is required for a UNIFORM obstruction.
Take c_+=c_* and c_-=c_* exp(6*pi*i/(5N)). By (3),

    c_- J_N(c_-)=-c_+ J_N(c_+)(1+o(1)).

The triangle inequality therefore implies

    max_(c=c_+,c_-)|A_N-c J_N(c)|
                                  >=N exp(N gamma)(1+o(1)). (11)

Both marks may be multiplied by exp(i*pi/(7N)) if c^N=1 is excluded
by an auxiliary chart. Their two N-th-power sets then stay uniformly
away from one, while their asymptotic slope ratio is still -1.

Thus the complete three-star block has an exponentially large relative
first normal slope somewhere within O(1/N) of the SAME fixed regular
c_*, regardless of the first star's derivative. For reference, an exact
alternative uniform statement follows by Fourier orthogonality:

    (1/(2*pi)) integral_0^(2*pi)|A_N-e^(it)J_N(e^(it))|^2 dt
                       =|A_N|^2+sum_(k=0)^(N-2)|F_k|^2. (12)

The same real Laplace argument applied to (5), now without any complex
phase, gives the positive energy asymptotic

    sum_(k=0)^(N-2)|F_k|^2
             =3^(-1/4) N^(3/2) exp(2 N gamma)(1+o(1)). (13)

Indeed 2I''(5/6)=-2*pi*sqrt(3), and the squared prefactor at the
maximum is N. This is an exact Plancherel obstruction to a uniform
tame normal-jet assertion, in addition to the explicit phase-coherent
point (2).

These are statements about an actual integrated subnetwork. They do
not assert its exterior original-source pairing is nonzero.

## 5. What this does and does not rule out

The exact collision identity B_N(c,c)=1 cannot be thickened to a
uniform exp(o(N)) estimate for the COMPLETE fiber-integrated beta
source on polynomial normal neighborhoods. A proof that removes a
collision by first integrating that whole fiber and then using tame
normal jets would lose a real exponential saddle.
Conversely, a normal disk centered at this diagonal point on which the
complete source is bounded by exp(o(N)) must have radius at most
exp(-N gamma+o(N)), by the same Cauchy estimate.

This does NOT obstruct the unintegrated, fixed finite shape-one collar
patch. The derivative saddle above has Newton order k/N=5/6, away from
the local all-six-shapes collar; global fiber integration can reach it.
Local holomorphic regularization and preservation of its side currents
remain valid. Nor is gamma an excess over the figure-eight volume
rate: it is the single regular-tetrahedron rate. A sharp whole-knot
bound still requires control after the exterior pairing, or a contour
argument separating that saddle from the collision collar. No positive
geometric intersection or knot-volume asymptotic is proved here.

Reproducible finite/source and saddle checks:
[audit script](../experiments/audit_actual_beta_collision_normal_jet.py).
