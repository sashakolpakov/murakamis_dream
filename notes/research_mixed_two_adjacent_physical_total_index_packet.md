# The complete physical total-index packet of the merged pair

Research deduction, 7 November 2026. Group the literal adjacent
power-two source by its total physical index. At equal Fourier
endpoints, each complete inner finite sum has a nonzero Gaussian
packet, uniformly when the total normalized index stays in a compact
subinterval of \((0,1)\). Its actual row moduli are exactly unimodal,
so every inner endpoint and every other physical inner index is
controlled directly. No contour or alias assumption is needed for
this finite inner contraction.

The total index remains physical. The theorem does not continue
that index off grid or prove a packet for the remaining outer sum.
No numerical evaluation is used.

## 1. The literal finite contraction

Retain the original conventions
\[
 D=N-1,\quad r=e^{-2\pi i/N},\quad
 P_j=(r;r)_j,\quad p_j(X)=(rX;r)_j,\quad X=e^{-2\pi ix}.
 \tag{1}
\]
At equal external endpoints \(x=y\),
[the merged-source identity](research_mixed_two_adjacent_merged_source.md),
equation (14), becomes
\[
 \boxed{\quad
 V_{22,N}(x,x)=e^{2\pi iDx}
                    \sum_{m=0}^{D} B_{N,m}(x),
 \quad}
 \tag{2}
\]
where
\[
\begin{split}
 B_{N,m}(x)&=\sum_{j=0}^{m}T_{N,m,j}(x),\\
 T_{N,m,j}(x)&=
 \frac{r^{-j(m-j)}P_m p_j(X)p_{m-j}(X)}
                         {P_j^2P_{m-j}^2}.
\end{split}
 \tag{3}
\]
This is the whole original triangular source, regrouped by
\(m=j+k\). In particular \(B_{N,0}=1\).
The exact symmetry
\[
                       T_{N,m,j}=T_{N,m,m-j}
 \tag{4}
\]
includes its phase, not only its modulus.

Let the external parameter range over a fixed compact subset of
\[
                   \mathcal U=\{x:0<\Re x<1/2,\ \Im x>0\}.
 \tag{5}
\]
This includes a fixed complex neighborhood of \(x_0\).
The physical products \(p_j(X)\) are nonzero here because
\(|X|>1\), and every \(P_j\) in (3) has \(j<N\).

## 2. Exact finite unimodality

For real \(0<t<1\), define
\[
 \mathcal R_x(t)=
           \frac{|1-Xe^{-2\pi it}|}{4\sin^2(\pi t)},\qquad
 K_x'(t)=\log\mathcal R_x(t).
 \tag{6}
\]
One can take
\[
 K_x(t)=\Re\{g_+(t+x)-g_+(x)\}-2J(t),\qquad J(t)=\Re g(t),
 \tag{7}
\]
with the original upper continuation across any shifted real
wall. Only the real derivative of this expression is used
in the following comparison.

**Lemma 1.** For \(x\in\mathcal U\), \(\mathcal R_x\) is
strictly decreasing on \((0,1/2)\). For \(1/2<t<1\),
\[
                         \mathcal R_x(t)<\mathcal R_x(1-t).
 \tag{8}
\]
Consequently, whenever \(0<s<t<1\) and \(s+t\le1\),
\[
                              \mathcal R_x(t)<\mathcal R_x(s).
 \tag{9}
\]

*Proof.* On \(0<t<1/2\),
\[
 K_x''(t)=\pi\Re\cot\pi(t+x)-2\pi\cot\pi t<0.
 \tag{10}
\]
If \(t+\Re x<1/2\), the positive shifted cotangent real part
is at most the real cotangent at \(t+\Re x\), which is
strictly less than \(\cot\pi t\). If \(t+\Re x\ge1/2\),
the shifted real part is nonpositive while \(\cot\pi t>0\).
This proves strict decrease, also at the transition.

Write \(X=R e^{-2\pi i\xi}\), where \(R>1\) and
\(0<\xi<1/2\). The numerator squared difference is exactly
\[
 |1-Xe^{-2\pi it}|^2
   -|1-Xe^{-2\pi i(1-t)}|^2
                  =4R\sin(2\pi\xi)\sin(2\pi t)<0
 \tag{11}
\]
for \(t>1/2\). The denominators in (6) agree, proving (8).
For (9), if \(t<1/2\) use strict decrease directly. If
\(t\ge1/2\), then \(s\le1-t\le1/2\), and use (8) followed
by strict decrease; at \(t=1/2\) the latter alone suffices.
\(\square\)

The exact consecutive-row ratio is
\[
 \frac{T_{N,m,j+1}}{T_{N,m,j}}
 =
 r^{2j+1-m}
 \frac{1-Xr^{j+1}}{1-Xr^{m-j}}
 \left(\frac{1-r^{m-j}}{1-r^{j+1}}\right)^2,
                      \qquad 0\le j<m.
 \tag{12}
\]
Therefore
\[
 \left|\frac{T_{N,m,j+1}}{T_{N,m,j}}\right|
       =\frac{\mathcal R_x((j+1)/N)}
                    {\mathcal R_x((m-j)/N)} .
 \tag{13}
\]
The two arguments sum to \((m+1)/N\le1\).
Lemma 1 proves that (13) is greater than one before the
center, less than one after it, and equal to one only when
\(j+1=m-j\). For even \(m\) there is one largest row,
\(j=m/2\). For odd \(m\) the two largest rows
\(j=(m-1)/2,(m+1)/2\) are exactly equal by (4).
This holds at every level and for every \(0\le m<N\).

The comparison is only of moduli. The complex factors in
(12) have not been replaced by positive numbers, and no
lower bound for the signed sum follows from unimodality alone.

## 3. Uniform control of all noncentral physical rows

Fix
\[
              0<c_-<c_+<1,\qquad c=m/N\in[c_-,c_+].
 \tag{14}
\]
Choose a small fixed \(\eta>0\) so that the interval
\([c/2-2\eta,c/2+2\eta]\) lies in a compact subinterval of
\((0,1/2)\), uniformly in \(c\). On any fixed external
compact set as in (5), (10) gives a constant \(\mu>0\) with
\[
                         (\log\mathcal R_x)'(t)\le-\mu
 \tag{15}
\]
throughout those intervals. For large \(N\), both arguments
of (13) are in this region when \(|j-m/2|\le\eta N\).
Their difference is \((2j+1-m)/N\). Multiplying the resulting
ratio bounds and using symmetry yields, with
\(j_0=\lfloor m/2\rfloor\),
\[
 |T_{N,m,j}|
 \le |T_{N,m,j_0}|
       \exp\left\{-\frac{\mu}{N}
               \left[(j-m/2)^2-\frac14\right]\right\}
                 \qquad(|j-m/2|\le\eta N).
 \tag{16}
\]
For even \(m\) the harmless \(1/4\) can be omitted.
The complete finite unimodality then extends the value of
(16) at the boundary of this central interval to every
remaining physical index. In particular, after a possible
decrease of constants,
\[
 \sum_{|j-m/2|>\eta N}|T_{N,m,j}|
       \le N |T_{N,m,j_0}|e^{-\gamma N}
 \tag{17}
\]
for a fixed \(\gamma>0\).

Equations (16)--(17) include the true rows \(j=0,m\).
No regular factorial approximation is imposed on those
endpoint rows. They are bounded by their original exact
ratios to a regular central row, with all finite phases
and products retained.

## 4. The original phase and the complete inner Gaussian

On a central regular chart put
\[
\begin{split}
 F_c(a;x)={}&g(c)+g(a+x)+g(c-a+x)
                -2g(a)-2g(c-a)-2g(x)+2\pi ia(c-a),\\
 b_c(a;x)={}&
 \frac{\mathfrak a(c)\mathfrak a(a+x)\mathfrak a(c-a+x)}
 {\mathfrak a(x)^2\mathfrak a(a)^2\mathfrak a(c-a)^2}.
\end{split}
 \tag{18}
\]
At \(a=j/N\), the original row expansion is
\[
 T_{N,m,j}
       =N^{-3/2}b_c(a;x)e^{NF_c(a;x)}(1+O(N^{-1})).
 \tag{19}
\]
It follows by direct substitution in the exact factorial
source, and retains the normalization of (3).
All factorial arguments in this central chart have real
part in \((0,1)\). The expansion has uniform fixed external
derivatives on smaller compact sets.

The full phase and symbol in (18) are symmetric about
\(a=c/2\), so the actual derivative is zero there, without
an exponentiation or logarithmic-lift selection. Define
\[
\begin{split}
 \Phi(c,x)&=g(c)+2g(c/2+x)-4g(c/2)-2g(x)
                                      +\frac{\pi i}{2}c^2,\\
 H(c,x)&=\partial_a^2F_c(c/2;x)
       =2\pi\cot\pi(c/2+x)-4\pi\cot(\pi c/2)-2\pi i,\\
 \mathcal A(c,x)&=
 \frac{\sqrt{2\pi}\,\mathfrak a(c)\mathfrak a(c/2+x)^2}
 {\mathfrak a(x)^2\mathfrak a(c/2)^4\sqrt{-H(c,x)}} .
\end{split}
 \tag{20}
\]
Equation (10) gives
\(\Re H(c,x)=2K_x''(c/2)<0\). The square root is the
analytic branch with positive real part. On the compact
families above, \(\mathcal A\) is holomorphic in \(x\)
and nonzero.

**Theorem 2.** Uniformly for physical \(c=m/N\in[c_-,c_+]\),
\(x\) on fixed compact subsets of \(\mathcal U\), both level
parities and both parities of \(m\),
\[
 \boxed{\quad
 B_{N,m}(x)=N^{-1}\mathcal A(m/N,x)
             e^{N\Phi(m/N,x)}(1+O(N^{-1})).
 \quad}
 \tag{21}
\]
Every fixed \(x\) derivative of the normalized error is
\(O(N^{-1})\) on smaller external compact sets.

*Proof.* The central row in (17) has modulus
\(O(N^{-3/2}e^{N\Re\Phi})\) by (19), since its distance from
the exact center is at most \(1/(2N)\).
Equations (16)--(17) thus control every physical row outside
a growing Gaussian neighborhood.

Inside it write \(d=j-m/2\). The exact symmetry of (18)
eliminates all odd derivatives of both phase and symbol.
The quadratic approximation is
\[
             e^{N\Phi(c,x)}e^{H(c,x)d^2/(2N)} .
 \tag{22}
\]
The centered lattice is \(\mathbb Z\) for even \(m\) and
\(\mathbb Z+1/2\) for odd \(m\). For either shift \(\sigma\),
the ordinary Gaussian Poisson identity gives
\[
 \sum_{d\in\mathbb Z+\sigma}e^{H d^2/(2N)}
      =\frac{\sqrt{2\pi N}}{\sqrt{-H}}\,
                      (1+O(e^{-\gamma_1 N})),
                   \qquad \sigma\in\{0,1/2\}.
 \tag{23}
\]
Here \(\Re(-H)>0\) and \(\Re((-H)^{-1})>0\) uniformly
on the compact set, so its nonzero Fourier terms have a
uniform exponential loss. This is a Gaussian summation
identity, not an omitted lattice correction of the original
source.

For example restrict first to \(|d|\le N^{1/2+1/16}\).
The quartic phase error is bounded by \(C d^4/N^3\),
and the first symbol error by \(C d^2/N^2\).
Gaussian moment bounds make their total contribution
\(O(N^{-1})\) relative to (23); the row error in (19)
has the same order. The part outside this growing window
is smaller than every inverse power by (16), followed by
(17) outside the fixed central interval.
Thus multiplication of (23) by \(N^{-3/2}b_c(c/2;x)\)
proves exactly (20)--(21), including its phase and branch.
The power is \(N^{-3/2}\sqrt N=N^{-1}\).

The finite sum is holomorphic in \(x\); the nonzero phase
and coefficient are also holomorphic there. Establish the
bounds first on a larger external compact neighborhood,
then apply Cauchy's inequalities to the normalized errors.
This proves all claimed fixed external derivatives.
No derivative in the physical variable \(m/N\) is asserted.
\(\square\)

## 5. What remains for the whole adjacent source

Equation (2) is now a one-index sum of complete inner
packets on each compact physical total-index interval.
All inner endpoints and all inner lattice parities have
been included; no inner contour remainder remains on the
stated domain.

The phase in (20) has an analytic formula on its regular
complex chart, but Theorem 2 is only a theorem about the
physical values \(c=m/N\). The outer equation is specifically
\[
 \partial_c\Phi(c,x)
   =g'(c)+g'(c/2+x)-2g'(c/2)+\pi ic.
 \tag{24}
\]
At \(x=x_0\), the original merged critical point gives
\(c_*=2a_*\), with \(\Im c_*>1/10\). Its real part is
inside a compact physical interval to which Theorem 2
applies, but its positive imaginary part has not been
reached by an off-grid theorem for the complete finite
inner sum.

At that critical point the normalization identities are
\[
 H(c_*,x_0)=2\lambda_-,\qquad
 \Phi_{cc}(c_*,x_0)=\lambda_+/2,\qquad
 H(c_*,x_0)\Phi_{cc}(c_*,x_0)=\det F''(a_*,a_*),
 \tag{25}
\]
where \(\lambda_\pm\) are the original eigenvalues in
[the critical-corridor theorem](research_mixed_two_adjacent_critical_corridor.md).
Thus a justified subsequent outer Gaussian would have
exactly the two-index normalization. Equation (25) is
only that compatibility check.

The physical end-strip bounds may control discarded
ranges of the total index in the exact outer sum. They
do not justify an incoming deformation of the complete
inner packet by themselves. Such a deformation, or a
direct treatment of the remaining outer oscillation,
must preserve its finite cutoff, period factors and
closing observation. The full two-Fourier-end lower
bound is not inferred from (21).

