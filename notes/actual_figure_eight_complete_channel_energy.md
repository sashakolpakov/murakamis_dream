# The fixed complete Hermite energy overshoots the original figure-eight rate

29 October 2026. The complete positive channel metric constructed in
[the actual source multiplicity module](actual_complete_source_multiplicity_module.md)
has polynomial BOTH original boundary norms. Its full coherent energy
nevertheless exceeds the sharp knot-volume rate already for the literal
original figure-eight word. This is proved by one EXACT complete channel,
not by a dephased path, an unconstrained clock sector, or a numerical fit.

For every odd N=2m+1>=3, the simple Casimir channel c=-2 has the exact
amplitude

    z_simple=N Q^[m(m+1)] F_m B_m,
    B_m=sum_(r=0)^m |[m choose r]_Q|^2 >0.                (1)

All original Cartan phases and cap/cup normalizations are included.
Consequently the normalized fixed-Gram energy satisfies

    E_N >=N^2 B_m^2,
    log(N^2 B_m^2)=N v_8/pi+O(log N),                    (2)

where v_8=4 Catalan is the regular ideal octahedron volume. Since
v_8>Vol(S^3 minus 4_1), this fixed Gram CANNOT supply a sharp
figure-eight energy upper bound. It remains a valid Cauchy metric.
The obstruction concerns this explicitly specified complete energy,
not every coherent metric or a source-specific regrouping.

## 1. The complete metric and the original word

Use N>=2, d=N-1, q=exp(pi*i/N), Q=q^2, x=-q^-1=q^d,
F_a=(Q;Q)_a, and kappa=q^(d^2/2). On the complete N-dimensional
three-head Hom space W use the physical basis |a,d-a>.
Let R be the original positive pair crossing on degree d, including
kappa, and let J be the exact symmetric anti-Pascal recoupling from
[the complete module](actual_complete_source_multiplicity_module.md).
The original pair source is

    p_a=Nx^(a-d), ell_a=x^a/N.

The full signed generators are R_12=R and R_23=J^-1 R J.
Let V be the COMPLETE degree-d canonical Hermite frame of the actual
pair Casimir A, with f_0(c)=1, and define

    S=V^-1 J, G_N=S^*S/N.

The metric is full rank and depends only on the original module and N.
Its normalized ordinary-cap dual norm is <=1 and its initial cup
energy is O(N^2), as proved in the complete source theorem.

The TRUE figure-eight four-plat has chronological word

    [2,-1,2,2], W=R_23^2 R_12^-1 R_23.                  (3)

It is NOT the original three-braid trace word with a newly attached
cup. The [whole-source proof](figure_eight_whole_source_identity.md)
identifies (3), its literal turns and its oriented framing. At
completeness it gives EXACTLY

    ell Wp=K_N(4_1)=sum_(a=0)^d |F_a|^2.                (4)

In particular no unknown knot scalar is used to define G_N. The
complete coherent output and normalized energy tested here are

    z=SWp, E_N=||z||_2^2/N.                             (5)

The external line chi_N, if retained as a separate convention, is
put inside the transported state and multiplies (5) by |chi_N|^2.
In the reduced, zero-framing normalization (4) the scalar is the
displayed positive original period. We never replace the full
Cartan by its modulus inside the finite algebra below.

## 2. A positive full-channel covector, derived from the actual Casimir

Assume N=2m+1. The pair Casimir has the SIMPLE channel
c_m=q^(2m+1)+q^(-2m-1)=-2. It has no derivative column.
Let f=f(-2) be its canonical eigenvector f_0=1. The exact identities
from the source module are

    J=J^T,
    J A J^-1=B^T,
    B e_j=c_j e_j+b_j e_(j-1),
    c_j=q^(2j+1)+q^(-2j-1), b_j=Q^j+Q^-j-2.             (6)

For completeness symmetry of J follows directly from its formula:
J_ij/J_ji reduces to1 using
F_jF_(d-j)=N(-1)^j Q^[j(j+1)/2] and x^2Q=1.

Set y=Jf. Since (B^T+2)y=0, its coordinates below m are zero.
For j=m+r, r>=1, its recurrence has the real positive ratio

    y_(m+r)/y_(m+r-1)=b_(m+r)/b_r
                  =|1-Q^(m+1-r)|^2/|1-Q^r|^2.

The last row of J is e_0^T, so y_d=f_0=1. Thus EXACTLY

    y_i=0 for i<m,
    y_(m+r)=|[m choose r]_Q|^2, 0<=r<=m.                (7)

This is an eigenvector calculation on the COMPLETE original module.
It retains the coherent q-Hahn sums within f and J. No path phases
have been deleted. The root phases cancel only in the proved
recurrence (7).

## 3. The original finite source reduces the selected channel to one sum

The first actual crossing on the cup has the exact highest-chart
coefficient

    (R_23 p)_a=kappa p_a F_(d-a).                        (8)

Indeed the cup has third physical color0, and extracting output
third color0 uses the literal ground-output coefficient
R_(b,0;b,0)=kappa F_b. This does not change the rest of the source.
Set v=R^-1(R_23 p). In RIGHT physical coordinates the remaining
two R_23 factors are R^2. At the simple channel its CD inverse row
is f^T/sigma, with

    sigma=x^d nu_m, nu_m=(-1)^m q^[m(m+1)],
    kappa^2=x^d.

Consequently the full simple-channel coordinate is

    z_simple=(kappa^2 nu_m^2/sigma)y^T v=nu_m y^T v.      (9)

All kappa factors have been accounted for, rather than dropped.

Here is a source-exact finite evaluation of y^T v. Substitution
of the original negative crossing into (8), followed only by
root complementation of factorials, gives for every 0<=i<=d

    v_i=x^(i-d)(-1)^i Q^[i(i+1)/2-d] F_(d-i)/F_i
                     *sum_(b=i)^d Q^b F_b^3/F_(b-i).     (10)

This is the full negative matrix applied to (8), not one route.
Put

    zeta_m=(-1)^m x^-m Q^[m(m+1)/2+1].

Using (7), each term in the selected contraction becomes exactly

    y_(m+r)v_(m+r)
      =zeta_m Q^(r^2)/F_r^2
                     *sum_(b=m+r)^(2m) Q^b F_b^3/F_(b-m-r).

Swap b=m+t and r. The elementary finite Durfee-square identity

    sum_(r=0)^t Q^(r^2)/(F_r^2 F_(t-r))=1/F_t^2          (11)

therefore gives

    y^T v=zeta_m Q^m F_m^3 U_m,
    U_m=sum_(t=0)^m Q^t (a;Q)_t^3/F_t^2,
    a=Q^-m=Q^(m+1).                                    (12)

One direct proof of (11) works first with a formal variable Q.
The generating function for partitions with largest part at most t
is1/F_t. Decomposing them by Durfee square r gives
sum_r Q^(r^2)[t choose r]_Q/F_r: the right rectangle contributes
the Gaussian polynomial and the lower partition contributes1/F_r.
Substitution of the factorial expression gives (11). This rational
identity extends to the present root because all its factorial
indices are<N. No convergence argument at a unit root is used.

## 4. An elementary terminating transform makes the WHOLE projection positive

The finite identity needed in (12) is

    U_m=(-1)^m Q^[-m(3m+1)/2] B_m,
    B_m=sum_(k=0)^m Q^[-k(m-k)] [m choose k]_Q^2.        (13)

The last summands are precisely the positive magnitudes in (1).
Here is a derivation, independently reproduced in the
[finite transform proof](actual_half_color_quadratic_source_transform.md).
Expand the THIRD (a;Q)_t by the finite q-binomial theorem and put
t=k+j,n=m-k. Its inner sum is the terminating Chu identity

    sum_(j=0)^n (Q^-n;Q)_j^2 Q^j/
                              [F_j(Q^(k+1);Q)_j]
       =Q^(-n^2)(a;Q)_n F_k/F_m.                       (14)

For a direct finite proof, the general identity with one numerator
replaced by b and the denominator by c is

    sum_(j=0)^n (Q^-n;Q)_j(b;Q)_j Q^j/[F_j(c;Q)_j]
       =b^n(c/b;Q)_n/(c;Q)_n.

After multiplication by (c;Q)_n it is the Newton expansion of
product_(i=0)^(n-1)(b-cQ^i) in the basis (b;Q)_j.
The recursion b(b;Q)_j=Q^-j[(b;Q)_j-(b;Q)_(j+1)]
and Gaussian Pascal give its coefficients by induction. Taking
b=Q^-n,c=Q^(k+1), and Q^(m+1)=a proves (14).

Inserting (14), use

    (a;Q)_k=(-1)^k Q^[-mk+k(k-1)/2] F_m/F_(m-k).

The total sign is(-1)^m. Its exponent is
-m(3m+1)/2-k(m-k). The remaining factorial ratio is
[m choose k]_Q^2. This proves (13) with no uncomputed scalar.
Combining (12),(13), its remaining phase is

    Q^[-2m^2+m+1]=Q^[(1-m)(2m+1)]=1.

Hence y^T v=F_m^3 B_m. Finally F_m^2=N nu_m, and (9) yields

    z_simple=nu_m F_m^3 B_m=N nu_m^2 F_m B_m,

which is exactly (1). This proves the witness for EVERY odd level,
including composite levels, using only nonzero factorials of index<N.

## 5. Rigorous exponential excess of the normalized complete energy

Let J(t)=integral_0^t log(2sin(pi*s))ds and
Lambda(theta)=-integral_0^theta log(2sin u)du. The uniform root
factorial estimate gives, simultaneously for every 0<=r<=m,

    log |[m choose r]_Q|
      =N[J(m/N)-J(r/N)-J((m-r)/N)]+O(log N).

At m/N->1/2 the unique maximum is r/N->1/4. The derivative
is log[sin(pi*(m/N-t))/sin(pi*t)], so its unique zero is
t=m/(2N), with the expected sign on either side. Rounding to
the nearest integer changes the objective by O(log N/N).
There are only m+1 positive summands. Therefore

    log B_m=(4N/pi)Lambda(pi/4)+O(log N)
           =(2N/pi) Catalan+O(log N).                  (15)

Here Catalan=2Lambda(pi/4); J(1/2)=0. Since |F_m|^2=N,
the selected coordinate of (5) alone proves

    E_N>=|z_simple|^2/N=N^2 B_m^2,
    liminf_(N odd) log E_N/N>=8Lambda(pi/4)/pi=v_8/pi.    (16)

The original scalar (4) instead has squared rate
Vol(S^3 minus 4_1)/pi=6Lambda(pi/3)/pi. Strict concavity of
Lambda on(0,pi/3), with Lambda(0)=0, gives
Lambda(pi/4)>(3/4)Lambda(pi/3). Thus

    v_8=8Lambda(pi/4)>6Lambda(pi/3)=Vol(S^3 minus 4_1).

The excess is strict, without relying on numerical knot recognition
or a fitted limit. In particular no polynomial factor can repair a
sharp-volume upper bound for THIS E_N.

We do not assert that the full energy limit equals v_8/pi. The
proved lower witness is enough to decide the question. Other complete
channels can only increase this positive energy. The ordinary-cap
scalar still sums their VALUE coordinates COHERENTLY and gives (4).
Thus the excess is not a counterexample to the invariant's volume
limit or to Cauchy--Schwarz; it locates cancellation/energy discarded
by this fixed metric. A non-diagonal source/word regrouping can change
that energy and is not excluded.

The same witness also applies to the complete diagonal CD-weighted
channel metric with block weight |sigma_j|: its simple c=-2 weight
is EXACTLY1. More generally any replacement channel metric bounded
below by exp(-o(N)) times the identity retains the exponential excess.
This does not exclude a coherent non-diagonal terminal/source Gram
with a small eigenvalue on the offending full packet. Such a Gram
requires an additional actual contraction or source argument; the
polynomial boundary norms alone do not supply it.

### No positive metric separated by Casimir node has a sharp Cauchy budget

There is a stronger conclusion that does not require a lower bound on
the metric. Work in the full channel coordinates z=SWp and keep the
actual cap row a=ell S^(-1). At the SIMPLE odd-level node c=-2,

    a_s=x^d/N, z_s=N Q^[m(m+1)]F_m B_m.

Let D_N be ANY positive Hermitian metric block diagonal by distinct
Casimir nodes. Its two-by-two Hermite blocks may be arbitrary positive
matrices; their weights may depend exponentially on N or on the word.
The isolated simple block is some number g_s>0. Positivity gives

    a D_N^(-1) a^*>=|a_s|^2/g_s,
    z^*D_N z>=g_s|z_s|^2.

Consequently its ENTIRE Cauchy budget, not merely its state energy,
satisfies

    (a D_N^(-1) a^*)(z^*D_N z)
                       >=|a_s z_s|^2=N B_m^2.             (17)

By (15) this has exponential rate v_8/pi, strictly above the squared
original invariant's rate. Thus arbitrary reweighting of separate
Casimir nodes cannot fix the estimate by trading source cost against
state energy. The sharp metric must mix distinct nodes, or use an
actual coherent packet contraction that does so. The
[terminal positive Gram](actual_terminal_packet_positive_gram.md)
provides precisely such a contraction on the same full module for
the benchmark, with all original source factors retained.

## 6. Stable whole-source audit

[Audit](../experiments/audit_actual_figure_eight_complete_channel_energy.py)
retains the literal full original R and inverse, all half-Cartan
kappas, the complete cup and cap, and the actual chronological word
(3). Exact finite-field checks verify the selected FULL channel,
not an isolated path. High-precision complex checks use the original
q-binomial pair matrix, its exact antiunitary negative, and the
closed CD inverse blocks. There is NO ill-conditioned dense numerical
inverse. The exact scalar is compared to (4) at every tested level.

The saved audit reports eight exact odd-root source witnesses,
ten growing-level high-precision complete energies through N=129,
and precision-refinement comparisons including the highest tested
level. These are supplementary to
Sections2--5, which prove the all-odd-level witness and strict
exponential excess. The independent finite-transform artifact
checks its elementary identities separately from the asymptotic.
