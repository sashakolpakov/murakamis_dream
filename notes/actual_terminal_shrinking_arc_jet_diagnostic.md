# An exact original-source jet test for the shrinking-arc metric

29 October 2026. This records an exact original prefix, its complete
terminal polynomial, and high-precision evaluations of its first jet
and FULL finite Cayley-arc energy. The closed scalar is proved
polynomially bounded. The data show amplified jets at the tested levels.
An all-N positive exponential jet rate has NOT been proved here, so
this is not an asymptotic counterexample to the shrinking-arc proposal.

No conclusion about the coefficient of an escaping classical branch
is inferred from its character equations. The actual quantum quantities
below are evaluated directly from the original finite matrices.

## 1. The literal source prefix and its exact coefficients

Keep N>=2,d=N-1,q=exp(pi*i/N),Q=q^2,x=q^d=-q^-1,
F_j=(Q;Q)_j,kappa=q^(d^2/2). Use the COMPLETE original Hom module
W=(V tensor V)_(integer degree d), the original cup

    p_j=Nx^(j-d),

and the original adjacent signed generators R_12,R_23. Let R be
the literal positive pair crossing on W, INCLUDING kappa, and T
the [complete original terminal packet](actual_terminal_packet_closed_kernel.md).
The prefix in this test is

    B=R_12 R_23^(-1),

so the true full chronological word is [-2,1,2,2], with the same
ordinary/marked whole source as in the terminal theorem. It is not
a newly chosen vector at the terminal cut.

The prefix state has an elementary EXACT formula:

    R_23^(-1)p=N kappa^(-1)e_d,
    v_j=(Bp)_j=N^2 x^(j-d)/F_(d-j).                      (1)

For a proof of the first identity, apply the original negative crossing
to the highest source p_12 tensor |0>. Its negative transfer must be
zero because the second input is0. The outgoing third color is then
the old second color. Extracting third color0 leaves only the old
cup component |d,0>, of coefficient N, with crossing scalar kappa^-1.
This extraction is the inverse of the COMPLETE highest Hom chart,
so no arbitrary physical projection is imposed. The strict original
positive coefficient R_(j,d)=kappa N x^(j-d)/F_(d-j) gives (1).

Define the actual recorded-color polynomial and its coefficients by

    f_N(t)=sum_(n=0)^d a_(N,n)t^n, a_N=Tv.               (2)

The complete terminal factorization gives an efficient expression
with NO dense inverse:

    T=N^-1 X R P_rev R,
    X=diag(x^n),
    P_0=1, P_j=(1-Q^j)^2P_(j-1)+Q^j,
    P_rev=diag(P_(d-j)).                                 (3)

Thus, explicitly,

    a_(N,n)=x^n/N sum_(i,j) R_(n,i) P_(d-i) R_(i,j)
                                      N^2x^(j-d)/F_(d-j). (4)

Equations (1)--(4) retain every original Cartan factor, finite endpoint,
cup/cap normalization and coherent Green summation. They are complete
source identities, not isolated paths or critical-point ansatzes.
The external original scalar chi_N multiplies all of (2), its jets
and the corresponding squared energy by its stated exact factors.
It is not absorbed into T or fitted from a knot value.

## 2. The raw closed value is polynomial: a direct source proof

The exact original terminal ROW, from the cap/Hopf calculation, is

    sum_n T_(n,j)=(xQ)^(j-d)/N.                           (5)

This is equation (18) of
[the effective-Cartan source calculation](actual_terminal_effective_cartan_kernel_and_graph.md),
and is independently checked here on every input column using the
original physical projectors. Combining (1),(5) and x^2Q=1 gives

    f_N(1)=N sum_(j=0)^d 1/F_(d-j)
          =sum_(j=0)^d conjugate(F_j)
          =conjugate(P_d).                              (6)

The second identity uses F_(d-j) conjugate(F_j)=N. The whole
endpoint source estimate in
[the terminal Green theorem](actual_terminal_green_capacity_bound.md)
proves |P_d|<=3N^2 at ALL parities and composite levels. Hence

    |f_N(1)|<=3N^2.                                     (7)

This proof uses coherent source identities; replacing the sum by
sum |F_j| would lose the polynomial bound. For topological context,
the original marked four-plat has rational slope3/2:
T^2 U^-1 T^-1(0,1)^T=(3,2)^T in the established cap marking.
The proof of (6)--(7) does not require a knot census or a framing guess.

## 3. Exact finite first-jet and arc-energy formulas

The centered physical first jet is

    D_N=2f_N'(1)-d f_N(1)
       =sum_(n=0)^d(2n-d)a_(N,n).                        (8)

It is a recorded PHYSICAL clock moment. It is not identified with
an original meridian derivative or an ordinary-color q-jet. Such an
identification would require another source/normal Ward theorem.

There is a stable complete-polynomial calculation of the proposed arc
energy. Define integers K_r(n) by

    K_0(n)=1, K_1(n)=2n-d,
    (r+1)K_(r+1)(n)=(2n-d)K_r(n)-(d-r+1)K_(r-1)(n).

These are exactly the coefficients of
(1+z)^n(1-z)^(d-n). Consequently the ENTIRE Cayley polynomial is

    Q(y)=(1-iy)^d f_N((1+iy)/(1-iy))=sum_(r=0)^d c_r y^r,
    c_r=i^r sum_n K_r(n)a_(N,n), c_1=iD_N.                (9)

For a prescribed arc width h>0 its normalized weighted energy is
therefore the exact FINITE sum

    E_h=1/2 integral_(-1)^1 |Q(hs)|^2 ds
       =sum_(r+s even) h^(r+s)c_r conjugate(c_s)/(r+s+1). (10)

All degrees0,...,d and mixed terms are retained. This is not a
Taylor truncation, quadrature approximation, or a sum of independently
estimated jets. The original unweighted arc energy E_h^0 obeys

    E_h/(1+h^2)^d <= E_h^0 <= E_h.                       (11)

The independently proved
[sharp derivative-evaluation norm](actual_shrinking_arc_cauchy_metric.md)
also gives the exact necessary lower test

    E_h>=h^2 |D_N|^2/D_d,
    D_d=[(2r+1)(2r+3)binom(2r,r)/4^r]^2/3,
    r=floor((d-1)/2).                                   (12)

Thus a PROVED positive exponential rate for this actual D_N would
prove excessive energy for EVERY polynomial width h=N^-A, A>0.
The present data do not prove that rate. They do show which exact
source insertion must be controlled before using a shrinking arc.

### The missing normal current is an explicit all-input row

Let r=(x^j)_(j=0)^d be a ROW and J=diag(0,...,d). The original
cup eigenrelation and the symmetric physical pair crossing give
rR=kappa r. Set F_row(t)=sum_n t^n T_n, so f_N(t)=F_row(t)v.
Using (3) and differentiating only this recorded phase gives the
following identity on EVERY complete input:

    F_row'(1)=N^-1 r J R P_rev R
             =(kappa/N) r J P_rev R
                     +N^-1 r[J,R]P_rev R,               (13)
    [J,R]_(c,a)=(c-a)R_(c,a).

The same full R and Green register occur on both sides; in particular
P_rev is not commuted through a crossing. Applied to v in (1), (13)
is the literal first derivative in (8). This specifies an original
matrix-valued normal current before the final source pairing. It is
not a new meridian Ward identity. A proposed coherent cancellation
must transport the second row in (13), with its neighboring factors,
or supply its compensated source; the unweighted row identity (5)
does not set this current to zero. No exponential estimate for either
separate term is asserted.

## 4. High-precision data, explicitly diagnostic

The table uses the raw original source above, natural logarithms,
and the FULL weighted energy (10) with h=N^-2.

| N | log abs f_N(1)/N | log abs D_N/N | log E_h/N |
|---:|---:|---:|---:|
| 16 | .259042 | .694506 | .637717 |
| 32 | .162528 | .604089 | .740650 |
| 64 | .097444 | .543196 | .809301 |
| 128 | .056861 | .504738 | .849268 |
| 256 | .032490 | .481476 | .872016 |

At N=32,64,128,256 the ratios of E_h to the first-linear-jet energy
h^2|D_N|^2/3 are respectively1.000644,1.000278,1.000105,1.000037.
This is a diagnostic comparison of the ENTIRE polynomial with its
first-jet contribution, not an all-N error estimate.

The raw value trend is explained by the proved bound (7). The jet and
energy trends suggest amplification but are not a rigorous asymptotic
lower bound. In particular no limiting rate is fitted or asserted,
and no comparison with a different knot's geometric action is used
as proof. The missing statement is a source-derived bound, cancellation,
or exact asymptotic for the normal insertion (8).

## 5. Audit and current limitation

[Audit](../experiments/audit_actual_terminal_shrinking_arc_jet_diagnostic.py)
uses ORIGINAL E/F/R matrices and physical terminal projectors for nine
exact finite-root source checks. It verifies (1),(3),(5),(6), all
normalizers, the full first-jet coefficients, and the all-input
normal-current row (13). Ten high-precision
profiles through N=256 then use only the finite R matrices and the
coherent first-order Green recurrence; there is no numerical inversion.
The Krawtchouk recurrence computes ALL coefficients in (9), followed
by the complete monomial Gram (10).

At N=128, increasing working precision from228 to360 decimal digits
changes the centered first jet by less than2.2e-198 relatively and
the complete energies at h=N^-1,N^-2 by less than1.7e-198. These
checks make the finite diagnostic reproducible; they do not replace
an analytic exponent theorem. The closed source bound is proved,
while positive exponential growth of D_N and failure of all polynomial
shrinking arcs for this source remain explicitly UNPROVED.
