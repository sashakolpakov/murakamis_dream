# Original three-channel corner and the positive factorial identity

29 October 2026. The original coproduct fixes a general trivalent corner,
including its endpoint phases, at both level parities. The positive
factorial evaluation is now proved by the
[short finite transformation](actual_trivalent_square_linearization_bridge.md)
and the independent [Fourier/Newton transformation](finite_trivalent_euler_racah_transform.md).
This historical filename retains the original formulation and exact
source normalization. The [general theorem and regular-cube corollary](actual_trivalent_all_channel_positive_scalar_and_regular_cubes.md)
record the completed scope. No graph-volume equality or full vertex
norm is inferred from this scalar theorem.

## 1. General physical columns and endpoint phases

Put d=N-1, q=exp(pi i/N), Q=q^2, x=q^d=-q^-1,
F_r=(Q;Q)_r and s_r=|F_r|. For 0<=j<=floor(d/2), let h=d-j and

    H^(j)_a=q^(a^2)[h choose a]_Q at |a,h-a>,
    W^(j)_r=F_pair^r H^(j)/F_r, 0<=r<=2j.             (1)

These are the original balanced physical pair and its original ordered
coproduct. The highest equation follows directly from

    H_(a+1)/H_a=-x^-1 Q^a(1-Q^(h-a))/(1-Q^(a+1)).

For a+b=h+r, their finite binomial expansion is

    W_r(a,b)=F_a F_b F_h
      *sum_s q^(s^2)x^(-r+a-s)Q^[s(r-a+s)]
       /[F_s^2 F_(h-s)^2 F_(a-s) F_(r-a+s)],          (2)

where max(0,a-r)<=s<=min(h,a). All denominators have index<N.
This follows by expanding F_pair=A+B with AB=Q^-1 BA, just as in
the [central proof](actual_trivalent_steinberg_central_anchor.md).

The exact endpoints at EVERY retained j are

    W_(2j)(j+t,d-t)=ell_j H_t, 0<=t<=h,
    ell_j=q^[j(d-2j)],
    W_j(0,d)=q^(-j^2).                                (3)

For the first, its lowest-vector recurrence fixes the successive ratios;
the first coefficient in (2) is

    q^(-j^2) sum_s Q^(s^2)[h choose s]_Q[j choose s]_Q
       =q^(-j^2) F_d/(F_h F_j)=q^[j(d-2j)].

The equality in the middle is finite Vandermonde, proved by coefficient
extraction in the finite binomial product. Root reflection gives
F_h F_j=N(-1)^j q^[j(j+1)] and F_d=N. The last expression in (3)
comes from the sole s=0 term of (2). The displayed lowest column also
has zero next F arrow by its literal ratio; no generic semisimple
decomposition is assumed.

## 2. The corner of the actual black tensor

Choose j_1=a, j_2=b, j_3=c with the triangle inequalities and let
r=b+c-a. The magnetic indices (2a,r,0) have physical pair degrees

    (d+a, d-a+c, d-c),

whose sum is exactly 3d. Apply the three rows W^dagger P to the
original nested cup source p_16 p_23 p_45. Its corner is N^3 A_N,
where the exact original-source kernel gives

    A_N=conjugate(ell_a) sum_(k=0)^min(d-a,d-c)
       x^(k+a+c-2d)
       conjugate[H^(a)_k H^(c)_k
                  W^(b)_r(c+k,d-a-k)].               (4)

Indeed set the first physical cup color to d-k in the literal
[black vertex kernel](actual_trivalent_complete_circle_vertex_kernel.md).
Its other two colors are a+k and c+k. Formula (3) then gives (4),
including the conjugate lowest-column scalar. The positive evaluation
below is proved by the separate finite transformations linked above.

## 3. Precisely normalized positive evaluation

Set J=a+b+c and delta=J-d. For delta>=0 define

    R_N=N sum_(max(a,b,c)<=t<=min(a+b,a+c,b+c))
      s_t/[s_(t-a)s_(t-b)s_(t-c)s_(d+t-J)
                       s_(a+b-t)s_(a+c-t)s_(b+c-t)],
    C_N=s_a s_b s_c/(N s_delta),
    e=2a^2-ab-ac+bc-J-3.                              (5)

The proved original-source identity is

    A_N=(-1)^(N+J) q^e C_N R_N,   J>=d;
    A_N=0,                       J<d.                (6)

The zero branch is now proved independently by the
[root-Fourier coefficient theorem](actual_trivalent_root_fourier_source_certificate.md):
the actual scalar is a specified coefficient of degree d in a polynomial
of degree J. That proof keeps the complete Fourier mode and its exact
low-mode cancellation. The two finite transformations linked above
prove the positive branch, its exact phase, and every root denominator.

The asymmetry of e belongs to the specified ordered corner (2a,r,0).
The positive modulus C_N R_N is symmetric. Neither C_N nor the support
cutoff may be suppressed. For example the unnormalized candidate has
R_N(0,0,0)=1 whereas the original source is zero, and at even N=4,
a=b=c=1 one has R_N=2sqrt(2), C_N=1/sqrt(2), |A_N|=2.

At odd N=2m+1, (a,b,c)=(m,j,m), C_N=1 and (6) reduces to the
[proved one-channel formula](actual_trivalent_one_channel_source_packet.md).
At the even nearest center a=b=c=N/2-1, C_N=cos(pi/N), consistent
with the separately proved
[weighted quartic and retained normal](actual_trivalent_even_central_normal_packet.md).

The [joint scalar saddle theorem](actual_trivalent_candidate_racah_partition_geometry.md)
proves a unique joint saddle, a strict global color gap, and a complex
packet for the positive expression in (5). Through the proved (6),
these are now original-source SCALAR estimates. The
complete CD normalization, the magnetic tensor, ordinary/marked
white rows and their ordered sewing are additional data.

## 4. Exact checks and their logical limit

The [independent finite-source audit](../experiments/audit_actual_trivalent_general_scalar_candidate.py)
builds W from the ORIGINAL coproduct, instead of (2) or (5), and
evaluates the literal source corner. It checks every retained triangle
triple at N=2,...,16: 539 supported triples and 1,212 vanishing triples,
including all root phases and both parities. It also checks (3) at
every retained j in those levels. A separate high-precision calculation
checked the full complex phase and modulus on all 636 triangle triples
at N=2,...,13; an additional 305 supported triples at N=11,13,17
were used to determine and check the candidate phase modulo N.

These computations supply reproducible counterexample searches and
normalization evidence. They do not by themselves prove the positive
branch of (6) for arbitrary N. That proof is the finite algebra linked
above, with an independent derivation and internal analytical reviews;
it is not an assumed literature identity.
