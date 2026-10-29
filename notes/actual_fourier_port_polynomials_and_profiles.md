# Exact physical port polynomials and global conditional angular profiles

28 October 2026. The ORIGINAL four-full-Psi crossing has exact
finite-band Laurent-polynomial interpolants in each port, while the
other three ports stay on their specified correlated grids. These
are the actual finite Fourier interpolants, with their entire source
normalization fixed by a known local kernel entry. Their apparent
full-Psi poles cancel after the exact fixed-grid period factors and
integer aliases are retained.

This proves a nonzero analytic symbol for a single actual finite
Fourier adapter on a compact positive crossing chart. It also gives
the unique GLOBAL angular modulus maximum on the whole conditional
port circle. It does not justify moving several unrelated ports
simultaneously or suppressing a whole knot's boundary sectors.

## 1. Actual kernel, grids, and the two integer chamber labels

Use the EXACT original operator and source of
[the balanced Fourier theorem](actual_balanced_fourier_crossing_kernel.md).
Write q=exp(pi*i/N), Q=q^2, h=2pi*i/N, d=N-1, x=-q^(-1),
X=pi*i-h/2. The marked grids have

    z0=r0 Q^i, z1=r1 Q^j,
    z6=x r1 Q^k6, z7=x r0 Q^l,
    r0^N=A, r1^N=B, A B(B-x^N A)!=0.

Retain a,b,c,d0 for their logarithms and define

    k=the representative of l-i modulo N in {1,...,N},
    m=the representative of k6-j modulo N in {1-N,...,0}.

Choose the corresponding matched logarithmic lifts so that
d0-a-X=k h and c-b-X=m h. The whole-turn characters are one
at the original balanced grids, so this does not change M or
discard its compensating central factors.

The positive octahedral chamber has

    1<=k<=N-1, 2-N<=m<=0.                              (1)

Indeed its positive angle sums are, up to the recorded half-step,
theta1+theta3=2pi*k/N and
theta2+theta3=2pi*(N+m-1)/N. These are both between zero and 2pi.
The EXACT polynomial statements hold for all those cyclic
representatives, including k=N and m=1-N. Only the positive-chart
estimates need the strict ranges in (1).

Let M be the actual normalized Fourier matrix entry, including
its original kappa and every fixed central factor. It is explicitly
the four-full-Psi expression (14) of the linked theorem; every grid
entry is nonzero on its regular torus.

## 2. The exact ORIGINAL finite-band interpolants

Write (v;Q)_L=product_(r=0)^(L-1)(1-Q^r v).
For a single variable Z and all other ports fixed on the ORIGINAL
grids, define the following Laurent polynomials:

    P0(Z)=Z^m (z1/(xZ);Q)_(N+m-1),
    P1(Z)=(Q^(k+1)x z0/Z;Q)_(N-k),
    P6(Z)=Z^(N-k)(Q^(1-k)Z/z0;Q)_(k-1),
    P7(Z)=(Q^m Z/(x z6);Q)_(-m).                       (2)

P0 and P7 use m in {1-N,...,0}; P1 and P6 use k in {1,...,N}.
They have the exact physical spectra

| Port | Powers | Physical frequency indices |
| --- | --- | --- |
| input z0 | negative | -m,...,N-1 |
| input z1 | negative | 0,...,N-k |
| output z6 | positive | N-k,...,N-1 |
| output z7 | positive | 0,...,-m |

Every coefficient inside the stated interval is nonzero. Each
interval is contained in the ORIGINAL head band 0,...,N-1.

Choose any fixed grid value Z_* for the port under consideration.
Then its exact original Fourier interpolation is

    g_port(Z)=M(Z_*) P_port(Z)/P_port(Z_*).              (3)

This preserves the full ORIGINAL scalar. M(Z_*) is a known explicit
local four-full-Psi value, not an unknown knot period. P_port(Z_*)
is nonzero since its root central argument is not one. No new
normalization is introduced by (3).

Equation (3) agrees with M at EVERY old grid point. Since its
physical frequency interval lies in 0,...,N-1, finite Fourier
uniqueness makes it the actual original finite-band interpolation.
It therefore holds for every complex nonzero Z, with no omitted
residues or approximate projection.

At the two cyclic endpoint cases the table is literal: k=N
gives P1=1 and P6 of degree N-1; m=1-N gives the input
monomial P0=Z^(1-N) and P7 of degree N-1. There is no
degree-N norm polynomial substituted for a constant grid row.

## 3. Full-function proof, including every period and alias factor

In the exact kernel use

    beta=b-a-X, f=d0-c-X, rho=c-a,
    lambda=d0-b+2pi*i, G=d0-a-X, J=b-c+X.

Its full-function part is
Psi(beta)Psi(h-f)Psi(lambda+2pi*i+h)/Psi(rho).
First use the EXACT whole-turn identity

    Psi(lambda+2pi*i+h)
       =Psi(h+d0-b)/(1-exp[N(d0-b)])^2.                 (4)

On the old grids exp[N(d0-b)]=x^N A/B, and
R=exp(Nrho)=x^N B/A. Thus the central density
R(1-R)^2 in kernel (14), divided by (1-1/R)^2 from (4),
is exactly R^3. For interpolation, these are the fixed old-grid
constants. They are retained in the normalizer in (3).

This qualification matters: substituting a moving Z into the RAW
four-Psi expression changes those Nth powers. That meromorphic
continuation is generally NOT the finite Fourier interpolation.
For example (4) creates moving double poles at (z7/Z)^N=1;
they are absent from the polynomial (3). No contour is moved
across such artificial poles by the present theorem.

For input z0, rho-beta=c-b+X=(N+m-1)h. Hence

    Psi(beta)/Psi(rho)=(exp beta;Q)_(N+m-1).

The exact Gaussian in kernel (14) has a-dependent power exp(m a).
This gives P0 after the fixed central factors are retained.

For input z1, beta+(d0-b)=G=kh. Full inversion gives

    Psi(beta)Psi((k+1)h-beta)
       =zeta exp[pi*i*(sqrt(N)beta/(2pi)-c_b)^2]
              *(Q^(k+1)exp(-beta);Q)_(N-k).

Combining its Gaussian with the ORIGINAL kernel Gaussian leaves
exp(-N beta), times a factor independent of b. On the old grid
exp(-N beta) is a known fixed central scalar. Retaining that
scalar gives precisely P1. This is the integer alias +N b;
it is compensated by its known old-grid value.

For output z6, h-f=rho+(1-k)h, so

    Psi(h-f)/Psi(rho)=(Q^(1-k)exp rho;Q)_(k-1).

The original Gaussian power is exp[-(N+k)c]. Its fixed-grid
alias exp(-2N c) is retained as a central scalar, leaving
exp[(N-k)c] and giving P6.

For output z7 put t=h-f. Then

    t+(h+d0-b)=(N+m+1)h.

The same full inversion gives a polynomial of length -m,
with argument Q^m z7/(xz6). Its Gaussian combines with
the original one to give exp(3N d0), independent of the
remaining polynomial. This is again a known old-grid
central scalar and gives P7.

All displayed Gaussian cancellations are exact, including
the affine logarithmic marks and half-step in X. Thus the
integer aliases +N b,+2N c,-3N d0 are NOT discarded phases:
their known central values are in (3). Nonzero coefficients
in (2) follow from the finite q-binomial theorem, since all
factorial indices in its lengths are less than N.

There is also a genuine TWO-port result. With b,c fixed on
their original grids, the physical interpolant factors exactly:

    M_interp(Z0,Z7)=M(z0_*,z7_*)
          *P0(Z0)P7(Z7)/[P0(z0_*)P7(z7_*)].            (3a)

With a,d0 fixed, the analogous formula uses P1(Z1)P6(Z6).
To prove this, kernel (14) on the original grids separates
into an a-only factor times a d0-only factor when b,c are
fixed: its Gaussian has no a*d0 term, and its full functions
and central factors split. The other pair splits likewise.
Every two-by-two conditional minor is zero. Tensor-product
finite Fourier uniqueness then proves (3a) for BOTH free
complex variables, with the complete original scalar.
This is a paired polynomial identity, not the assertion
that the raw four-Psi formula is the same off-grid function.

### The pair scalar is explicit and tame

The reference value in (3a) can be eliminated altogether.
Use the [uniform signed role table](actual_signed_overbridge_unwinding.md)
and write the paired kernel as c_sigma Pout Pin, with the
physical over/under clock h in 0,...,d used there. Then

    c_(+,over)=kappa/N *(-1)^h Q^(h(h+1)/2) z6^h,
    c_(+,under)=kappa/N *(-1)^h Q^(h(h+1)/2) z0^(-h),
    c_(-,over)=kappa^(-1)/N
                         *(-1)^h Q^(-h(h+1)/2) z7^h,
    c_(-,under)=kappa^(-1)/N
                         *(-1)^h Q^(-h(h+1)/2) z1^(-h). (3b)

These retain the ENTIRE original crossing scalar and phase.
Their magnitudes lie between c_K/N and C_K/N on fixed
nonzero central compacta, uniformly in every spectator label
and h. Their explicit Gaussian and monomial phases can still
carry a leading oscillatory action; tameness is not positivity.

Here is an independent all-level proof directly from ORIGINAL
coefficients. For the positive over-pair extract over-input
physical frequency h and over-output frequency zero. Since the
chosen Pin starts with Z^(-h) and Pout with 1, this coefficient
is exactly c. The original sparse crossing gives

    c=kappa/N^2 z6^h F_h
          sum_(t=0)^(d-h) [h+t choose t]_Q Q^(-ht).

Root complementation turns its summand into
(-1)^t Q^(t(t+1)/2)[d-h choose t]_Q. The finite q-binomial
theorem makes that sum F_(d-h). Finally

    F_h F_(d-h)=N(-1)^h Q^(h(h+1)/2).

This proves the first line. For the positive under-pair
extract input frequency zero and output frequency h; the
same original coefficient sum appears, multiplied by z0^(-h).
The exact negative mirror conjugates kappa and Q and swaps
ports, proving the other lines. Reversing a Q^(-1) product
only reorders its factors and introduces no further scalar.
All steps hold for even and composite levels as well.

This improves merely specifying the scalar by a known local
value: no hidden exponential magnitude is left in the pair
normalization. It also fixes the normalization of every
source-preserving bridge contraction in the linked theorem.

## 4. Actual adapter action and a nonzero analytic symbol

For an outgoing positive-band port the exact finite adapter
F(r')F(r)^(-1) acts on the sampled polynomial by

    g(r Q^j) -> g(r' Q^j).                             (5)

For an incoming port the inverse/contravariant adapter has
the same evaluation statement with the matching direction
and the negative powers in (2). This is finite Fourier
interpolation, not a formal pseudodifferential assertion.

Take r'/r=exp(delta/N) with delta in a fixed compact set.
On a compact positive octahedral chart every factor in the
corresponding Pochhammer arc stays uniformly away from zero.
The arc connects two nonreal positive-orientation endpoints
without crossing 1. Its length is at most N. Thus

    log[g(Z exp(delta/N))/g(Z)]
       =delta p_port(Z)+O_K(1/N),
    p_port=(1/N) Z partial_Z log P_port.                (6)

The estimate is uniform, with derivatives: the second
logarithmic derivative of each factor is bounded, so the
sum of N such derivatives is O_K(N). Equation (6) follows
by Taylor expansion through a displacement delta/N.
Ordinary Riemann sums on the zero-free arc give p_port's
explicit classical limit with another O_K(1/N) error.
The resulting adapter symbol is exp(delta p_port), nonzero
and bounded above and below on compact data.
The sign convention in (6) is the Laurent power of the
kernel: physical incoming momentum is -p_port, whereas
physical outgoing momentum is +p_port.

The REAL parts of its physical incoming/outgoing momenta,
after the just-proved fixed aliases, are

    p_in,0=1-(theta2+theta3)/(4pi),
    p_in,1=1/2-(theta1+theta3)/(4pi),
    p_out,0=1-(theta1+theta3)/(4pi),
    p_out,1=1/2-(theta2+theta3)/(4pi).                  (7)

Every one belongs to (0,1), uniformly away from its ends
on every compact positive chamber. At the regular octahedron
they are (3/4,1/4;3/4,1/4). This agrees with the ORIGINAL
finite-head indices, not an independently selected wave packet.

Equivalently, the exact global linear alias of the original
action is 2pi*i(b+2c-3d0), with inverse scalar compensation
by exp[-N(b+2c-3d0)]. On the original grids this scalar is
known and bounded for fixed central data. Its derivative
puts all four momenta in the physical band without changing
any actual matrix value or original source.

## 5. Unique GLOBAL fixed-port angular maxima

Assume additionally |A|!=|B|, as in the fixed regular choice
A=2,B=3i. Along each original port circle all Pochhammer
roots are radially separated by a constant times 1/N.
Uniformly on the ENTIRE conditional angular circle,

    sum_(j=0)^(L-1) log|1-e^((gamma+i phi)/N)
                                    e^(i theta)Q^j|
       =N integral_0^(L/N) log|1-e^(i(theta+2pi t))|dt
                                                     +O_K(log N). (8)

Here gamma ranges in a compact set bounded away from zero,
L<=N, and phi is bounded. To prove (8), regularize the
periodic logarithmic singularity at radial distance |gamma|/N.
Its total variation is O_K(log N), giving that Riemann-sum
error; its integrated change from the boundary logarithm
is O_K(log N/N). This also proves the endpoint uniformity.
Known monomial and source constants do not depend on theta.

Let L(theta)=D(exp(i theta)). On a fixed positive crossing
chart the four angles sum to 2pi. A conditional port varies
only one of the following two FULL-circle profiles, up to
constant and reversal of its angular coordinate:

    H_delta(theta)=L(theta)-L(theta+delta),
    J_delta(theta)=L(theta)+L(delta-theta),
                                  0<delta<2pi.          (9)

For input z0 and output z6 use H with the sum of the two
other relevant positive angles; for input z1 and output z7
use J with the fixed sum of their two varying positive angles.
By (8) these are the true leading logarithmic modulus
profiles of the ORIGINAL finite polynomials on the whole circle.
Explicitly, (2pi/N)log|g_port| equals its H_delta or J_delta
profile, plus an angularly constant normalization and
O_K(log N/N). The profile itself is not divided by 2pi.
All quantum whole-turn factors are already in the fixed
source normalization from Section 3.

The maxima in (9) are UNIQUE and GLOBAL:

    max H_delta=2L(pi-delta/2), theta_*=pi-delta/2,
    max J_delta=2L(delta/2), theta_*=delta/2.            (10)

For H, differentiation gives

    H'=log|sin((theta+delta)/2)/sin(theta/2)|.

Its only stationary points are theta_* and theta_*+pi.
The former is the strict global maximum; the latter is
the strict minimum. At shape-1 points the derivative is
logarithmically infinite with the same monotone direction
on both sides, so no extra endpoint maximum is concealed.
For J the same computation gives its maximum theta_*
and minimum theta_*+pi. The curvatures at the maxima are
-tan(delta/4) and -cot(delta/4), respectively.

At these maxima the two varying positively oriented
tetrahedron angles are equal. If the other pair was
positive, the maximum lies in the positive chamber.
Every other sheet or endpoint on this conditional circle
is strictly lower. On compact delta ranges, excluding
a fixed neighborhood of theta_* gives a UNIFORM gap.

This is a conditional statement. The other ports are
held fixed. Its maximum is not automatically the complete
global geometric point after sewing the original knot.

## 6. Composition scope and the remaining global source issue

The exact formulas may collapse ONE adapter, or the paired
adapters of (3a), while the untouched opposite ports remain
on their correlated original grids. Nothing here permits
applying the other pair's formula after arbitrary movements
of the first pair. In particular a general geometric
complex deformation can destroy its integer relation.

The exact [deck-character calculation](balanced_crossing_deck_characters.md)
makes the obstruction explicit. If the first pair moves
so that D!=sA, then the other input port has
mu_b-1=(sD-A)/(A-sB), generically nonzero. The physical
FOUR-variable Laurent polynomial remains single-valued;
the raw four-Psi continuation does not. Known fixed-grid
constants and integer alias multipliers alone cannot
turn that raw continuation into a simultaneous equality.
An asymptotic comparison in a complex neighborhood may
still be possible, but it needs the additional seam terms
or their actual bounds, beyond the one-pair theorem.

Known phase oscillation is not removed by the modulus
maxima. On the positive real-angle chamber the mixed
input-output Hessian of the retained leading REAL action is

    partial_(theta_out) partial_(theta_in) Re W
                                      =-(1/2) I_2.

Head-only or input/output-only gauges do not remove it.
The exact one-port adapter result (5)--(7) controls its
local Fourier action; it does not make the entire sewn
original scalar a positive Laplace integral. Global
cycle selection, compatible elimination order, and the
retained cap/boundary source still need a proof.

The [audit](../experiments/audit_actual_fourier_port_polynomials.py)
checks (2)--(3) against independently evaluated ORIGINAL
crossing matrices and their Fourier transforms, every
allowed k/m frequency support and scalar normalization,
and the analytic adapter and profile estimates.
