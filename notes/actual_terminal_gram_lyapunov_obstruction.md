# Exponential metric motion is necessary for the current terminal Gram

29 October 2026. This is an exact obstruction to a UNIFORM, all-port
Lyapunov propagation of the presently constructed terminal Gram at
subexponential extra cost. Its test vector is now proved to occur on a
FIXED original source trajectory, by the cup slide below. It is not an
obstruction to Cauchy, a substantially changing positive metric, or a
source estimate which first retains the relevant coherent cancellations.

Use the original principal root and complete source module W from
[the closed kernel](actual_terminal_packet_closed_kernel.md):
q=exp(pi*i/N), Q=q^2, d=N-1, x=q^d, F_a=(Q;Q)_a,
s_a=|F_a|, kappa=q^(d^2/2), e_j=|j,d-j>. Let R be the FULL original
positive checked crossing on W, and let T be the actual terminal
projector map. The verified identities are

\[
 T=N^{-1}X R P_{\mathrm{rev}}R,\qquad
 H:=TR^{-1}=N^{-1}X R P_{\mathrm{rev}},\qquad
 X=\operatorname{diag}(x^j),\quad
 P_{\mathrm{rev}}=\operatorname{diag}(P_{d-j}),                    \tag{1}
\]

where P0=1 and the ACTUAL endpoint satisfies

\[
 P_d=\sum_{j=0}^dF_j=-q\Phi_N(r_N^3),\qquad |P_d|\leq3N^2.     \tag{2}
\]

The full original pivotal functional, odd simple node, even levels,
Cartan and framing phases behind (2) are retained in
[the quantitative Green proof](actual_terminal_green_capacity_bound.md#2-the-actual-endpoint-closes-polynomially-at-every-parity).
No estimate of a sum of absolute Green currents is used here.

## 1. A complete exact energy comparison

Put

\[
 Z_N=\sum_{j=0}^d s_j^2,\qquad v_N=R^{-1}e_0.
\]

Three literal finite crossing identities give everything needed:

\[
 R e_0=\kappa x^{-d}e_d,\qquad
 (R^{-1}e_0)_j=\kappa^{-1}x^jF_{d-j},\qquad
 |(R e_d)_j|=s_j.                                          \tag{3}
\]

The second uses the original NEGATIVE crossing formula, rather than
assuming a unitary inverse. The third uses root factorial reflection.
In particular ||v_N||^2=Z_N, while ||R v_N||=1. Applying (1),

\[
 \boxed{\displaystyle
 \|T v_N\|^2=|P_d|^2/N^2,\qquad
 \|T Rv_N\|^2=\|T e_0\|^2=Z_N/N^2.}                       \tag{4}
\]

Both equalities are of COMPLETE coherent packet energies, not of one
expanded shear path. The denominator is an original polynomial source
endpoint, and the numerator is the entire positive factorial sum.

Let epsilon_N=exp(-N^2), and let the current positive terminal Gram be

\[
 G_N=T^\dagger T+\epsilon_N I.
\]

Every uniform Lyapunov inequality

\[
 R^\dagger G_N R\preceq C_N G_N
\]

must therefore satisfy the exact finite lower bound

\[
 \boxed{\displaystyle
 C_N\geq\frac{Z_N+N^2\epsilon_N}
 {|P_d|^2+N^2\epsilon_N Z_N}.}                              \tag{5}
\]

This includes levels at which T is singular; nothing is inverted
except the genuine original crossing. It also holds after tensoring
the physical ports with any spectator coefficient Hilbert space.

The sine-factorial estimate, including its endpoint uniformity,
gives

\[
 \log Z_N=\frac{v_3}{\pi}N+O(\log N),                         \tag{6}
\]

where v3 is the regular ideal tetrahedron volume. Indeed
log s_j=N J(j/N)+O(log N), and J has its unique maximum v3/(2pi)
at 5/6. Polynomially many terms and a nearest lattice point give (6).
No volume-conjecture asymptotic is a premise.

Combining (2), (5), (6), and epsilon_N=e^(-N^2) proves

\[
 \boxed{\displaystyle
 \log C_N\geq\frac{v_3}{\pi}N-O(\log N).}                    \tag{7}
\]

One may use the finite bound C_N>=Z_N/(9N^4+1) for every N>=2:
Z_N<=N4^(N-1) implies N^2 exp(-N^2)Z_N<1 in this range.

Thus this FIXED original terminal Gram does not have a
subexponential-cost all-port Lyapunov inequality even for R12.
The exponent is forced by a retained source endpoint, not by a
generic nonnormal-matrix norm estimate.

For the related source-slot Gram
\(\widehat G_N=H^\dagger H+\epsilon_N I\), the flat unit vector e0
gives the even simpler exact quotient

\[
 \frac{\|HR e_0\|^2+\epsilon_N\|Re_0\|^2}
 {\|H e_0\|^2+\epsilon_N}
 =\frac{Z_N+N^2\epsilon_N}{|P_d|^2+N^2\epsilon_N}.            \tag{8}
\]

So the conclusion is not caused only by the Euclidean size of v_N.

## 2. Any uniformly comparable moving metric must pay the same cost

The statement also quantifies what an adaptive metric has to change.
Suppose positive metrics G_before,G_after obey

\[
 G_{\mathrm{before}}\preceq A_N G_N,\qquad
 G_{\mathrm{after}}\succeq B_N^{-1}G_N,
\]

and a propagation inequality is asserted:

\[
 R^\dagger G_{\mathrm{after}}R\preceq C_N G_{\mathrm{before}}.
\]

Testing v_N proves, without additional assumptions,

\[
 C_N A_N B_N\geq
 \frac{Z_N+N^2\epsilon_N}{|P_d|^2+N^2\epsilon_N Z_N}.          \tag{9}
\]

If A_N and B_N are exp(o(N)), C_N must carry the exponent in (7).
Conversely a subexponential step cost requires exponential metric
motion relative to this terminal metric, of at least the displayed
amount. Exact pullback of a metric can of course make an individual
step an isometry; (9) says that its change of scale cannot be ignored
when comparing it with this fixed boundary-conditioned metric.

This does not forbid an angle/gluing dependent metric with a genuine
global certificate for its exponential variation. It specifies one
necessary quantitative condition such a construction must meet.

## 3. Original-source scope

The [literal all-input cup slide](actual_terminal_source_normalization_packet.md)
now strengthens the test to an ACTUAL fixed source trajectory:

    R23 p=N R12^(-1)e0, R12 R23 p=N e0.

Thus the two prefixes [2] and [2,1] realize the exact quotient (5),
with both test vectors multiplied by N. Their complete terminal
packet energies are respectively |P_d|^2 and Z_N. Restricting the
unchanged metric to vectors reached by original braid prefixes does
not remove the obstruction.

Their scalar closures retain cancellation: the second complete
packet is x^(-d)(Q^(-j) conjugate(F_j))_j and sums to the unit phase
x^(-d)Q. It is an explicit factorial divergence, with its endpoint
and arbitrary spectator finite differences retained in the linked
proof. The [shrinking-clock disk bound](actual_normalization_clock_disk_bound.md)
now proves a sharp zero-exponent energy estimate for this particular
normalization packet in a different coherent metric. No general
interior-source energy estimate follows from that repair.

The identity Rp=kappa p still holds on the bare cup, but does not
apply after the genuine adjacent prefix R23. Any successful source
argument must retain this distinction and its coherent closure.

At this chosen paired source cut, any diagonal product-head gauge
A_a B_b that fixes the cup term by term has A_j B_(d-j)=1.
It is therefore the IDENTITY on all of W. Such a paired-source
factorial gauge cannot alter this test. Interior gauges not satisfying
that condition, or coherent non-product metrics, have to retain their
actual interfaces and are outside this restricted observation.

All original co-source factors remain unchanged: K=chi 1^T T A p
and its polynomial Cauchy boundary cost are the ones already proved.
No arbitrary positive trace replaces the pivotal source. Equations
(4)--(9) diagnose the cost of propagating its CURRENT complete Gram;
they do not give an excess-volume lower bound for a knot scalar.

[Audit](../experiments/audit_actual_terminal_gram_lyapunov_obstruction.py)
uses the literal positive and negative crossing formulas and complete
open terminal kernel. It checks the original cup, all coherent
energies in (4),(8), and the regularized finite quotient rather than
diagonalizing an unresolved near-singular Gram.

The finite audit checks seven original complete terminal modules; nineteen
literal signed-crossing/source/Gram families at N=2,...,20; five
large-level exact energy quotients through N=384.