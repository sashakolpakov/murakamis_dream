# An exact odd central Clebsch anchor for the trivalent source

29 October 2026. At the odd-level simple Steinberg channel, the actual
trivalent black source has one genuine three-channel invariant tensor
and one explicit finite scalar. Its highest and lowest Clebsch columns,
middle column, normalization and positive complete-circle factor are
computed below. Its coherent scalar is then evaluated by OWN finite
binomial identities as a positive fourth-power sine-binomial sum,
with a nonzero all-odd asymptotic. This supplies a central anchor for the new
[ordered branching packet](actual_trivalent_complete_circle_vertex_kernel.md).
No even-level confluence estimate, uniform complex packet, global
source survival or geometric maximum is claimed.

## 1. The actual simple channel and its full Clebsch columns

Let N=2m+1>=3, d=2m, q=exp(pi i/N), Q=q^2, x=q^d=-q^(-1),
F_r=(Q;Q)_r. Use the ORIGINAL balanced Ecal,F,K and their ordered
coproducts. Define a physical pair vector of degree m by

    h=sum_(a=0)^m h_a |a,m-a>,
    h_a=q^(a^2) [m choose a]_Q
       =q^(ma) beta(m,a),
    beta(m,a)=|[m choose a]_Q|.                          (1)

The last equality uses the principal root: the Gaussian binomial has
phase q^[a(m-a)], and all its sine factors have positive sign. Its
highest-vector equation follows from the literal ratio

    h_(a+1)/h_a
      =-x^(-1) Q^a (1-Q^(m-a))/(1-Q^(a+1)).            (2)

Indeed Ecal_pair h=0 and its highest K is x, so its Casimir is -2.
Put

    W_r=F_pair^r h/F_r, 0<=r<=d,
    W|r>=W_r.                                         (3)

The same original commutator used for a physical highest-weight-N
module gives

    F_pair W_r=(1-Q^(r+1)) W_(r+1),
    Ecal_pair W_r=(Q^(-r)-1) W_(r-1),
    K_pair W_r=x Q^(-r) W_r.                           (4)

Endpoints are zero. All interior coefficients in (4) are nonzero, so
W is an actual injective Hopf intertwiner V_N -> V_N tensor V_N.
There is no generic semisimple replacement of the root module here.

Every entry has the explicit finite Clebsch form. If b=m+r-a and
0<=a,b<=d, then

    W_r(a,b)=F_a F_b F_m
       *sum_s q^(s^2) x^[-r+a-s] Q^[s(r-a+s)]
        /[F_s^2 F_(m-s)^2 F_(a-s) F_(r-a+s)],          (5)

where max(0,a-r)<=s<=min(m,a). If a or b is outside the physical
basis, the entry is zero. All denominator indices in this finite
range are less than N. To prove (5), write F_pair=A+B with
A=F_1, B=K_1^(-1)F_2, so AB=Q^(-1)BA. Expand

    (A+B)^r=sum_k [r choose k]_Q A^k B^(r-k),

and apply its k=a-s term to the s-th summand of (1). Dividing by
F_r leaves precisely the six displayed factorials. Thus (5) is an
own finite binomial calculation, with its full root phases.

## 2. Exact source normalizations, including both ends

Two useful cancellations are

    W_d(m+t,d-t)=h_t, 0<=t<=m,
    W_m(0,d)=q^(-m^2).                                 (6)

For the first, the lowest-vector equation in (4) shows that its
successive ratio is the ratio in (1); only its first scalar needs
checking. Substitute r=d,a=m in (5), then use

    F_t F_(d-t)=N(-1)^t Q^[t(t+1)/2].                  (7)

Its first scalar becomes

    (-1)^m q^[-m(3m+1)]
                  sum_(s=0)^m Q^(s^2) [m choose s]_Q^2.

Finite q-Vandermonde makes the sum [2m choose m]_Q=N/F_m^2.
For completeness, extract the coefficient of z^m in
(z;Q)_m(zQ^m;Q)_m=(z;Q)_(2m) using the finite binomial
expansion, then set a=m-k in its convolution. Its residual exponent
is a^2, which proves exactly this finite Vandermonde identity.
Since F_m^2=N(-1)^m q^[m(m+1)], the total scalar is
q^(-2mN)=1. This proves the first equation(6). In the second equation,
only s=0 survives in (5); the value is x^(-m)N/F_m^2=q^(-m^2).

Let f_a(z) be the ORIGINAL middle-degree Casimir continuants normalized
by f_0=1. The node -2 is SIMPLE at odd N. Consequently

    W_m(a,d-a)=q^(-m^2) f_a(-2).                       (8)

No derivative node is treated as a second simple value. The simple
node is being used only at the odd central anchor.

The exact positive/reflection normalization is

    W^dagger P W=I_N,
    (L_N P)_Steinberg=N W W^dagger.                    (9)

Here the subscript selects the actual -2 simple block on the full
physical pair, in every degree m,...,3m. To check the first column
of (9), use (1), conjugate the Gaussian phase, and apply terminating
q-Chu with parameters(Q^(-m),Q^(-m);Q), argument Q. It gives

    h^dagger P h
      =q^(m^2) sum_a Q^[a(a+1)] [m choose a]_Q^2
      =q^(m^2)(-1)^m Q^[-m^2-m(m+1)/2]=1.             (10)

The last exponent uses q^N=-1. The elementary finite q-Chu proof is
given in [the source quadratic transform](actual_half_color_quadratic_source_transform.md#2-elementary-finite-q-chu-and-durfee-identities);
it is a polynomial binomial expansion, not an imported summation
theorem. Adjoint covariance Ecal_pair^dagger P=-P F_pair now gives
the norm of each descendant: its ratio is |1-Q^(r+1)|^2 before
division by F_(r+1)/F_r. Thus every W_r has P-norm one, and
different r have disjoint physical degrees. The actual simple
spectral projector is W W^dagger P, proving the second part of (9).
Equivalently sqrt(N) W is a valid full-degree CD factor for this
channel; replacing first-entry normalization by it is a KNOWN unit
phase change within each magnetic row, not an arbitrary frame removal.

## 3. The entire central black vertex is one genuine 3j tensor

Use the actual nested six-head J=p_16 p_23 p_45 and define the
unscaled Hopf row pi=W^dagger P. Its central black packet is

    U^0=(pi tensor pi tensor pi) J.                    (11)

The row pi is a Hopf map by (4),(9) and the original adjoint covariance.
Hence (11) is a genuine invariant of V_N tensor V_N tensor V_N.
This invariant space is ONE dimensional. Bending its third leg by
the original duality identifies it with Hom(V_N,V_N tensor V_N).
Every such map has image in the -2 Casimir kernel. That actual
simple kernel is exactly the single W(V_N) above, with dimension N;
Schur's elementary E/F/K argument therefore gives dimension one.

Define its canonical nonzero tensor

    Theta=(W tensor I) p,
    Theta_(a,b,c)=N x^(-c) W_(d-c)(a,b).               (12)

In particular Theta_(d,m,0)=N q^(m^2), by (6). Therefore the WHOLE
central black vertex is

    U^0=N^2 q^(-m^2) A_N Theta,
    A_N=sum_(k=0)^m x^(k-d)
                         conjugate(h_k^2 W_m(m+k,m-k)). (13)

To obtain its scalar, evaluate (11) at the magnetic indices(d,m,0).
The only remaining physical colors are the N-term source contraction
of the branching kernel, with h_(m-t) from the lowest and highest
columns. Reindex k=m-t and use (6). It gives U^0_(d,m,0)=N^3 A_N,
which with (12) proves (13). In the positive CD factor sqrt(N) W,
the vertex is N^(3/2) times U^0, including the original N^3 of J.

Formula(5) makes A_N a fully explicit terminating factorial sum.
The next section proves its positive collapse, retaining all phases;
that positivity is not a premise of the source reduction above.

The ordinary and marked white packets remain the distinct actual
kernels of the branching theorem, with each f_alpha replaced by the
specified sqrt(N) W_r. In particular the marked vertex is NOT
declared to be a zero-current 3j covector: its last arc has the exact
P-removal and whole-source degree qualification already proved there.
Equation(13) concerns the invariant BLACK vertex only. Thus this
central reduction preserves the source distinction that prevented
the false trivalent norm-square replacement.

## 4. A finite coherent quartic transform

The scalar of the ACTUAL vertex has the exact evaluation

    A_N=q^[m(2-m)] sum_(k=0)^m beta(m,k)^4.             (14)

In particular it is nonzero at EVERY odd N, including composite
levels. Here is a finite proof, rather than an absolute-value bound.

Let f=(f_a(-2))_(a=0)^d and use the actual symmetric anti-Pascal
recoupling J on the complete N-channel source module. Root factorial
reflection(7) rewrites its entries as

    J_(i,j)=x D_i D_j [i+j choose i]_(Q^(-1)),
    D_i=(-q^(-1))^i, i+j<=d; zero otherwise.            (15)

It is important that this is the full invertible recoupling, not
just the simple node. It obeys

    conjugate(J) P J=P.                               (16)

This follows by finite q-binomial inversion. More explicitly, the
(i,j) entry of the left side has a=j,...,d-i. If i+j>d it is zero.
If n=d-i-j=0 its sole term is the squared modulus of an antidiagonal
entry, hence one. If n>0, put a=j+t and use(7) on its factorials.
After factoring the nonzero t-independent terms, the sum is

    sum_(t=0)^n (-1)^t Q^[t(t-1)/2+(1-n)t]
                        [n choose t]_Q
       =(Q^(1-n);Q)_n=0.

This proves(16) with the actual phase, without assuming a positive
or unitary ordinary pivotal trace.

The other actual pair Casimir is the real upper bidiagonal matrix
B with diagonal c_i=q^(2i+1)+q^(-2i-1) and upper entry
b_i=Q^i+Q^(-i)-2. The established source relation J A J^(-1)=B^T
gives y=J f explicitly:

    y_i=0, i<m;
    y_(m+k)=beta(m,k)^2, 0<=k<=m.                     (17)

For clarity, this needs only its first-order eigenvector recurrence.
Before i=m the diagonal c_i+2 is nonzero. After i=m,
-b_i/(c_i+2)=sin^2(pi(m+1-k)/N)/sin^2(pi k/N), i=m+k.
The final entry is y_d=f_0=1. This proves(17), including its absolute
normalization, directly from the two actual Casimir matrices.

By(1),(8),(13), A_N=q^(-3m^2) f^dagger J f. Since y is REAL,
(16) gives conjugate(f)=P J P y. Put z=P y. It has support0,...,m
and z_i=beta(m,i)^2. Therefore

    f^dagger J f=z^T J z.                             (18)

All entries i,j<=m in this quadratic form have i+j<=d, so the
zero-truncation in(15) no longer intervenes. Finite Vandermonde, by
the same product-coefficient proof as in Section2, gives

    [i+j choose i]_t
       =sum_(k=0)^min(i,j) t^(k^2)[i choose k]_t[j choose k]_t.

Consequently (15),(18) become

    z^T J z=x sum_(k=0)^m Q^(-k^2) C_k^2,
    C_k=sum_(i=k)^m beta(m,i)^2 D_i [i choose k]_(Q^(-1)). (19)

The SINGLE remaining transform is exactly evaluable:

    C_k=(-1)^m q^[k^2-m(m+1)] beta(m,k)^2.             (20)

To prove it, put n=m-k and convert every Gaussian factor in(19) to
base Q. Factoring its k-th term gives

    C_k=(-1)^k q^(-k) Q^[k^2-mk] [m choose k]_Q^2
      *sum_(r=0)^n (Q^(-n);Q)_r^2 Q^(-kr)
                              /[F_r(Q^(k+1);Q)_r].    (21)

Here Q^(m+1)=-q is precisely the half-root relation that cancels
the otherwise alternating summation argument. Apply the SECOND
terminating q-Chu identity with b=Q^(-n), c=Q^(k+1):

    sum_(r=0)^n (Q^(-n);Q)_r(b;Q)_r
                       (c Q^n/b)^r/[F_r(c;Q)_r]
       =(c/b;Q)_n/(c;Q)_n.                            (22)

Its argument is cQ^(2n)=Q^(-k), exactly as in(21). This is another
own finite identity: take the already proved q-Chu of Section2 at
base Q^(-1), parameters b^(-1),c^(-1), and use
(a;Q^(-1))_r=(-a)^r Q^[-r(r-1)/2](a^(-1);Q)_r.
That substitution gives(22) term by term and on its right side.
All its denominators here have indices<=m<N. At the root its right
side is

    (Q^(m+1);Q)_n/(Q^(k+1);Q)_n
        =(-1)^n Q^[-mn+n(n-1)/2].

Substituting this into(21) and using
[m choose k]_Q^2=Q^[k(m-k)] beta(m,k)^2 gives(20).

Now EVERY k-dependent phase cancels in(19):

    f^dagger J f=x q^[-2m(m+1)] sum_k beta(m,k)^4
                =q^(-2m^2) sum_k beta(m,k)^4.

Multiplying by q^(-3m^2) gives q^(-5m^2) times that positive sum.
Finally q^(-5m^2)=q^[m(2-m)], since their exponent difference is
-2mN. This proves(14) with the actual root lift and full source.

## 5. Nonzero local scalar asymptotic, with its exact normalization

Let G(t)=log(2sin(pi t)), J(t)=integral_0^t G(u)du and
j0=-8J(1/4)=v8/pi. Here v8=4 times Catalan's integral is only a
named numerical constant; no link-volume identification is assumed.
Then the finite positive scalar in(14) obeys

    sum_k beta(m,k)^4
       =(1/4) N^(-3/2) exp(N j0)(1+O(N^(-1))),
    A_N=(q^[m(2-m)]/4) N^(-3/2) exp(N j0)(1+O(N^(-1))). (23)

An elementary sine-factorial Laplace proof keeps the affine shift
m=(N-1)/2. On compact0<t<1, Euler summation after separating the
logarithmic endpoint gives

    s_a=sqrt(2N sin(pi a/N)) exp[N J(a/N)](1+O(N^(-1))).

The same endpoint separation gives the uniform logarithmic error
O(log N) for all0<=a<N, sufficient for a global large-deviation gap.
Since s_m^2=N EXACTLY, beta(m,k)^4=N^2/(s_k^4 s_(m-k)^4).
Its limiting exponent -4J(t)-4J(1/2-t) has a UNIQUE maximum at1/4:
its derivative is4log cot(pi t), positive before1/4 and negative
afterward, and its second derivative there is -8pi.

Write k=m/2+sqrt(N)u, retaining its actual integer or half-integer
coset. The compact factorial formula gives the symmetric local density

    beta(m,k)^4
       =(1/2)N^(-2) exp[N j0-4pi u^2]
          *[1+O((1+u^4)/N)]                          (24)

on a growing Gaussian window; outside a smaller fixed macroscopic
window there is the strict exponent gap just proved. The odd terms
cancel because k and m-k occur symmetrically. The shifted Gaussian
Riemann sum has mesh N^(-1/2), integral1/2 and relative errorO(1/N),
by the integrable second-derivative trapezoidal estimate. Multiplying
the factor1/2 in(24) by this integral gives exactly1/4 in(23).
This proves both the all-odd nonvanishing and its scalar rate.

The corresponding highest black-source coefficient in the CD frame
sqrt(N)W is N^(9/2)A_N, hence has leading magnitude
(N^3/4) exp(Nj0). The ENTIRE black tensor still includes Theta in(13).
No claim about its full positive norm, the marked white tensor, even
confluent channels or a sewn graph's maximum follows by maximizing
this one coefficient. Those are the next genuine branching estimates.

Audit: [actual generators, every finite Clebsch entry, source endpoint and central invariant tensor](../experiments/audit_actual_trivalent_steinberg_central_anchor.py).

Independent full analytical review and a separate fresh replay passed
all ten original odd Clebsch/source/quartic levels and five scalar
Laplace calibrations. The review independently rederived the second
q-Chu phases, the finite full-J inversion, and the affine-shift factor
1/4 in(23). Even confluence, the marked white packet, full Theta norm
and sewn geometric survival remain separate.
