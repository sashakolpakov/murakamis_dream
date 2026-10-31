# Root-channel H insertions and their actual relative-period transport

30 October 2026. The two root insertions
in the [normal adapter](actual_explicit_root_channel_normal_adapter.md)
admit a specified meromorphic representative with polynomial size on
the original resonant chart. This is an exact change of representative
of the original finite root period. Its different relative boundary
currents are computed below; no off-grid equality with the generic
descendant or finite clock polynomial is asserted.

## 1. The finite insertion and three continuations

Put N>=2, d=N-1, q0=exp(pi i/N), Q=q0^2, and

    H_l=2N sum_(j=1)^l (1-Q^j)^-1, 0<=l<=d; H_0=0.

The actual adapter uses H=diag(H_l) and X(p)H in the SAME routed
root channel C0. It proves

    eta I=(C0-z0 Id)(H),
    Delta'_0(p)=eta X(p)-(C0-z0 Id)(X(p)H),
    X(p)_(r,s)=p^(r-s)/N.                              (1)

Here Delta_e=C_e(X(p))-z(e)X(p). The scalar derivative z'(0)
is separate. The following calculation transports the literal ROOT
insertions in (1), not a differentiated root simplification of C_e.

Let Fhat_P be the specified [moving-period factorial](actual_moving_period_factorial_normals.md),
P=pi i/Log(q0 exp(e)), and P'=iN^2/pi. Its logarithmic index
derivative f'(z)=partial_z Log Fhat_N(z) is single valued meromorphic.
Define

    Hhat(x)=P'[f'(d-x)-f'(d)].                          (2)

This function has Hhat(l)=H_l on the physical interval. In contrast,
the actual finite diagonal descendant has the specified continuation

    h_e(x)=exp(pi i x) zeta^[x(x+1)]
                      Fhat_P(d)/[Fhat_P(x)Fhat_P(d-x)].

Exact moving-period reflection, with d FIXED, gives

    h_0(x)=Y,       partial_e h_e(x)|0=Y Hhat(x),
    Y=exp(2pi i x)=U^N, U=exp(2pi i x/N).                (3)

Here b_d is the exact fixed-endpoint gauge

    b_d(e,x)=zeta^[x(d-x)]
                 Fhat_P(x)Fhat_P(d-x)/Fhat_P(d).

Indeed h_e=exp(pi i x)zeta^(Nx)/b_d(e,x). Differentiating
the exact fixed-endpoint reflection gives
partial_e Log b_d=P'[f'(d)-f'(d-x)-pi i x/N]; hence
partial_e Log h_e=Nx-partial_e Log b_d=(2).
The character Y in the LITERAL derivative (3) has not been dropped.

There is also the unique polynomial in the actual clock of degree<N:

    Hpol(U)=meanH-2 sum_(r=1)^d r U^r/(1-Q^-r),
    meanH=2 sum_(r=1)^d r/(1-Q^-r).                     (4)

Finite Fourier inversion in the adapter proves Hpol(Q^l)=H_l.
Thus Hpol(U), Hhat(x), and Hlit(x)=Y Hhat(x) have identical
physical values, but they are DIFFERENT meromorphic functions.

## 2. An exact algebraic formula for the tame representative

The Gamma-defined function (2) is in fact the following finite
rational expression in U and the retained logarithmic head x:

    S(U)=sum_(r=1)^d U^r/(1-Q^-r),
    Hhat(x)=2N[x-d/2+S(U)]/(1-Y)+meanH+N/(pi i).         (5)

Physical singularities in (5) are removable. Here is a direct proof,
including the normalization. Write Halg for its right side. Since

    S(QU)-S(U)=sum_(r=1)^d (QU)^r,

one obtains

    Halg(x+1)-Halg(x)=2N/(1-QU),
    Halg(x+N)-Halg(x)=2N^2/(1-Y).                       (6)

This is an explicit additive cyclic descent. For any rational b(U),
let sigma U=QU, let mean_b=N^-1 sum_(j=0)^(N-1) sigma^j b, and put
R=N^-1 sum_(j=0)^(N-1) j sigma^j b. One telescoping sum proves
sigma R-R=b-mean_b. Extending sigma by sigma x=x+1, the function
x mean_b+R therefore solves its full, possibly nonzero-trace,
difference equation. Here b=2N/(1-QU), mean_b=2N/(1-Y), and
R=2N[d/2+S(U)]/(1-Y). Formula (5) makes the invariant correction
-d mean_b+meanH+N/(pi i). The zero-trace part is solved rationally;
the nonzero trace requires the retained logarithmic head x. This
is the elementary descent calculation itself, not an imported
cohomology theorem or a choice of a source-period coefficient.

At l=0,...,d, S(Q^l)=d/2-l. L'Hopital's rule in (5) gives
Halg(l)=meanH-2 sum r Q^(rl)/(1-Q^-r)=H_l, including Halg(0)=0.
At every integer l its residue is P' floor(l/N).

The factorial unit equation gives the SAME unit difference (6)
for (2). The original Gamma product has no zeros or poles off the
integer lattice when P=N: its initial Gamma factor and numerator
factors give the negative-integer poles, while its denominator
factors give the positive-integer zeros. Counting these factors in
f'(d-x) gives residue P' floor(l/N), exactly as above. Consequently
Halg-Hhat is entire and 1-periodic.

For completeness, this entire difference has polynomial vertical
growth at fixed N. In the direct formula for partial_P Log Fhat_P,
split the convergent digamma sum at K comparable to
1+|Im x|/N, with 0<=Re x<=1. The first K terms cost O_N(K^2);
the tail, by the same canceled digamma expansion used in the
[logarithmic-escape estimate](actual_moving_period_factorial_logarithmic_escape.md),
costs O_N((1+|Im x|)^3/K). Thus (3) gives Hhat=O_N(1+|Im x|^2).
Halg is at most linear vertically, as follows directly from (5)
at U->0 and U->infinity. All nonzero Fourier coefficients of the
entire periodic difference therefore vanish: move their horizontal
integration line to the half-plane where the Fourier exponential
decays. The difference is constant, and its value at zero is zero.
This proves (5), without selecting an unproved periodic correction.

The two exact marked transport rules are consequently

    Hhat(x+N)-Hhat(x)=2N^2/(1-Y),
    Hlit(x+N)-Hlit(x)=2N^2 g(x),
    g(x)=Y/(1-Y).                                      (7)

Hpol is N-periodic. Even their unit differences are distinct:

    Hpol(QU)-Hpol(U)
      =2N Y/(1-QU)-2QU(1-Y)/(1-QU)^2,
    Hlit(x+1)-Hlit(x)=2N Y/(1-QU).                      (8)

The extra term vanishes at interior physical nodes. It cannot be
discarded in a continuation through the missing endpoint arrow.

## 3. Exact finite periods and the polynomial insertion bound

Retain an original charged band delta, its primitive integral head
lattice, actual finite support, original marked co-source, and every
outside tensor. In that band X(p)H has the finite weight
p^delta H_l/N at the second INPUT head l. H alone is the zero-band
diagonal weight. Replace H_l by Hhat(l) in the original finite sum;
this changes no term, at every N and either parity.

The equivalent initial cotangent realization uses the original
ordered small tori with normalization (2pi i)^(-n_free). On an
admissible node where the retained source germ is holomorphic, the
cotangent residue evaluates the multiplier at that node, so each
of the three representatives gives EXACTLY the same inserted period.
An original representation with extra source poles must first retain
its actual cancellations or its recorded ordered finite parts;
agreement of point values alone never identifies such finite parts.
The external finite head weights may always be kept outside those
internal periods until this condition is met. No source-null polar
torus is added merely by choosing a new interpolation.

On the physical-head logarithmic strips of the
[common original chart](actual_original_network_resonant_boundary_chart.md),

    delta<=Re(x/N)<=1-delta,
    |Im(x/N)|<=C(1+log N),

both x and d-x obey the moving-factorial estimates. The exact identity

    Hhat(x)=x(x+1)+g_d-g_x-g_(d-x),
    g_z=partial_e Log Fhat_(P(e))(z)|0,

first gives a polynomial bound. Formula (5) sharpens it to, with
L_N=1+log N,

    |partial_x^j Hhat(x)|<=C_j N^(2-j) L_N              (9)

for each fixed j, on a slightly smaller strip. Here is a direct
proof. The elementary sine lower bound gives
sum_(r=1)^d |1-Q^-r|^-1=O(N log N) and meanH=O(N^2 log N).
When |Im x|>=1, |1-Y| is comparable to max(1,|Y|), and each
|U^r|/max(1,|Y|)<=1. With |x|=O(N L_N), (5) gives the bound.
When |Im x|<=1, use fixed-radius disks about the physical integers.
The numerator B=x-d/2+S(U) vanishes at their centers, and
|B'|=O(N log N) on those disks; the denominator has a uniformly
simple zero there. Outside the disks it is bounded away from zero.
This proves the same bound across every removable physical point.
Higher derivatives follow by Cauchy on a pole-free head disk of
radius cN. The proof also covers the nonreal exterior class
|Re(x/N)|<=C, delta<=|Im(x/N)|<=C L_N, with a smaller such disk.
It does not include approaches to an outside-head integer pole.
This is an ABSOLUTE bound, not
nonvanishing or a relative estimate at a zero of Hhat. The factor
p^delta/N is retained; it is at most e^A/N when |log|p||<=A/N.

This advantage belongs to the NEW root-period representative.
For example, on |U| comparable to N^2, the literal clock polynomial
has the asymptotic

    Hpol(U)=-2d U^d/(1-Q^-d) [1+O(N^-2)].               (10)

Indeed every nonconstant coefficient is O(N^2), the top one has
magnitude at least cN^2, and the geometric tail is O(|U|^-1);
the constant coefficient is O(N^2 log N). The exact power U^d
remains. The literal descendant normal has its own factor U^N
in (3). Neither can silently be replaced by the bound (9) OFF GRID.
Only the exact finite-period replacement and its boundary corrections
justify choosing Hhat for a subsequent deformation.

## 4. Inserted-period translation and explicit endpoint anomalies

Let S0(x) be an original root source on a primitive free lattice,
after its recorded scalar Laurent cancellations. For an integral
translation b suppose the actual tensor connection gives
S0(x+Nb)=chi(b)S0(x). Let l(x) be the second physical head and
k=D_b l its integral slope. Keep delta fixed in the X(p)H band.
Any retained external weight not covered by this proved quasiperiod
keeps its shifted value explicitly; an interpolated coherent row,
for example, is not assigned the tensor's parity character.
Write I_Gamma for the original cotangent period, with its complete
marked source and normalization. Changing variables and using (7)
gives the exact identities

    I_(Gamma+Nb)[Hhat(l)S0]
      =chi(b){I_Gamma[Hhat(l)S0]
                     +2N^2 k I_Gamma[S0/(1-Y_l)]},
    I_(Gamma+Nb)[Hlit(l)S0]
      =chi(b){I_Gamma[Hlit(l)S0]
                     +2N^2 k I_Gamma[g(l)S0]}.          (11)

They apply bandwise with p^delta/N and to their original finite sum.
The displayed root quasiperiod is a hypothesis on the genuinely
canceled root coefficient. For an uncleared Laurent sector use the
full finite-jet connection first: its constant coefficient can mix
lower Laurent coefficients under translation.
For Hpol there is no insertion correction in this N-translation,
but its difference from the other representatives carries precisely
the opposing current. These are continued-cycle identities, not
permission to wrap any physical head or identify Gamma+Nb with Gamma.

The first two outside-head Laurent coefficients are explicit. If
y=x-x0, write Hrep=R/y+B+O(y). Then

    representative       x0=-1: (R,B)              x0=N: (R,B)
    Hhat                  (-P',-N)                 (P',N^2)
    Hlit                  (-P',2N^2-N)             (P',-N^2)
    Hpol                  (0,N(N-1))               (0,0).       (12)

For Hhat these follow from (6), Hhat(0)=0 and Hhat(d)=N(N-1).
Multiplication by Y changes the finite part by 2pi i R, where
2pi i P'=-2N^2. Hpol has its literal periodic node values.
More generally, write ANY integer l=mN+r with 0<=r<=d. The same
translation gives the complete carry table

    Hhat(l+y)=mP'/y+H_r+mN^2+O(y),
    Hlit(l+y)=mP'/y+H_r-mN^2+O(y),
    Hpol(Q^(l+y))=H_r+O(y).                             (12a)

Thus every integral deck carry has an explicit anomaly, including
negative carries; none is turned into an allowed physical state.
Against pi cot(pi x) and a complement regular at x0, the crossed
residue is therefore

    B S0(x0)+R partial_x S0(x0).                       (13)

In particular the two correction densities in (11), at a primitive
integer head with regular complement, have residues respectively

    2N^2 Res[pi cot(pi l) S0/(1-Y_l)]=P'S0'+N^2 S0,
    2N^2 Res[pi cot(pi l) g(l)S0]=P'S0'-N^2 S0.          (14)

The derivative of the actual complement is required. If l=A x_j+B
is not itself primitive, its pulled-back measure is
(pi/A)cot(pi(l-B)/A) dl. Use that measure and its Jacobian; if it
is regular at a crossed head wall its value multiplies the residue
instead. When l is constant on the free lattice there is no such
head deformation. Intersections with other source divisors require
their original iterated or multivariable residues, not (13).

To deform either initial representative to a proposed geometric
relative cycle, apply the [common-band chain identity](actual_matching_graph_common_band_ward_current.md)
to its actual support. Every crossed source tube, the anomalies
(12)--(14), and all remaining relative ends stay in that identity.
The polynomial bound (9) supplies no reason for those ends to vanish.
Explicitly, for a difference D of two representatives and a specified
oriented deformation Gamma_phys=Gamma_new+sum T_j+Gamma_end,
the initial equality gives

    I_Gamma_new[D S0]=-sum_j I_T_j[D S0]
                                  -I_Gamma_end[D S0].   (14a)

Here the T_j are the ACTUAL crossed-divisor tubes and the last term
retains the actual relative end. Formula (14a) is used only when that
deformation is constructed; it does not supply one. In particular,
pointwise growth of Hpol on the boundary is not an obstruction to
using Hhat, but replacing it there without (14a) is not justified.

## 5. What the H-weighted Ward equation does and does not compute

The literal truncated relation [H,F0]=2N T_1 proves scalarity in (1):
K covariance makes (C0-z0 Id)(H) diagonal, and F covariance forces
its diagonal entries equal. It does not give eta.

More explicitly use the ACTUAL coherent current M_l and L_a in the
[braided current theorem](actual_braided_residual_framing_current.md),
with beta_a the legitimate first-cut binomial row. Weight its finite
interval identity by H_l. On the WHOLE physical interval its endpoint
arrows vanish, and the identity reduces to

    sum_(l=0)^(d-1) M_l/(1-Q^(l+1))
      =z0 sum_(a=0)^(d-1) L_a/(1-Q^(a+1))
      =z0[1-q0-beta_d+q0 beta_0].                      (15)

The eta I term disappears because the dual Ward row annihilates I.
At the root M_l/(1-Q^(l+1)) is the actual pairing of
C0(E_(l+1,l)-q0 E_(l,l+1)); thus (15) is precisely the already known
unwrapped Toeplitz identity. On a proper interval the terms
H_R M_R-H_L M_(L-1) remain. They are not determined by scalarity.

Equations (5), (9), and (11)--(14) give a concrete reduction: the
adapter's TWO inserted root periods may use tame, algebraically
specified head weights, with explicit relative-transport currents.
What remains is the pushforward of those original charged cycles and
their endpoint/divisor chain to the geometric framing boundary.
Neither a nonzero relative end, a geometric contribution coefficient,
a bound for the full root channel, nor z'(0) is computed here.

Focused verification: [source/transport audit](../experiments/audit_actual_root_channel_H_period_transport.py)
and [saved results](../experiments/actual_root_channel_H_period_transport_results.json).
It checks 299 removable physical nodes, 912 unit/level transports,
228 exact cyclic descents, 1495 general carry expansions, and 24
residue/Jacobian identities. Nine original routed sources supply 54
inserted-period comparisons and nine actual weighted Ward identities.
Twelve logarithmically escaping moving-factorial heads give 24
independent reflection/algebraic comparisons, 12 retained characters,
and six clock-growth checks at 75 digits; the maximum identity error
is below 6.05e-72. These finite and analytic checks do not assert a
global contour deformation or a relative contribution coefficient.

The H-period transport retains the end contribution in (14a).

The source quasiperiod is conditional, and the Ward conclusion is scalarity only. The theorem does not evaluate the geometric relative end.