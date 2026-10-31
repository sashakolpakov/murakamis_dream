# Exact sine-binomial coefficients and a positive finite-moment law for the original Green tail

31 October 2026. Internally reviewed analytical research theorem. This starts from
the ORIGINAL nodal tail T_(a,M) in the maximal-Green block transport.
It provides an exact positive-moment representation of that signed
kernel. It does not bound the signed pairing by an endpoint source
or by Phi_D. Every moment and polynomial truncation is explicit.

## 1. Original node, tail, and normalization

Let N>=3, theta=pi/N, q=exp(i theta),
M=floor(N/2)-1, and choose 0<=a<=M. Put

\[
m=M-a,\qquad h=a+1,\qquad s_r=2\sin(r\theta),
\qquad d_r=a_a-a_r=s_{r+a+1}s_{r-a},
\qquad a_r=2+2\cos((2r+1)\theta).
\]

The original positive nodal tail is precisely

\[
T_{a,M}(x,c,y)=
\sum_{r=0}^m c^{m-r}K_{a,a+r}(x,y;-a_a)
\prod_{i=r+1}^m s_i s_{2a+i+1}.
\tag{1}
\]

In particular its actual Green occurrence is T_(a,M)(x,-c,y).
Nothing changes the original level, unused suffix, node a, or
parent pairing [c^M].

Define, on the finite ranges used below,

\[
\begin{aligned}
B_a(l)&=\prod_{i=1}^l\frac{s_{a+i}}{s_i},&B_a(0)&=1,\\
A_r&=\prod_{i=1}^r\frac{s_{a+i}}{s_{2a+i+1}},&A_0&=1,\\
D_{a,m}&=\prod_{i=1}^m s_i s_{2a+i+1}.
\end{aligned}
\tag{2}
\]

All these factors are strictly positive for 0<=r,l<=2m.
Indeed the largest denominator index in A_(2m) is N-1 at even N
and N-2 at odd N. The largest numerator index in B_a(2m) is also
strictly less than N. Empty products are one.

## 2. The exact nodal continuant coefficients

Normalize the original interval continuant by

\[
Q_r(x,y)=
\frac{K_{a,a+r}(x,y;-a_a)}{\prod_{i=1}^r s_{a+i}^2}.
\]

The actual nodal recurrence is

\[
\begin{gathered}
Q_0=1,\qquad Q_1=x+y,\qquad
Q_r=(x+y)Q_{r-1}-\gamma_rxyQ_{r-2},\\
\gamma_r=\frac{s_{r-1}s_{2a+r}}{s_{a+r}s_{a+r-1}},
\qquad r\ge2.
\end{gathered}
\tag{3}
\]

The gamma identity is the original cofactor identity, not a
positivity assumption. The following explicit formula holds:

\[
Q_r(x,y)=\sum_{l=0}^r
\frac{B_a(l)B_a(r-l)}{B_a(r)}x^l y^{r-l},
\qquad 0\le r\le m.
\tag{4}
\]

Proof. The endpoint coefficients are one. For an interior l,
substitute B_a(n)/B_a(n-1)=s_(a+n)/s_n into the coefficient
recurrence (3). After multiplication by the common denominator,
the required identity is exactly

\[
s_r s_{a+l}s_{a+r-l}
=s_{a+r}\bigl[s_{r-l}s_{a+l}+s_l s_{a+r-l}\bigr]
-s_{2a+r}s_l s_{r-l}.
\tag{5}
\]

Expanding each sine into exponentials, or using the product-to-sum
identity twice, proves (5). This proves (4) inductively from the
literal original recurrence. No identification with an external
orthogonality measure or quantum turn is needed.

Insert (4) into (1). The scalar factors telescope:

\[
\frac{\prod_{i=1}^r s_{a+i}^2}{B_a(r)}
\prod_{i=r+1}^m s_i s_{2a+i+1}
=D_{a,m}A_r.
\]

Consequently the FULL original tail is

\[
\frac{T_{a,M}(x,c,y)}{D_{a,m}}
=\sum_{\substack{l,k\ge0\\l+k\le m}}
A_{l+k}B_a(l)B_a(k)x^l y^k c^{m-l-k}.
\tag{6}
\]

The original negative child character is therefore retained by
c->-c; it is not absorbed into an unknown normalization.

## 3. Exact unit-circle alphabet, on the required finite coefficient range

Let

\[
W_a(x,y)=
\{xq^{a-2r}:0\le r\le a\}
\uplus
\{yq^{a-2r}:0\le r\le a\}.
\tag{7}
\]

as a MULTISET, so repeated values are retained. For any finite
multiset W, define H_r(W) by

\[
\prod_{w\in W}(1-wt)^{-1}
=\sum_{r\ge0}H_r(W)t^r.
\]

This is a formal rational identity, with no convergence claim.
The finite sine-binomial identity is

\[
\prod_{r=0}^a(1-q^{a-2r}t)^{-1}
=\sum_{l\ge0}b_l t^l,
\qquad b_l=B_a(l)\quad(0\le l\le2m).
\tag{8}
\]

For clarity, the sine quotient is asserted ONLY before the
denominator reaches a sine zero. The rational series defines b_l
at all higher degrees; a literal sine quotient need not do so.

One elementary proof of (8) is induction on a using the actual
geometric progression of the variables: separating q^a gives
b_l^(a)=q^a b_(l-1)^(a)+q^(-l)b_l^(a-1).
The product sine expression in (2) satisfies this relation by the
finite geometric-series identity. Equivalently, multiplying the
rational series by its denominator verifies its coefficients up
to degree 2m, where every sine division is legitimate.

Thus on the required range,

\[
H_r(W_a(x,y))
=\sum_{l=0}^r B_a(l)B_a(r-l)x^l y^{r-l}.
\tag{9}
\]

The unit-circle phases in (7) are exact original-level phases.
Their existence alone does not identify a positive inner product
on the shared face coefficient or justify a physical turn.

## 4. A positive beta-product law with the exact moments

There exists a positive random variable X_(N,a) such that

\[
\mathbb E X_{N,a}^{\,r}=A_r,\qquad 0\le r\le2m.
\tag{10}
\]

Its construction retains all original sine factors. Use h=a+1 and
take mutually independent variables

\[
B_0\sim\operatorname{Beta}(h,h),\qquad
V_k\sim\operatorname{Beta}(kN+h,h),\qquad
U_k\sim\operatorname{Beta}(kN-2h+1,h),\qquad k\ge1.
\tag{11}
\]

All shape parameters are positive. Define the partial products

\[
X_K=B_0\prod_{k=1}^K\frac{V_k}{U_k}.
\]

For real s in the open interval

\[
-h<s<N-2h+1.
\tag{12}
\]

the beta integral gives

\[
\begin{aligned}
\mathbb E B_0^s
&=\frac{\Gamma(h+s)\Gamma(2h)}
{\Gamma(h)\Gamma(2h+s)},\\
\mathbb E(V_k/U_k)^s
&=\frac{\Gamma(kN+h+s)\Gamma(kN+2h)}
{\Gamma(kN+h)\Gamma(kN+2h+s)}\\
&\quad\cdot
\frac{\Gamma(kN-2h+1-s)\Gamma(kN-h+1)}
{\Gamma(kN-2h+1)\Gamma(kN-h+1-s)}.
\end{aligned}
\tag{13}
\]

At an integer r, Euler's sine product yields

\[
A_r=\frac{(h)_r}{(2h)_r}
\prod_{k\ge1}\prod_{i=0}^{r-1}
\frac{kN-h-i}{kN-2h-i}
\frac{kN+h+i}{kN+2h+i}.
\tag{14}
\]

Here (h)_r denotes the rising factorial. This is precisely the moment of X_K in the limit, with the
two factors in (13). No square is present here; this is a
different law from the [earlier protected-cap moment](research_flat_cap_positive_moment_form.md).

For completeness, convergence is not merely formal. For fixed
N,a and s in a compact subinterval of (12), the logarithm of the
k-th factor in (13) is O_s((kN)^(-2)); its first two derivatives
in s obey the same bound. The two potential terms of order
1/(kN) cancel. Hence

\[
\sum_k\left|\mathbb E\log(V_k/U_k)\right|<\infty,
\qquad
\sum_k\operatorname{Var}\bigl(\log(V_k/U_k)\bigr)<\infty.
\]

The centered log series converges in L2, and its means converge
absolutely. Thus X_K converges in probability to a positive finite
X_(N,a). For any integer 0<=r<=2m choose epsilon>0 with
r+epsilon<N-2h+1. Formula (13) and its convergent product give
sup_K E X_K^(r+epsilon)<infinity. Uniform integrability then gives
E X_(N,a)^r=lim_K E X_K^r, proving (10).

The same argument gives the EXACT Mellin transform for every real
s in (12), not only the integers:

\[
M_{N,a}(s):=\mathbb E X_{N,a}^{\,s}
=\mathbb E B_0^s\prod_{k\ge1}\mathbb E(V_k/U_k)^s.
\tag{14a}
\]

with the factors in (13). For s!=0 choose p>1 sufficiently close
to 1 that ps is still in (12). The convergent gamma product at
ps bounds E|(X_K)^s|^p uniformly. This proves uniform
integrability also for negative s, since X_K converges in
probability to a strictly positive X. The value at s=0 is one.

Gamma recursion followed by Euler's sine product gives the exact
successive-Mellin ratio

\[
\frac{M_{N,a}(s+1)}{M_{N,a}(s)}
=\frac{\sin((h+s)\theta)}{\sin((2h+s)\theta)}.
\tag{14b}
\]

whenever both s and s+1 lie in (12). In this domain both sine
arguments lie strictly between 0 and pi. This is a consequence of
the explicit Mellin product (14a), not an assertion that a shift
equation alone determines a measure.

There is a stronger FINITE simplification because h=a+1 is an
integer. Finite gamma recursion in each factor of (13), followed
by Euler's sine product, gives

\[
M_{N,a}(s)=
\prod_{j=h}^{2h-1}
\frac{\sin(j\theta)}{\sin((j+s)\theta)}.
\tag{14c}
\]

for every real s in (12). Explicitly, the base gamma ratio becomes
product_j j/(j+s), and the k-th pair becomes
product_j [(kN+j)(kN-j)]/[(kN+j+s)(kN-j-s)]. These are exactly
the Euler factors in (14c). For integer r the same identity is
also immediate by telescoping the two length-r sine products.

In particular an alternative exact realization needs only h
independent variables: for h<=j<=2h-1 let Y_j have density

\[
\frac{\sin(\pi j/N)}{\pi}\,
\frac{y^{j/N-1}}{1+y}\,dy,\qquad y>0,
\qquad
X_{N,a}=\prod_{j=h}^{2h-1}Y_j^{1/N}.
\tag{14d}
\]

Every j/N lies strictly between zero and one. The Euler beta
integral proves that the density is normalized and that
E Y_j^(s/N)=sin(j theta)/sin((j+s)theta) whenever
-j<s<N-j. Intersecting these intervals gives exactly (12).
Thus (14d) proves (14c) and all finite moments directly. It has
the same law as the earlier construction, since their log-variable
moment-generating functions agree on an interval about zero.
Either realization may be used in the finite identities below.

The available upper threshold is EXACTLY

\[
N-2h+1=
\begin{cases}
2m+1,&N\text{ even},\\
2m+2,&N\text{ odd}.
\end{cases}
\tag{15}
\]

Thus every moment needed for the degree-m kernel, even its
squared finite polynomial, is justified. No moment beyond this
domain is asserted or used.

## 5. Exact signed kernel and original boundary pairing

Combining (6), (9), and (10) gives the finite identity

\[
T_{a,M}(x,c,y)
=D_{a,m}\,\mathbb E H_m\bigl(\{c\}\uplus X_{N,a}W_a(x,y)\bigr).
\tag{16}
\]

Here H_m is the complete homogeneous polynomial of degree m,
not an untruncated rational function. The original signed tail is

\[
T_{a,M}(x,-c,y)
=D_{a,m}\,\mathbb E H_m\bigl(\{-c\}\uplus X_{N,a}W_a(x,y)\bigr).
\tag{17}
\]

Let the actual CROSS spectator product retain its original shared
variables and write

\[
P_N(c,Y)=\sum_s p_s(Y)c^s,\qquad
P_{\le M}(c,Y)=\sum_{s=0}^M p_s(Y)c^s.
\]

Then EXACTLY

\[
[c^M]T_{a,M}(x,-c,y)P_N(c,Y)
=D_{a,m}(-1)^m\,\mathbb E
\sum_{r=0}^m H_r\bigl(-X_{N,a}W_a(x,y)\bigr)p_{a+r}(Y).
\tag{18}
\]

The actual factor R_a(x,b,y;-a_a) is to be multiplied afterward,
as in the original Q_(a,N). Equation (18) uses precisely the
original face demand M in the reduced block, hence the original
d demand before the already proved lower-block factorization.
The only spectator coefficients used are a<=s<=M. Nothing here
permits changing a, shifting a neighboring demand, or assigning
independent radii to shared faces.

Every random power in (16)-(18) is at most m. The sum is finite,
so extraction and expectation may be interchanged. For a
nontrivial cap component the existing independent signed
path-dilation averages may be applied coefficientwise first;
the same total-degree truncation remains mandatory.

The formal generating representation behind (16) is useful but
must remain a FINITE coefficient statement. The integral of
product_(w in W)(1-Xwt)^(-1) is not automatically a holomorphic
function near t=0, and may have actual poles for real t. For
example if a is even, W contains x and y themselves; X has
unbounded support, so positive real t can meet a denominator
zero. No untruncated rational integral, missing moment, or
absolute contraction is inferred from (16).

## 6. Exact limitation of copying the protected-cap tail argument

Unlike the earlier cap law, this law does not have a uniformly
bounded last available even moment. Put S_j=product_(r=1)^j s_r.
The elementary reflection S_(N-1-r)=N/S_r gives

\[
A_{2m}=
\begin{cases}
\dfrac{S_{2h-1}}{S_hS_{h-1}},&N\text{ even},\\[6pt]
\dfrac{s_1S_{2h-1}}{S_{h+1}S_{h-1}},&N\text{ odd}.
\end{cases}
\tag{19}
\]

These are exact, including m=0. If h/N->alpha in (0,.5),
uniform sine-product Riemann sums give

\[
\begin{aligned}
\lim_{N\to\infty}\frac1N\log A_{2m}
&=\int_0^{2\alpha}\log(2\sin(\pi t))\,dt
-2\int_0^\alpha\log(2\sin(\pi t))\,dt\\
&=2\int_0^\alpha\log(2\cos(\pi t))\,dt>0.
\end{aligned}
\tag{20}
\]

The final strict inequality is elementary: log(2cos(pi t))
decreases, crosses zero once at 1/3, and its integral from 0
to 1/2 is zero. Its partial integral is therefore strictly
positive at every interior alpha.

Thus the bounded-last-moment estimate used by the protected-cap
[shared-star proof](research_cap_cross_shared_star_spectral_gap.md) cannot simply be imported at a macroscopic
Green node. This is an exact obstruction to that proposed proof
step, not a counterexample to the signed pairing estimate.
The signed expression (18), including its original source
coefficients, can still be much smaller than any positive
moment or norm estimate.

## Provenance and scope

The original K, T, and lower-block factors are those of
[the original maximal-Green block transport](research_maximal_green_component_block_transport.md) sections 4–6.
Equation (3) is its original normalized nodal recurrence.
The positive-product construction is derived explicitly here
rather than identified with the previous cap metric.

This draft gives exact finite algebra and a finite-moment law.
It proves neither a polynomial bound on Q_(a,N), nor a shared
Phi_D comparison, nor a general long-filling theorem.
No numerical scan or external proof import is used.
Internal review: root full analytical/source review, PASS, including the
real Mellin and finite beta-prime extensions; geometry full independent
analytical/source review of sections 1–6, PASS. These reviews cover the
original nodal coefficients and cutoff, exact probability laws and
convergence, signed parent extraction, and last-moment obstruction.
They do not assert a boundary-reference or Phi_D comparison. No external
peer-review or numerical-audit claim is made.
