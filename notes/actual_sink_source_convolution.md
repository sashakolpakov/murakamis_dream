# Exact sink convolution and a growing actual trivalent source

28 October 2026. The ORIGINAL trivalent sink source has a finite
q-binomial polynomial, an explicit inhomogeneous central current,
and an exact balanced-residue/Barnes decomposition. The balanced
source has an exact POSITIVE norm ratio. This removes phase
cancellation from its magnitude, including geometric root lifts.
On a nonempty open boundary chamber its marked geometric rate
strictly exceeds the retained current rate, so the ORIGINAL sink
has that growing rate with a nonzero coefficient.

This is a local source theorem, for a literal original sink. No
claim is made that every vertex of a broad knot class lies in
the required gap chamber or that this proves its global volume
limit. The exact source-cycle construction and its infinite Barnes
bound are also developed in
[the companion beta theorem](actual_trivalent_quantum_beta_source.md).

The subsequent [exact Fermat normalizer](exact_balanced_source_normalizer_fermat.md)
fixes the entire central source function, not merely its magnitude.
It extends the growing-source rate and gap theorem below to the
ENTIRE positive boundary chamber, with norm-rate
max(0,log|u|,log|v|). Sections 4--5 retain the independent
elementary positive-norm proof on |u|<1.

## 1. The actual finite source, with every Q tag

Put Q=exp(2pi*i/N), d=N-1, F_a=(Q;Q)_a, and

    p_a=(-1)^a Q^(a(a-1)/2)/F_a,
    p_a^-=Q^a/F_a.

These are respectively the Psi_+ and Psi_- coefficients below
order N. At the original sink its U-diagonal, V-transfer and
positive-factorial orders satisfy h_0+h_4+h_2=d. Reflect the last
order: a=d-h_2=h_0+h_4. The ORIGINAL coefficients are then

    F_a * (1/F_(h_0)) * p_(h_4).

Consequently its two-boundary generating kernel is exactly

    B_N(u,v)=sum_(i+j<N) F_(i+j)/F_i * p_j u^i v^j
            =sum_(a=0)^d product_(j=0)^(a-1)(u-Q^jv).     (1)

For fixed a, the second equality is precisely the finite
q-binomial theorem. It retains EVERY boundary coefficient;
therefore it may be paired with the same arbitrary exterior
boundary functional, not just evaluated at a selected color.

For the reflected full-Psi field in
[the actual bipyramid note](positive_bipyramid_source_transport.md),

    F_N(L;U,V)=r^d Psi_-(Log U-L)
                       Psi_+(Log V-L)Psi_+(-L), r=exp L,

its first-jet Laurent constant is

    C_N(U,V)=sum_(i+j+k=d) p_i^- p_j p_k U^i V^j,
    NQ^d C_N(U,V)=B_N(Q^2U,QV).                            (2)

Indeed p_(d-a)=Q^(-(d-a))F_a/N. The remaining inner
q-binomial sum is the product in (1). Thus the actual tags are
u=Q^2U,v=QV, with NQ^d retained. Equivalently the original
reciprocal coefficient has its Q^(-1) tag and the reflected
factorial window its Q^(-1) tag. They have not been simplified
at Q=1. The companion relative moment theorem retains the
complete circle/outer-ray chain represented by (2), including
mixed individual-ray terms; (2) does not delete those terms.

Set P_a(u,v)=product_(j<a)(u-Q^jv). Its recurrence gives

    (u-v)B_N(u,Qv)=B_N(u,v)-1+u^N-v^N.                    (3)

The last term is P_N=u^N-v^N. The inhomogeneous source is
therefore the explicit central current

    D_N=1-u^N+v^N.                                        (4)

No homogeneous descent or scalar normalization is assumed.

## 2. Balanced nonvanishing and its exact positive norm ratio

Suppose u^N-w^N=1, uw!=0. Define

    p_a=product_(j<a)(u-Q^jw),
    r_k=w^(-k)product_(j<k)(u-Q^(-j)).

Then p_N=p_0=1, and the cyclic vector p satisfies

    p_(a+1)=(u-Q^aw)p_a.

For the UNNORMALIZED discrete Fourier transform

    p_hat_k=sum_(a=0)^d Q^(ka)p_a,

the recurrence becomes

    w p_hat_(k+1)=(u-Q^(-k))p_hat_k,
    p_hat_k=r_k B_N(u,w).                                  (5)

Every factor is nonzero: w!=0 and u^N-1=w^N!=0.
The Fourier transform is invertible, and p is nonzero. Thus

    B_N(u,w)!=0.                                          (6)

More quantitatively Parseval gives the exact identity

    |B_N(u,w)|^2
       =N * [sum_(a=0)^d |p_a|^2]/[sum_(k=0)^d |r_k|^2].   (7)

Both sums are strictly positive. This identity holds for ALL
root choices w and gives the entire magnitude, not merely
nonvanishing of a formal leading term. It is the appropriate
replacement for assuming that the finite oscillatory sum
selects its growing branch.

Fixed small logarithmic lifts can give polynomial Fourier
coefficients, as in the earlier Fermat source comparisons.
That estimate does not apply automatically to geometric lifts
whose logarithms or clock rotations grow with N. Section 4
uses (7) directly along those actual lifts instead.

## 3. Exact original source as a balanced residue plus its current

Use compatible logs in the chamber

    -pi<phi=Arg u<0,
    0<gamma=Arg(v/u)<pi,
    Log v=Log u+Log(v/u).

Write h=2pi*i/N, c=Log(v/u) and use the ORIGINAL full function

    g(a)=exp(a Log u) Psi_+(c)/Psi_+(c+ha).                  (8)

Its integer values are P_a(u,v). Off integers its exact norm
is VARIABLE:

    g(a+1)=(u-v exp(ha))g(a),
    g(a+N)=[u^N-v^N exp(2pi*i*a)]g(a).                     (9)

Replacing the second bracket by u^N-v^N off integers is false.

Put t=exp(2pi*i*a), lambda(t)=u^N-v^Nt and

    t_*=(u^N-1)/v^N,
    exp(2pi*i*alpha)=t_*, w=v exp(h alpha).

Assume first D_N!=0 and u^N!=1. The marked meromorphic form

    omega=2pi*i D_N * t g(a) da/[(t-1)(1-lambda(t))]        (10)

has residues P_k at integers k, EXACTLY the original source.
Its other poles alpha+k have residue -g(alpha+k). Their
monodromy is exactly one, and u^N-w^N=1. Thus their full
N-orbit residue is

    -R_N(u,v), R_N=g(alpha)B_N(u,w).                       (11)

This residue is nonzero. The marked full function in (8) is
regular and nonzero at c. Its denominator at alpha cannot
be a zero or pole: exp[N(c+h alpha)]=1-u^(-N) differs from
both zero and one at a regular parameter. Changing alpha
by an integer changes g(alpha) and the balanced B by inverse
factors in (5), so their product R_N is unchanged.

A finite rectangle of width N enclosing k=0,...,d and the
corresponding alpha-orbit gives, with all FOUR edges retained,

    B_N=R_N+(1/(2pi*i))integral_boundary omega.             (12)

The extra numerator t in (10) is important at the horizontal
ends. Choose the left vertical edge Re a=-epsilon, with
0<epsilon<N gamma/(2pi). The inverse full function has no
poles in this rectangle: Im(c+ha)>0. Its possible upper
Phi poles give zeros, not poles, of g. The full-function
asymptotics or its defining integral show both horizontal
ends of (10) vanish as their heights tend to infinity.
On paired vertical edges omega(a+N)=lambda(t)omega(a).
Their difference therefore gives EXACTLY

    B_N(u,v)=R_N(u,v)+D_N I_N(u,v),
    I_N=integral_(Re a=-epsilon,up)
                      g(a)/(exp(-2pi*i*a)-1) da.           (13)

All constants are fixed by residues; no knot period occurs
in a denominator. At D_N=0 the identity extends by the
matched limit: alpha may be chosen to tend to zero, w tends
to v, g(alpha) tends to one, and the finite source tends
to its nonzero balanced value. No central-norm denominator
is inverted there separately.

This is the same local Frobenius gluing as the original field.
Writing U_0=U^N=u^N,V_0=V^N=v^N, its multiplier-one internal
radius is

    r_crit^N=1/(1-t_*)=V_0/(1+V_0-U_0).                   (14)

Thus the balanced source in (11) lies on the ACTUAL central
gluing divisor; a free central normalization was not substituted.

On every compact subset of the above positive boundary chamber,

    |I_N(u,v)|<=C.                                        (15)

Here is the quantitative reason. Put a=-epsilon+iNy. The
full-Psi strip estimate, including its nonzero amplitude,
gives a leading logarithmic modulus profile with derivative

    R'(y)=-phi-Arg(1-(v/u)exp(-2pi*y)).

Uniformly, delta<=R'(y)<=2pi-delta. The denominator in
(13) is bounded below on this vertical line and supplies
exp(-2pi Ny) at the upper end. Thus the lower profile has
a uniform positive slope and the upper weighted profile a
uniform negative slope. Its amplitude grows at most exp(C|y|),
and g(-epsilon)=O(1). The measure is Ndy, so integration
against exp(-delta N|y|) is O(1). The finitely many small N
are bounded by continuity and the same absolutely convergent
tails. This proves (15), with every boundary current retained.
The companion beta theorem supplies the fuller contour and
continuation details; the finite-height audit checks (12).

## 4. Uniform balanced growth on a genuine geometric lift chamber

Now suppose additionally 0<rho=|u|<1. Take a compact subset
of this chamber, bounded away from rho=0,1 and its angular
ends. Choose alpha in any fixed width-one real interval.
Then uniformly

    w=v exp(h alpha)=exp(i Arg v)(1+O(1/N)),
    |w|=1+O(rho^N/N).

Let I_rho(theta)=Im Li_2(rho exp(i theta)) and
theta_rho=acos(rho/2). Elementary uniform product Riemann
sums give, for x=a/N or k/N,

    log|p_a|=N P(x)+O(1),
    P(x)=integral_0^x log|u-exp(i Arg v+2pi*i*t)|dt,

    log|r_k|=N Qprof(x)+O(1),
    Qprof(x)=integral_0^x log|u-exp(-2pi*i*t)|dt.

Every factor is bounded away from zero since rho<1. The
O(1) is uniform in ALL indices; there is no fixed-small-log
assumption or omitted rotated endpoint. Positive Laplace
bounds and (7) consequently give

    log|B_N(u,w)|=N(max P-max Qprof)+O(log N).              (16)

Both maxima can be computed directly. The common periodic
derivative is log|1-rho exp(i theta)|, of zero mean, with
zeros at theta=+/-theta_rho. The maximizers are its
positive-to-negative transitions. Their antiderivative is
-I_rho(theta). Hence

    max P=[I_rho(gamma)+I_rho(theta_rho)]/(2pi),
    max Qprof=[I_rho(phi)+I_rho(theta_rho)]/(2pi),

    max P-max Qprof=[I_rho(gamma)-I_rho(phi)]/(2pi)>0.      (17)

The second maximizer may lie near either end of the period;
both positions give the SAME formula. Omitting one of these
periodic possibilities would give an incorrect exponent.

The full-Psi estimate in (8), with its actual logarithms,
also gives

    log|g(alpha)|=N G(u,v)+O(1),
    G=[-phi log|v|+ImLi_2(v/u)
                   -ImLi_2(exp(i gamma)/rho)]/(2pi).

Inversion in the upper half-plane gives

    ImLi_2(exp(i gamma)/rho)
       =I_rho(gamma)+log(rho)(gamma-pi).

Combining with (16)--(17) proves the explicit rate theorem

    log|R_N(u,v)|=N Lambda(u,v)+O(log N),

    Lambda=[ImLi_2(v/u)-ImLi_2(u)
              +(pi-gamma)log|u|-phi log|v|]/(2pi).         (18)

The integer/affine mark in (18) is essential. For example it
is the imaginary part, divided by 2pi, of

    W=Li_2(v/u)-Li_2(u)+1/2 Log(u)^2
                              -Log(u)Log(v)+pi*i Log(u).  (19)

It cannot be discarded as a central factor with limit one.

## 5. An open local class where the ORIGINAL sink grows geometrically

Let delta_norm=max(0,log|v|). Equation (4) gives
|D_N|<=C exp(N delta_norm) on the present rho<1 chamber.
Suppose a compact family has the explicit strict gap

    Lambda(u,v)>=delta_norm+eta, eta>0.                   (20)

Equations (13), (15), and (18) then prove

    B_N(u,v)=R_N(u,v)[1+O(N^C exp(-N eta))],
    log|B_N(u,v)|=N Lambda(u,v)+O(log N).                  (21)

This is noncancellation of the ORIGINAL local source. Its
balanced contribution has coefficient exactly one, and its
remaining original current is exponentially smaller under
the stated checked inequality. No complex phase of the
oscillatory sum was assumed to be nonzero.

The exact source normalizer now proves the same Lambda formula
for all |u|, including |u|=1. In that extension replace
delta_norm by max(0,log|u|,log|v|); the compact gap and relative
error statement are otherwise unchanged. Its proof is the
explicit two-full-Psi source formula, not extrapolation of
the nonsingular product sums of Section 4.

All bounds are uniform for N-dependent parameters staying in
the indicated compact chamber. In particular the ACTUAL tags
u_N=Q^2U,v_N=QV from (2) are allowed whenever U,V belong to
a compact gap family: for large N they stay in a slightly
larger such family. Smoothness gives
Lambda(u_N,v_N)=Lambda(U,V)+O(1/N). The factors NQ^d in
(2) remain in the exact source; their magnitude adds log N
to a logarithmic rate rather than being reset.

The class is nonempty and open. If |v|=1, then G=0 and

    Lambda=[I_rho(gamma)-I_rho(phi)]/(2pi)>0,

because gamma is upper and phi lower. Every compact family
therefore has a positive gap, which persists in a full open
neighborhood by continuity. For example u=0.7-0.4i and
v=0.9+0.2i have Lambda approximately 0.191315 and norm-rate
zero. A certified neighborhood follows from continuity;
the theorem itself uses the explicit inequality (20), not
that numerical example.

There is also a literal unique regular critical action.
The finite product's analytic action is

    W_source(s)=Li_2(v/u)-Li_2((v/u)exp s)+s Log u.

Its stationary equation is u-v exp s=1. The marked solution
is s_*=Log(1-u)+pi*i-Log v, with 0<Im s_*<2pi.
Its second derivative is 1-u!=0. The elementary Euler and
quad dilogarithm identities give

    W_source(s_*)=W+pi^2/6.

Thus (18) is precisely this marked geometric critical
rate, not an unrelated estimate on a maximum. The real
constant has been recorded; no arbitrary complex period
normalization is chosen to achieve the identity.

## 6. Scope and audit

Equation (1) is a polynomial kernel identity, valid with
every original exterior functional. Equations (13)--(21)
give a local analytic growing-source theorem on a specified
open chamber. To use it for an entire knot, one must prove
that its actual positive-chart transport places the needed
internal fibers in this chamber, control their joint exterior
cycle, and retain all other source currents. Those global
hypotheses have not been established for a broad knot class.
No whole-knot volume conjecture follows from the present note.

The [audit](../experiments/audit_actual_sink_source_convolution.py)
checks the original coefficient/tag identity, central current,
balanced nonvanishing, full-Psi VARIABLE monodromy, all four
finite contour edges, exact Parseval ratio and representative
growing-source comparisons. The uniform proofs above do not
infer their all-level statements from finite checks.
