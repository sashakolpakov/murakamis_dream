# The original factorial endpoint has a nonzero Gaussian leading term

29 October 2026. The endpoint in the exact normalization/Green source
has the following all-level asymptotic, with its phase fixed:

\[
 P_{N-1}:=\sum_{j=0}^{N-1}(Q;Q)_j
 =N^{3/2}\exp\!\left[i\pi\left(\frac14-\frac N{12}
                                  +\frac1{4N}\right)\right]
       +O(\sqrt N),\qquad Q=e^{2\pi i/N}.                 \tag{1}
\]

The implied constant is independent of every integer N>=2; no parity
or residue class is omitted. In particular |P_(N-1)|>=N^(3/2)/2 for
all sufficiently large N. This is a polynomial endpoint lower bound,
not a positive hyperbolic-volume rate. Its use below is to keep a
nonzero coefficient in an actual neighboring-crossing Green current.

## 1. A finite original-source formula

Write d=N-1, q=e^(pi i/N), F_j=(Q;Q)_j. The original source identity
already proved in the [terminal Green calculation](actual_terminal_green_capacity_bound.md)
is P_d=-q Phi_N(r_N^3), with its full Cartan and pivotal factors.
For k=0,...,d put

\[
 c_k=q^{2k+1}+q^{-2k-1},\quad A_k=q^{2k+1}-q^{-2k-1},\quad
 \nu_k=(-1)^kq^{k(k+1)}.
\]

The literal spectral-jet source gives the exact finite formula

\[
 P_d=\frac q2\sum_{k=0}^{d}\nu_k^3
       \left[c_k-\frac32(d-2k)A_k\right].                \tag{2}
\]

To verify the fold, at every double node the original contribution is
-nu_k^3[c_k-3(d-2k)A_k/2] to Phi_N(r_N^3). The index d-k has
the SAME c and nu, and the opposite A and d-2k. Thus (2) counts each
double contribution exactly once. When N is odd the remaining node
has c=-2 and A=0; its half-sum contribution to Phi is precisely
nu_k^3, the original simple-node term. N=2 is included. This uses
the exact [spectral-jet source proof](casimir_braiding_and_recoupling_lattice.md#8-the-actual-closing-trace-is-a-spectral-jet-functional),
not a chosen semisimple trace or a fitted endpoint value.

Set s_k=(k+1/2)/N, and define fixed smooth functions on [0,1]

\[
 a(s)=(1-2s)\sin(2\pi s),\qquad b(s)=\cos(2\pi s),\qquad
 S_N(A)=\sum_{k=0}^{N-1}A(s_k)e^{i\pi N(3s_k^2+s_k)}.
\]

Since nu_k^3=-i exp[-3pi i/(4N)] exp[i pi N(3s_k^2+s_k)],
(2) becomes EXACTLY

\[
 P_d=e^{i\pi/(4N)}\left[-\frac{3N}{2}S_N(a)-iS_N(b)\right]. \tag{3}
\]

In particular every phase needed in (1) is specified before taking a
limit. The external original period line, if present, remains external;
it is not used to change the finite endpoint (2).

## 2. An elementary half-grid quadratic-sum lemma

For a fixed smooth A on [0,1] with A(0)=A(1), finite Fourier
inversion of its periodization gives

\[
 S_N(A)=N\sum_{m\in\mathbb Z}(-1)^m I_{m,N}(A),\qquad
 I_{m,N}(A)=\int_0^1 A(s)
      e^{i\pi N[3s^2+(1-2m)s]}\,ds.                    \tag{4}
\]

Indeed the periodized function A(s)exp[i pi N(3s^2+s)] is continuous
at its endpoints, since exp(4pi iN)=1. Its piecewise smooth derivative
has bounded variation, so its Fourier coefficients are absolutely
summable: integrating twice, with the possible derivative jump retained,
gives O_N((1+|n|)^-2). Summing its Fourier series at s_k keeps exactly
the coefficients n=Nm, with factor exp(pi im)=(-1)^m. This proves
(4), including the half-grid sign. The following estimates are uniform
in m and N and justify its asymptotic use.

Only m=1,2,3 have stationary points in (0,1), namely

\[
 s_m=(2m-1)/6,\qquad
 3s^2+(1-2m)s=3(s-s_m)^2-(2m-1)^2/12.                  \tag{5}
\]

There is no omitted endpoint resonance: the endpoint derivatives are
the odd integers 1-2m and 7-2m, never zero. The endpoint PHASES still
matter, and agree exactly at every integer N as used below.

If m is outside this set, the phase derivative has absolute minimum
delta_m>=c(1+|m|)>0. Two integrations by parts give

\[
 |I_{m,N}(A)|\le
 \begin{cases}
 C_A/(N^2\delta_m^2),& A(0)=A(1)=0,\\
 C_A/(N\delta_m^2),& A(0)=A(1).
 \end{cases}                                         \tag{6}
\]

For clarity, the first boundary term in the second case is exactly
A(0)/(i pi N) times [1/(7-2m)-1/(1-2m)]. Both endpoint phases
are one, so this difference is O(delta_m^-2), rather than an
unsummable O(|m|^-1). If A vanishes there, that term is zero; the
next boundary and integral terms have the stronger N^-2 bound.
All derivatives of A in (6) are fixed. Summing the nonstationary
terms in (4) therefore costs O(1/N) in the first case and O(1)
in the second.

At each of the three stationary points choose a fixed smooth cutoff
inside (0,1). Completing the square gives

\[
 I_{m,N}(A)=\frac{e^{i\pi/4}}{\sqrt{3N}}
        A(s_m)e^{-i\pi N(2m-1)^2/12}
       +\begin{cases}O(N^{-3/2}),& A(0)=A(1)=0,\\
                      O(N^{-1}),& A(0)=A(1).
         \end{cases}                                  \tag{7}
\]

Here is an elementary error proof. For a compactly supported smooth
amplitude B in the centered variable, Fourier inversion and the damped
Gaussian integral give

\[
 \int B(u)e^{3\pi iNu^2}du
 =\frac{e^{i\pi/4}}{\sqrt{3N}}
       \int\widehat B(\xi)e^{-i\pi\xi^2/(3N)}d\xi.
\]

Subtracting B(0)=integral Bhat and using |exp(iv)-1|<=|v| bounds
the error by C N^-3/2 integral xi^2|Bhat(xi)|dxi. This integral is
finite. The identity follows first with Gaussian damping and then
by its limit; compact support and rapid Fourier decay justify that
passage. The portion outside the cutoff has no stationary point;
the same integrations by parts as (6) give O(N^-2) for zero endpoints
and O(N^-1) otherwise. This proves (7) without assuming a selected
WKB branch or an asymptotic theorem for a knot invariant.

Combining (4),(6),(7), when A has zero endpoints one obtains

\[
 S_N(A)=e^{i\pi/4}\sqrt{N/3}
      \sum_{m=1}^3(-1)^m A(s_m)e^{-i\pi N(2m-1)^2/12}
          +O(N^{-1/2}).                                \tag{8}
\]

For a smooth amplitude with matching nonzero endpoints the same
formula has error O(1); in particular S_N(A)=O(sqrt N).

## 3. The two surviving Gaussian terms reinforce at every level

For a(s) above,

\[
 a(1/6)=a(5/6)=\sqrt3/3,\qquad a(1/2)=0.
\]

The half-grid signs for m=1 and m=3 are BOTH minus. Their phases
coincide at every integer N, since their quotient is exp(-2pi iN)=1.
Thus (8) simplifies to

\[
 S_N(a)=-\frac23\sqrt N\,
             e^{i\pi/4-i\pi N/12}+O(N^{-1/2}).           \tag{9}
\]

The function b has matching endpoints, so S_N(b)=O(sqrt N).
Substitution in the exact source equation (3) proves (1).
There is no parity cancellation between the two leading points,
and the possible odd simple node was already retained in (2).

## 4. A quantitative consequence for the actual Green current

The original first-order current obeys

\[
 P_t=F_t^2\left[\frac{P_d}{N^2}
                  -\sum_{r=t+1}^d\frac{Q^r}{F_r^2}\right]. \tag{10}
\]

If t/N stays in a compact subinterval of (1/2,1), with t<=d,
the tail in (10) is O(1/N^2) uniformly. To see this, reflect r=d-k:
it is Q^-1/N^2 times a partial sum of Q^-k conjugate(F_k)^2.
Here k runs only up to (1/2-delta)N. Its k=0 term is one, and the
rest is uniformly bounded: up to a small fixed fraction of N the
factorials decrease geometrically, while on a fixed interval below
1/2 they are exponentially small. Thus the partial absolute sum is
O(1). This argument needs no cancellation in that reflected short tail.

Together with (1), this proves on every such compact interval

\[
 P_t=\frac{F_t^2P_d}{N^2}\,[1+O(N^{-3/2})],\qquad
 |P_t|=N^{-1/2}|F_t|^2[1+O(1/N)].                        \tag{11}
\]

The endpoint source in (1) therefore supplies a nonzero polynomial
coefficient of the interior factorial current. It does NOT justify
dropping that current or bounding it by its tame endpoint. This is
the coefficient needed in an all-physical-input neighboring-crossing
test; it does not assert that the full closed knot has a positive
volume contribution from this sector.

### A sharp all-input normal current of one complete original crossing

There is a direct local consequence, with an ordinary original pivotal
closure and arbitrary outside spectators retained. Put
g_b=theta Q^(-b), theta=x^(1-N), x=q^d, kappa=q^(d^2/2), and define

\[
 \mathcal M_\pm(t)=\operatorname{Tr}_2[(I\otimes g\,t^J)R_\pm],
 \qquad J|b\rangle=b|b\rangle .
\]

This partial trace has NO extra factor1/N. Literal integer-degree
conservation makes it diagonal on the remaining physical head. Its
complete original coefficients are

\[
 \mathcal M_+(t)=\kappa\theta\,\operatorname{diag}(D_a(t)),\qquad
 D_a(t)=F_a^2\sum_{b=0}^a\frac{Q^{b^2}t^b}{F_{a-b}F_b^2},           \tag{12}
\]
\[
 \mathcal M_-(t)=\kappa^{-1}\theta^{-1}
       \operatorname{diag}\!\left(t^dD_{d-a}^{\overline Q}(t^{-1})\right).
                                                                    \tag{13}
\]

The superscript in (13) replaces every Q coefficient by Q^(-1).
Both known scalar Markov factors have modulus one. For (12), a
diagonal positive R coefficient has transfer a-b and value
kappa x^(-2b)Q^(b^2)F_a^2/(F_(a-b)F_b^2). The original pivot cancels
x^(-2b)=Q^b. The negative formula follows from its literal inverse
coefficient by b->d-b and factorial reflection; theta^2Q=1 retains
its displayed phase. Thus these are full crossing/source identities,
not new favorable traces. They tensor with every spectator identity.

The actual finite packets close under a second-order Ward recurrence:

\[
 D_0=1,\quad D_1=1-Q+Qt,\qquad
 D_a=(1+Q-2Q^a+Q^{2a-1}t)D_{a-1}
                         -Q(1-Q^{a-1})^2D_{a-2}.        \tag{14}
\]

One coefficient check proves this including all endpoints. For b<a,
divide by the nonzero t^b coefficient in D_(a-1), and set
u=Q^(a-b), v=Q^b. The required identity is

\[
 \frac{(1-uv)^2}{1-u}
       =1-2uv+u+\frac{u^2(1-v)^2}{1-u}.
\]

The top coefficient b=a is Q^(a^2) on both sides. Initial values
therefore show D_a(1)=1 at EVERY physical a. At the other source
endpoint, root reflection gives an exact whole-polynomial identity

\[
 D_d(t)=Qt^d H_N(Q/t),\qquad H_N(z)=\sum_jF_jz^j.        \tag{15}
\]

Its apparent inverse powers cancel, so it is a polynomial. The Ward
equation for H_N at one gives Q^2H_N'(Q)=P_d-1, whence

\[
 u_a:=D_a'(1),\qquad u_0=0,\quad u_d=N-P_d,\qquad
 u_a-u_{a-1}=Q^aP_{a-1}.                               \tag{16}
\]

To verify the last equality directly, differentiate (14); its successive
difference obeys v_a=Q(1-Q^(a-1))^2v_(a-1)+Q^(2a-1), v_1=Q.
The original Green recurrence identifies v_a=Q^aP_(a-1) exactly.
The retained current in (16), rather than a dropped exterior forcing,
is what a neighboring crossing generates.

The original finite bound |P_j|<=N+4s_j^2 gives

\[
 \max_a|u_a|\le N^2+4\sum_js_j^2,\qquad
 |u_a|\le4N^3(1+s_a^2)\quad\text{for every }a.           \tag{17}
\]

Here is a source-aware proof of the pointwise version. Let
p=d-floor(N/6) be a factorial maximum index. If a-1<=p, sum (16)
forward. The largest factorial on that prefix is at one of its endpoints,
so |u_a|<=N^2+4N max(1,s_(a-1)^2). Use
s_(a-1)<=N s_a/4. If a-1>p, sum (16) BACKWARD from the literal
endpoint u_d=N-P_d; the remaining factorials decrease, giving
|u_a|<=N+|P_d|+N^2+4Ns_a^2. The proved bound |P_d|<=N^2+floor(N/6)
implies (17), with the generous constant displayed. The negative
normal current has the corresponding bound with s_(d-a), by (13).
No exponentially conditioned eigenframe is used.

Conversely choose p/N->5/6 with p+1<=d. Equation (11) and (16) give

\[
 \max_a|u_a|\ge\tfrac12|u_{p+1}-u_p|
             =\tfrac12|P_p|\asymp N^{-1/2}s_p^2.
\]

The uniform factorial estimate in (17) now proves the SHARP all-input
first-normal norm for BOTH original signs:

\[
 \boxed{\displaystyle
 \log\|\mathcal M_\pm'(1)\|_{\mathrm{op}}
                  =\frac{v_3}{\pi}N+O(\log N).}        \tag{18}
\]

At phase one the same complete operators are only the known scalar
Markov units. Nevertheless Cauchy's derivative inequality implies
that a uniform subexponential bound on a c/N COMPLEX disk, for every
physical input, is impossible. More generally its supremum is at least
exp[Nv_3/pi-o(N)] on every radius exp[-o(N)]. This does not contradict
the [specific normalization-clock disk theorem](actual_normalization_clock_disk_bound.md):
that theorem keeps one specified recording/source packet, not every
physical input of an opened normalization tangle. It also does not
contradict a bound with the explicit factorial energy (17), a coherent
multi-crossing reduction, or a statement on the actual fixed marked
source trajectory. No off-phase change of the chosen cut is made here.

## 5. Audit

[The independent finite audit](../experiments/audit_actual_normalization_endpoint_gaussian.py)
checks the original factorial sum against the complete spectral-jet
formula, the full centered quadratic sum and all source phases. It
also checks the nonzero leading normalization and the reflected Green
tail on growing levels. These tests supplement the uniform proof in
Sections2--3; no lower bound is inferred from a fitted numerical rate.

The finite audit checks nine literal full-R-cubed original pivotal sources
N=2,...,10, including every open-cut column and the full Cartan scalar;
768 literal signed twisted-Markov polynomial coefficients at ALL
physical inputs, their exact Ward recurrences and normal endpoints;
thirteen exact quadratic-source/Green/current levels through N=768;
and three
finite-integral Poisson boundary checks. The latter use an exact finite
Gaussian-erf formula with both endpoints, independently checked against
direct integration before testing truncated Poisson sums.