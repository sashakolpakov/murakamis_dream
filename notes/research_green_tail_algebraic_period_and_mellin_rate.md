# The original Green pairing as a finite algebraic period and its exact Mellin cost

31 October 2026. **Internally reviewed analytical research theorem.**
Unpublished. The kernel below is the original nodal Green tail with its
original face extraction.
Its contour form is an exact reformulation, not a new quantum
invariant. The final volume comparison remains unproved.

## 1. The finite source data

Use the [exact sine-binomial and finite-moment theorem](research_green_tail_sine_binomial_moment_transform.md). Put

\[
 M=\lfloor N/2\rfloor-1,\quad 0\le a\le M,\quad
 m=M-a,\quad h=a+1,\quad q=e^{\pi i/N},\quad
 s_j=2\sin(\pi j/N),\quad S_j=\prod_{r=1}^j s_r.
\]

Let W be the MULTISET of 2a+2 values

\[
 W=W_a(x,y)=\{xq^{a-2r},yq^{a-2r}:0\le r\le a\}.
\tag{1}
\]

Keep all repeated nodes. Write H_r for the complete homogeneous
polynomial on a multiset. The original tail identity is

\[
 T_{a,M}(x,c,y)=D_{a,m}\,\mathbb E H_m(\{c\}\cup XW),
 \qquad D_{a,m}=\prod_{i=1}^m s_i s_{2a+i+1}.
\tag{2}
\]

Here $X=X_{N,a}>0$ is the independently constructed beta-product
variable. Its actual Mellin transform $M_{N,a}(t)=\mathbb E X^t$ exists on

\[
 -h<t<N-2h+1,
 \qquad
 \frac{M_{N,a}(t+1)}{M_{N,a}(t)}
 =\frac{\sin(\pi(h+t)/N)}{\sin(\pi(2h+t)/N)}
\tag{3}
\]

whenever both moments in the ratio exist. For nonnegative integer r
this is exactly the retained sine product A_r. In particular all
integer moments from -a to m exist. No moments beyond the actual
domain in (3) will be used.

In fact the integer h makes this transform FINITE:

\[
 M_{N,a}(t)=\prod_{j=h}^{2h-1}
          \frac{\sin(\pi j/N)}{\sin(\pi(j+t)/N)}.
\tag{3a}
\]

One concrete choice is $X=\prod_{j=h}^{2h-1}Y_j^{1/N}$, with
independent positive variables of density

\[
 \frac{\sin(\pi j/N)}\pi\,
        \frac{y^{j/N-1}}{1+y}\,dy,\qquad y>0.
\tag{3b}
\]

The Euler beta integral gives each factor of (3a), with exactly the
moment interval in (3). This agrees with the upstream infinite-product
law: for integer h its gamma factors telescope to j/(j+t) and, for
each k>=1, (kN+j)(kN-j)/((kN+j+t)(kN-j-t)); Euler's sine product
then gives (3a). Thus no moment-interpolation uniqueness is assumed.

Let P(c,Y)=sum_s p_s(Y)c^s be the actual CROSS spectator product,
with its shared boundary variables still identified, and define
P_<=M by truncating ONLY its c degree at M. The original nodal
pairing is

\[
 Q_{a,N}(Y)=R_a(x,b,y;u_a)
             [c^M]T_{a,M}(x,-c,y)P(c,Y).
\tag{4}
\]

Thus its untruncated original parent demand remains the one established
in the [maximal-Green component theorem](research_maximal_green_component_block_transport.md). No extra sum or independent
face radius is introduced.

## 2. An exact confluent divided difference

For nodes zeta_1,...,zeta_n, define their confluent divided difference
of a polynomial F by

\[
 [\zeta_1,\ldots,\zeta_n]F
 =\frac1{2\pi i}\oint
        \frac{F(t)}{\prod_{j=1}^n(t-\zeta_j)}\,dt,
\tag{5}
\]

with a positive contour enclosing every node. This definition remains
valid at collisions, including zero nodes. Expanding at infinity proves

\[
 [\zeta_1,\ldots,\zeta_n]t^d
 =\begin{cases}0,&d<n-1,\\H_{d-n+1}(\zeta_1,\ldots,\zeta_n),&d\ge n-1.
 \end{cases}
\tag{6}
\]

The signed version of (2), followed by the ORIGINAL coefficient
extraction, therefore gives exactly

\[
 Q_{a,N}
 =(-1)^m R_a(x,b,y;u_a)D_{a,m}\,
 \mathbb E\,[ -XW ]\bigl(t^{a+1}P_{\le M}(t,Y)\bigr).
\tag{7}
\]

Indeed n=2a+2, so the monomial p_s t^(a+1+s) gives
H_(s-a)(-XW); only a<=s<=M survive. This recovers exactly the
signed finite sum from the upstream kernel theorem. Every surviving
power of X is between 0 and m.

## 3. A fixed contour, retaining all scalar factors

There is a useful stronger form of (7). Define the finite diagonal
Mellin operator on the truncated polynomial by

\[
 (\mathscr M_{N,a}P)(w,Y)
 =\sum_{s=0}^M M_{N,a}(s-a)\,p_s(Y)w^s.
\tag{8}
\]

Choose a fixed circle |w|=R>max(|x|,|y|). For each X>0 take the
contour t=Xw in (5). Homogeneity gives

\[
 \mathbb E\,[ -XW ]\bigl(t^{a+1}P_{\le M}(t,Y)\bigr)
 =\frac1{2\pi i}\oint_{|w|=R}
 \frac{w^{a+1}(\mathscr M_{N,a}P)(w,Y)}
      {\prod_{v\in W}(w+v)}\,dw.
\tag{9}
\]

The exchange of expectation and this FIXED contour is justified, not
formal: before expectation its numerator is X^(-a)P_<=M(Xw,Y).
Every absolute random power is X^(s-a), with -a<=s-a<=m strictly
inside (3), and the fixed denominator is bounded away from zero on
the circle. There are finitely many terms. This also explains why
the untruncated spectator polynomial cannot simply be inserted.

The exact original cofactor adapter is R_a=S_(2a)D_a(x,b,y), where
D_a is the physical half-triangle determinant. Reflection
S_(N-1-r)=N/S_r proves the FULL scalar simplification

\[
 R_aD_{a,m}=\gamma_{N,a}D_a(x,b,y),\qquad
 \gamma_{N,a}=
 \begin{cases}
 N/s_{2a+1},&N\text{ even},\\
 N/(s_{2a+1}s_{m+1}),&N\text{ odd}.
 \end{cases}
\tag{10}
\]

To check it, D_(a,m)=S_m S_(a+M+1)/S_(2a+1). In the even case
S_m S_(a+M+1)=N; in the odd case it is N/s_(m+1). These identities
include m=0. In particular gamma is nonzero and bounded above and
below by powers of N, uniformly in a. It is retained explicitly.

Combining (7), (9), and (10) is the exact original-source period:

\[
 Q_{a,N}(Y)=
 \frac{(-1)^m\gamma_{N,a}D_a(x,b,y)}{2\pi i}
 \oint_{|w|=R}
 \frac{w^{a+1}(\mathscr M_{N,a}P)(w,Y)}
 {\prod_{r=0}^a(w+xq^{a-2r})(w+yq^{a-2r})}\,dw.
\tag{11}
\]

All integer Mellin entries in (8) are finite products of sine ratios
by (3). Thus (11) is a finite algebraic functional over the original
cyclotomic coefficient field. The positive probability law gives one
representation and useful estimates for that functional; it does not
change its definition. Repeated poles in (11) mean confluent residues,
not factors to be divided out or discarded.

The diagonal operator also has an exact finite q-differential
description. On its actual coefficient range 0<=s<=M,

\[
 M_{N,a}(s-a)=\frac{S_{2a+1}S_s}{S_aS_{s+a+1}}.
\tag{11a}
\]

Define the symmetric sine derivative on polynomials by

\[
 \partial_q f(w)=\frac{f(qw)-f(q^{-1}w)}{iw},\qquad
 \partial_q w^n=s_n w^{n-1}.
\]

For the actual numerator $F(w)=w^{a+1}(\mathscr M_{N,a}P)(w)$,

\[
 \partial_q^{a+1}F(w)=\frac{S_{2a+1}}{S_a}P_{\le M}(w).
\tag{11b}
\]

Every sine division here has index at most M+a+1<=2M+1<N.
Thus this is a literal root-safe polynomial identity. Moreover F
is the unique solution divisible by w^(a+1) of degree at most
M+a+1: the displayed diagonal derivative has no zero coefficient
on that space. No root-of-unity resonance is silently inverted.
This supplies a finite operator characterization of the same
numerator in (11); it asserts no generic-q AJ equation or new
topological invariance theorem.

There is a precise affine freedom here. All solutions of (11b) of
degree at most M+h form a torsor for the additive space of polynomials
of degree below h. The full-node contour in (11) annihilates this
space: its denominator has degree 2h, and a numerator of degree below
h has no residue at infinity. The original period is therefore
independent of those q-integration constants. This statement concerns
the stated full-node cycle; it need not hold for a contour enclosing
only a selected subset of poles.

This freedom can remove one whole q-string without losing a residue.
Put

\[
 P_x(w)=\prod_{r=0}^a(w+xq^{a-2r}),\qquad
 F(w)=P_x(w)B_x(w)+A_x(w),\quad \deg A_x<h.
\]

This is ordinary division by a MONIC polynomial; it is valid even at
zero or colliding face arguments. The remainder does not contribute
to the full period. Also $\partial_q^h A_x=0$. Thus B_x is exactly the
unique polynomial of degree at most M solving

\[
 \partial_q^h\bigl(P_x(w)B_x(w)\bigr)
      =\frac{S_{2a+1}}{S_a}P_{\le M}(w).
\tag{11c}
\]

Uniqueness follows from the same degree bound: a difference would make
P_x times a polynomial lie in the degree-below-h kernel, hence vanish.
Finally the symmetric q-string divided-difference identity is

\[
 [zq^a,zq^{a-2},\ldots,zq^{-a}]B
        =\frac{\partial_q^aB(z)}{S_a},\qquad \deg B\le M.
\]

Check it on w^s: both sides vanish for s<a, and for s>=a the
finite sine-binomial identity gives
S_s z^(s-a)/(S_a S_(s-a)). All required indices are below N.
The exact same original nodal pairing is therefore

\[
 Q_{a,N}=
 \frac{(-1)^m\gamma_{N,a}D_a(x,b,y)}{S_a}
             (\partial_q^a B_x)(-y).
\tag{11d}
\]

Confluent nodes cause no exception: monic division and the polynomial
q-string identity include them. In particular x=y retains the
repeated-pole information of the original contour. The additional
factor 1/S_a in (11d) is explicit and can be exponential; it has not
been declared harmless. The order h grows with the quantum node, so
(11c) is not a fixed-order generic-q quantum A-polynomial assertion.

For a genuine cap tree, first replace the spectator coefficients by
their [proved finite signed path-dilation averages](research_maximal_green_component_block_transport.md). Its total
component degree is truncated at M before that average. The independent
Green variable X then gives the same (7)-(11) coefficientwise, retaining
the original outside factor U_0^(number of cap edges). All moments used
by each independent variable stay in its proved range.

## 4. The exact interior Mellin growth

Consider ANY sequence of the original indices for which
h/N -> alpha with 0<alpha<1/2. Put Y_N=log X_(N,a). For

\[
 -\alpha<s<1-2\alpha,
\qquad
 \kappa_\alpha(s)=\int_0^s
 \log\frac{\sin(\pi(\alpha+t))}{\sin(\pi(2\alpha+t))}\,dt,
\tag{12}
\]

the integral is oriented when s<0. Then

\[
 \frac1N\log\mathbb E e^{NsY_N}\longrightarrow\kappa_\alpha(s).
\tag{13}
\]

Convergence is uniform on compact subsets of the admissible
(alpha,s) region. This covers both parities without replacing N.

Proof at integer t=Ns uses (3) and M(0)=1: log M(t) is the sum of
the retained log sine ratios, oriented backward for negative t.
On a compact subregion the two sine arguments stay uniformly away
from their zeros. The Riemann sums therefore give (12) uniformly.
For arbitrary real t between adjacent integers, convexity of log M(t)
places it below the joining chord and above the extrapolated preceding
chord. The successive integer differences are uniformly bounded on
these compact sets, again by (3). Interpolating changes the logarithm
by O(1), which proves (13). No derivative of an unproved asymptotic is
used.

There is also a direct proof from the finite product (3a), valid for
real s without interpolation. Its normalized logarithm is the Riemann
sum of log(sin(pi t)/sin(pi(t+s))) over h/N<=t<2h/N. The limit is
the integral over alpha<=t<=2alpha. It equals (12): both vanish at
s=0, and their s derivatives are the first expression in (14).
All arguments remain in a fixed compact subset of (0,1) on the stated
parameter compacts, so the convergence is uniform.

The limit is strictly convex:

\[
 \begin{aligned}
 \kappa_\alpha'(s)&=
 \log\frac{\sin(\pi(\alpha+s))}{\sin(\pi(2\alpha+s))},\\
 \kappa_\alpha''(s)&=
 \frac{\pi\sin(\pi\alpha)}
 {\sin(\pi(\alpha+s))\sin(\pi(2\alpha+s))}>0.
 \end{aligned}\tag{14}
\]

Its first derivative ranges from -infinity to +infinity on the
open interval in (12). The typical positive value is
exp(kappa_alpha'(0))=1/(2cos(pi alpha)).

## 5. A proved large-deviation cost, not a bounded-moment shortcut

Define for y real

\[
 I_\alpha(y)=\sup_{-\alpha<s<1-2\alpha}
              \{sy-\kappa_\alpha(s)\}.
\tag{15}
\]

The laws of Y_N satisfy the large-deviation bounds with speed N
and this rate: the logarithmic probability of any open set is at
least minus the infimum of I there, and that of any closed set is
at most minus its infimum. The rate is good, finite and strictly
convex, with its unique zero at log(1/(2cos(pi alpha))).

Here is a direct proof sufficient for the stated claim. Fixed positive
and negative s in (12), together with (13) and Markov's inequality,
give exponential tightness. For a compact set, apply the same bound
with a near-optimal s at each point and take a finite interval cover;
letting interval widths decrease proves the closed-set upper bound.
For the lower bound at y choose the unique s with kappa_alpha'(s)=y
and tilt the probability law by exp(NsY_N)/M(Ns). Under this law,
small positive and negative tilts, (13), and strict differentiability
give exponentially small probabilities for Y_N outside (y-epsilon,
y+epsilon). Undoing the tilt on that interval gives lower rate
-I_alpha(y)-|s|epsilon. Let epsilon decrease to zero and then take
the best y in the open set. Exponential tightness extends the upper
bound from compact to closed sets. Finally I grows at least linearly
at both infinities by choosing one fixed tilt of each sign, so its
level sets are compact. These arguments establish the asserted
bounds directly rather than importing a large-deviation theorem.

The optimizing tilt has an explicit form. For xi=e^y>0 put

\[
 \vartheta=\operatorname{Arg}(1-\xi e^{-\pi i\alpha})
       \in(0,\pi(1-\alpha)),\qquad
 s_\xi=\vartheta/\pi-\alpha.
\tag{16}
\]

Indeed xi=sin(pi(alpha+s))/sin(pi(2alpha+s)) is equivalent to
tan vartheta=xi sin(pi alpha)/(1-xi cos(pi alpha)), with precisely
the displayed continuous argument branch. Equations (15)-(16)
therefore evaluate the cost without a free saddle choice.

At the upper endpoint, the continuous value of (12) is

\[
 \kappa_\alpha(1-2\alpha)
 =2\int_0^\alpha\log(2\cos(\pi t))\,dt>0.
\tag{17}
\]

This agrees with the exact last-even-moment computation in the
upstream theorem. It is the exponential cost missed by copying
the bounded-last-moment cap argument. The large-deviation statement
does not make that cost disappear.

## 6. Uniform multiplier rates at every node and the exact Plancherel norm

The interior probability limit has an all-node algebraic counterpart.
Define the continuous function

\[
 \ell(t)=\int_0^t\log(2\sin(\pi u))\,du,\qquad 0\le t\le1,
\]

with its integrable endpoint values, and put

\[
 K(\alpha,\beta)=\ell(2\alpha)+\ell(\beta)
                     -\ell(\alpha)-\ell(\alpha+\beta),
 \qquad 0\le\alpha,\beta\le\tfrac12.
\tag{18}
\]

Uniformly over ALL original integers $0\le a,s\le M$ and both parities,

\[
 \frac1N\log M_{N,a}(s-a)
   =K(a/N,s/N)+O(\log N/N).
\tag{19}
\]

To prove it, split the log-sine sum at its midpoint, where its
monotonicity changes. Comparison of each monotone part with its
integral gives, uniformly for $0\le r\le N-1$,

\[
 \log S_r=N\ell(r/N)+O(\log N).
\]

The first and last intervals contribute $O(\log N)$ by integrating
$\log t$ and $\log(1-t)$; away from them the monotone-sum error is
bounded by the endpoint oscillation, also $O(\log N)$. Apply this to
the four products in (11a). Replacing $(2a+1)/N$ and $(s+a+1)/N$
by $2a/N$ and $(s+a)/N$ changes $N\ell$ by at most $O(\log N)$,
including at the endpoints. This proves (19). In the interior,
$K(\alpha,\beta)=\kappa_\alpha(\beta-\alpha)$, either directly by
changing the integral limits or by comparing the derivative in
$\beta$ and the value at $\beta=\alpha$. Equation (19) remains valid
when $\alpha$ approaches zero or $1/2$; it does not claim exponential
tightness of the probability laws at those endpoints.

The original period annihilates the spectator degrees below $a$.
Write its surviving part as $P(c)=c^a p(c)$, where
$p(c)=\sum_{r=0}^m d_rc^r$. On this quotient the exact diagonal
operator is

\[
 (\mathcal T_{N,a}p)(c)=\sum_{r=0}^m A_r d_r c^r,
 \qquad A_r=M_{N,a}(r).
\tag{20}
\]

For $1\le p\le\infty$ give coefficient vectors the weighted norm
$\|d\|_{p,R}=\|(d_rR^r)_{r=0}^m\|_{\ell^p}$, with $R>0$.
If $\rho=R_{\mathrm{out}}/R_{\mathrm{in}}$, the EXACT operator norm is

\[
 \|\mathcal T_{N,a}\|_{p,R_{\mathrm{in}}\to p,R_{\mathrm{out}}}
     =\max\{1,A_m\rho^m\}.
\tag{21}
\]

Indeed a diagonal positive multiplier has norm
$\max_{0\le r\le m}A_r\rho^r$, attained on a monomial. The function
$\log M_{N,a}(r)+r\log\rho$ is convex by Holder's inequality for
the actual positive law, so its maximum on the interval is at an
endpoint. This includes $m=0$. For $p=2$, Fourier orthogonality gives

\[
 \frac1{2\pi}\int_0^{2\pi}|p(Re^{it})|^2\,dt
      =\sum_{r=0}^m|d_r|^2R^{2r}.
\tag{22}
\]

Thus (21) is also the exact Plancherel operator norm on these finite
Fourier polynomials. No unproved polynomial bound is needed for this
step. It is a norm of the Mellin multiplier only, not yet of the full
q-boundary solution or the original signed pairing.

For any sequence $a/N\to\alpha\in[0,1/2]$, (19) implies

\[
 \frac1N\log A_m\longrightarrow\frac12\ell(2\alpha),
\tag{23}
\]

and for fixed positive $\rho$,

\[
 \frac1N\log\|\mathcal T_{N,a}\|
  \longrightarrow
  \max\left\{0,\frac12\ell(2\alpha)
                  +(\tfrac12-\alpha)\log\rho\right\}.
\tag{24}
\]

For (23), the limiting coefficient index in (19) is $s=M$, hence
$\beta=1/2$. The reflection identity $\ell(1-t)=-\ell(t)$,
$\ell(1/2)=0$, and

\[
 \ell(2\alpha)=2\ell(\alpha)
                    +2\int_0^\alpha\log(2\cos(\pi t))\,dt
\]

give $K(\alpha,1/2)=\ell(2\alpha)/2$. The same uniform estimates
justify both endpoint values and both parities. At equal radii the
multiplier has subexponential norm for $0\le\alpha\le1/4$ and at
$\alpha=1/2$, and positive norm rate for $1/4<\alpha<1/2$.
The rational denominator and the divided-difference functional in
(11) still have to be estimated. Neither (21) nor (24) pays those
additional costs or proves a whole-source volume bound.

## 7. What this resolves and what it does not

The isolated Green/CROSS pairing is now one explicit cyclotomic
rational period with a finite diagonal sine-ratio operator, and the
positive representation of that operator has an explicit rate
function. This retains the actual quantum jets, parent demand,
odd scalar, and all confluent poles. Its derivation makes no appeal
to equality with a different invariant or a generic A-polynomial.

An absolute estimate on (11) is still required. Its denominator has
O(N) factors and its input polynomial has degree O(N); a contour
deformation, a residue expansion, or a Cauchy inequality can therefore
carry exponential costs. The proved moment rate quantifies one such
cost but does not bound the whole signed integrand by Phi_D. Nor does
the positive law justify replacing the signed integral by its Laplace
maximum. The original peripheral action is retained by the prior
whole-source assembly, not newly identified by (11).

The interior probability-rate proof assumes alpha stays away from zero
and one half. Section 6 gives uniform algebraic multiplier rates at ALL
endpoint indices; it does not assert a good probability large-deviation
principle there. No general prescribed-diagram volume theorem is claimed
here.

## Review and scope

The parent derived and read the complete analytical argument. Two
independent internal reviewers read the original period and interior-rate
argument (now sections 1–5 and 7) in full and reported
PASS, including the confluent residues, original coefficient demand,
negative moments, both parity factors, uniform interior Mellin limit,
and tilted-law proof. A further independent adversarial review of
(11a)–(11d) checked the q-integration constants, monic division,
colliding strings, and explicit $S_a^{-1}$ factor. The new section 6
received a separate full analytical/source review: uniform all-node
log-sine errors, exact surviving-degree normalization, weighted diagonal
norm, Parseval identity, and both parity/endpoint limits all PASS.
These are internal
proof reviews, not external peer review. Reader/link validation is
separate from mathematical validation; no numerical asymptotic scan
is presented as a proof.

The [block-contraction theorem](research_original_block_contraction_and_cap_budget.md)
still governs any use of this kernel in the complete source. A mask
that cuts an internal signed sum need not preserve the period. The
[current critical path](research_general_long_twist_critical_path.md)
records the remaining absolute comparison and the distinction between
selected diagrams and arbitrary prescribed long-twist diagrams.
