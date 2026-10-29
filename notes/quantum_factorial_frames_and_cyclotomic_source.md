# Quantum-factorial frames and the cyclotomic source boundary

Research proof, 27 October 2026. Moving the quantum parameter together
with the integral color gives an actual finite representation on the
whole path. A symmetric quantum-factorial frame makes its principal
compact-source map a smooth sphere twist, with the correct clock.
The singularity of a different natural polynomial frame is carried by
an exact diagonal quantum-factorial gauge, whose norm has exponential
size. Thus a singular source chart need not be an intrinsic obstruction.

The retained inverse eigenflag has a different issue: two explicitly
computed boundary bubbles remain even in the smooth frame. All these
statements precede a quantum-geometric period comparison. In particular,
this does not prove a selected hyperbolic contribution or volume growth.

## 1. Two actual frames on one integral-color path

Put n=N-1 and, for 0<=lambda<=1,

    q=exp(pi*i lambda/N), Q=q^2, s=2pi*i lambda,
    m=q^N=exp(s/2), M=-m, rho=q-q^(-1).

The actual common-Verma wall M Q^(-N)-M^(-1) is identically zero.
Its N-dimensional head therefore is a genuine quotient, even when
Q^N!=1. This assertion is about the module, not about pivotal cups
or a generic ADO invariant. The other wall 1-Q^N remains present.

Write [k]_q=(q^k-q^(-k))/rho, with its removable value k at q=1.
For the standard q-spin highest-weight basis u_j with
F_std u_j=u_(j+1), two frames are

    p_j=u_j/(n)_j,
    f_j=u_j/[n]_q^(fall,j), 0<=j<=n.

Here (n)_j is the ordinary falling factorial. Thus

    p_j=R_j f_j,
    R_j=product_(k=N-j)^(N-1) [k]_q/k.                 (1)

All factors are strictly positive on this real path, including their
removable lambda=0 values. These changes of frame are exact and
invertible at finite N, including the cyclotomic endpoint.

Use the symmetric Gauss pair Ecal=rho E_std, F_G=rho F_std.
In the f-frame, with J z^j=jz^j and D_q z^j=q^jz^j, they are

    Ecal=(D_q-D_q^(-1))/z,
    F_G=z(q^n D_q^(-1)-q^(-n)D_q),
    K=q^n D_q^(-2).                                  (2)

Their entries are rho[j]_q and rho[n-j]_q. The symmetric standard
operators E_std,F_std have removable continuation at q=1. The
literal common-Verma Hopf normalization is instead

    E_actual=Ecal/rho^2=rho^(-1)E_std,
    F_actual=F_G=rho F_std.

This opposite Hopf scaling leaves E_actual tensor F_actual and
the actual universal R unchanged. It must not be confused with
identifying the individual ordinary and balanced generators.
The finite Gauss pair and actual R extend regularly at q=1;
the displayed Hopf rescaling itself need not. In the p-frame
the same Gauss generators have entries

    Ecal p_j=rho [j]_q[N-j]_q/(N-j) p_(j-1),
    F_G p_j=rho(n-j)p_(j+1).

The diagonal relation (1) conjugates these formulas exactly; it
also conjugates every crossing, source and inserted matrix. A
rank-one coupon psi phi becomes R^(-1)psi phi R. It must not be
replaced by the original constant coupon after a frame change.
The [global q-difference source theorem](integral_color_global_q_difference_source.md)
gives its exact balanced frame and crossing comparison, including
the normalization just specified. The exact comparison to the
ordinary-falling head, including all such
coupons and the pivotal adapter, is in
[the actual coherent-symbol theorem](integral_color_coherent_symbols_and_uniform_poles.md),
Section 6. That note also proves uniform C^l generator convergence
on the whole compact sphere, including its poles. This is distinct
from a full crossing-word asymptotic estimate.

## 2. The whole function in the frame torsor

Set

    b_lambda(x)=sin(pi lambda x)/(pi lambda x),
    S_lambda(T)=integral_(1-T)^1 log b_lambda(x) dx.     (3)

Use b_0=1 and the positive real logarithm for lambda<1. At lambda=1
the endpoint logarithm is integrable. For T=j/N, uniformly for all
0<=lambda<=1 and 0<=j<N,

    (1/N)log R_j=S_lambda(j/N)+O((1+log N)/N).           (4)

Indeed [k]_q/k=b_lambda(k/N)/b_lambda(1/N). The denominator has
logarithm O(N^(-2)), uniformly. For the numerator, write

    log b_lambda(x)=log(1-lambda x)+g(lambda x),
    g(y)=log[sin(pi y)/(pi y(1-y))].

The removable function g is C^1 on [0,1]. Its Riemann sums have
uniform error O(N^(-1)). Monotonicity bounds the logarithmic part
by its last grid value and its final-interval integral, each at most
O((1+log N)/N). This proves (4), including both endpoints, without
assuming a regular Taylor expansion at lambda=1.

This is a dilogarithmic whole function. For s=2pi*i lambda put

    J_s(x)=2sinh(sx/2)/(sx)=b_lambda(x),
    B_s(x)=s x^2/4+Li_2(exp(-sx))/s-x Log(sx)+x.

On the marked branch continuous from 0<lambda<1,

    dB_s/dx=Log J_s(x),
    S_lambda(T)=B_s(1)-B_s(1-T).                       (5)

The endpoint x=0 is interpreted continuously. The logarithms in
(5) are marked together, so its right side is real on this path.
Equation (5) describes the scalar frame period before its quantum
jets. It is not the knot's complete Bloch regulator.

At lambda=1 the conditioning is already exponentially large. The
elementary sine product gives exactly

    R_n=N/[(2sin(pi/N))^(N-1)(N-1)!],
    lim (1/N)log cond(R)=log(2pi)-1.                   (6)

For this real path [k]_q/k<=1, so 1=R_0>=R_j>=R_n>0;
cond(R)=1/R_n in the coordinate Euclidean metric or any common
diagonal coherent metric. To prove the sine product, factor
(z^N-1)/(z-1) at z=1 and take absolute values. Stirling's formula,
or integral bounds for log((N-1)!), then gives (6).
The same rate follows directly from
S_1(1)=integral_0^1 log[sin(pi x)/(pi x)]dx=1-log(2pi).

Consequently, an exact change of frame may move an exponential
norm into its source or metric. Algebraic invertibility does not
justify discarding that norm in the volume problem.

## 3. The symmetric frame has a smooth clock-preserving source map

On the compact-source surface use coordinates (v,a), T=va and
Omega=dv wedge da=dlog v wedge dT. Its real sphere has
T=|v|^2/(1+|v|^2). At fixed lambda the coherent principal symbols
of (2) are

    k=m exp(-sT),
    e=2sinh(sT/2)/v,
    f=2v sinh(s(1-T)/2).                              (7)

They obey ef=m+m^(-1)-k-k^(-1). In particular

    H=[[k,e],[kf,m+m^(-1)-k]], det H=1.

The m-eigenflag of H is

    z_+=(m-k)/e=exp(s(1-T)/2)v.                       (8)

Both formulas continue at the poles. Thus the compact-source
map to the eigenflag-marked Grothendieck family is the shear

    Psi_s(v,a)=(r v,a/r), r=exp(s(1-T)/2).

It keeps T and the actual principal clock exp(sT) unchanged and
obeys Psi_s^*Omega=Omega exactly. The local generator for the
change of log v, using the primitive log v dT, is

    W_s(T)=s(T/2-T^2/4), W_s'(T)=Log r.                (9)

For imaginary s on the specified path |r|=1 on the real sphere.
Hence Psi_s maps that sphere to itself, including lambda=1. It
is a regular area-preserving sphere twist. This is a concrete
principal clock-preserving map, stronger than the earlier
exponential-current detour that changed the clock.

The p-frame instead has e_p=J_s(1-T)e and f_p=f/J_s(1-T).
Its source coordinates relate by

    v_f=v_p/J_s(1-T), T_f=T_p.                        (10)

This is also symplectic wherever defined; its generator has
derivative -Log J_s(1-T)=-S_lambda'(T). It explains the apparent
p-frame flag factor s(1-T)/(1-exp[-s(1-T)]). Its pole at
lambda=1,T=0 is carried by the genuine factorial frame torsor
(1), rather than by a singularity of (8). The finite frame is
invertible there; its nonuniform classical limit is quantified
by (4)--(6). Source and metric changes remain essential.

### An exact finite quantization of the smooth shear

There is an actual finite star automorphism behind (8), not
merely a principal coordinate formula. On the polynomial frame set

    U_j=q^[Nj-j(j+1)/2]=m^j q^[-j(j+1)/2], U_0=1.      (10a)

All exponents are integers. This diagonal matrix is unitary for
real lambda in any of the common diagonal coordinate/coherent
metrics. It commutes with the entire finite clock Q^J, K,
all index moments and both diagonal endpoint projectors.
Conjugation gives the exact finite automorphism

    sigma_A -> sigma_(U A U^(-1))

of the already specified coherent star algebra. Its inverse,
products, trace and all pointed word pairings are literal matrix
identities, with the coupon and its dual conjugated as well.

For the coordinate operators a_hat=J_-/n, b_hat=J_+/n,
T_hat=J/n, where J_+ z^j=(n-j)z^(j+1), their exact symbols are

    sigma_(U a_hat U^(-1))
       =m^(-1)q a [1+(q-1)T]^(n-1),
    sigma_(U b_hat U^(-1))
       =m q^(-1)b [1+(q^(-1)-1)T]^(n-1),
    sigma_(U T_hat U^(-1))=T.                         (10b)

The binomial derivative identity proves both first formulas.
Uniformly on the compact sphere, they tend in every fixed
derivative norm to a/r, r b, T. Thus this exact star automorphism
quantizes precisely Psi_s. It is not the literal pullback by
Psi_s on finite symbols; that pullback need not preserve their
finite-dimensional space. Its whole diagonal phase is

    Log U_j=N W_s(j/N)-s j/(4N),                      (10c)

with the marked logarithm from q=exp(s/(2N)). The subleading
term is retained rather than replacing this phase by its leading
quadratic generator.

It also equals the actual balanced frame map at the roots. In
the basis-vector convention of the global q-difference theorem,

    h_j=D_j w_j,
    D_j=(-1)^j q^[j(j+1)/2]/{n choose j}_q.

For every parameter on the path one has exactly

    D_j U_j=M^j/{n choose j}_q,
    D^(-1)=U diag({n choose j}_q/M^j).                 (10d)

At q_N, {N-1 choose j}_(q_N)=1 and M=1. Therefore

    U(q_N)=D(q_N)^(-1).                               (10e)

So the actual root crossing, source, cups, caps and weighted
word are transported by this unitary finite star map. Away
from the root the last factor in (10d) remains present, with
all its source and quantum-normal data; U alone is not the
whole balanced frame map there.

Finally its top phase is the original normalization phase:

    U_n=q^[N(N-1)/2],
    U_n(q_N)=i^(N-1)=i^(N+3)=epsilon_N.                (10f)

This is an exact comparison with the phase already fixed in
the full modified dimension, not a phase chosen to fit volume.
The rest of that dimension, the root-normal pivotal adapter
and the knot's selected regulator period are separate data.

## 4. The retained inverse eigenflag has two boundary bubbles

Changing the eigenvalue mark is not the same operation as changing
polynomial frames. For the actual meridian mu=-H, the inverse
eigenvalue M^(-1) corresponds to H-eigenvalue m^(-1). Its flag is

    z_-=-exp(-sT/2) sinh(s(1-T)/2)/sinh(sT/2) v.        (11)

For 0<lambda<1, z_- sends the north source pole to infinity
and the south pole to zero. Its projection degree is -1.
At lambda=1, for every 0<T<1, it equals z_+ and extends as
the smooth degree +1 map z_+=-exp(-pi*i T)v.

This difference consists of two explicit negative bubbles, not
a contradiction about the full meridian matrix, which extends.
To see this without a limiting stationary-phase argument, let

    u_lambda(T)=|z_-|^2/(1+|z_-|^2)
      =T sin^2(pi lambda(1-T)) /
       [T sin^2(pi lambda(1-T))+(1-T)sin^2(pi lambda T)].

For lambda<1 its endpoint values are u(0)=1,u(1)=0.
Pointwise in the interior u_lambda->T as lambda->1.
The pullback of the normalized flag sphere form is
du_lambda wedge dphi/(2pi). For any smooth test function,
angular averaging and integration by parts therefore prove
the weak-current identity

    z_-^*omega_flag -> omega_Gamma-delta_north-delta_south. (12)

For example, against a radial test h(T) the limit is exactly
integral_0^1 h(T)dT-h(0)-h(1). Dominated convergence applies
to u_lambda in [0,1], so it also proves (12) for general smooth
tests after angular averaging.

The local profiles fix both signs. For epsilon=1-lambda:

    v=epsilon zeta near north: z_- -> -1/bar(zeta),
    1/v=epsilon zeta near south: z_- -> bar(zeta).

Both are maps of degree -1 on their compactified bubble spheres.
Thus the inverse-eigenflag/source boundary survives in the frame
where the m-eigenflag is perfectly smooth. Switching marks must
carry the full source and peripheral character; merely equating
the two flags at the complete central eigenvalue loses (12).

## 5. Scope for the actual A-period

This supplies an exact finite quantum-factorial frame torsor and
a genuine principal compact-source map matching the moving-q
clock. Equations (10a)--(10f) give an exact finite star quantization
and identify its root restriction with the actual balanced frame.
They do not give a global continuation or quantum-geometric
pushforward of the internal knot component. The latter may
meet other critical branches.

The actual root-pivot K^(1-N) and ordinary integral-color pivot K
also differ offroot by K^(-N), with the accompanying twist factor.
The adapter is a weight-dependent whole clock, not a scalar.
It becomes scalar at the marked root; its normal jets do not.
The literature-defined invariant and all its factors remain fixed.

The [whole Gamma-source theorem](whole_gamma_frame_profile.md)
now also resolves the residual in (10d) on the scaled quantum
normal. Its middle-index factor is exactly a marked holomorphic
unit times the actual meridian Weyl half-adapter, with their
resonance zeros aligned by a specified parameter change. The
opposite Gamma profiles give the centered whole source character
H(z)=2sinh(z/2)/z. The
[regular-profile theorem](scaled_meridian_regular_profile.md)
retains that character and the unknown knot-dependent regular
coefficient, with uniform division through its resonance zeros.

Rivin's unique positive algebraic optimizer supplies the marked
classical branch. Equations (1)--(12) provide source and period
transport data near its shell. One still must prove that the
whole knot pushforward carries the original selected source to
that branch with its regulator norm. Neither uniqueness of the
critical shapes nor the smooth shear proves this statement.

Verification: [independent audit script](../experiments/audit_quantum_factorial_frames.py)
and [results](../experiments/quantum_factorial_frames_results.json).
The [independent proof audit](quantum_factorial_frames_independent_audit.md)
checks the whole frame function, metric rate, source normalization,
both bubbles and the exact finite star map, including its root phase.
