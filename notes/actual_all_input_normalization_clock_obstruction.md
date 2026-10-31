# The normalization clock disk is not uniformly tame on the physical head

29 October 2026. The selected original normalization scalar has a tame
clock disk, but its ALL-INPUT physical operator does not. The distinction
can be proved at the first normal jet, with the actual sources and full
Cartan factor retained. This gives an explicit physical Ward current
which a gluing theorem has to cancel coherently.

The result does not assert exponential growth of a closed knot scalar,
or failure of the source-specific shrinking-arc construction. It rules
out promoting its selected scalar estimate to a uniform physical-head
operator estimate.

## 1. The literal open-head normalization operator

Let N>=2, d=N-1, q=exp(pi*i/N), Q=q^2, x=q^d,
F_j=(Q;Q)_j, s_j=|F_j|, and kappa=q^(d^2/2). Let R be the FULL
original positive crossing on the physical pair degree-d block W,
and set L=kappa^(-1)R. Keep the original cup and ordinary cap.

The all-input cup slide exposes the operator

\[
 \mathcal C_N(t)=(\ell_{12}\otimes I_3)
          (I_1\otimes R^2)t^{J_2}(I_1\otimes p_{23}),
 \qquad J|a\rangle=a|a\rangle.
\]

Here R^2 acts on the degree-d subspace of the last physical pair;
the full original physical crossings restrict to this block and the
first head is its untouched spectator. This is the same actual local
normalization slot as in
[the mesoscopic-current theorem](actual_mesoscopic_clock_packet_currents.md#4-why-the-scalar-packet-does-not-already-solve-physical-gluing).
The remaining physical input is arbitrary. Integer degree makes the
operator diagonal, with EXACT entries

\[
 C_a(t)=x^{-a}Q^{-a}\sum_{n=0}^d(L^2)_{d-a,n}(xt)^n.
                                                               \tag{1}
\]

Indeed the three factors are the cup coefficient N x^(n-d), the
original crossing square kappa^2(L^2)_(d-a,n), and the cap
x^(-a)Q^(-a)/N. The identity kappa^2=x^d gives (1).
The apparent all-input source freedom is therefore fixed, not chosen
by a favorable scalar period. At t=1 every entry is x^d=kappa^2.

Write u(t)_j=(xt)^j and v(t)=L^2u(t). Because x^2=Q^(-1),

\[
 C_a(t)=x^a v_{d-a}(t),\qquad
 \max_a|C_a'(1)|=\|v'(1)\|_\infty.                          \tag{2}
\]

## 2. The exact finite Ward register before the second crossing

For 0<=i<=d define

\[
 D_i^+(s)=F_i^2\sum_{b=0}^i
       \frac{Q^{b^2}s^b}{F_{i-b}F_b^2}.
\]

Let D_i^-(s) denote the same polynomial with Q replaced by Q^(-1).
All factorial indices are below N. Finite Durfee convolution gives
D_i^+(1)=D_i^-(1)=1. Directly from the original crossing entries,

\[
 \boxed{\displaystyle (Lu(t))_i=x^i t^d D_i^-(1/t).}           \tag{3}
\]

For clarity, the intermediate finite coefficient is

\[
 (Lu(t))_i=x^{-i}Q^{i(d-i)}t^{d-i}F_i^2
  \sum_{k=0}^i\frac{(-1)^kQ^{k(k-1)/2}t^k}{F_kF_{i-k}^2}.
\]

Replace k by i-b and use
(Q^(-1);Q^(-1))_b=(-1)^b Q^(-b(b+1)/2)F_b to obtain (3).
This is an all-port factorial identity, not an adjoint/unitarity claim.

The finite polynomials obey

\[
 D_i^+(s)=(1+Q-2Q^i+Q^{2i-1}s)D_{i-1}^+(s)
               -Q(1-Q^{i-1})^2D_{i-2}^+(s).                \tag{4}
\]

One elementary derivation uses formal series through degree d:
U(z)=sum z^k/F_k has U(Qz)=(1-z)U(z), and
W(z)=sum Q^(b^2)s^b z^b/F_b^2 satisfies
W(z)-2W(Qz)+(1-sQz)W(Q^2z)=0. Compare coefficients of U(z)W(z).
This proves (4) at the root without using any denominator F_N.

Let P_i be the original Green register,

\[
 P_0=1,\qquad P_i=(1-Q^i)^2P_{i-1}+Q^i.
\]

Differentiating (4) at s=1 and factoring the resulting first difference
gives the exact normal current

\[
 (D_i^+)'(1)-(D_{i-1}^+)'(1)=Q^iP_{i-1}.                   \tag{5}
\]

The base case is (D1^+)'(1)=Q. Equivalently, set w=Lu'(1); (3)
gives w_i=x^i[d-(D_i^-)'(1)]. Therefore

\[
 \boxed{\displaystyle
 x^{-i}w_i-x^{-(i-1)}w_{i-1}
                    =-Q^{-i}\overline{P_{i-1}},\quad1\leq i\leq d.} \tag{6}
\]

This is the retained physical normal current. It is not zero at a
normalization leaf merely because its value at t=1 is a scalar.

## 3. The source endpoint forces a large interior current

The all-parity original source endpoint has the independently derived
quadratic-Gaussian asymptotic

\[
 P_d=N^{3/2}\exp\!\left[i\pi\left(\frac14-\frac N{12}
                              +\frac1{4N}\right)\right]+O(\sqrt N).
                                                               \tag{7}
\]

Its proof retains the complete pivotal derivative source, including
the odd simple node:
[the endpoint Gaussian theorem](actual_normalization_endpoint_gaussian_asymptotic.md).
In particular |P_d|>=c N^(3/2) for all sufficiently large N. No
volume asymptotic or fitted saddle branch is assumed.

The exact backward Green identity from
[the terminal capacity proof](actual_terminal_green_capacity_bound.md) is

\[
 P_t=F_t^2\left(\frac{P_d}{N^2}
                       -\sum_{b=t+1}^d\frac{Q^b}{F_b^2}\right). \tag{8}
\]

Choose i nearest 5N/6, with 1<=i<=d, and t=i-1. For large N,
s_t>N. The sine-factorial sequence increases up to its high peak
and then decreases to s_d=N. Consequently s_b>=N for every b>t,
so the tail in (8) has absolute value at most1/N. It follows from
(7) that

\[
 |P_{i-1}|\geq c_1 N^{-1/2}s_{i-1}^2.                      \tag{9}
\]

Put J(s)=integral_0^s log(2sin(pi*u))du. Uniform sine-factorial
asymptotics give

\[
 \log|P_{i-1}|\geq\frac{v_3}{\pi}N-O(\log N),                \tag{10}
\]

since J has maximum v3/(2pi) at 5/6, where v3 is the regular ideal
tetrahedron volume. The lower bound is a coherent source result: the complex
tail in (8) is estimated only AFTER the actual nonzero endpoint
has been evaluated.

## 4. A quantitative all-input obstruction after the second crossing

The literal original NEGATIVE crossing supplies

\[
 |(L^{-1})_{r,j}|=
 \begin{cases}
 \displaystyle\frac{N^2}{s_r^2s_j^2s_{d-r-j}},&r+j\leq d,\\
 0,&r+j>d.
 \end{cases}                                                 \tag{11}
\]

No conjugate-transpose inverse is used. Define the exact row mass
B_r=sum_j |(L^(-1))_(r,j)|. Since w=L^(-1)v'(1), (6) implies the
FINITE inequality

\[
 \boxed{\displaystyle
 \max_{a\geq i-1}|C_a'(1)|
                   \geq\frac{|P_{i-1}|}{B_i+B_{i-1}}.}        \tag{12}
\]

The color restriction follows from the two strict supports in (11),
not from an imposed geometric color. It is enough to control the
operator on its upper sixth of physical inputs.

The global factorial minimum is
log s_j>=-N v3/(2pi)-O(log N), and for r=i or i-1,
log s_r^2=N v3/pi+O(log N). Hence (11) gives

\[
 \log(B_i+B_{i-1})\leq
   N\left(-\frac{v_3}{\pi}+\frac{3v_3}{2\pi}\right)+O(\log N)
       =\frac{v_3}{2\pi}N+O(\log N).
\]

Combining this with (10) proves a positive explicit exponent:

\[
 \boxed{\displaystyle
 \liminf_{N\to\infty}\frac1N\log\max_a|C_a'(1)|
       \geq\gamma:=\frac{v_3}{2\pi}>0.}                       \tag{13}
\]

The numerical value gamma is about0.16153. It is a rigorous LOWER
bound, not the claimed exact jet exponent.

Every C_a is a polynomial. Cauchy's derivative inequality now gives,
for EVERY fixed c>0,

\[
 \boxed{\displaystyle
 \liminf_N\frac1N\log
    \sup_{|t-1|\leq c/N}\|\mathcal C_N(t)\|_{\mathrm{op}}
                                  \geq\gamma>0.}            \tag{14}
\]

The same assertion holds for any disk radius r_N<=1 with
log(1/r_N)=o(N). It is therefore not repaired by choosing a smaller
polynomial clock disk. This is a statement about the ALL-INPUT
physical operator, not about the selected scalar row.

This particular obstruction is independent of a choice of positive
inner product on the SAME physical input/output head. The C_a(t) are
the actual eigenvalues of the diagonal operator, so every such operator
norm is at least max_a|C_a(t)|, even for N- and t-dependent metrics.
A change between DIFFERENT input and output metrics has additional
interfaces and is not covered by that observation.

## 5. The missing moment constraint is an actual normal Ward defect

For a=d the original source packet is still
C_d(t)=x^(-d)P_N(t), in the notation of the mesoscopic-current theorem.
Its first derivative is x^(-d)Q conjugate(P_d-1), polynomial in N;
the whole selected c/N disk is polynomially bounded by the original
clock-disk proof. There is no contradiction with (13): the large
normal response occupies other physical inputs.

It can also be stated directly as a failure of the untwisted Hopf
moment condition. The original single-head F acts by
F|a>=(1-Q^(a+1))|a+1>. Therefore

\[
 [F,\mathcal C_N'(1)]|a\rangle
   =(1-Q^{a+1})(C_a'(1)-C_{a+1}'(1))|a+1\rangle.             \tag{15}
\]

The terminal C_d' is polynomial, while (13) is exponential. Telescoping
the physical differences and using |1-Q^(a+1)|>=4/N proves

\[
 \liminf_N N^{-1}\log\|[F,\mathcal C_N'(1)]\|_{\mathrm{op}}
                                      \geq\gamma.            \tag{16}
\]

The same holds for Ecal, whose relevant coefficient magnitudes agree.
Thus a polynomial-norm same-head correction cannot make this jet an
intertwiner: its commutator would have to cancel (16). The required
normal current is explicitly (5)--(6), not an unproved abstract error.

The exact all-input tensor Ward identity identifies the omitted
two-color insertion more directly. Put S=I tensor p and
A_cap=ell tensor I, and let U=I tensor R_phys^2 act on the FULL
physical pair space, not only its degree-d block. Define

\[
 \mathcal J_F(t)=A_{\mathrm{cap}}U K_1^{-1}F_2 t^{J_2}S,\qquad
 \mathcal J_E(t)=A_{\mathrm{cap}}U E_{{\mathrm{cal}},2}t^{J_2}K_3S.
\]

The actual coproduct and cup/cap intertwinings give

\[
 [F,\mathcal C_N(t)]=(1-t)\mathcal J_F(t),\qquad
 [E_{\mathrm{cal}},\mathcal C_N(t)]=(1-t^{-1})\mathcal J_E(t).      \tag{17}
\]

Indeed only the middle-head term in the total coproduct fails to
commute with t^(J2). In particular
[F,C_N'(1)]=-J_F(1) and [Ecal,C_N'(1)]=J_E(1).
The F insertion goes through pair degree d+1 and the E insertion
through degree d-1. Replacing either by a shift of the recording
register inside the degree-d scalar packet would omit that sector.
Equations (16)--(17) prove that these ACTUAL physical normal-current
operators have exponential norm; no polynomial operator correction
may simply erase them.

A full exterior may cancel it with neighboring clock/crossing currents
or may retain a source projection excluding these inputs. Such a
cancellation must be shown in its actual tensor slot, with the marked
source unchanged. Replacing (1) by the selected value C_d(t), imposing
a lowest-color projection on an internal head, or declaring the clock
insertion a Hopf map omits the defect above.

This proves the requested uniform physical operator extension FALSE.
It leaves a source-compatible correlated/mesoscopic gluing theorem
open. Tensoring a spectator identity does not change the lower bound;
no claim about a general correlated whole-knot scalar or a one-dimensional
unit-circle arc follows solely from the disk inequality (14).

[Audit](../experiments/audit_actual_all_input_normalization_clock_obstruction.py)
checks the original full R/cup/cap operator, the finite Ward
recurrence, the exact derivative current, literal inverse row masses,
and finite inequality (12). The endpoint Gaussian input has its
separate all-level proof and original-source audit.

The finite audit checks twelve literal all-input physical normalization
operators at N=2,...,12,14, their exact root Ward jets and Hopf
commutators; ten complete complex current/lower-bound families through
N=96. Numerical jet rates are recorded only as diagnostics, not used
to infer the positive lower exponent (13).