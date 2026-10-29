# Mesoscopic diagonal currents on the actual cup-slide packet

29 October 2026. The original cup-slide normalization packet admits a
coherent subexponential estimate with operator-valued diagonal clock
couplings of growing, sublinear Laurent bandwidth. This uses the
source-exact packet before taking absolute values, not a dephasing of
its individual factorial coefficients.

The statement is about the specified exposed recorded packet. It is
not automatically an operator identity on an arbitrary remaining
physical head. The all-input distinction is explicit in Section 4.

## 1. Literal source packet and its exact controlled-clock contraction

Use the original notation and full Cartan factor of
[the all-input cup slide](actual_terminal_source_normalization_packet.md):

    N>=2, d=N-1, Q=exp(2pi*i/N), x=exp(pi*i*d/N),
    F_j=(Q;Q)_j, b_j=x^(-d)Q^(-j) conjugate(F_j),
    Gbar_N(z)=sum_(j=0)^d conjugate(F_j) z^j.

This is exactly b=T R12 R23 p, with the original physical recorded
middle-color projectors, ordinary cap and specified lowest marked cut.
All original external framing/peripheral factors chi_N stay outside.
The finite identity Q^(j+1)F_j=F_j-F_(j+1), F_N=0, gives

    P_N(z):=sum_(j=0)^d Q^(-j) conjugate(F_j) z^j
          =Q[(1-1/z)Gbar_N(z)+1/z].                       (1)

The apparent singularity at zero is removable. In particular P_N(1)=Q
and the original packet closes to x^(-d)Q, with its full unit phase.

Let A_r(t), |r|<=D, be operators on any spectator space. Define the
EXPLICIT diagonal recorded-color exterior

    f_j(t)=sum_(|r|<=D) A_r(t) (tQ^r)^j.

The exact contraction, preserving original operator order, is

    sum_j f_j(t)b_j=x^(-d) sum_(|r|<=D) A_r(t)P_N(tQ^r).  (2)

Only distributivity is used in (2). The A_r need not commute with one
another or be scalar. Their norm is retained below. In particular an
arbitrary exterior with O(N) Laurent bandwidth is not silently replaced
by a fixed-band clock polynomial.

## 2. Mesoscopic source bound

The independently proved
[clock-disk theorem](actual_normalization_clock_disk_bound.md) gives,
for 0<C<=N/2,

    sup_(|z-1|<=C/N)|G_N(z)| <= B_N(C),
    B_N(C)=2exp(2C)N^2 (1+2N/(3C))^(C/4).                 (3)

Coefficient conjugation gives the SAME bound for Gbar_N. Suppose
|t-1|<=c/N and put C=c+2pi*D. Then

    |tQ^r-1| <= |t-1|+|Q^r-1| <= C/N, |r|<=D.           (4)

When C<=N/2, every argument in (2) has modulus at least1/2. Equations
(1)--(4) consequently prove the actual coherent inequality

    ||sum_j f_j(t)b_j||
      <= (sum_r ||A_r(t)||) [2+(2C/N)B_N(C)].             (5)

Any supplied norm on the spectator coefficient space may be used.
No N-dependent change of physical source metric appears in (5).
The phase x^(-d) has modulus one and remains in the exact identity (2).

Let now c=c_N and D=D_N grow with N. If

    c_N+D_N=o(N),
    log^+ sup_(|t-1|<=c_N/N) sum_r||A_r(t)|| = o(N),      (6)

then the right side of (5) is exp(o(N)). Indeed

    log B_N(C)=O(log N+C+C log(1+N/C))=o(N),

since s log(1+1/s) tends to zero as s=C/N tends to zero. The cases
C=0 or D=0,t=1 follow directly from P_N(1)=Q. Fixed bandwidth,
fixed c, and polynomial spectator mass give a polynomial bound.

This controls a genuinely growing set of diagonal clock observables
on the known original packet. Individual |F_j| can still be
exponential; the coherent identity (1) has been used before estimation.

## 3. Normal jets and compatible normalization leaves

If the coefficient operators are holomorphic on a slightly larger
disk with the same subexponential mass condition, Cauchy's formula
also bounds fixed clock-normal derivatives. For a radius r_N>0 with
log^+(1/r_N)=o(N),

    || (1/s!) partial_t^s sum_j f_j(t)b_j |_(t=1)||
      <= r_N^(-s) sup_(|t-1|=r_N)||sum_j f_j(t)b_j||.    (7)

Thus fixed s costs exp(o(N)); growing orders are allowed whenever
s log^+(1/r_N)=o(N), in addition to the stated supremum bound.
This is a derivative of the recorded packet, not a meridian
identification or a physical two-color raising/lowering insertion.

The [normalization-current quotient](actual_normalization_boundary_current_quotient.md)
may be composed with (2) when its literal all-input pointing map
exposes this packet and its spectator coefficients in exactly this
slot. For example, its fixed-forest radial Mellin Taylor coefficients
have polynomial coefficient mass; (5) then retains that mass and gives
the same subexponential clock bound. Each leaf contraction must be an
actual tensor/source identity before it is estimated. No independent
mark or new 1/N average is introduced for such a leaf.

The assertion is deliberately typed. It does not say that any internal
recorded-color seam can be moved to the marked cut, or that arbitrary
original crossings preserve this filtered clock class. Their factorial
dependence and frequencies can have order N.

## 4. Why the scalar packet does not already solve physical gluing

There is a simple all-input test. The original cup slide is

    (R12 R23)(p12 tensor I)=I tensor p23.

Keep an arbitrary physical input color a on the remaining head,
record the middle color n, and perform the SAME terminal R23^2 and
ordinary cap as before. Write L=kappa^(-1)R12 on degree d. The
resulting actual open-head operator is diagonal, with entries

    C_a(t)=sum_(n=0)^d t^n x^(n-a)Q^(-a)(L^2)_(d-a,n).   (8)

To derive (8), multiply the literal cup coefficient N x^(n-d),
the full crossing square kappa^2(L^2)_(d-a,n), and the cap
x^(-a)Q^(-a)/N, using kappa^2=x^d. All original turns and phases
are therefore fixed. At t=1, Hopf closure gives C_a(1)=kappa^2 for
EVERY a. At a=d, (8) is exactly x^(-d)P_N(t), the scalar packet
estimated above.

A scalar bound for this last row does not prove a uniform all-a
operator bound for (8). Likewise applying a unilateral shift to the
RECORDING register is not automatically inserting physical Ecal or F
before the projector: Pi_j Ecal Pi_k retains two colors and changes
the remaining terminal coefficients. Such a move needs an actual
two-color/all-port identity. Equations (2)--(7) apply to diagonal
controlled-clock exteriors on the already exposed original packet;
they do not assume those missing identities.

This is a quantitative source-current class, not a sharp full-knot
volume theorem. Binding the complete internal currents to the knot's
geometric regulator remains unproved.

[Audit](../experiments/audit_actual_mesoscopic_clock_packet_currents.py)
checks the original physical packet, its full phase and operator-valued
controlled-clock contractions; it also tests the quantitative disk
comparison on growing bandwidths without separating factorial modes.
