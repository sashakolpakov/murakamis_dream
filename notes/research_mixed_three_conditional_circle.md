# A full-circle packet for the original three-vertex conditional sum

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

After one neighboring index family is fixed, an original three-vertex
conditional can be summed over its entire physical support. Its exact
coefficient representation has one global Cauchy-circle saddle, uniformly
when both neighboring indices lie between \(N/5\) and \(9N/20\).
This gives a nonzero packet without discarding the conditional real-index
complement. The statement is for physical integer neighbors; it does not
silently continue a varying-degree polynomial to complex neighbors.

## 1. The exact conditional source and its full circle

Let \(N\ge30\), \(r=e^{-2\pi i/N}\), and
\(P_j=(r;r)_j\). For physical integers \(a,b\) assume
\[
                  \frac N5\le a,b\le\frac{9N}{20}.
 \tag{1}
\]
Use the literal conditional sum from the
[exact conditional-leg theorem](research_mixed_conditional_leg_sum.md):
\[
 L_0(a,b)=\sum_{j=0}^{N-1-\max(a,b)}
          \frac{r^{-aj}P_{j+a}P_{j+b}}{P_j^2},\qquad
 p_a(z)=\prod_{h=1}^a(1-r^hz).
 \tag{2}
\]
Its all-level identity is
\[
                    L_0(a,b)=N[z^a]p_a(z)p_b(z).
 \tag{3}
\]
In particular, the vanished terms beyond the physical cutoff have
already been accounted for by exact polynomial zeros. There is no
root-of-unity alias in (3), because the degree \(a+b\) lies below
\(a+N\).

Put \(w=\eta+i\theta\), \(\rho=e^\eta\), and, near the selected
arc defined below, use the actual logarithms
\[
 f_N(w)=\sum_{h=1}^a\Log(1+e^{w-2\pi ih/N})
          +\sum_{h=1}^b\Log(1+e^{w-2\pi ih/N})-aw.
 \tag{4}
\]
Define the two block centers
\[
       \alpha_a=\frac{\pi(a+1)}N,\quad
       \alpha_b=\frac{\pi(b+1)}N,\qquad
       I=[\min(\alpha_a,\alpha_b),\max(\alpha_a,\alpha_b)].
 \tag{5}
\]
Their distance is at most \(\pi/4\). On this arc every factor
angle has absolute value at most
\[
        \frac{\pi(\max(a,b)-1)}N+|\alpha_a-\alpha_b|
                                            <\frac{7\pi}{10}<\pi.
 \tag{6}
\]
Thus these logarithms have their principal lifts with no zero or
negative-real crossing. Elsewhere on a Cauchy circle we use the exact
polynomial, including any zeros, and need no logarithmic branch.

## 2. A global angular comparison

**Lemma 1.** At every radius \(\rho>0\), every global maximum of
\(|p_a(-\rho e^{i\theta})p_b(-\rho e^{i\theta})|\) lies in
the short arc \(I\). At radii \(1/3\le\rho\le3\) it is unique.
On \(I\), if \(G_N=\Re f_N\),
\[
                    -\partial_\theta^2G_N>\frac{N}{10800}.
 \tag{7}
\]

*Proof of the global assertion.* Pair the roots of a single block
symmetrically about its center. A pair has angles \(\theta-\alpha\pm\delta\),
where \(0\le\delta<9\pi/20\). Its squared modulus, as a function
of \(c=\cos(\theta-\alpha)\), is
\[
 Q_{\rho,\delta}(c)
   =(1-\rho^2)^2+4\rho^2\cos^2\delta
       +4\rho(1+\rho^2)\cos\delta\,c+4\rho^2c^2.
 \tag{8}
\]
This is convex in \(c\). If the new angular distance is
\(0\le d_0\le\pi/4\), then
\[
 \begin{split}
 Q(\cos d_0)-Q(-1)
   =4\rho(1+\cos d_0)
      [(1+\rho^2)\cos\delta-\rho(1-\cos d_0)]>0.
 \end{split}
 \tag{9}
\]
Indeed \(\cos\delta>\sin(\pi/20)>31/200\), while
\(\cos d_0\ge1/\sqrt2>7/10\), so the bracket is greater
than \(\rho/100\). Convexity now implies
\(Q(\cos d)\le Q(\cos d_0)\) whenever the old circular
distance satisfies \(d\ge d_0\), strictly if \(d>d_0\).
An unpaired central factor has the same comparison directly.

For any point outside \(I\), one can choose an endpoint of \(I\)
whose distances to both block centers are no greater than the old
distances and are at most \(|I|\le\pi/4\). To see this, unwrap
the centers as \(\alpha\le\beta\le\alpha+\pi/4\). On
\([\beta,\alpha+\pi]\) choose \(\beta\); on
\([\alpha+\pi,\beta+\pi]\) either endpoint works; and on
\([\beta+\pi,\alpha+2\pi]\) choose \(\alpha\).
At least one block comparison is strict. Applying (9) pair by pair
proves the global assertion, including points where the old polynomial
vanishes.

*Proof of the curvature assertion.* For an individual factor with
angle \(\gamma\),
\[
 -\frac{d^2}{d\gamma^2}\log|1+\rho e^{i\gamma}|
 =\Re\frac{\rho e^{i\gamma}}{(1+\rho e^{i\gamma})^2}
 =\frac{\rho[(1+\rho^2)\cos\gamma+2\rho]}
              {(1+\rho^2+2\rho\cos\gamma)^2}.
 \tag{10}
\]
Its value is invariant under \(\rho\mapsto1/\rho\).
It is enough to use \(1/3\le\rho\le1\). By (6),
\(\cos\gamma> -\sin(\pi/5)>-59/100\). The numerator in
(10) is therefore greater than
\[
 \rho\left[2\rho-\frac{59}{100}(1+\rho^2)\right]
                                  \ge\frac1{270}.
\]
For example its derivative is at least \(23/150>0\) on
\([1/3,1]\), so its minimum is its value at \(1/3\).
The denominator is at most \((1+\rho)^4\le16\), giving a
lower bound \(1/4320\) per factor. There are
\(a+b\ge2N/5\) factors, proving (7).

If the centers differ, the angular derivative at the left center is
positive and at the right center negative. In fact a paired block
strictly decreases with its distance from its center on
\([0,\pi/4]\), since \(Q'(c)>0\) for \(c\ge1/\sqrt2\).
Together with (7), this gives exactly one angular maximum inside
\(I\). If the centers agree, symmetry gives that same assertion
at their common point. \(\square\)

The scalar inequalities in this proof are elementary strict bounds.
For example \(\sin(\pi/20)>31/200\) follows from
\(\pi>25/8\), \(\pi<22/7\), and \(\sin x\ge x-x^3/6\);
\(\sin(\pi/5)<59/100\) follows from the corresponding upper
Taylor polynomial through degree five. The focused checker verifies
their rational margins.

## 3. The unique full-circle critical point

Let \(\theta(\eta)\) be the angular maximum in Lemma 1 and put
\(M_N(\eta)=G_N(\eta,\theta(\eta))\).

**Lemma 2.** There is exactly one critical point of (4) with
\[
             -\log3<\eta_N<\log3,\qquad\theta_N\in I.
 \tag{11}
\]
It is a genuine zero of \(f_N'\), with its original logarithmic
lifts, and
\[
                  \Re f_N''(w_N)>N/10800,
                  \qquad w_N=\eta_N+i\theta_N.
 \tag{12}
\]

*Proof.* Holomorphy and (7) give
\(G_{\eta\eta}=-G_{\theta\theta}>N/10800\). Differentiating
the angular maximum yields the exact Schur formula
\[
 M_N''=G_{\eta\eta}
              -\frac{G_{\eta\theta}^2}{G_{\theta\theta}}
                                                    >N/10800.
 \tag{13}
\]
For any factor angle, the radial derivative of its logarithmic
modulus is
\[
 R_\rho(\gamma)=\frac{\rho^2+\rho\cos\gamma}
                         {1+\rho^2+2\rho\cos\gamma}.
 \tag{14}
\]
For \(\rho=1/3\), it is at most \(1/4\); for \(\rho=3\),
it is at least \(3/4\). This follows either by differentiation
in \(\cos\gamma\) or by clearing the positive denominator.
The subtraction \(-aw\) in (4) therefore gives
\[
 M_N'(-\log3)\le\frac{b-3a}{4}\le-\frac{3N}{80},\qquad
 M_N'(\log3)\ge\frac{3b-a}{4}\ge\frac{3N}{80}.
 \tag{15}
\]
Strict convexity proves existence and uniqueness of \(\eta_N\).
Both real derivatives of \(G_N\) vanish there, so the
Cauchy--Riemann equations give \(f_N'(w_N)=0\), not just its
exponentiation. Equation (12) follows from (7). \(\square\)

Here and below the case \(a=b\) has no difficulty: the maximizing
angle is fixed by symmetry, and the radial argument is unchanged.

## 4. Uniform control of the entire complementary circle

Let \(d_{\mathbb T}\) be circular distance in radians. For
\(0<\varepsilon\le\pi\), define
\[
 \delta_\varepsilon=
       \min\left\{\frac{\varepsilon^2}{88000},
                    \frac{1-\cos(\varepsilon/2)}{480}\right\}>0.
 \tag{16}
\]
At the radius \(\rho_N=e^{\eta_N}\), every point with
\(d_{\mathbb T}(\theta,\theta_N)\ge\varepsilon\) satisfies
\[
 \log\left|e^{-a(\eta_N+i\theta)}
                  p_a(-\rho_Ne^{i\theta})p_b(-\rho_Ne^{i\theta})\right|
       \le\Re f_N(w_N)-N\delta_\varepsilon.
 \tag{17}
\]
At a zero the left side is interpreted as \(-\infty\).

To prove (17), first suppose \(\theta\in I\). Integrating (7)
from the maximum proves the stronger loss
\(N\varepsilon^2/21600\). Otherwise choose the projecting
endpoint \(\theta'\) in the proof of Lemma 1. If
\(|\theta'-\theta_N|\ge\varepsilon/2\), the same curvature
argument and the nonnegative projection gain give loss at least
\(N\varepsilon^2/86400\).

In the remaining case, the circular distance from \(\theta\) to
the block centered at \(\theta'\) is at least
\(\varepsilon/2\). For any of its pairs,
\[
 \frac{Q(1)-Q(c)}{Q(1)}
 \ge(1-c)\frac{4\rho(1+\rho^2)\cos\delta}{(1+\rho)^4}
                         >\frac{1-c}{20}.
 \tag{18}
\]
Indeed \(\rho/(1+\rho)^2\ge3/16\),
\((1+\rho^2)/(1+\rho)^2\ge1/2\), and
\(\cos\delta>31/200\). Since
\(-\log(1-x)\ge x\), the pair's logarithmic modulus gain is
at least \((1-\cos(\varepsilon/2))/40\). This block has at
least \(N/12\) pairs for \(N\ge30\), because its length is
at least \(N/5\). All other pair and unpaired gains are nonnegative
by Lemma 1. This proves the second loss in (16), and completes the
whole-circle estimate.

## 5. The original conditional packet

**Theorem 3.** Uniformly over all physical neighbors (1), as
\(N\to\infty\),
\[
 \boxed{\qquad
 L_0(a,b)=
   \frac{(-1)^a N\,e^{f_N(w_N)}}{\sqrt{2\pi f_N''(w_N)}}
                         \{1+O(N^{-1})\}.
 \qquad}
 \tag{19}
\]
The square root is its accretive branch. The coefficient is nonzero
for all sufficiently large \(N\), uniformly in (1). Dividing (19)
by the literal nonzero factor \(P_a^2\) gives the original
\(T_0(a,b)\) with unchanged relative remainder.

*Proof.* The exact coefficient integral is
\[
 [z^a]p_a(z)p_b(z)
       =\frac{(-1)^a}{2\pi}
          \int_{\theta_N-\pi}^{\theta_N+\pi}
            e^{-a(\eta_N+i\theta)}
             p_a(-e^{\eta_N+i\theta})p_b(-e^{\eta_N+i\theta})\,d\theta.
 \tag{20}
\]
In a fixed neighborhood of \(\theta_N\) its integrand is
exactly \(e^{f_N(w_N+i(\theta-\theta_N))}\). Every factor is
uniformly separated from zero there by (6) and (11). Consequently
\(f_N^{(r)}=O_r(N)\) for every fixed derivative order, uniformly
over (1). Its quadratic term is
\(-f_N''(w_N)(\theta-\theta_N)^2/2\), with the uniform positive
real part (12). The entire remaining circle has the exponential
loss (17). Holomorphic Gaussian integration now gives
\(e^{f_N(w_N)}/\sqrt{2\pi f_N''(w_N)}\), with relative
error \(O(N^{-1})\). The first cubic contribution is odd on a
symmetric local cutoff; all higher remainder estimates are uniform.
Multiplying by the exact factor \(N\) in (3) proves (19).
\(\square\)

The size of \(f_N''\) is bounded above and below by fixed positive
multiples of \(N\). Thus (19) has the original \(N^{1/2}\)
conditional power before division by \(P_a^2\). No physical endpoint
row or additional Fourier mode is missing: (3) already sums the
entire original support, and (20) is its entire Cauchy circle.

## 6. The continuous action and its original absolute normalization

Put \(\alpha=a/N,\beta=b/N\). The functions below also make sense
for continuous real \((\alpha,\beta)\in[1/5,9/20]^2\):
\[
 \begin{split}
 h(\alpha,\beta,w)&=
       \int_0^\alpha\Log(1+e^{w-2\pi ix})\,dx
      +\int_0^\beta\Log(1+e^{w-2\pi ix})\,dx-\alpha w,\\
 q_0(\alpha,\beta,w)&=\tfrac12\bigl[
       \Log(1+e^{w-2\pi i\alpha})+
       \Log(1+e^{w-2\pi i\beta})-2\Log(1+e^w)\bigr].
 \end{split}
 \tag{21}
\]
Every logarithm is the central branch used above. The continuous
versions of Lemmas 1--2 give a unique critical point \(w_0\),
with \(|\Re w_0|<\log3\), imaginary part between
\(\pi\alpha\) and \(\pi\beta\), and
\(\Re h_{ww}(w_0)>1/10800\). The action and its critical point
are holomorphic on a neighborhood of each real parameter point;
this follows from the implicit function theorem and the strict bound.

Euler--Maclaurin summation in a fixed neighborhood of these critical
points gives, with every fixed \(w\)-derivative,
\[
 f_N(w)=Nh(\alpha,\beta,w)+q_0(\alpha,\beta,w)+O(N^{-1}),
 \qquad w_N=w_0+O(N^{-1}),
 \tag{22}
\]
uniformly over the real parameter box. The endpoint factors in (21)
stay separated from zero, so no singular summation formula is used.
For completeness, the strict curvature bounds and the radial endpoint
reserves persist for the limiting integrals. Their unique saddle is
the uniform limit of the finite saddles. Applying the implicit
function theorem to \(f_N'/N=h_w+O(N^{-1})\) then gives the
second assertion in (22).

Write \(A=e^{-2\pi i\alpha}\), \(B=e^{-2\pi i\beta}\),
\(Z=e^{w_0}\). The actual derivative of (21), including its lift,
is \(h_w=-q_0/(\pi i)-\alpha\). Hence
\[
 \begin{split}
 q_0(w_0)&=-\pi i\alpha,\\
 (1+ZA)(1+ZB)&=A(1+Z)^2,\\
 (1-A)+(B-A)Z+A(B-1)Z^2&=0.
 \end{split}
 \tag{23}
\]
The selected quadratic root is the one specified by the full-circle
saddle, not an independently chosen square-root branch.

Here the continuous phase has its original absolute constant. Let
\(g(z)=J(z)+i\pi(z-z^2)/2\), on the original factorial strip,
and set \(s=1/2+iw/(2\pi)\). Then
\[
 \begin{split}
 h(\alpha,\beta,w)+i\pi\alpha
   &=\mathcal Q(\alpha,\beta,s),\\
 \mathcal Q(\alpha,\beta,s)
   &=g(s+\alpha)+g(s+\beta)-2g(s)+2\pi i\alpha s.
 \end{split}
 \tag{24}
\]
Indeed \(g'(s+x)=\Log(1+e^{w-2\pi ix})\), and integrating
this equality proves (24) directly, with no undetermined constant.
All three factorial arguments stay in \(0<\Re z<1\) on the
selected chart. The phase \(\mathcal Q\) is precisely that of the
literal summand \(r^{-aj}P_{j+a}P_{j+b}/P_j^2\). In particular,
\(U=e^{-2\pi is}=-Z\) changes (23) into its original conditional
stationary equation. Also \(-\mathcal Q_{ss}=4\pi^2h_{ww}\).

**Corollary 4.** With \(s_0=1/2+iw_0/(2\pi)\), the packet
in Theorem 3 has the equivalent form
\[
 L_0(a,b)=\sqrt N\,
       \frac{e^{-\pi i\alpha}}{\sqrt{2\pi h_{ww}(w_0)}}
       e^{N\mathcal Q(\alpha,\beta,s_0)}
                        \{1+O(N^{-1})\}.
 \tag{25}
\]
Its nonzero coefficient and action have the holomorphic germs just
described, and the asymptotic is uniform over all physical neighbors
(1). To obtain (25), insert (22) into (19), use stationarity to
replace \(w_N\) by \(w_0\), and use (23)--(24). The exact factor
\((-1)^a=e^{i\pi N\alpha}\) accounts for the phase shift in (24).
This statement still makes no assertion that the whole varying-degree
finite sum is defined or controlled at noninteger complex neighbors.

## 7. Scope for mixed-word cancellation

All constants and the neighbor box are independent of the word length
and arrangement. The interval in (1) contains the displaced value
\(.24\) used in the
[absolute-complement obstruction](research_mixed_absolute_complement_obstruction.md).
Thus this conditional theorem does not repeat the invalid step of
taking absolute values of that unsummed index complement.

It proves a packet for a whole original conditional sum at physical
integer neighbors. It does not assert a fixed complex-neighbor packet:
such a continuation must handle the varying polynomial degrees and
the full-circle seams using an exact interpolant. Nor does (19)
control the four-vertex weighted functional or the residual coherent
sum over the remaining neighbor indices. Those are explicit remaining
requirements for a full alternating or arbitrary mixed-word source
theorem. No mixed-word volume limit is inferred here.

## 8. Reproduction

Run `python3 experiments/check_mixed_three_conditional_circle.py`.
The focused checker verifies the paired-factor identity, radial and
angular inequalities, exact rational trigonometric margins, full-circle
gap budget, and Cauchy/Gaussian normalization. The all-neighbor theorem
follows from the above global comparisons, not from sampling saddle
locations or finite words.

The saved result is
[`research-mixed-three-conditional-circle.json`](../repro/results/research-mixed-three-conditional-circle.json).
