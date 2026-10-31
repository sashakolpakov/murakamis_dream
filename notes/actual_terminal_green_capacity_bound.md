# Boundary control of the original terminal Green packet

29 October 2026. The original terminal packet admits a quantitative
all-input estimate after one literal adjacent inverse is retained.
The argument uses its ACTUAL complete endpoint value before taking
absolute values. It does not bound independent Green summands or
discard the current. An arbitrary preceding three-head braid and an
arbitrary external coefficient space remain open.

Use the conventions of
[the closed terminal kernel](actual_terminal_packet_closed_kernel.md):
N>=2, d=N-1, q=exp(pi*i/N), Q=q^2, x=q^d, F_a=(Q;Q)_a,
s_a=|F_a|, kappa=q^(d^2/2). R below is the FULL original positive
checked crossing restricted to pair integer degree d. T is the original
N-row physical terminal map (1) of that note, on the complete module W.

## 1. The whole Green--Pascal packet is a crossed diagonal current

Let X=diag(x^n), and let P be the actual coherent finite solution

\[
 P_0=1,\qquad P_t=(1-Q^t)^2P_{t-1}+Q^t,
 \qquad P_t=F_t^2\sum_{v=0}^t Q^v/F_v^2.
\]

Put P_rev=diag(P_(d-j)). Then the ENTIRE terminal matrix is

\[
 \boxed{\displaystyle T=\frac1N X R P_{\mathrm{rev}}R.}             \tag{1}
\]

This is an identity on every input column, independently of a prefix.
Both full Cartan scalars remain in R. To check (1) directly from the
closed kernel, put L=kappa^(-1)R, and use its exact strict entries

\[
 L_{i,j}=x^{-d+h}Q^{(d-j)(d-i)}
        \frac{F_iF_j}{F_hF_{d-j}F_{d-i}},\qquad h=i+j-d\geq0.
\]

For the squared Pascal matrix U^(2) in that note, root reflection gives

\[
 L\,\mathrm{Rev}=x^{-d}D_\alpha U^{(2)}D_\beta,
\quad
 \alpha_n=(-1)^nx^nQ^{-n(n+1)/2},\quad
 \beta_t=(-1)^tx^{-t}Q^{t(t-1)/2}.
\]

The two diagonal interfaces in its formula (13) simplify exactly:
D_out D_alpha^(-1)=X and D_beta^(-1)D_in=I. Finally
kappa^2=x^d, giving (1). No sum or absolute value is used in this
step. In particular this is not a claim that arbitrary Pascal factors
are unitary or that an unmatched source frame can be removed.

The all-input packet immediately following a literal R12^(-1) is

\[
 H_N:=TR^{-1}=\frac1N X R P_{\mathrm{rev}}.                       \tag{2}
\]

Its original boundary row is 1^T H_N. Thus the positive completion
H_N^dagger H_N+exp(-N^2)I has the SAME polynomial boundary dual cost
at most N as the original terminal construction. No inverse of P
or T is involved.

## 2. The actual endpoint closes polynomially at every parity

The endpoint of this Green solution is exactly

\[
 \boxed{\displaystyle P_d=\sum_{j=0}^d F_j.}                  \tag{3}
\]

Indeed the shifted Durfee identity proved with the closed kernel gives

\[
 P_d=N\sum_{r=0}^d\frac{(-1)^rQ^{r(r+1)/2}}{F_r}.
\]

Reflecting F_(d-r) and using
Q^[d(d+1)/2]=(-1)^d turns the last sum into sum_j F_j.
This uses no endpoint asymptotics or nonvanishing assumption.

There is now a shorter independent endpoint estimate, with no spectral
trace input. Put H_N(t)=sum_j F_j t^j and k=floor(N/6). Its exact
Ward identity is (1-t)H_N(t)+tQH_N(Qt)=1. Backward propagation for
k steps at t=1 has forcing at most k and remainder at most
s_k sum_j s_j. Since s_k=min_j s_j and max_j s_j=N/s_k,

    |P_d|=|H_N(1)|<=k+N^2.

The complete argument, including complex disks and all normal
derivatives, is in the
[clock-disk theorem](actual_normalization_clock_disk_bound.md).
It independently implies the 3N^2 bound used below. The original
trace derivation is retained as a second source check.

Here is the source-specific bound on (3), including the nonsemisimple
trace. The previously derived original trefoil source is
K_N=Q sum_j F_j=(-q)^3 Phi_N(r_N^3), so
P_d=-q Phi_N(r_N^3). The actual pivotal functional is

\[
 \Phi_N(f)=-\sum_{a\text{ odd},\,0<a<N}
       [c_a f(c_a)+(c_a^2-4)f'(c_a)]
              +\begin{cases}f(-2),&N\text{ odd},\\0,&N\text{ even},\end{cases}
\]

where c_a=q^a+q^(-a), and

\[
 |\nu_a|=1,\qquad r_N(c_a)=\nu_a,\qquad
 r_N'(c_a)/\nu_a=-\frac{N-a}{2(q^a-q^{-a})}.
\]

These are the finite generic-q specialization and full pivotal
partial trace, independently proved in
[the spectral-source theorem](casimir_braiding_and_recoupling_lattice.md#8-the-actual-closing-trace-is-a-spectral-jet-functional),
with the literal original source identification in
[the complete clock calculation](actual_overclock_sector_obstruction.md#3-two-successive-macroscopic-cancellations).
No positive trace is substituted. A double-node contribution for f=r^3
has modulus at most 2+3N: c is bounded by 2, and its derivative term
has modulus at most 3(N-a)|q^a-q^(-a)|/2<=3N. The possible odd simple
term has modulus one. Consequently, at EVERY N>=2,

\[
 |P_d|\leq3N^2.                                               \tag{4}
\]

The common Cartan and framing factors in this source calculation
combine to the explicit unit phase above. There is no unknown knot
period in (4), and the formula includes every Jordan derivative.

## 3. Boundary-to-interior Green bound

For all 0<=t<=d one has the uniform finite estimate

\[
 \boxed{\displaystyle |P_t|\leq N+4s_t^2.}                    \tag{5}
\]

For t<=floor(N/6), forward recurrence has |1-Q^j|^2<=1, hence
|P_t|<=t+1<=N. For larger t use the EXACT backward expression

\[
 P_t=F_t^2\left(\frac{P_d}{N^2}
                        -\sum_{v=t+1}^d\frac{Q^v}{F_v^2}\right). \tag{6}
\]

The sequence s_v first increases after its low minimum, and then
decreases to s_d=N. Therefore, for v>=t in the indicated range,
s_v>=min(s_t,N). Substitution of (4) in (6) gives

\[
 |P_t|\leq3s_t^2+N\max(1,s_t^2/N^2)\leq N+4s_t^2.
\]

Thus the coherent endpoint cancels the potentially large forward
Green current before any norm estimate. Merely applying absolute
values to the defining partial sum does not give (5).

There is a useful nonzero local density. Uniformly for t/N in any
compact subinterval of (1/6,1/2),

\[
 P_t=\frac1{2-Q^t}+O(1/N).                                  \tag{7}
\]

To prove it, put m=floor(N/2) in (6). The endpoint and terms with
v>=m are exponentially small after multiplication by F_t^2:
J(t/N)<0 whereas J(v/N)>=-O(log(N)/N), where
J(u)=integral_0^u log(2sin(pi*s))ds. On t<v<m all inverse factors
|1-Q^v|^(-2) are bounded by a fixed number r<1. For v=t+k,

\[
 Q^{t+k}F_t^2/F_{t+k}^2
       =Q^t(1-Q^t)^{-2k}+O(k^2 r^k/N),
\]

after possibly increasing r while keeping r<1. This follows by
telescoping the k product factors; the factors and their derivatives
are uniformly bounded on this compact interval. Sum the error and
the geometric series. Its negative sum is
-z/[(1-z)^2-1]=1/(2-z), z=Q^t. This proves (7), with no formal
adiabatic assumption and no division by P_t.

## 4. A sharp one-octahedron norm for the complete terminal-with-inverse

Define the explicit finite factorial maximum

\[
 M_N=\max_{0\leq k\leq i\leq d}s_i^2/s_k.
\]

Then (2) and (5) imply the finite operator bound

\[
 \boxed{\displaystyle
 \|H_N\|_{\mathrm{op}}\leq\|R|_W\|_{\mathrm{HS}}+4M_N.}                 \tag{8}
\]

Here is the full metric calculation. On the actual support h=i+j-d,
root reflection gives

\[
 |R_{i,j}|=\frac{s_i^2s_j^2}{N^2s_h}.
\]

The matrix in (2) consequently obeys the entry bound

\[
 |(H_N)_{i,j}|\leq|R_{i,j}|+4N|R_{i,j}|/s_j^2.
\]

The second matrix has Hilbert--Schmidt norm at most 4M_N, since
there are at most N^2 entries and
|R_ij|/s_j^2=s_i^2/(N^2s_h). This proves (8). It estimates the
coherent source-selected Green current together with its ACTUAL
crossing and physical complementary charge. It does not independently
maximize unrelated P and Pascal factors.

Let v3 be the regular tetrahedron volume and v8 the regular octahedron
volume. The uniform sine-factorial estimate gives

\[
 \log M_N=\frac{3v_3}{2\pi}N+O(\log N),\qquad
 \log\|R|_W\|_{\mathrm{HS}}=\frac{v_8}{2\pi}N+O(\log N).             \tag{9}
\]

For the first formula maximize 2J(i/N)-J(k/N): J has maximum
v3/(2pi) at 5/6 and minimum -v3/(2pi) at 1/6, simultaneously
admissible. For the second, the actual support has i+j>=d and the
limiting profile is 2J(u)+2J(v)-J(u+v-1). Put
alpha=pi(1-u), beta=pi(1-v), gamma=pi(u+v-1). At fixed gamma,
Lambda(alpha)+Lambda(beta) has unique maximum at alpha=beta.
The remaining derivative of
4Lambda((pi-gamma)/2)+Lambda(gamma) is log cot(gamma/2).
The maximum is at (alpha,beta,gamma)=(pi/4,pi/4,pi/2), with value
v8/2. This proves the second formula directly for this pair degree.
The rounding of d=N-1 and all boundary points costs O(log N).

Since 3v3<v8, (8) yields an upper exponent v8. This is SHARP for
the full open operator, not just an upper diagnostic:

\[
 \boxed{\displaystyle
 \log\|T R^{-1}\|_{\mathrm{op}}
           =\frac{v_8}{2\pi}N+O(\log N).}                     \tag{10}
\]

Indeed take i=j nearest 3N/4. Its actual crossing entry has the
maximal exponent in (9), while t=d-j has t/N->1/4. Formula (7)
gives \(P_{d-j}\to1/(2-\mathrm i)\), a fixed nonzero number. The single entry
of (2), with its factor 1/N retained, supplies the lower bound.
Even and composite levels require no separate argument.

## 5. Arbitrary-prefix source consequence and its limit

For ANY original prefix A on the complete W, consider the literal
terminal word R23^2 R12^(-1) A, with its genuine whole marked source.
Its original scalar and positive coherent energy are

\[
 K_N=\chi_N\,1^{\mathsf T}H_NAp,\qquad
 E_N(A)=\|H_NAp\|^2.
\]

Equations (8)--(10) give the SOURCE-EXACT all-prefix inequality

\[
 |K_N|^2\leq |\chi_N|^2 N E_N(A)
 \leq |\chi_N|^2 N(\|R|_W\|_{\mathrm{HS}}+4M_N)^2\|Ap\|^2.        \tag{11}
\]

Every displayed map can be tensored with an arbitrary exterior
coefficient Hilbert space. The same norm bound holds, with that
space and its ordering untouched. This does not assert a factorization
of an unrelated larger physical multiplicity space into W factors.

The block costs ONE crossing exponent v8 rather than separately
charging three crossings. For example, if A is a fixed m-crossing
three-head prefix, its original highest physical source is p tensor
|0>. Each original physical signed crossing has operator norm bounded
by its Hilbert--Schmidt norm with exponent v8/(2pi); extraction of
the last color0 is the complete multiplicity inverse of norm one.
Thus (11), with all source factors polynomial, yields

\[
 \limsup_N\frac{2\pi}{N}\log|K_N|\leq(m+1)v_8,               \tag{12}
\]

for every one-component original four-plat word of that literal form.
The generic crossing bound for the same displayed word is (m+3)v8.
No favorable packet is substituted for Ap. If an inverse was not
actually present, inserting one and its inverse charges the added
factor in A and does not give this improvement for free.

This is a reusable open-source energy estimate, not the sharp knot
volume theorem. The surviving one-octahedron operator capacity can
still exceed the geometric contribution of a closed knot. Sharper
bounds must use coherent information in Ap and its exterior gluing.

[Audit](../experiments/audit_actual_terminal_green_capacity_bound.py)
checks the exact full-Cartan matrix identity, both actual endpoint
formulas and all small parities, the finite bound (8), and the nonzero
quarter-window density. Its numerical norm rates are diagnostics for
the proved asymptotic, not a replacement for (6)--(10).

The finite audit checks eight original full-Cartan packet matrices;
79 levels of the actual source endpoint and every Green color;
ten coupled finite operator inequalities; five quarter-window
nonzero densities through N=384.