# A coarea audit of regular phase descent

28 October 2026. This proves the boundary-mass assertion needed in
Section 4 of [quantitative regular phase descent](quantitative_regular_phase_descent.md).
It does not estimate the exponential size of the boundary periods. In
particular, the boundary current below includes grazing curtains; its
support need not be contained in a single physical collar hypersurface.

## 1. Precise transport statement

Let C be a compact oriented piecewise smooth p-chain, with integer
multiplicities, in a recorded logarithmic chart. The same argument applies
to compact integral currents. Both M(C) and M(partial C) are assumed to
be exp(o(N)). Let phi be the actual phase and a its target value. Suppose
C lies in {rho<1}, where rho is a Lipschitz exhaustion and {rho<=2} is
contained in a legal regular chart. All actual quantum poles and all
chart seams which cannot be crossed are excluded from this chart.

On {rho<=2, phi>=a}, let X satisfy

    d phi(X)=-1.

Extend X to a globally defined smooth bounded vector field in a slightly
larger real chart. The extension is only a device for defining a complete
flow Phi_t; it must agree with X on the displayed region. Suppose, for
the available time T_N, that

    sup |X| <= B_N,  sup |DX| <= K_N,
    T_N=O(log^2 N),
    K_N T_N=o(N),

and that B_N, Lip(rho), and the first derivatives of phi on the initial
chain are exp(o(N)). In the application these are fixed powers of
L=N^epsilon, with epsilon sufficiently small. Define

    tau(z)=max(phi(z)-a,0),  0<=tau<=T_N,
    H(u,z)=Phi_(u tau(z))(z),  0<=u<=1,
    m(u,z)=max_(0<=v<=u) rho(H(v,z)).                  (1)

There is a level r in (1,2) for which the following currents are defined,
have mass exp(o(N)), and satisfy

    partial T_r = C_low,r - C - B_r + E_r.             (2)

Here T_r is the transported truncated cylinder, C_low,r is supported in
{phi<=a}, B_r is the transported side coming from the original boundary
partial C, and E_r is the complete exit-associated current. The image
of every term on the right lies in the legal closed window {rho<=r}.
Thus a closed p-form omega on that window obeys the exact identity

    integral_C omega = integral_(C_low,r) omega
                       + integral_(E_r) omega
                       - integral_(B_r) omega.        (3)

The orientation of B_r is specified below. When C is closed it is absent.
Formula (3) retains all relative boundary data; it is not a bound on the
last two integrals by their mass alone.

## 2. Running maxima and quantitative slicing

Orient S=[0,1] x C with du first. Then

    partial S = {1} x C - {0} x C - [0,1] x partial C.

The variational equation and differentiation of u tau(z) give a local
Lipschitz bound

    |DH| <= Lambda_N,
    Lambda_N <= const exp(K_N T_N)
                    (1+B_N(T_N+Lip(tau))).           (4)

All fixed powers of Lambda_N are exp(o(N)). The positive-part definition
of tau is Lipschitz and causes no difficulty. Bounds can equivalently be
read in local parametrizations and integrated with their multiplicities.

The running maximum in (1) is also Lipschitz. Indeed, write it as

    m(u,z)=max_(0<=v<=1) rho(H(vu,z)).

Every function in this maximum has the same local Lipschitz bound,
at most const Lip(rho) Lambda_N. The supremum inherits that bound. This
argument does not differentiate a maximizing time or a first-hit time.
Let Q_N be this bound. Coarea on the PARAMETER cylinder gives

    integral_1^2 M(<S,m,r>) dr <= Q_N M(S).            (5)

For almost every r, restriction to {m<r} is a finite-perimeter current
and its boundary is

    partial(S restricted to {m<r})
       = (partial S) restricted to {m<r} + <S,m,r>.   (6)

One may choose a common such r with

    M(<S,m,r>) <= 2 Q_N M(S).                         (7)

The harmless factor 2 leaves a positive-measure choice of levels; the
almost-everywhere current identities can therefore be imposed at the
same time. A finite collection of chains or charts is handled by applying
coarea to the sum of their unsigned slicing masses.

Define

    T_r     = H_#(S restricted to {m<r}),
    E_r     = H_#<S,m,r>,
    C_low,r = H(1,.)_#(C restricted to {m(1,.)<r}),
    B_r     = H_#(([0,1] x partial C) restricted to {m<r}).

The u=0 face is all of C because rho(C)<1. Equations (6) and the product
orientation give (2), including its minus sign on B_r. Pushforward
commutes with boundary. In particular, (2) includes the boundary of the
retained subset of the u=1 face; it is not permissible to discard it
separately.

For m(1,z)<r the entire trajectory up to tau(z) remains in the region
where the extension is the actual normalized descent. Consequently its
endpoint has phase a if phi(z)>a, and is unchanged with phase at most a
otherwise. This proves the stated support of C_low,r. Monotonicity of
m in u makes {m<r} an initial time interval in each fibre. There is no
re-entry ambiguity, even if the physical trajectory later re-enters the
window in the extended flow.

Finally, mass pushforward and (7) give

    M(T_r) <= Lambda_N^(p+1) M(S),
    M(E_r) <= 2 Lambda_N^p Q_N M(S),
    M(C_low,r) <= Lambda_N^p M(C),
    M(B_r) <= Lambda_N^p M(partial C).                (8)

These are bounds on parametrized currents WITH their multiplicities.
No inference from the size of an image set or from cancellation of its
parametrization is used. All quantities in (8) are exp(o(N)). Stokes
applied to the legal image of T_r proves (3).

## 3. Why the exit current includes curtains

It is in general false that E_r is supported on {rho=r}. A local model
is

    rho(H(t,z))=z-(t-t_0)^2.

For t>=t_0 its running maximum is z. At z=r, the parameter slice
{m=r} therefore includes the whole interval t>=t_0, although the
physical value of rho is strictly less than r after t_0. These portions
are grazing curtains in the boundary of the first-exit truncated
cylinder. Coarea bounds their mass together with all other slice pieces.

This distinction is essential. The construction proves controlled
regular transport into a low-action chain PLUS an exit-associated
current. It does not prove that this latter current has low action, or
that its contribution is determined by data on one collar hypersurface.
An additional estimate or an exact source cancellation is still required
for a sharp full-period upper bound.

## 4. Audit verdict

The saturation certificate and normalized-gradient estimates in Sections
2--4 of the root note support the interior transport assertion. Equations
(1)--(8) supply the missing coarea argument without a first-hit derivative
bound. They require a legal collar with the recorded derivative bounds,
and retention of the complete exit-associated and original-boundary
currents. No new general upper or lower volume bound follows from this
boundary-mass result alone.
