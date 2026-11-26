# Absolute conditional bounds with incoming decrease

Research deduction, 7 November 2026. The real maximized conditional
profile decreases uniformly as the incoming coordinate moves from
\(1/2\) to \(7/10\). Its optimizer stays in an explicit fixed interval.
This gives an upper bound for the **whole finite** conditional factor
and, using the existing absolute cap bound, for the whole
cap--conditional product on that arc. No relative cap asymptotics
away from the half face are needed.

The decrease concerns the real upper profile, not an asserted ratio
of oscillatory finite values. No sign of the actual complex critical
derivative \(\Theta_a\) is assumed. Both selected Fourier alternatives
and their actual reference-dependent affine comparison are retained.
No numerical evaluation is used.

## 1. The real maximization and its optimizer

Use the original full conditional polynomial and phase from
[the complete real-arc packet](research_mixed_real_arc_complete_conditional_packet.md):
\[
\begin{gathered}
C_{1,N}(X,Y)=\sum_{j=0}^{N-1}
       \frac{X^{-j}p_j(X)p_j(Y)}{P_j^3},\qquad
X=e^{-2\pi ia},\quad Y=e^{-2\pi i(x+iH)},\\
Q(t;a,y)=g(a+t)+g(y+t)-3g(t)-g(a)-g(y)+2\pi iat,\\
\frac12\le a\le\frac7{10},\qquad
\frac{11}{50}\le x\le\frac9{20},\qquad
0\le H\le\frac1{100}.
\end{gathered}                                                    \tag{1}
\]
Every primitive, constant, and chirp is the original one.
For real \(0<t<1-a\), define
\[
q_H(t;a,x)=\Re Q(t;a,x+iH),\qquad
          \bar q_H(a,x)=\max_{0<t<1-a}q_H(t;a,x).                 \tag{2}
\]

**Lemma 1.** The maximum has a unique interior optimizer
\(\tau_H(a,x)\), smoothly depending on the real parameters, with
\[
                 \frac9{50}<\tau_H(a,x)<\frac{13}{50}.           \tag{3}
\]

*Proof.* Put \(C(z)=\Re\cot\pi z\). On the real interval in
(2), \(C(a+t)<0\) and \(\cot\pi t>0\). If \(x+t\ge1/2\),
then \(C(x+t+iH)\le0\). Otherwise, since \(H\ge0\),
\[
 C(x+t+iH)\le\cot\pi(x+t)<\cot\pi t.
\]
Therefore
\[
 \partial_t^2q_H
       =\pi\{C(a+t)+C(x+t+iH)-3\cot\pi t\}<0.                   \tag{4}
\]
The first derivative tends to \(+\infty\) at zero and
\(-\infty\) at \(1-a\). This proves existence, uniqueness
and smooth implicit dependence.

The exact derivative is
\[
 \exp(\partial_tq_H)=
 \frac{2\sin\pi(a+t)\,
       |1-e^{2\pi H-2\pi i(x+t)}|}
      {(2\sin\pi t)^3}.                                        \tag{5}
\]
At \(t_-=9/50\), increasing \(e^{2\pi H}\) from one increases
the outgoing modulus. Also
\[
\begin{split}
\sin\pi(a+t_-)&\ge\sin(3\pi/25)>\frac{375}{1024},\\
\sin\pi(x+t_-)&>\frac{91}{100},\qquad
\sin\pi t_-<\frac{11}{20}.                                    \tag{6}
\end{split}
\]
The first bound uses \(\pi>25/8\) and
\(\sin(3/8)\ge3/8-(3/8)^3/6\).
For the second, \(x+t_-\in[2/5,63/100]\); its minimum sine
is \(\cos(13\pi/100)>1-(41/100)^2/2>91/100\).
For the last, \(9\pi/50<4/7\), and
\[
\sin(4/7)<\frac47-\frac{(4/7)^3}{7}
                  =\frac{1308}{2401}<\frac{11}{20}.
\]
Indeed, for \(0<z<1\), the alternating sine estimate gives
\(\sin z\le z-z^3/6+z^5/120<z-z^3/7\), and the latter
polynomial is increasing there. Thus
\[
 \exp(\partial_tq_H(t_-))>
 \frac{(375/1024)(91/100)}{2(11/20)^3}>1.                       \tag{7}
\]
The final cross-product difference is \(205600>0\).

At \(t_+=13/50\),
\[
\sin\pi t_+>\sin(13/16)\ge\frac{17771}{24576}>
\frac{18}{25},\qquad \cos\pi t_+<\frac7{10}.                    \tag{8}
\]
The cosine comparison follows from
\(1-(18/25)^2=301/625<49/100\).
Since \(a+t_+\in[19/25,24/25]\),
\(\sin\pi(a+t_+)\le\cos\pi t_+\). The original elementary
radius bound gives \(e^{2\pi H}<175/164<11/10\).
The numerator in (5) is therefore less than \(147/50\),
whereas its denominator is greater than
\[
 (36/25)^3=\frac{46656}{15625}>\frac{147}{50}.
\]
The last cross-product difference is \(35925>0\).
The derivative at \(t_+\) is negative, proving (3).
\(\square\)

## 2. Exact and elementary incoming decreases

Set \(d=a-1/2\), \(t_-=9/50\), and define
\[
 \mathcal D(a)=J(a)-J(a+9/50)+J(17/25)-J(1/2).                  \tag{9}
\]
In particular \(\mathcal D(1/2)=0\).

**Theorem 2.** Uniformly in (1),
\[
\boxed{\quad
 \bar q_H(a,x)\le\bar q_H(1/2,x)-\mathcal D(a),\qquad
 \mathcal D(a)\ge\frac6{37}d+\frac{15}{16}d^2.
\quad}                                                         \tag{10}
\]
The second inequality is strict for \(d>0\).

*Proof.* At the interior optimizer the envelope derivative is
the incoming derivative of the original phase:
\[
 \partial_a\bar q_H(a,x)
   =\log\frac{\sin\pi(a+\tau_H)}{\sin\pi a}
   \le\log\frac{\sin\pi(a+9/50)}{\sin\pi a}.                     \tag{11}
\]
The outgoing height changes only its independent numerator,
and the real part of the incoming chirp is zero on these real
rows. The ratio decreases with the internal coordinate because
\(a+t\in(1/2,1)\). Integrating (11) gives exactly (9)--(10).

For an explicit bound put \(s=9\pi/50\). The ratio on the right
of (11) is
\[
 \cos s-\tan(\pi d)\sin s
             =\cos s\{1-\tan(\pi d)\tan s\}>0.                  \tag{12}
\]
The cosine alternating bound gives
\[
\cos s<\cos(9/16)
 \le1-\frac{81}{512}+\frac{6561}{1572864}
 =\frac{1330593}{1572864}<\frac{17}{20}.
\]
The final cross-product difference is \(126828>0\).
Thus \(\log\cos s<-6/37\), using
\(\log(20/17)>2(20-17)/(20+17)\). Also
\[
\tan s>\frac9{16}+\frac{(9/16)^3}{3}
                 =\frac{2547}{4096}>\frac35,\qquad
                         \pi\tan s>\frac{15}{8}.               \tag{13}
\]
Use \(\log(1-z)\le-z\) in (12) and
\(\tan(\pi d)\ge\pi d\). The right side of (11) is at most
\(-6/37-(15/8)d\). Integration proves the quadratic bound.
\(\square\)

Equation (11) retains the exact incoming dependence when that
is useful; the elementary bound is not a numerical fit.

## 3. Height allowance and the actual complete polynomial

The optimizer enclosure also improves the outgoing height cost:
\[
 \boxed{\qquad
 \bar q_H(a,x)\le\bar q_0(a,x)+\frac{13\pi}{25}H .
 \qquad}                                                       \tag{14}
\]
At the optimizer \(\tau_H<13/50\), the only change from height
zero is the exact numerator integral
\[
 \int_0^{\tau_H}
 \log\frac{|1-Re^{-2\pi i(x+u)}|}
          {|1-e^{-2\pi i(x+u)}|}\,du,\qquad R=e^{2\pi H}.
\]
All angles have \(x+u\in[11/50,71/100]\), so their
doubled-angle cosines are less than \(1/5\). Squaring shows
\[
 |1-Re^{i\theta}|\le R|1-e^{i\theta}|
 \quad\hbox{if }R\ge1,\quad
              \cos\theta\le(1+R^{-1})/2.
\]
Our angle guard satisfies this condition. The integral is
at most \(\tau_H\log R\le13\pi H/25\), proving (14).

Let \(\Theta(a,y)\) be the original complex critical action
of the complete real-arc packet. Its critical point has real
part in \((1/16,1-a)\). The all-height curvature theorem makes
\(\eta\mapsto\Re Q(\Re t(a,y)+i\eta;a,y)\) convex.
Its derivative is zero at the actual critical height. Its
height-zero value is consequently at least the critical value.
It follows that
\[
 \Re\Theta(a,x+iH)\le\bar q_H(a,x)
 \le\bar q_0(1/2,x)+\frac{13\pi}{25}H-\mathcal D(a).              \tag{15}
\]
This uses the original critical point and zero logarithmic lift.

The [conditional-curvature theorem](research_mixed_half_face_conditional_curvature.md)
proves, with \(c=-J(1/4)\) and \(\delta=x-1/4\),
\[
\begin{split}
\bar q_0(1/2,x)
 &\le5c+\tfrac12\log2\,\delta-\tfrac\pi3\delta^2,\\
\bar q_0(1/2,x)-J(x)/2
 &\le\tfrac{11}{2}c+\tfrac14\log2\,\delta
                                  -\tfrac{143\pi}{384}\delta^2 .
\end{split}                                                       \tag{16}
\]
Both upper profiles therefore retain the additional decrease
\(-\mathcal D(a)\) and the height cost \(13\pi H/25\).

These are upper bounds for the complete finite conditional
polynomial. For all sufficiently large \(N\),
\[
\begin{split}
|C_{1,N}(e^{-2\pi ia},e^{-2\pi i(x+iH)})|
 \le C N^{-1}
 \exp N\left\{5c+\tfrac12\log2\,\delta-\tfrac\pi3\delta^2
                   +\tfrac{13\pi}{25}H-\mathcal D(a)\right\}.
\end{split}                                                       \tag{17}
\]
The constant is uniform on (1), for both parities. Each fixed
mixed \(a,y\)-derivative satisfies the same exponential bound
with a polynomial factor depending on its order, by the
complete holomorphic packet and its original symbol and phase.
All physical rows, aliases and unweighted joins are included.
There is no new deletion or continuation of sampled rows in
(17).

## 4. The whole cap may be bounded absolutely

The [continuous far-half cap theorem](research_mixed_three_four_continuous_far_half_cap.md)
and its [all-real-color completion](research_mixed_three_four_complementary_real_colors.md)
give, for every real ordinary color \(w\) and every \(\tau>0\),
\[
 |U_{0,N}(w,e^{-2\pi ia})|
       \le C_\tau N^{B_\tau}e^{N(B_0+\tau)},\qquad
                         B_0=\frac{1549}{1500},                 \tag{18}
\]
uniformly in the incoming interval (1). Each fixed
ordinary-color derivative has the same rate by the inherited
Markov bound on the complete polynomial. No critical action or
relative asymptotic is assigned to (18). Multiplying (17) and
(18) is a whole-source absolute bound for \(U_{0,N}C_{1,N}\).

Here is its explicit insertion into the actual ordinary-next
selected source. Retain the references and entire finite
factors of [the selected comparison](research_mixed_next_filtered_selected_plateau.md),
with \(H=1/100\), \(y=x+iH\), \(z=u+i\Im z_*\), \(u\in P\),
and \(\beta\in\{0,1\}\). Their third-factor plane and remaining
selected halfweight obey
\[
\begin{split}
|C_{\beta,N}(Y,Z)|\,|d_N(Y)Y^{-N}|^{1/2}|d_N(Z)|^{\beta/2}
 &\le\operatorname{poly}(N)e^{N(B_3(x,u)+7/250+\tau)},\\
h_{\rm sel}(x)&\le\max\{-J(x)/2-3\pi H/4,0\}.
\end{split}                                                       \tag{19}
\]
Both Fourier alternatives and the original correlated
reference are retained. When \(\beta=0\), no outgoing
halfweight is inserted.

Put
\[
\begin{array}{lll}
K_{\rm fac}^{\rm abs}
 =B_0+\tfrac{11}{2}c-\tfrac{23\pi H}{100}+\tfrac7{250},
&b_{\rm fac}=\tfrac14\log2,
&\mu_{\rm fac}=\tfrac{143\pi}{384},\\[1mm]
K_{\rm force}^{\rm abs}
 =B_0+5c+\tfrac{13\pi H}{25}+\tfrac7{250},
&b_{\rm force}=\tfrac12\log2,
&\mu_{\rm force}=\tfrac\pi3 .
\end{array}                                                       \tag{20}
\]
The first height term is exactly
\((13/25-3/4)\pi H=-23\pi H/100\).
The whole selected density has the bound
\[
\begin{split}
&|U_{0,N}(w,X)C_{1,N}(X,Y)d_N(Y)Y^{-N}C_{\beta,N}(Y,Z)|
                                      |d_N(Z)|^{\beta/2}\\
&\quad\le C_\tau N^{B_\tau}
\exp N\left[
 B_3(x,u)+
 \max_{\sigma\in\{\mathrm{fac},\mathrm{force}\}}
 \{K_\sigma^{\rm abs}+b_\sigma\delta-\mu_\sigma\delta^2\}
                      -\mathcal D(a)+\tau\right].
\end{split}                                                       \tag{21}
\]
It is uniform for all real ordinary colors and both next types.
In particular it requires only the absolute bound for the
whole cap, not its continued relative packet.

For an actual reference, its allocated action \(A_*\), real
coordinate \(a_*\), and real marginal \(p_*\) still satisfy
\[
 A_*+p_*(x-a_*)+B_3(x,u)\le\Lambda_{123}(z).
\]
The difference between this actual affine action and (21)
must still be assessed with these correlated quantities.
The clipped quadratic maximum in the conditional-curvature
theorem applies with (20) and the additional
\(-\mathcal D(a)\). No sign of that comparison is asserted.

## 5. Symbolic transport of any paired endpoint lower bounds

This short consequence explains how the stronger height
allowance and curvature can be used without discarding an
interior minimum. It does not evaluate or reinterpret the
inconclusive saved test.

For one Fourier alternative let \(L_{\rm old}(x)\) be its
earlier affine half-face cost, with the sharp cap ceiling
\(\widehat M\) and the old height allowance \(\pi H\).
The constant \(c\) in that cost may also be replaced by its
same previously established upper bound. Let
\[
 m(x)=A_*+p_*(x-a_*)-L_{\rm old}(x).
\]
This is affine in \(x\). Suppose two numbers \(m_-,m_+\)
are simultaneous valid lower bounds for it at
\(x=11/50,9/20\) on whatever reference set is being considered.
Set
\[
 d_-=-3/100,\quad d_+=1/5,\quad
 s=\frac{m_+-m_-}{d_+-d_-},\qquad
                         \Delta_H=\frac{12\pi H}{25}.           \tag{22}
\]
The improved half-face margin is bounded below by
\[
 m_-+s(\delta-d_-)+\mu\delta^2+\Delta_H,
                       \qquad d_-\le\delta\le d_+,              \tag{23}
\]
where \(\mu\) is the corresponding value from (20).
Indeed affine interpolation gives the first two terms, while
(14), (16) subtract \(\mu\delta^2+\Delta_H\) from the old cost.
Its exact minimum occurs at
\[
 \delta_*=\max\{d_-,\min\{d_+,-s/(2\mu)\}\},                     \tag{24}
\]
and is the expression (23) evaluated at \(\delta_*\).

For the real-arc absolute-cap bound (21), the same valid
lower bound has the additional term
\[
                  \mathcal D(a)-(B_0-\widehat M).               \tag{25}
\]
This merely accounts for replacing the half-face cap ceiling
by (18) and retaining the incoming decrease.

The endpoint premises here are genuine lower bounds on the
same reference set; isolated boundary-cell values cannot be
promoted to such premises without their full transport proof.
Equations (22)--(25) are purely algebraic and assert no
numerical sign. The earlier saved result remains inconclusive.
No retry, refinement, new comparison calculation, or numerical
evaluation is authorized by this corollary.

The new source conclusion is (17), (21), with the explicit
optimizer and incoming decrease. It does not prove a complete
later Fourier sector, a cap relative packet on the whole arc,
or a ratio bound between actual conditional values.

