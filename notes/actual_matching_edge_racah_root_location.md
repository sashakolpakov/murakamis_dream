# The source-normalized Racah polynomial has all its zeros above two

30 October 2026. For EVERY folded original
channel, the exact matching-edge Casimir polynomial has simple real
zeros strictly greater than 2. A positive matrix factorization proves
this, including maximal channels at both level parities. Its canonical
logarithm and leading action consequently continue to the whole slit
plane C minus [2,infinity), including every real geometric target below
2. No continuation of a finite target color g is required.

This theorem concerns the actual scalar polynomial. It does not prove
a relative amplitude, control moving-q normal derivatives, estimate
the complementary tensor contraction, or select a global source cycle.

## 1. The exact original polynomial at the root

Use the generic source identity proved in
[the geometric target polynomial theorem](actual_matching_edge_geometric_target_polynomial.md).
Its normalization is

    D_a G_ag D_g=p_a(lambda_g),
    lambda_g=zeta^(2g+1)+zeta^(-2g-1),

with all generic source factors retained. Put q=exp(pi i/N),
theta=pi/N, d=N-1, 0<=a<=M=floor(d/2), and specialize to q.
Let s_k=product_(r=1)^k 2sin(r theta), and set

    lambda_r=2cos((2r+1)theta),
    phi_k(x)=product_(r=0)^(k-1)(lambda_r-x).

The generic terminating formula becomes EXACTLY

    p_a(x)=sum_(k=0)^a c_(a,k) phi_k(x),
    c_(a,k)=s_(a+k)/(s_(a-k)s_k^4).                 (1)

Indeed [d-r]=[r+1] and [d+r+2]=-[r+1] at q, so the generic
alternating signs cancel. Also

    [g-r][g+r+1]=(lambda_r-lambda_g)/(4sin^2 theta),
    product_(r<k)(lambda_r-lambda_a)=s_(a+k)/s_(a-k).

These identities yield (1) without changing the original spectral
variable. In particular p_a(lambda_0)=1 and its leading coefficient is

    kappa_a=(-1)^a s_(2a)/s_a^4.                    (2)

All displayed denominators are nonzero for 2a<N. For a=0 the
polynomial is identically one.

## 2. An own three-term recurrence

For 0<=n<M define

    A_n=-4sin^4((n+1)theta)
                    /[sin((2n+1)theta)sin((2n+2)theta)],
    B_n=2/[cos(n theta)cos((n+1)theta)],
    C_n=-4sin^4(n theta)/[sin(2n theta)sin((2n+1)theta)],
    C_0=0.

Then the finite polynomials (1) satisfy

    x p_n(x)=A_n p_(n+1)(x)+B_n p_n(x)+C_n p_(n-1)(x).          (3)

Here is a direct coefficient proof. Since
x phi_k=lambda_k phi_k-phi_(k+1), the coefficient of phi_k on
the left is lambda_k c_(n,k)-c_(n,k-1). The required ratios are

    c_(n+1,k)/c_(n,k)=sin((n+k+1)theta)/sin((n-k+1)theta),
    c_(n-1,k)/c_(n,k)=sin((n-k)theta)/sin((n+k)theta),
    c_(n,k-1)/c_(n,k)
       =4sin^4(k theta)/[sin((n+k)theta)sin((n-k+1)theta)].       (4)

Substitution in (3), followed by the sine addition identities,
gives equality. More explicitly the identity after division by
c_(n,k) is

    lambda_k-4sin^4(k theta)/[sin((n+k)theta)sin((n-k+1)theta)]
      =A_n sin((n+k+1)theta)/sin((n-k+1)theta)
         +B_n+C_n sin((n-k)theta)/sin((n+k)theta).

It is a rational identity in exp(i theta), exp(i n theta) and
exp(i k theta); clearing its displayed denominators gives zero.
The top coefficient k=n+1 is A_n=kappa_n/kappa_(n+1).
The case n=0 follows directly from p_0 and p_1. Thus no presumed
orthogonality or external q-Racah recurrence enters the proof.

Set P_n=p_n/kappa_n, the monic polynomials. Equation (3) becomes

    P_(n+1)=(x-B_n)P_n-e_n^2 P_(n-1),
    e_n^2=A_(n-1)C_n
       =4sin^6(n theta)
          /[cos^2(n theta)sin((2n-1)theta)sin((2n+1)theta)]>0.   (5)

Consequently P_a(x)=det(xI-J_a), where J_a is the real symmetric
Jacobi matrix with diagonal B_0,...,B_(a-1) and adjacent entries
e_1,...,e_(a-1)>0.

## 3. The positive shift by two

Let Dpos_a be the previously proved positive q-Hahn matrix; the
distinct scalar face factor retains its original name D_a:

    (Dpos_a)_(n,n)=1/[cos(n theta)cos((n+1)theta)],
    (Dpos_a)_(n-1,n)=sqrt(beta_n),
    beta_n=sin^2(n theta)
          /[cos^2(n theta)sin((2n-1)theta)sin((2n+1)theta)].

For completeness, its leading principal minors are

    det Dpos_m=2^m product_(r=1)^m sin(r theta)
                        /product_(r=m+1)^(2m)sin(r theta)>0.

This finite formula was proved by the determinant recurrence in
[the original q-Hahn determinant theorem](actual_q_hahn_joint_accretive_determinant.md#4-a-positive-definite-real-part).
Every factor is positive because 2m<N, so Dpos_a is positive definite
also at a=M. Put

    H=diag(sin((n+1/2)theta))_(n=0)^(a-1),
    s0=sin(theta/2).

There is the exact matrix factorization

    J_a-2I=2 H Dpos_a H+2s0^2 Dpos_a.              (6)

The diagonal identity is
sin^2((n+1/2)theta)+sin^2(theta/2)
=1-cos(n theta)cos((n+1)theta).
The adjacent identity is
sin((n-1/2)theta)sin((n+1/2)theta)+sin^2(theta/2)
=sin^2(n theta). These are precisely the entries in (5),(6).

The right side of (6) is positive definite. Therefore EVERY
eigenvalue of J_a is strictly greater than 2. The nonzero adjacent
entries also imply simple spectrum: an eigenvector is determined
by its first coordinate through the tridiagonal recurrence, and
that coordinate cannot vanish. Hence

    ALL zeros of p_a are simple, real, and strictly greater than 2. (7)

This is uniform in the folded channel, with no restriction to
odd levels or to channels bounded away from the fold.

## 4. The canonical logarithm and its uniform derivative bounds

Write the zeros as r_1,...,r_a>2. Since p_a(lambda_0)=1,

    p_a(x)=product_(h=1)^a (r_h-x)/(r_h-lambda_0).

On Omega=C minus [2,infinity), define

    Log p_a(x)=sum_h Log((r_h-x)/(r_h-lambda_0)),     (8)

where each logarithm is continued from its positive real value
at any x<2. Equivalently its argument has the principal logarithm
in each individual factor. This is a single holomorphic branch
on Omega, real on the whole interval x<2. For m>=1,

    |partial_x^m Log p_a(x)|
       <=(m-1)! a/dist(x,[2,infinity))^m.           (9)

Thus the original scalar itself, rather than a complexly continued
finite color g, supplies a canonical selected branch at every
geometric real target x<2.

## 5. Leading source action continues through the physical endpoint

Here the scalar leading limit can also be proved directly. Let
a_N/N tend to alpha in (0,1/2]. For a real x<-2, every term in
(1) is positive. Uniform sine-factorial estimates and Riemann sums
give

    N^-1 log p_(a_N)(x) -> max_(0<=t<=alpha) E_alpha(t;x),
    E_alpha(t;x)=J(alpha+t)-J(alpha-t)-4J(t)
                    +integral_0^t log(2cos(2pi u)-x) du,
    J(v)=integral_0^v log(2sin(pi u)) du.            (10)

The endpoint logarithmic singularities in the sine factorials
cost O(log N), uniformly in their integer indices. The final
integrand in (10) is smooth and positive-argument for x<-2.
The number of summands is at most N, so maximum-term comparison
proves (10), including sequences approaching the folded channel.

The maximum is unique and interior. Put A=sin^2(pi alpha), v=2-x
and z=sin^2(pi t). Its derivative is

    partial_t E=log[(A-z)(v-4z)/(4z^2)].

For x<-2 this strictly decreases from +infinity to -infinity.
The critical equation is linear after cancellation of its z^2
terms, and gives

    z_*=A v/(v+4A),
    t_*=pi^-1 arcsin(sqrt(A v/(v+4A))).             (11)

Now fix an anchor x0<-2. The bounds (9), divided by N, make
N^-1 Log p_(a_N) a locally bounded normal family on the connected
slit domain Omega: its value at x0 is bounded by (10), and its
derivative is uniformly bounded along any fixed compact path.
Every subsequential holomorphic limit agrees with (10) on the
real interval x<-2. The identity theorem therefore makes the
limit unique. Consequently

    N^-1 Log p_(a_N)(x) -> Psi_alpha(x)             (12)

locally uniformly on ALL of Omega, with every fixed x derivative.
This is the actual source logarithm (8), not a formally chosen
solution of a characteristic equation.

On the entire real interval x<2 the continuation is explicitly

    Psi_alpha(x)=E_alpha(t_*(x);x),                 (13)

with (11). Indeed 0<z_*<min(A,v/4), so all logarithms in the
integral up to t_* have positive arguments. Formula (13) is real
analytic on x<2 and agrees with (10) on x<-2, proving the claimed
continuation. In particular the passage through x=-2 is regular.
There is no claimed uniformity at the removed boundary x=2.

The result proves a leading selected SCALAR action. It does not
turn the original tensor contraction into a scalar evaluation,
or justify discarding its generic first normals. Those distinctions
remain essential to the global volume problem.

Audit: [original root values, the own recurrence and positive matrix shift](../experiments/audit_actual_matching_edge_racah_root_location.py).

The result concerns the scalar polynomial and its leading action. It does not replace the contracted operator by that scalar.