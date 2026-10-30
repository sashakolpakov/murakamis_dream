# The original physical operator kernel and its positive anti-diagonal packet

30 October 2026. The actual pivotal reshuffle turns an anti-diagonal
entry of the completed exceptional Casimir polynomial into the squared
modulus of ONE original ordinary column, with an explicit positive
factor. The same exact identity factors every entry within its bandwidth
into two ordinary columns. It supplies a literal holomorphic root-kernel
continuation and its nonzero relative amplitude. Both level parities
are included, without a spectral contour argument. The surrounding
coherent contraction and its global selected frame remain additional
requirements; genuine q normals are bounded here only at physical rows.

## 1. Exact original root identity

Put d=N-1, q=exp(pi i/N), s_n=product_(r=1)^n 2sin(pi r/N),
and 0<=a<=floor(d/2). Let J_t be the ORIGINAL physical Casimir block
in total degree 0<=t<=d, in its original order u=0,...,t. Let p_a be
the [original exceptional polynomial](actual_matching_edge_geometric_target_polynomial.md).
Choose u<=v with u+v=t and set h=v-u. If h>a, then

    [p_a(J_t)]_(u,v)=0.                              (1)

If 0<=h<=a, write f_(d-h,a)(u) for the original normalized physical
column with first entry one, in degree d-h and compiler channel a.
Then the exact finite identity is

    [p_a(J_t)]_(u,v)
       =s_(a+h)/(s_h^2 s_(a-h)) |f_(d-h,a)(u)|^2.    (2)

No projectors or target channels have been discarded in (2). The
polynomial is the completed operator, including its root nilpotent
parts. The root face factor is D_a(q)=1. The opposite anti-diagonal
entry equals (2), since the original root J_t is symmetric under
transpose. The high physical total uses the already proved exact
generic translated adapter, and hence the same formula in its low
coordinates.

Here is the full source and phase proof. Use the actual maps of the
[completed projector theorem](actual_matching_edge_completed_projector_block.md):

    B(K)_(a,b,c,e)=K_(a,b;d-e,d-c) pV(d-e)pV(d-c),
    (R Psi)_(a,b,c,e)=s(a) Psi_(b,c,e,a),
    s(j)=(-1)^d q^(d-2j), A=B^-1 R B.

In the first line pV(j)=pV(j,d-j), and dummy outside labels are
unrelated to the channel a. Direct inversion, retaining the nested
cup order, gives for every physical operator K

    (A^-1 K)_(a,b;x,y)
      =s(d-x)^-1 pV(d-b)/pV(x)
                          K_(d-x,a;y,d-b).           (3)

The original measure cancellation is h0_a K_a=k_a N A p_a(Omega),
where h0_a=k_a N s_(2a)/s_a^2 and K_a=W_a pi_a. On the chosen
anti-diagonal, (3) therefore gives

    [p_a(J_t)]_(u,v)
       =s_(2a)/s_a^2 s(d-v)^-1 pV(d-v)/pV(v)
                           K_a(d-v,u;u,d-v).          (4)

At the root the actual physical cup is

    pV(j)=N q^(-d^2+dj).

Consequently s(d-v)^-1 pV(d-v)/pV(v)=1 EXACTLY: its remaining
exponent is N(d-2v), and its sign cancels (-1)^d. The original white
map, in channel row r=a-h, is

    pi_a(r;x,y)=G_(a,r)^-1 conjugate(W_a(y,x;r)),
    G_(a,r)=s_(2a)/(s_r s_(2a-r)).

Thus (4) is s_(a-h)s_(a+h)/s_a^2 times
|W_a(d-v,u;a-h)|^2. The channel row is absent if h>a, proving
(1) independently of polynomial bandwidth.

When h<=a, this Clebsch column has low degree d-h. Its actual
first endpoint has modulus s_a/(s_h s_(a-h)). The root reflected
recurrence gives |f_(d-h,a)(d-v)|=|f_(d-h,a)(u)|, because those
two indices add to d-h. Substitution proves (2). In particular
d-h>=d-a automatically lies in the original complete-column range;
no unsupported ordinary formula at a different degree is invoked.

## 2. A uniform nonzero relative operator amplitude

Write the ACTUAL scaled parameters

    alpha=a/N, delta=h/N, nu=u/N,
    tau_prime=(d-h)/N=1-delta-1/N.

Consider any fixed compact inside

    0<delta<alpha<=1/2, 0<nu<(1-delta)/2.            (5)

As usual alpha denotes an admissible discrete sequence; its endpoint
1/2 is interpreted by the actual folded sequences a/N. Physical
u+v<=d is retained. The transformed ordinary arguments stay in a
fixed compact of the full physical tube, since tau_prime>1/2 and
0<nu<tau_prime. The original total (u+v)/N may be BELOW 1/2.

The proved [ordinary full-domain packet](actual_q_hahn_full_physical_complex_packet.md)
has the actual, nonzero amplitude B_alpha and phase Phi_alpha:

    f_(d-h,a)(u)=N^-1/2 B_alpha(tau_prime,nu)
          exp[N Phi_alpha(tau_prime,nu)](1+O(N^-1)).

Equation (2) now gives directly

    [p_a(J_t)]_(u,v)
      =s_(a+h)/(N s_h^2 s_(a-h)) |B_alpha(tau_prime,nu)|^2
         exp[2N Re Phi_alpha(tau_prime,nu)](1+O(N^-1)).           (6)

The error is uniform on (5), and the leading factor is positive
and nonzero. Both integer offsets remain in tau_prime and in B;
there is no replacement of tau_prime by 1-delta inside the
N-scaled exponential.

For an entirely smooth amplitude, put
J(x)=integral_0^x log(2sin(pi s)) ds. The uniform sine-factorial
formula s_(Nx)=sqrt(2N sin(pi x)) exp[N J(x)](1+O(N^-1))
on compact subsets of 0<x<1 rewrites (6) as

    [p_a(J_t)]_(u,v)=N^-2 C_alpha(delta,tau_prime,nu)
                         exp[N H_alpha(delta,tau_prime,nu)]
                         (1+O(N^-1)),                         (7)

    H_alpha=J(alpha+delta)-2J(delta)-J(alpha-delta)
                         +2Re Phi_alpha(tau_prime,nu),
    C_alpha=|B_alpha(tau_prime,nu)|^2/(2sin(pi delta))
                     *sqrt(sin(pi(alpha+delta))/sin(pi(alpha-delta))).

All scalar arguments in (7) remain strictly between zero and one
on the stated compact. This is an actual local matrix-entry
asymptotic, rather than a scalar-symbol substitution or a spectral
stationary-phase conjecture.

## 3. Genuine q jets come from the generic reshuffle

One MUST NOT differentiate the absolute square in (2). The original
generic identity is instead

    p_a(Omega)=D_a/(rho_a beta_N) B^-1 R^-1 S_(2a),
    S_(2a)=W_a p_(2a) W_a^T.                         (8)

Every anti-diagonal entry of the right side has exactly ONE channel
row r=a-h and its complement 2a-r. The two Clebsch entries, original
ordinary cup, physical inverse cups, turn, and scalar in (8) retain
their genuine q dependence. There is no sum in this entry which
could hide cancellation between exponentially larger summands.

The [physical all-q-jet theorem](actual_q_hahn_physical_generic_jet_bound.md)
bounds each fixed jet of the normalized physical columns by a
polynomial times its root modulus. Their original Clebsch endpoint
factors and the cups in (8) are root-unit products with harmonic
logarithmic derivative bounds. The generic high adapter is exact,
so it applies to the second, high-degree Clebsch entry as well.
The scalar D_a/(rho_a beta_N) is a nonzero canceled root-unit product;
its fixed relative jets have polynomial cost by the original
normalization theorem.

Therefore, for each fixed m, on (5) there are constants C_m,L_m
independent of the physical labels and level parity such that

    |partial_epsilon^m [p_a(Omega(q exp(epsilon)))]_(u,v)|_0
          <=C_m N^L_m [p_a(J_t(q))]_(u,v).            (9)

All derivatives in (9) include the q dependence of the polynomial
AND of the original matrix. The completed face-normalized operator
has the same bound. This is an upper bound for genuine normals,
not their nonzero amplitude. The analogous entry remains
identically zero outside |u-v|<=a at generic q, by bandwidth.

## 4. The entire physical kernel, with its original phase

The same proof also gives every entry. Let 0<=u<=v<=t<=d,
h=v-u, and 0<=h<=a. Then

    [p_a(J_t)]_(u,v)
      =q^[-d(t-u-v)] s_(a+h)/(s_h^2 s_(a-h))
             *conjugate(f_(d-h,a)(u)) f_(d-h,a)(t-v).           (10)

Here (3) uses the original entry
K_a(d-v,u;t-v,d-t+u), in degree d-h. Its white reversal gives
W_a(d-v,u) times conjugate(W_a(d-t+u,t-v)), divided by the
same G_(a,a-h). The root reflected recurrence is

    f_(d-h,a)(d-h-r)=f_(d-h,a)(d-h)
                                      conjugate(f_(d-h,a)(r)).

The two endpoint factors cancel because the final normalized endpoint
has modulus one. The remaining cup and turn ratio in (3) is exactly
q^[-d(t-u-v)]. This proves (10), including its phase. Entries below
the diagonal follow by transpose symmetry of the ROOT J_t.

Both arguments u and t-v are actual physical arguments in the same
complete column. The generic tensor corresponding to (10) still has
only one channel row. Consequently the genuine-jet bound (9) holds
for every strict physical entry covered below, with the positive
right side replaced by the modulus of (10). This uses (8), not
differentiation of the conjugation or root reflection in (10).

There is a useful finite product for its entire scalar. The exact
root identity s_h s_(d-h)=N gives

    s_(a+h)/(s_h^2 s_(a-h))
       =P_(N,a)(h)
       :=N^-1 product_(r=1)^(d-a) 2sin[pi(h+r)/N]
                *product_(r=1)^a 2sin[pi(h+r)/N].               (11)

For h<=a, cancel the two products using
s_(d-a+h)=N/s_(a-h). For each physical integer a<h<=d, the first
product instead contains its factor with h+r=N, hence vanishes.
Thus (11) is a literal finite entire function, not an interpolation
inferred from the leading sine-factorial rate.

## 5. A source-matching complex root kernel and relative amplitude

Use independent scaled variables delta,nu,lambda, corresponding on
the physical grid to

    h=N delta, u=N nu, t-v=N lambda,
    v=N(nu+delta), t=N(nu+lambda+delta).

For fixed actual alpha=a/N, take compact subsets of the convex tube

    0<Re delta<alpha, Re nu>0, Re lambda>0,
                       Re(nu+lambda+delta)<1.                   (12)

The channel remains an integer. Put tau_prime=1-delta-1/N.
For all large N, (tau_prime,nu) and (tau_prime,lambda) lie in
fixed compacts of the proved full physical ordinary tube. If fhat
denotes that ORIGINAL finite continuation, define

    fhat_a^#(tau,nu)=conjugate(fhat_a(conjugate(tau),conjugate(nu))),

where fhat_a(tau,nu) is understood to have the scaled arguments
(Nnu,N(tau-nu)). This is a holomorphic function, not pointwise
conjugation at complex arguments. Define the finite root kernel

    K_(N,a)(delta,nu,lambda)
      =exp[-pi i(N-1)(lambda-nu)] P_(N,a)(N delta)
            fhat_a^#(tau_prime,nu) fhat_a(tau_prime,lambda).      (13)

Equation (10) proves EXACT equality with the original physical
matrix entry at every grid point in (12). All factors of (13)
are explicit original finite functions or the finite product (11).
No noninteger target channel or arbitrary interpolation is used.
For large N the ordinary factors are nowhere zero on these compacts.
Every sine argument in (11) has real part strictly between zero
and one there, so the scalar is nonzero as well.

Let J be the holomorphic continuation of the real primitive of
log(2sin(pi z)) in 0<Re z<1. Use the branch real on (0,1).
Write Phi_alpha^# and B_alpha^# with the same holomorphic-conjugate
convention. Put

    H=J(alpha+delta)-2J(delta)-J(alpha-delta)
         +Phi_alpha^#(tau_prime,nu)+Phi_alpha(tau_prime,lambda)
         -pi i(lambda-nu),
    C=exp[pi i(lambda-nu)] B_alpha^#(tau_prime,nu)
            B_alpha(tau_prime,lambda)/(2sin(pi delta))
             *sqrt(sin(pi(alpha+delta))/sin(pi(alpha-delta))).   (14)

The square root is its positive real branch continued on (12).
Then the ACTUAL finite function (13) satisfies

    K_(N,a)=N^-2 C exp(N H)(1+O(N^-1)).             (15)

The amplitude is holomorphic and nowhere zero. The relative error
and all its fixed derivatives are uniform on smaller compacts.
The actual value alpha=a/N and the offset tau_prime=1-delta-1/N
are retained throughout (14),(15).

For completeness, no complex factorial interpolation is needed to
prove the scalar part. Apply the elementary trapezoidal estimate
to the TWO literal sums of log sine in (11). The first upper index
is d-a=N(1-alpha)-1; the second is a=N alpha. Their integrals add
to J(alpha+delta)-2J(delta)-J(alpha-delta), using
J(1-z)=-J(z). Their endpoint terms give exactly

    P_(N,a)(N delta)
      =N^-1 sqrt(sin(pi(alpha+delta))/sin(pi(alpha-delta)))
                   /(2sin(pi delta))
        *exp{N[J(alpha+delta)-2J(delta)-J(alpha-delta)]}
                                            *(1+O(N^-1)).

All derivatives of the summands are bounded on the compact enlarged
strip, so the error is uniform and holomorphic. Multiplying the TWO
proved actual ordinary packets proves (15), with its exact monomial
phase. The real anti-diagonal formula (7) is its lambda=nu slice.

This complex continuation is for the ROOT kernel. It does not by
itself continue the genuine generic-q normals of (8) to complex
magnetic rows, nor identify (13)'s branch at a particular geometric
frame. Those are separate requirements.

## 6. What this does and does not resolve

The anti-diagonal completed operator has a source-exact positive
formula and its own nonzero relative local packet. In this chamber
one no longer needs to prove that a chosen off-spectrum saddle
contributes merely to compute this individual matrix entry.

An arbitrary surrounding tensor is not anti-diagonal. Placing the
actual geometric boundary data in these coordinates, matching its
selected action and derivatives, and proving the coherent global
contraction still require their own arguments. Nor does the
root positivity in (2) replace the original whole-network first
normal by a positive root-value state sum. In particular, compatibility
of a local real target frame with the selected frame on every other
original factor is not supplied by this kernel identity.

The [exact global tube obstruction](actual_matching_edge_kernel_tube_geometric_obstruction.md)
makes this limitation concrete. Under the presently used global
shaded-exterior flags and controlled ordinary complement, undoing the
actual turn maps all of (12) back to two strictly physical original
factors. The resulting all-physical frame is excluded by the proved
white-normal obstruction. Thus this valid root-kernel packet does NOT
contain that prescribed global geometric point. A larger continuation
domain, another coupled grouping, or an exact local frame-transition
construction is still required.

Focused audit: [original matrices, generic tensor jets and actual complex
kernel amplitudes](../experiments/audit_actual_matching_edge_antidiagonal_operator_packet.py).

Primary-agent full analytical review: PASS. The reader checked the exact
original reshuffle, cup/turn phases, white-map square, complete-column
support, retained integer offsets and genuine generic single-term
tensor, then the full entry formula, finite entire sine product,
holomorphic conjugate, exact trapezoidal endpoints and complex root
amplitude. Complex generic normals and global geometric membership
remain excluded as stated.

Independent full analytical review of sections 1--6 and fresh focused
replays: PASS. The reader reproduced 175 anti-diagonal generic tensor
four-jets, 460 positive-square identities and 510 four-jet bandwidth
zeros, followed by 2,901 general original entries, 430 all-entry generic
tensor four-jets and 268 finite scalar products. Twelve anti-diagonal
amplitudes at 140 digits and twelve real/complex kernel amplitudes with
24 independent literal-source comparisons at 160 digits also passed.
The review distinguishes the root complex packet from genuine q normals
at complex rows, and from a global geometric selected-frame assertion.
