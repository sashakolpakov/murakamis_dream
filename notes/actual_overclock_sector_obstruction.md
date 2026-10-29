# A macroscopic clock current surviving exact source fusion

28 October 2026. Fixed overclock sectors cannot separately be bounded by
the regulator of the closed knot, even after exact closure/full-block
fusion. This is an all-level calculation in the ORIGINAL enhanced
source. It identifies a remaining macroscopic current whose coherent
clock sum is essential. It does not establish a new hyperbolic case
or obstruct a source-specific upper bound after that sum.

## 1. Exact original source and its clock sectors

Use N>=2, d=N-1, q=exp(pi*i/N), Q=q^2, and exactly the enhanced
crossing/pivot conventions of
[the original crossing audit](kashaev_crossing_and_period_lattice.md):
mu=-q S and alpha=-q. Take the positive two-strand word [1,1,1],
with its original fixed first cut. The exact cyclic-source peeling
proof gives

    K_N=Q^(-1) (T_+^3)_(0,1).                       (1)

Here K_N is the original reduced enhanced period with unknot value
one. In the full modified-trace convention multiply EVERY sector
and both sides of the subsequent identities by its original known
external line. That common line is retained and has no exponential
modulus at completeness; it is never replaced by an unknown scalar.

The factor Q^(-1)=(-q)^(-2) includes the ORIGINAL closing coefficient
and full writhe correction. No new average, source or normalization
is introduced. The entries of this actual boundary operator are

    T_(0,j)=Q^(1-j), T_(k,0)=0 for k>0,
    T_(k,j)=(-1)^(j-1) Q^[k+(j-1)(j-2)/2]
                              [k-1 choose j-1]_Q,
                 1<=j<=k<=d.                       (2)

All other entries vanish. These are the directly proved q-Pascal
entries of the original crossing, including T_(0,0)=Q.

Every supported cut path has first head zero throughout. At a
positive crossing its actual overclock is h=[b-a-1]+[a-c]=[b-1].
Thus its three clocks are (0,H,J), with H,J in 0,...,d, and its
intermediate second-head values are

    i(H)=H+1 if H<d, i(d)=0;
    i(J)=J+1 if J<d, i(d)=0.                       (3)

There is exactly ONE such peeled path for each supported clock pair.
The positive-index triangular block and the wrap row in (2) give

    K_(N;H,J)=0, H>J,
    K_(N;H,J)=(-1)^H Q^[1+H(H+1)/2]
                                   [J choose H]_Q, H<=J. (4)

This is an identity of actual original clock contributions, not an
arbitrary inserted coefficient. For J<d it follows by multiplying
T_(i(H),1), T_(i(J),i(H)) and T_(0,i(J)) and the factor Q^(-1).
For J=d it follows from

    [d choose H]_Q=(-1)^H Q^[-H(H+1)/2],

which is exact factorial reflection. This also includes H=J=d and
the absorbing wrap state zero. There is no excluded parity or prime
level and no division by F_N.

## 2. The same current after all charged full-block reductions

The source of (4) is also visible in the
[whole charged bridge coefficient](actual_global_charged_bridge_flow.md).
After its three full contractions and one loop extraction, put X,Y
for the two surviving anchors. Up to the explicitly retained unit
root phases its clock sector is

    (Q^(-J);Q)_J [X^d Y^(d-J)]
       B_(d-H)(Y,X;Q)
       B_H(X,Y;Q^(J+1))
       B_(d-J)(X,Y;Q^(H+J+1)),                    (5)

where B_L(U,V;a)=product_(r<L)(U-Q^r a V). The two parallel
X-to-Y intervals concatenate to length d+H-J. If H>J this contains
a FULL N-orbit, hence vanishes in the actual nilpotent source
X^N=Y^N=0. This recovers the exact support condition in (4).

If H<=J, the degree-complement identity at charge d fuses the two
remaining edges. Its binomial is [d-H choose J-H]_Q. Its last loop
has scalar

    (Q^(J+1);Q)_(d-J)=N/F_J,

while the first loop in (5) has modulus |F_J|. Therefore the
COMPLETE charged coefficient has modulus

    N |[J choose H]_Q|.                            (6)

The N is canceled by the original single exterior 1/N. The other
original W_h, kappa, pivot, framing and normalization factors are
retained; in this alternating singleton-bridge diagram they have
unit modulus, up to the common tame source line. Thus the large
sector survives the existing full-block/zero-charge/loop reduction.
Equation (4) independently supplies its exact normalized phase.

## 3. Two successive macroscopic cancellations

Choose H=floor(N/3), J=floor(2N/3). The uniform actual factorial
estimate gives

    log |[J choose H]_Q|
          =N[v_3/pi]+O(log N)>0,                  (7)

where v_3 is the regular ideal tetrahedron volume. Indeed, with
I(s)=integral_0^s log|2sin(pi*t)| dt, the rate is
I(2/3)-2I(1/3)=v_3/pi. This is the figure-eight volume rate, despite
the present closed word being the trefoil, whose volume is zero.
No figure-eight asymptotic theorem is a premise of (7).

The FIRST coherent sum is itself an exact general q-binomial
identity inside this actual source:

    sum_(H=0)^J K_(N;H,J)=Q F_J,
    F_J=(Q;Q)_J.                                  (8)

Use the finite q-binomial theorem with argument Q. This collapses
the entire H current before estimation. It lowers its maximal
rate, but does not make it polynomial: at J=floor(5N/6),

    log |F_J|=N[v_3/(2pi)]+O(log N)>0.             (9)

Thus even the partially summed current in (8) cannot be assigned
the closed knot's zero regulator or dropped as a small boundary.
The complete original scalar is exactly

    K_N=Q sum_(J=0)^d F_J.                         (10)

The last sum has polynomial size. This follows independently from
the already derived ACTUAL spectral-jet closing functional, not a
named torus-knot asymptotic. Write its normalized crossing as r_N.
At double nodes c=q^a+q^(-a), a odd, 0<a<N, it obeys

    r_N(c)=nu, |nu|=1,
    r_N'(c)/nu=-(N-a)/[2(q^a-q^(-a))].

The original pivotal functional is

    Phi(f)=-sum_double [c f(c)+(c^2-4)f'(c)]
                     + one simple-node value if N is odd.

For f=r_N^3, each first term has modulus at most 2 and each
derivative term at most 3N, because c^2-4=(q^a-q^(-a))^2.
The possible simple-node term has modulus one. The full writhe
factor is (-q)^3, of modulus one. Hence, at EVERY level,

    |K_N|<=3N^2.                                  (11)

All node derivatives and the original pivotal source are retained
in this bound. These formulas were independently proved from the
finite R and its generic tensor specialization in
[the spectral source note](casimir_braiding_and_recoupling_lattice.md).
They do not rely on semisimplicity at the root.

## 4. Consequence for the next source-specific operation

The first fusion (8) is constructive and exact, but a second
macroscopic cancellation is still needed. A bound on individual
fixed-h charged coefficients, or even on the first fused current
at each J, cannot equal the closed knot regulator. Those currents
are not separately honest closed-knot representation periods.

The new physical-face outward estimates can control their actual
endpoint continuations; they do not remove the internal coherent
sum exhibited by (8)--(11). A proposed broad source fusion must
retain and use that final clock connection, rather than fixing
the clocks and then applying a knot-volume bound. This is an
explicit failure of that sectorwise route, not a no-go for phase-aware
fusion of the entire original source or the volume conjecture.

No arbitrary consecutive-run or arbitrary-width positive-kernel
extension is claimed here. The theorem is restricted to the actual
source and exact current proved above.

[Audit](../experiments/audit_actual_overclock_sector_obstruction.py)
checks every sector against the literal original crossing, both
coherent sums, the original spectral normalization, the fully reduced
charged coefficients and the displayed exponential rates.
