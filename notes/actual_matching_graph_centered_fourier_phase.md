# The original shared Fourier source has an explicit centered quadratic phase

30 October 2026. In the exact positive
Fourier partition, every Clebsch endpoint phase and every ordinary
cup/cap constant cancels explicitly. The remaining original phase is
a quadratic form in the shared integer labels, with the original
half-twist phases and marked Fourier charge retained. This is an
exact source identity, not a claim that its stationary point
contributes to the finite sum.

## 1. Exact paired endpoint phase

Use the original definitions in
[the positive Fourier partition](actual_matching_graph_positive_fourier_partition.md).
Put q=exp(pi i/N), d=N-1, r=a+w, t=d-|w|, and

    B_N(a,w)=k_a N s_(a+|w|)
                    /(s_a^2 s_|w|^2 s_(a-|w|)).

The actual first endpoint scalars c_W,c_pi and the actual finite
polynomial scalar c_(t,a) satisfy the stronger COMPLEX identity

    h0_a c_W c_pi c_(t,a)^2
             = B_N(a,w) q^[(2a-d)t].               (1)

Indeed, the original reversed-conjugate white map gives

    c_W c_pi=|c_W|^2 conjugate(f_(t,a)(t))/G_(a,r).

The original generic physical endpoint specializes to

    f_(t,a)(t)=(-1)^a q^[dt+a^2+a].                (2)

This retains the actual endpoint convention; the term -2Na in its
generic exponent has become the root unit q^(-2Na)=1. Meanwhile
F_a=(Q;Q)_a=(-i)^a q^[a(a+1)/2]s_a gives

    c_(t,a)^2
       =(-1)^a q^[2a(t-d)+a(a-1)]/s_a^2.           (3)

Multiplying (2),(3), the signs cancel and the exponent is
(2a-d)t-2a(d+1). Its final term is -2aN and hence contributes one.
The remaining modulus is exactly the already-proved B_N. This
proves (1), including high-degree columns and both level parities;
no choice of a Chevalley square root remains in the phase.

## 2. Center every actual physical port

Work on the same shared state space S_N as in the positive
partition: exact bounded Kirchhoff flows w, coefficient indices
k_v, and ALL physical-cycle congruences, including charge one on
the original marked cycle. On a restored physical cycle, let x be
its integer base coordinate and write the actual FIRST coordinate
at each node n as

    u_n=epsilon_n x+B_n,       epsilon_n in {+1,-1}.

Here B_n is the literal integer affine offset. At a Clebsch node v
incident to edge i the actual total is T_n=d+w_i. At a cup or cap
it is T_n=d. Define

    delta_n=B_n-T_n/2,
    gamma_v=d-2a_i+2k_v,       gamma_b=d at cups/caps.             (4)

In particular delta_n can be a half-integer. Its definition is
independent of the low/high adapter: the compiler offset b_v
satisfies b_v+t_i/2=T_n/2 exactly.

The residual exponent of a vertex in the original finite expansion
can therefore be written as

    gamma_v(B_v-b_v)-t_i k_v
       =gamma_v delta_v+(d-2a_i)t_i/2.             (5)

Each matching edge has TWO such vertices. Their last terms in (5)
cancel exactly against the paired endpoint phase (1). This uses
their shared a_i,w_i,t_i; independent vertex normalization would
hide the cancellation.

For a cup or cap, its coordinate monomial contributes

    d B_b=d delta_b+d^2/2.

There are H original cups and H restored ordinary caps. Their
2H constant terms add to H d^2, exactly canceling the H original
cup constants q^(-d^2). Their powers of N have already canceled
in the positive partition. The original marked cap is still
represented by its specified charged-cap ratio; that ratio's
global q^(-d^2) remains outside the sum.

Consequently the COMPLETE residual phase is

    Theta_N(a,w,k)
      = product_i omega_(a_i)^epsilon_i * q^Lambda_N(a,w,k),
    Lambda_N=sum_(all ordinary vertices v) gamma_v delta_v
                             +d sum_(all cups/caps b) delta_b.   (6)

The epsilon_i in the first line is the recorded half-twist sign,
whereas epsilon_n in (4) is a physical-coordinate slope. Their
roles are distinct.

Although individual terms in Lambda_N may be half-integral,
Lambda_N itself is an INTEGER. Modulo two, every gamma_n is d,
and every physical matching total occurs at two vertices. There
are an even number of cup/cap totals. Hence

    sum_n gamma_n T_n =0 modulo 2,
    Lambda_N=sum_n gamma_n B_n-(1/2)sum_n gamma_n T_n in Z.       (7)

Thus (6) uses the original q itself, unambiguously at both level
parities. No new half-character choice has been introduced. The
original omega factors retain their already-specified root convention.

## 3. The resulting exact shared quadratic sum

The original complete-circle source is exactly

    A_(D,N)=q^(-d^2) N^(C-1)
       sum_(S_N) product_i[omega_(a_i)^epsilon_i B_N(a_i,w_i)]
                  *q^Lambda_N(a,w,k)
                  *product_(v incident to i) p_(t_i,a_i,k_v).   (8)

For a fixed recorded Morse graph, every B_n is affine in the
matching variables w_i and d, obtained by the literal propagation
u_next=T_n-u. Equation (6) is therefore an explicit quadratic
polynomial in (a,w,k,d), restricted to the actual shared lattice.
In particular the absolute values |w_i| in the positive amplitudes
do not appear in this residual polynomial. The retained omega
factors add their original quadratic channel phases.

For an unmarked cycle, writing its new integer base coordinate as
x'=x+h changes Lambda_N by -h m_c, where
m_c is its total Fourier frequency. On the retained congruence
m_c=0 modulo 2N this leaves q^Lambda_N unchanged. On the marked
cycle the base coordinate is fixed as the SECOND original marked
coordinate; its one-unit charge must not be discarded in making
a similar reparametrization.

This exact simplification preserves the positive upper comparison.
It also isolates what that comparison removes: the bilinear
interaction between the Fourier labels gamma_v and the actual
centered affine offsets delta_v. In an interior coefficient chart
the normalized logarithmic phase is
N^-1 log(q^Lambda_N)=i pi Lambda_N/N^2. Its derivative with respect
to lambda_v=k_v/N is 2pi i delta_v/N, precisely the real-center data in
[the radial reconstruction obstruction](actual_positive_fourier_radial_geometric_obstruction.md).
No equality of exponential rates, geometric maximum, holomorphic
coefficient-index continuation, or contributing cycle follows from
the quadratic form alone.

Audit: [original paired phases and full centered cycle convolutions](../experiments/audit_actual_matching_graph_centered_fourier_phase.py).

The result is an exact phase identity, not an assertion of a contributing saddle or equality of exponential rates.