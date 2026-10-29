# Exact boundary reduction of the original quantum-A energy

28 October 2026. This implements the proposed boundary-to-interior
strategy at the level of the ORIGINAL pointed operator. A regular
interior with a weighted symbol gap can be eliminated with controlled
cost. Its entire effect is an explicit positive operator on the retained
boundary packets. This operator retains the original source, turning
regions, endpoint resonance and selected observable.

The reduction is proved below. A sharp estimate for its selected boundary
response is not proved. In particular, uniqueness does not supply that
estimate: a concrete two-endpoint example in Section 4 has an excellent
interior gap and an exponentially small boundary eigenvalue.

The complementary [interval propagation theorem](actual_pointed_a_interval_observability.md)
gives a controlled whole-line Green extension and exponential inward
decay from both retained endpoint packets, including shrinking symbol
gaps. This note identifies the exact positive operator that determines
those packets in the original global source.

A subsequent [macroscopic actual-source estimate](actual_macroscopic_a_spectral_upper_bound.md)
does now bound the whole original value by a classical spectral
integral, under its explicit actual-operator and classical-order
hypotheses. Comparing that rate with volume remains open broadly.
For the proposed stepwise energy mechanism, the
[pointed metric calculation](actual_pointed_metric_transport_and_crossing_obstruction.md)
shows precisely what source and endpoint costs must be retained and
why tame full-space metrics can lose coherent phase cancellation.

## 1. Eliminate only an interior whose estimate has been proved

Use the full bounded-jet system and weights in
[the actual bulk energy theorem](actual_pointed_a_bulk_agmon_energy.md):

    L u=f, P=L* L, g=L* f, beta=f* f.                    (1)

Here * means Hermitian transpose. The actual source consists of the fixed
initial identity rows. Choose the remaining column set B to contain their
colors, the complete color, and every turning, end or other exceptional
packet. Write I for the regular interior columns. Thus g_I=0 exactly.
No color or normal jet in B is removed.

Suppose the full-output estimate on vectors supported in I gives

    mu ||v||^2 <= <v,P_II v>, ||P|| <= C, mu>0.          (2)

For example a fixed weighted symbol gap eta gives mu=eta^2/4 for large
N by the proved localized Plancherel estimate. Several regular intervals
are allowed: keep enough exceptional columns between them that the
full banded operator does not couple their supports, or apply that same
estimate to their union with its uniform gap. The operator in (2)
retains ALL output rows meeting I.

Set

    A=P_II, H=-A^(-1)P_IB,
    S=P_BB-P_BI A^(-1)P_IB, E v=(H v,v).               (3)

Then the exact original solution obeys

    u_I=H u_B, S u_B=g_B.                              (4)

Moreover

    0<=S<=P_BB, ||H||<=C/mu,
    ker P=E ker S.                                    (5)

Proof. Complete the square, for arbitrary v_I,v_B:

    <v,Pv>=<v_I-Hv_B,A(v_I-Hv_B)>+<v_B,Sv_B>.          (6)

This proves positivity, the Schur bound and the kernel assertion; the
normal equations P u=g with g_I=0 prove (4). Conversely (4) implies
the normal equations. Since the original system is consistent, their
solutions also satisfy L u=f: their residual is perpendicular to the
range of L while belonging to that range. Thus no spurious boundary
solution has replaced the original source.

For a weighted complete-color projection T_B, its value is T_B u_B.
The original unweighted value is exp(-N phi(1)) times that value.
For any full observable R u, its exact boundary observable is

    R_eff=R_I H+R_B, R u=R_eff u_B.                    (7)

The fixed-jet pointing theorem gives ker P subset ker R for the selected
constant-color observables (including their weighted versions).
Consequently ker S subset ker R_eff. Higher-jet nonuniqueness is retained
and does not change the observable. The estimates in (5) show that bulk
elimination itself costs at most a power of N whenever mu^(-1) does.

## 2. The residual boundary period is positive and source-exact

Let nu=dim ker S, equal to dim ker P and hence bounded by the original
fixed jet budget. Define the two polynomials

    Q_B(lambda)=det(S+lambda I),
    D_B(lambda,z)=det[ S+lambda I+z R_eff* R_eff   g_B;
                       g_B*                       beta ].       (8)

Then the SAME original selected energy is exactly

    ||R u||^2=[lambda^nu z]D_B/[lambda^nu]Q_B.         (9)

The denominator is positive; all coefficients of both polynomials are
nonnegative real numbers. In particular (9) keeps the boundary source,
rather than substituting a maximum eigenvalue or arbitrary boundary
vector.

Here is a direct proof. Since (1) is consistent, (4) gives

    beta=<u,Pu>=<u_B,S u_B>=g_B* S^+ g_B.              (10)

The matrix [S,g_B;g_B*,beta] is positive semidefinite: it is the Schur
complement of A in the Gram matrix [P,g;g*,beta]. Factor it as Z* Z.
Appending rows sqrt(lambda)[I,0] and sqrt(z)[R_eff,0] gives the matrix
in (8). Expanding its determinant as squared minors proves coefficient
nonnegativity. The same argument applies to Q_B.

Decompose the boundary space orthogonally into ker S and its orthogonal
complement. Both g_B and R_eff vanish on the kernel in the appropriate
sense. Thus D_B has a factor lambda^nu. On the complement, S is positive
definite and (10) makes its bordered Schur complement zero at z=0.
Its derivative in z at lambda=0 is

    g_B* S^(-1) R_eff* R_eff S^(-1) g_B=||R_eff u_B||^2.

Multiplication by det(S on (ker S)^perp) proves (9).

This is a smaller exact period whenever I occupies most colors. With
finitely many exceptional windows of width o(N), its matrix size is
o(N), although its entries may retain exponentially small transport
information. The latter qualification is essential. Auxiliary regulator
weights need not themselves be algebraic; they are an estimating metric,
not a new definition of the quantum invariant. Undoing the weight gives
the original period exactly.

## 3. Regular interior coupling decays with distance

Assume the block bandwidth of P is w and its norm is at most C>0.
The proof of (2) gives mu<=C. In the original color distance, the
interior Green blocks satisfy

    ||(A^(-1))_(jk)|| <= mu^(-1)
                       exp[-mu |j-k|/(2 C w)].       (11)

If w=0 the inverse is block diagonal instead. To prove (11), expand

    A^(-1)=(2C)^(-1) sum_(n>=0) (I-A/(2C))^n.

The norm of the n-th power is at most (1-mu/(2C))^n. Its (j,k) block
vanishes for n<ceil(|j-k|/w), even when I has gaps. Summing this tail
and using 1-a<=exp(-a) gives (11). This is a direct banded-matrix proof,
independent of diagonalizing the classical transfer.

For widely separated boundary columns j,k, (3) therefore gives

    ||S_(jk)|| <= C' mu^(-1)
         exp[-c mu (|j-k|-2w)]    when |j-k|>2w.      (12)

Only finitely many P neighbors of j and k occur in the product in (3).
The analogous formula u_I=H u_B gives a sum of exponentially decaying
contributions from the retained boundary data. If those data and the
inverse gap are controlled, the regular interior carries their estimate
with polynomial loss. It does not generate an additional volume
exponent. The estimate is on the exact response, including all jets.

## 4. Why the residual boundary estimate is necessary

Consider a simple, fully rigid sourced recurrence on j=0,...,n:

    y_0=b, y_(j+1)-2 y_j=0.                          (13)

Its weighted gap with weight zero is |exp(i theta)-2|>=1. Its interior
Gram matrix on I={1,...,n-1} has diagonal 5 and off-diagonal -2, so
A>=I for every n. Keep B={0,n}. Eliminating I minimizes the energy

    |y_0|^2+sum_(j=0)^(n-1)|y_(j+1)-2y_j|^2

for prescribed endpoints. Since

    y_n-2^n y_0=sum_(j=0)^(n-1)2^(n-1-j)
                                      (y_(j+1)-2y_j),

Cauchy--Schwarz, with equality attained by proportional residuals, gives

    D_n=sum_(j=0)^(n-1)4^j=(4^n-1)/3,
    <y_B,S y_B>=|y_0|^2+|y_n-2^n y_0|^2/D_n,
    S=[1+4^n/D_n, -2^n/D_n;
       -2^n/D_n,       1/D_n].                     (14)

The retained source is g_B=(b,0), beta=|b|^2. Solving S y_B=g_B
gives y_0=b and y_n=2^n b, exactly as in (13). Yet ||S|| is bounded,
det S=1/D_n, and its smallest eigenvalue is asymptotic to 3*4^(-n)/4.
Thus a uniformly controlled bulk, a two-dimensional boundary space,
and uniqueness still allow exponential source amplification. In (9)
the selected period is exactly 4^n |b|^2.

This example is a logical test of the propagation inference, not a knot
counterexample. It explains why the actual boundary Schur operator and
its selected source must be estimated rather than deleted.

## 5. The exact remaining geometric target

For the actual complete-color observable, (9), together with undoing
the weight, reduces the desired upper bound to a selected boundary
response estimate. A sufficient condition is

    ||R_eff S^+ g_B||
       <= exp[N Vol(S^3 minus K)/(2pi)+o(N)],         (15)

when R_eff includes undoing the weight. If R_eff selects only the
weighted complete color, the right side is instead multiplied by
exp(N phi(1)). This equivalence is explicit; it is not a proof of (15).
One may also seek a source-compatible transport flag or an exact
boundary factorization which proves (15) without bounding S^+ on
irrelevant channels.

The regulator must retain its source anchor: phi(0)=0 fixes the initial
source scale, and a bound on absolute branch regulators alone controls
their differences by at most 2 Vol. Neither (3) nor (9) removes that
issue. The local physical-face fillings give possible information for
the exceptional packets, but their identification with this complete
boundary response still requires an exact source comparison.

The independently proved ordinary-color bound concerns the CONSTANT
color components j<N. It does not bound the normal jets in B. Those
jets are necessary at singular recurrence steps, and (3)--(9) retain
them. Replacing the complete boundary packet by its constant-color
projection would therefore be an additional unproved inference.

This is a constructive boundary-to-interior reduction, valid for the
actual original operator wherever its stated bulk gap is verified.
No broad sharp whole-source bound or geometric survival theorem is
claimed.

[Audit](../experiments/audit_actual_a_boundary_schur_transport.py):
four actual figure-eight source elimination identities, an exact
rank-deficient rational fixture for the selected coefficient ratio,
and four exact recurrence Schur complements. The actual scalar audit
does not assert truncated-jet uniqueness; that input is the full
pointed-system theorem used in the proof above.
