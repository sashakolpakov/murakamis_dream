# The trace at a product junction on a regular index window

A product junction without a crossing-circle operator contributes a polynomial trace to the Conway source. When its incident Newton indices lie in a compact part of the strict low-index region, that trace changes by an exponentially small relative amount under a bounded main-meridian deformation. The exact Fourier expansion groups Laurent coefficients whose indices differ by multiples of the level; these groups are called aliases below. Its first alias is independent of the meridian parameter, and strict log-concavity makes every higher alias exponentially smaller.

The [source-bound theorem](actual_main_meridian_source_bounds.md), Section 2, supplies the exact Fourier trace and the finite interval-tail inequality used here. The [grouped wire packet](actual_main_meridian_grouped_wire_packet.md) applies the result at the regular maximizing state. For signed coefficient arrays the conclusion is first an error relative to a positive absolute majorant; control of the whole signed contraction is a separate step.

## 1. The exact kernel and the regular window

Let \(N\ge2\), \(M=\lfloor(N-1)/2\rfloor\), and
\[
 S_r=\prod_{v=1}^r2\sin(\pi v/N),\qquad
 e_n(z)=S_n^{-2}\prod_{v=0}^{n-1}
                    \bigl(2\cos((2v+1)\pi/N)-z\bigr).
\]
Fix a number \(B\) of incident factors. For low indices \(0\le n_i\le M\), put
\[
 F_N(z)=\prod_{i=1}^{B}e_{n_i}(z),\qquad
 F_N(-u-u^{-1})=\sum_{k=-D}^{D}a_ku^k,
 \qquad D=\sum_i n_i.
 \tag{1}
\]
The actual finite q-binomial identity gives, for one factor,
\[
 e_n(-u-u^{-1})=\sum_{k=-n}^{n}a_k^{(n)}u^k,
 \qquad
 a_k^{(n)}=\frac{S_{2n}}{S_n^2S_{n+k}S_{n-k}}>0.
 \tag{2}
\]
The sequence is symmetric and unimodal. In particular
\[
 \frac{a_{k+1}^{(n)}}{a_k^{(n)}}
   =\frac{\sin((n-k)\pi/N)}{\sin((n+k+1)\pi/N)}\le1
 \quad(0\le k<n).
 \tag{3}
\]
Products correspond to convolutions, so the coefficients \(a_k\) in (1) are also symmetric and unimodal.

Choose a fixed \(0<\delta<1/4\). The regular window is
\[
 \delta\le u_i:=n_i/N\le\frac12-\delta,
 \qquad \sum_i u_i\ge1+\delta.
 \tag{4}
\]
An empty such family causes no difficulty. The upper bound keeps the sine-binomial factors uniformly away from the flat odd-endpoint case; the total bound keeps the old trace in its strict nonzero domain. The number of factors is fixed as \(N\) varies.

For \(P_s(z)=\mathsf T_N(z)+2\cos(2\pi s)\), use the exact normalized top trace
\(\phi_s=(-1)^{N-1}N^2[z^{N-1}]\operatorname{rem}_{P_s}\). Let
\[
 d_\ell=a_{\ell N-1}-a_{\ell N+1}\ge0,
 \qquad L=\left\lfloor\frac{D+1}{N}\right\rfloor.
\]
The proved finite Fourier identity, with both parities retained, is
\[
 \phi_s(F_N)=N^2\sum_{\ell=1}^{L}
 (-1)^{(N-1)(\ell+1)}
 U_{\ell-1}(\cos(2\pi s))\,d_\ell.
 \tag{5}
\]
The coefficient of \(d_1\) is exactly one for every \(s\). All these are fixed complete Newton factors; no moving-basis change or auxiliary color identification has been made.

## 2. Uniform coefficient rates and strong concavity

Write
\[
 J(t)=\int_0^t\log(2\sin\pi v)\,dv,
 \qquad
 b_u(t)=J(2u)-2J(u)-J(u+t)-J(u-t),\quad |t|\le u.
 \tag{6}
\]
Uniform sine-factorial estimates give
\[
 \log a_k^{(n)}=N b_{n/N}(k/N)+O(\log N),
 \tag{7}
\]
uniformly over (4) and the whole coefficient support. The estimate follows from \(\log S_r=NJ(r/N)+O(\log N)\), including \(r=0\); the two endpoint logarithmic cells contribute only \(O(\log N)\).

For \(|t|<u\),
\[
 b_u''(t)=-\pi\bigl[\cot\pi(u+t)+\cot\pi(u-t)\bigr]
 =-\frac{\pi\sin(2\pi u)}
         {\sin\pi(u+t)\sin\pi(u-t)}.
 \tag{8}
\]
Consequently on the compact range (4),
\[
 b_u''(t)\le-\lambda_\delta,
 \qquad \lambda_\delta:=\pi\sin(2\pi\delta)>0.
 \tag{9}
\]
The continuous function \(b_u\) remains strongly concave on its closed interval; its endpoint derivatives may be infinite.

Define the convolution action
\[
 \mathcal B_{\mathbf u}(t)=
 \max_{\substack{\sum_i t_i=t\\|t_i|\le u_i}}
                   \sum_i b_{u_i}(t_i).
 \tag{10}
\]
It is even and strongly concave with constant \(\lambda_\delta/B\). Indeed, interpolate two maximizing vectors at two total indices. The sum of (9)'s strong-concavity remainders is at least
\(\lambda_\delta\|\mathbf t-\mathbf v\|_2^2/2\), and
\(\|\mathbf t-\mathbf v\|_2^2\ge B^{-1}|\sum_i(t_i-v_i)|^2\).
Therefore \(\mathcal B_{\mathbf u}(t)+\lambda_\delta t^2/(2B)\) is even and concave. It is nonincreasing on its nonnegative interval. In particular,
\[
 \mathcal B_{\mathbf u}(t_2)-\mathcal B_{\mathbf u}(t_1)
 \le-\frac{\lambda_\delta}{2B}(t_2^2-t_1^2)
 \quad(0\le t_1\le t_2\le\sum_i u_i).
 \tag{11}
\]

The finite convolution has the uniform rate
\[
 \log a_k=N\mathcal B_{\mathbf u}(k/N)+O_{B,\delta}(\log N)
 \quad(|k|\le D).
 \tag{12}
\]
For the upper bound, use (7) and the polynomial number of tuples in the convolution. For the lower bound, round a maximizing real tuple in (10) to integers with its prescribed sum \(k\), changing each coordinate by at most one. This is possible by flooring all coordinates and then increasing the required number with nonzero fractional parts; the integer endpoints \(\pm n_i\) are respected. The uniform modulus
\(|J(x+h)-J(x)|\le C|h|\log(e/|h|)\) on \([0,1]\) bounds the resulting action error by \(O(\log N/N)\), even if a coordinate lies at an endpoint. One positive summand then proves the lower bound. Thus (12) does not assume an unproved derivative asymptotic for the convolution.

## 3. Higher aliases are exponentially small relative to the first difference

For \(\ell\ge2\) with \(\ell N-1\le D\), apply (11) with
\(t_1=1-1/N\), \(t_2=\ell-1/N\). Since
\[
 t_2^2-t_1^2=(\ell-1)(\ell+1-2/N)\ge2,
\]
equation (12) gives
\[
 \frac{a_{\ell N-1}}{a_{N-1}}
       \le N^C\exp(-\lambda_\delta N/B).
 \tag{13}
\]
The denominator exists because (4) implies \(D>N-1\). If the numerator lies outside the support, set it to zero.

It remains to compare a coefficient to its first discrete difference. The elementary interval-tail inequality for a convolution of \(B\) symmetric unimodal sequences supported in \([-M,M]\) states
\[
 a_k\le(2M+1)^B(a_k-a_{k+2})\qquad(k\ge M).
 \tag{14}
\]
Its proof is finite: decompose each sequence into a nonnegative sum of interval indicators. For a product of such indicators, the convolution count strictly drops by step two beyond the largest interval radius whenever the first count is nonzero; that positive integer difference is at least one, whereas the count is at most \((2M+1)^B\). Summing the interval decompositions proves (14). This is the same all-index lemma used in the adjacent-level source comparison.

Applying (14) at \(k=N-1\) gives
\[
 d_1\ge N^{-B}a_{N-1}>0.
 \tag{15}
\]
Combining \(0\le d_\ell\le a_{\ell N-1}\), (13), and (15) proves
\[
 \sum_{\ell=2}^{L}\frac{d_\ell}{d_1}
       \le N^{C'}\exp(-\lambda_\delta N/B).
 \tag{16}
\]
Here \(L\) is bounded in terms of \(B\). The conclusion is uniform throughout (4).

## 4. The local deformed trace has the same leading kernel

For every fixed complex disk \(|s|\le R\),
\[
 |U_{\ell-1}(\cos(2\pi s))|
       \le\ell\exp(2\pi(\ell-1)R).
 \tag{17}
\]
This follows from its finite exponential sum and holds through all sine resonances. At \(s=0\), the value is \(\ell\). Equation (16) therefore shows, for all sufficiently large \(N\),
\[
 \phi_0(F_N)=N^2d_1\bigl(1+O(e^{-\kappa N})\bigr)>0,
 \qquad
 \boxed{\quad
 \frac{\phi_s(F_N)}{\phi_0(F_N)}
       =1+O_{B,\delta,R}(e^{-\kappa N}).\quad}
 \tag{18}
\]
One can take any fixed \(\kappa<\lambda_\delta/B\), after absorbing the polynomial factors. The sign alternation at even levels is included in (5) and is harmless once (16) is proved. The opposite-color relation remains constant, so its corresponding statement is exact without a deformation.

For fixed \(B\le4\), there are no higher aliases for any low indices: \(D\le4M\le2N-2\), so \(L\le1\). Then
\[
                         \phi_s(F_N)=\phi_0(F_N)
 \tag{19}
\]
for every \(s\), with no regular-window hypothesis; a zero trace remains zero. This also follows by the one-division degree bound.

The ratio in (18) is entire in \(s\), with a constant positive denominator. Applying (18) on a slightly larger fixed disk and using Cauchy's estimate gives the same exponential error for every fixed derivative in \(s\). No contour avoiding a resonance is needed for this local trace statement.

## 5. Applying the local estimate to a source

The result concerns the exact raw polynomial trace of the prescribed fixed-coordinate factors. It has not replaced a physical auxiliary color by a coefficient index. Any original color dependence remains in the coefficients multiplying those factors. The typed turn, circle pivot, crossing scalar and primitive main-cut normalization are separate parts of the compiler.

On a compact bulk index window, the proved paired-turn formula also gives
\(W_n(s)/H_N(s)=1+O_R(N^{-1})\), and the six type scalars \(q^{\pm s^2/2}\) are \(1+O_R(N^{-1})\). Thus a fixed product of the local trace kernels in (18) and those specified bulk turn factors has the same leading fixed-state weight, with the appropriate \(O(N^{-1})\) turn error. This statement retains the actual types; it is not a replacement of the moving multiplication law by the complete one globally.

For arbitrary signed coefficient arrays supported in a common window satisfying (4), (18) implies an error bounded by \(e^{-\kappa N}\) times the corresponding complete positive absolute contraction. It does not imply a relative error with respect to a possibly canceling signed contraction. Similarly the turn errors have an \(O(N^{-1})\) absolute-majorant bound. To conclude a whole-source microscopic profile, one must also control the literal main-meridian deformation of the physical input coefficients, establish suitable conditioning or stationary cancellation for their contraction, and bound the complement of the regular window. None of these follows just from (18).

The [regular circle trace](actual_main_meridian_regular_circle_trace.md) gives the physical input deformation and its canonical analytic interpolation. The [component extension](actual_main_meridian_component_extension.md) controls grouped high-index errors, while the [grouped wire packet](actual_main_meridian_grouped_wire_packet.md) proves the finite-window and contour statements needed to use these local estimates. The [filled-volume theorem](actual_main_meridian_filled_volume.md) combines those inputs with a joint charge comparison. The present result is the regular-window trace estimate; it does not obtain a whole-source relative error from a potentially cancelling coefficient sum.
